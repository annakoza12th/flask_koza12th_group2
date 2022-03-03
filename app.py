import sqlite3
from flask import Flask, render_template, request, redirect, session, abort

app = Flask(__name__)
app.secret_key = 'LJYOITUFrtyujkJHGFRERTYhjhnbvferTHJhgfdFGHJytr'


@app.route("/")
def top():
    return render_template('index.html')


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
    conn = sqlite3.connect('2022_03_03.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?)", (name, password))
    conn.commit()
    conn.close()
    return redirect('/login')



@app.route('/list')
def food_list():
    conn = sqlite3.connect("food_tracking.db")
    c = conn.cursor()
    c.execute("SELECT * from lists;")
    food_lists = []
    for row in c.fetchall():
        food_lists.append({"check":row[5], "id":row[0], "date":row[1], "food":row[2], "category":row[3], "stock":row[4]})
    print(food_lists)
    c.close
    return render_template('lists.html', food_lists=food_lists)



@app.errorhandler(404)
def notfound(code):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)