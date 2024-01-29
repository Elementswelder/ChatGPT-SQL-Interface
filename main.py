# This is a sample Python script.
import os

from openai import OpenAI

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
OPENAI_SECRET = os.environ.get('OPENAI_SECRET')


def start_program():
    client = OpenAI(
        api_key=OPENAI_SECRET
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an SQL master and and you can only return your response in SQL questions."},
            {"role": "user", "content": "How would I select a statement?"},
        ]
    )

    print(completion)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
