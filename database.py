import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('users1.db')

    def login_user(self,username, password):
        sql = "select * from users where phone=? and pwd=?"
        cur = self.conn.execute(sql,(username, password))
        return cur.fetchall()

    def select_news(self):
        sql = "select * from news"
        cur = self.conn.execute(sql)
        records = cur.fetchall()
        return records

    def qk(self):
        self.conn.close()


if __name__ == '__main__':
    db = DataBase()
    r = db.login_user('1', '1')
    #r = db.select_news()
    print(r)
