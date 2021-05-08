import mysql.connector
from mysql.connector import Error

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock





import time

def create_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("sql3.freemysqlhosting.net", "sql3410985", "UAJI17ZhCS","sql3410985")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


pin13_on = """
UPDATE
    lights
SET
    activated = 1
WHERE
    id = 1
"""

pin13_off = """
UPDATE
    lights
SET
    activated = 0
WHERE
    id = 1
"""





class ArdApplication(Widget):

    def turn_on(instance):
        execute_query(connection, pin13_on)

    def turn_off(instance):
        execute_query(connection, pin13_off)





class Arduino2App(App):
    def build(self):
        Ard = ArdApplication()
        return Ard


if __name__ in ('__main__', '__android__'):
    Arduino2App().run()

