import os
import sqlite3
from database_creation import DatabaseCreation
from openai import OpenAI

OPENAI_SECRET = os.environ.get('OPENAI_SECRET')

QUESTIONS = ['Which user has the most money in their account?',
             'Who has either bought or sold a stock within the first two days of January 2022?',
             'What is the total amount of money in the database?',
             'What is the most expensive stock in the database?',
             'Who is using a broker other than TOS?',
             'Are there any users in the database that have never traded a stock?']

CREATE_TABLE_STATEMENT = """CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(45) NOT NULL,
    Name VARCHAR(45) NOT NULL
    AccountID INT NOT NULL,
    PASSWORD VARCHAR(20) NOT NULL
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
);

CREATE TABLE Account (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,
    Broker VARCHAR(45) NOT NULL,
    AccountType VARCHAR(10) NOT NULL,
    Balance DECIMAL(10, 2) NOT NULL,
);

CREATE TABLE StockData (
    StockDataID INT AUTO_INCREMENT PRIMARY KEY,
    Symbol VARCHAR(9) NOT NULL,
    SharePrice DECIMAL(8, 2) NOT NULL,
    TimeStamp DATETIME NOT NULL
);

CREATE TABLE ActiveOrders (
    ActiveOrdersID INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Type VARCHAR(4) NOT NULL,
    StockDataID INT NOT NULL,
    Status VARCHAR(10) NOT NULL,
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID),
    FOREIGN KEY (StockDataID) REFERENCES StockData(StockDataID)
);

CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    StockDataID INT NOT NULL,
    Quantity MEDIUMINT NOT NULL,
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID),
    FOREIGN KEY (StockDataID) REFERENCES StockData(StockDataID)
);

"""
ZERO_SHOT_MESSAGE = (f"You are an SQL master and and you can only return your response in SQL questions. I will tip "
                     f"you $200 if you do a good job. Here is the"
                     f"create table statements for this database. The user will ask you questions about the data, "
                     f"response only using SQL statements based on this database: {CREATE_TABLE_STATEMENT}")

ONE_SHOT_MESSAGE = ("You are an SQL master and and you can only return your response in SQL questions. I will tip you "
                    "$200 if you do a good job.  Here is an example of a question and its SQL answer:"
                    " Q:'What is the total amount of money in the database?' A:'SELECT SUM(Balance) FROM "
                    f"Account;' Here is the database schema: {CREATE_TABLE_STATEMENT}")

def clean_query(query):
    if 'sql' in query:
        query = query.replace('```sql', '')
        query = query.replace('```', '')
    return query


def run_sql_query(query):
    cleansed_query = clean_query(query)
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(cleansed_query)
        result = c.fetchall()
        if len(result) <= 0:
            print("No results found")
        conn.commit()
        conn.close()
        return result
    except Exception as e:
        print(f"ERROR: {str(e)}")
    finally:
        conn.close()


def start_program(prompt_strategy):
    client = OpenAI(
        api_key=OPENAI_SECRET
    )

    for i in range(len(QUESTIONS)):
        print("-------------------------------------------------------------------")
        print(f"Question: {QUESTIONS[i]}")
        print("-------------------------------------------------------------------")
        if prompt_strategy == "zero-shot":
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": ZERO_SHOT_MESSAGE},
                    {"role": "user", "content": QUESTIONS[i]},
                ]
            )
        else:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": ONE_SHOT_MESSAGE},
                    {"role": "user", "content": QUESTIONS[i]},
                ]
            )
        response = completion.choices[0].message.content
        print(response)
        sql_response = run_sql_query(response)
        print(sql_response)

        friendly = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"Using this database statement {CREATE_TABLE_STATEMENT} and the result of the"
                            f" SQL query {sql_response}, please provide a friendly response to the user's question."},
                {"role": "user", "content": QUESTIONS[i]},
            ]
        )

        response = friendly.choices[0].message.content
        print(response)


if __name__ == '__main__':
    # DatabaseCreation().create_database()
    start_program("zero-shot")
    start_program("one-shot")
