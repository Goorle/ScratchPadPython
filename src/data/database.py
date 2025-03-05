import mysql.connector


class Database():
    connect = None

    def __init__(self):
        try:
            self.connect = mysql.connector.connect(
                host = "192.168.15.118",
                port = "3306",
                user = "user01",
                password = "12345",
                database = "chernovik01"
            )
        except Exception as e:
            print(f"No connect with database {e}")

    def get_user(self ,login, password):
        select_account_query = f"SELECT * FROM AccountEmployee WHERE login={login} AND password={password}"
        
        with self.connect.cursor() as cursor:
            cursor.execute(select_account_query)
            result = cursor.fetchall()
            print(result)

db = Database()
if db.connect is not None:
    db.get_user("user1", "123")