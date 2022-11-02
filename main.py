
from flask import Flask
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)


@app.route('/')
def hello():
    try:
        connection = mysql.connector.connect(host=os.getenv('HOST'),
                                             database=os.getenv('DATABASE'),
                                             user=os.getenv('USER'),
                                             password=os.getenv('PASSWORD'))
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("hostname: ",os.getenv('HOST'))
        print("DB: ",os.getenv('DATABASE'))
        print("username: ",os.getenv('USER'))
        print("password: ",os.getenv('DATABASE_PASSWORD'))
        print("Error while connecting to MySQL", e)
        
    return '<h1>Hello, World!</h1>'
