from typing import Optional

from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')  # запрос к данным формы
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            print(records)
            if records:
                return render_template('account.html', full_name=records[0][1])
            else:
                return render_template('error.html')
        elif request.form.get("registration"):
            return redirect("/registration/")
    else:
        return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name = request.form.get('name')
        login_user = request.form.get('login')
        password = request.form.get('password')
        cursor.execute(f"SELECT * FROM service.users WHERE login='{str(login_user)}'")
        account = list(cursor.fetchall())
        if not account:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                           (str(name), str(login_user), str(password)))
            conn.commit()

            return redirect('/login/')
        else:
            return render_template('error_registration.html')
    else:
        return render_template('registration.html')


# redirect - меняет URL (одну ссылку на другую)

# @app.route('/login/', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         if request.form.get("login"):
#             username = request.form.get('username')  # запрос к данным формы
#             password = request.form.get('password')
#             cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
#             records = list(cursor.fetchall())
#
#             cursor.close()
#             if records:
#                 return render_template('account.html', full_name=records[0][1])
#             else:
#                 return render_template('error.html')
#         elif request.form.get("registration"):
#             return redirect("/registration/")
#
#     return render_template('login.html')

#

# redirect - меняет URL (одну ссылку на другую)

# @app.route('/login/', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         if request.form.get("login"):
#             username = request.form.get('username')  # запрос к данным формы
#             password = request.form.get('password')
#             cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
#             records = list(cursor.fetchall())
#
#             cursor.close()
#             if records:
#                 return render_template('account.html', full_name=records[0][1])
#             else:
#                 return render_template('error.html')
#         elif request.form.get("registration"):
#             return redirect("/registration/")
#
#     return render_template('login.html')

# @app.route('/registration/', methods=['POST', 'GET'])
# def reg():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         login = request.form.get('login')
#         password = request.form.get('password')
#
#         cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
#                        (str(name), str(login), str(password)))
#         conn.commit()
#
#         return redirect('/login/')
#
#     return render_template('registration.html')