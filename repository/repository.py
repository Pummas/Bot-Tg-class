import psycopg2


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
