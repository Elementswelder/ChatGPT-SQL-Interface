import sqlite3


class DatabaseCreation:

    def __init__(self):
        self.conn = sqlite3.connect('database.db')

    def create_database(self):
        c = self.conn.cursor()
        user_data = ("INSERT INTO users (UserID, Username, Name, AccountID, Password) VALUES (1, 'goldenboy', "
                     "'Billy Bob',"
                     "1, 'password')")
        c.execute(user_data)
        user_data = (
            "INSERT INTO users (UserID, Username, Name, AccountID, Password) VALUES (2, 'silverboy', 'Jane Doe', "
            "2, 'password')")
        c.execute(user_data)
        user_data = (
            "INSERT INTO users (UserID, Username, Name, AccountID, Password) VALUES (3, 'bronzeboy', 'Mel Del', "
            "3, 'password')")
        c.execute(user_data)

        account_data = ("INSERT INTO Account (AccountID, Broker, AccountType, Balance) VALUES (1, 'TOS', 'Individual', "
                        "1000.00)")
        c.execute(account_data)
        account_data = ("INSERT INTO Account (AccountID, Broker, AccountType, Balance) VALUES (2, 'TOS', 'Joint', "
                        "1000.00)")
        c.execute(account_data)
        account_data = ("INSERT INTO Account (AccountID, Broker, AccountType, Balance) VALUES (3, 'TOS', 'Individual', "
                        "1000.00)")
        c.execute(account_data)

        active_order_data = ("INSERT INTO ActiveOrders (ActiveOrdersID, AccountID, Type, StockDataID, Status) "
                             "VALUES (1, 1, 'BUY', 1, 'FILLED')")
        c.execute(active_order_data)
        active_order_data = ("INSERT INTO ActiveOrders (ActiveOrdersID, AccountID, Type, StockDataID, Status) "
                             "VALUES (2, 1, 'SELL', 2, 'ACTIVE')")
        c.execute(active_order_data)
        active_order_data = ("INSERT INTO ActiveOrders (ActiveOrdersID, AccountID, Type, StockDataID, Status) "
                             "VALUES (3, 2, 'BUY', 3, 'ACTIVE')")
        c.execute(active_order_data)
        active_order_data = ("INSERT INTO ActiveOrders (ActiveOrdersID, AccountID, Type, StockDataID, Status) "
                             "VALUES (4, 3, 'SELL', 4, 'FILLED')")
        c.execute(active_order_data)
        active_order_data = ("INSERT INTO ActiveOrders (ActiveOrdersID, AccountID, Type, StockDataID, Status) "
                             "VALUES (5, 3, 'BUY', 5, 'ACTIVE')")

        c.execute(active_order_data)
        transaction_data = ("INSERT INTO Transactions (TransactionID, AccountID, StockDataID, Quantity) "
                            "VALUES (1, 1, 10, 100)")
        c.execute(transaction_data)
        transaction_data = ("INSERT INTO Transactions (TransactionID, AccountID, StockDataID, Quantity) "
                            "VALUES (2, 1, 11, 100)")
        c.execute(transaction_data)
        transaction_data = ("INSERT INTO Transactions (TransactionID, AccountID, StockDataID, Quantity) "
                            "VALUES (3, 2, 12, 100)")
        c.execute(transaction_data)

        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (1, 'AAPL', 100.00, '2022-01-01 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (2, 'MSFT', 500.00, '2022-01-02 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (3, 'GOOG', 1000.00, '2022-01-03 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (4, 'AMZN', 2000.00, '2022-01-04 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (5, 'TSLA', 3000.00, '2022-01-05 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (10, 'AAPL', 150.00, '2022-01-06 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (11, 'MSFT', 550.00, '2022-01-07 00:00:00')")
        c.execute(stock_data_data)
        stock_data_data = ("INSERT INTO StockData (StockDataID, Symbol, SharePrice, TimeStamp)"
                           "VALUES (12, 'GOOG', 1100.00, '2022-01-08 00:00:00')")
        c.execute(stock_data_data)

        self.conn.commit()
        self.conn.close()
