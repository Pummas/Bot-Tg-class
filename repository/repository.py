import psycopg2
from psycopg2 import Error


class Repository:
    def __init__(self, password, database, user='postgres', host="127.0.0.1", port="5432"):
        self.connection = psycopg2.connect(user=user,
                                           password=password,
                                           host=host,
                                           port=port,
                                           database=database)

    def save_message(self, user_id, msg, time):
        try:
            cursor = self.connection.cursor()
            insert_query = """ INSERT INTO requests (cor_num, message, time) VALUES (%s,%s,%s)"""
            item_tuple = (user_id, msg, time)
            cursor.execute(insert_query, item_tuple)
            self.connection.commit()
            print("1 запись успешно вставлена")
            cursor.execute("SELECT * from requests")
            record = cursor.fetchall()
            print("Результат", record)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if self.connection:
                cursor.close()

    def check_registration(self, user_id):
            cursor = self.connection.cursor()
            us_id = "SELECT user_id FROM registration WHERE user_id = %s"
            item_tuple = (user_id,)
            cursor.execute(us_id, item_tuple)
            record = cursor.fetchone()
            cursor.close()
            return record is not None

    def register_user(self, user_id, name):
        try:
            cursor = self.connection.cursor()
            insert_query = """ INSERT INTO registration (user_id, name) VALUES (%s,%s)"""
            item_tuple = (user_id, name)
            cursor.execute(insert_query, item_tuple)
            self.connection.commit()
            print("1 запись успешно вставлена")
            cursor.execute("SELECT * FROM registration")
            record = cursor.fetchall()
            print("Результат", record)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if self.connection:
                cursor.close()

    # def return_name_skill(self,user_id):
    #     cursor = self.connection.cursor()
    #     us_id = "SELECT user_id FROM registration WHERE user_id = %s"
    #     item_tuple = (user_id,)
    #     cursor.execute(us_id, item_tuple)
    #     record = cursor.fetchone()
    #     print(record[1],record[2])
    #     print(user_id)
    #     cursor.close()
