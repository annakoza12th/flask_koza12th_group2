import sqlite3
from flask import Flask, render_template, request, redirect, session, abort

app = Flask(__name__)

app.secret_key = 'https://github.com/annakoza12th/flask_koza12th_group2.git'


@app.route("/helloworld") 
def hello_world():
    return "<p>Hello, World!</p>"



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









@app.errorhandler(404)
def notfound(code):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)