from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')  # запрос к данным формы
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall()) # грубо говроя "список" ввседенных данных
    cursor.close() #закрыли соnnet
    if records:  # если находит значания
        return render_template('account.html', full_name=records[0][1])
    else: # если не нашел данные в базе данных
        return render_template('error.html') # открывает файл error
