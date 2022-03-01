import sqlite3
from flask import Flask, render_template, request, redirect, session, abort

app = Flask(__name__)
app.secret_key = 'LJYOITUFrtyujkJHGFRERTYhjhnbvferTHJhgfdFGHJytr'


@app.route("/login") 
def login():
    return render_template('login.html')


@app.route('/register')
def register_get():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    name = request.form.get('name')
    password = request.form.get('password')
    conn = sqlite3.connect('flask_test.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?)", (name, password))
    conn.commit()
    conn.close()
    return redirect('/login')



@app.route('/list')
def list():
    return render_template('lists.html')





@app.errorhandler(404)
def notfound(code):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)