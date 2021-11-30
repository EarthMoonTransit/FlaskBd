import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="12345",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

#, login=records[2], password=[3]

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    record = dict(name=records[0][1], login=records[0][2], password=records[0][3])
    try:
        return render_template('account.html', record=record)
    except IndexError:
        return render_template('login.html', not_exist=True)