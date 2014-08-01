from PyQt4 import QtSql


class RpiControlDB():
    def __init__(self):
        self.db = None

    def connect(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('rpi_control.db')
        self.db.setUserName('pi')
        self.db.setPassword('raspberry')
        if self.db.open():
            return True
        else:
            print self.db.lastError().text()
            return False

    def createTables(self):
        query = QtSql.QSqlQuery()

        query_str = 'CREATE TABLE IF NOT EXISTS user (' \
                    'id INTEGER NOT NULL PRIMARY KEY,' \
                    'name text,' \
                    'balance real)'
                    # TODO: add field active(bool)
        if not query.exec_(query_str):
            print query.lastError().text()

        query_str = 'CREATE TABLE IF NOT EXISTS drink (' \
                    'id int NOT NULL PRIMARY KEY,' \
                    'name text,' \
                    'price real)'
        if not query.exec_(query_str):
            print query.lastError().text()

        query_str = 'CREATE TABLE IF NOT EXISTS usagelog (' \
                    'id int NOT NULL PRIMARY KEY,' \
                    'date int,' \
                    'user_id int,' \
                    'drink_id int,' \
                    'quantity int,' \
                    'payed int,' \
                    'FOREIGN KEY(user_id) REFERENCES user(id),' \
                    'FOREIGN KEY(drink_id) REFERENCES drink(id))'
        if not query.exec_(query_str):
            print query.lastError().text()

    def getUsers(self):
        query = QtSql.QSqlQuery()
        query_str = 'SELECT id, name, balance FROM user'
        if not query.exec_(query_str):
            print query.lastError().text()
        users = []
        while query.next():
            users.append([query.value(0).toInt()[0], str(query.value(1).toString()), query.value(2).toDouble()[0]])
        print users
        return users

    def getDrinks(self):
        query = QtSql.QSqlQuery()
        query_str = 'SELECT id, name, price FROM drink'
        if not query.exec_(query_str):
            print query.lastError().text()
        drinks = []
        while query.next():
            drinks.append([query.value(0).toInt()[0], str(query.value(1).toString()), query.value(2).toDouble()[0]])
        print drinks
        return drinks
