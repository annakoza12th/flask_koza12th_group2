from crypt import methods
from operator import methodcaller
import sqlite3
import datetime
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
    conn = sqlite3.connect("2022_03_03.db")
    c = conn.cursor()
    c.execute("SELECT * from lists;")
    food_lists = []
    for row in c.fetchall():
        food_lists.append({"id":row[0], "date":row[1], "food":row[2], "category":row[3], "stock":row[4], "priority":row[5], "check":row[6]})
    # print(food_lists)
    c.close
    return render_template('lists.html', food_lists=food_lists)

@app.route('/list_register')
def list_register():
    return render_template('/list_register.html')

@app.route('/list_register', methods=['POST'])
def food_post():
    food = request.form.get('food')
    category = request.form.get('category')
    priority = request.form.get('priority')
    stock = request.form.get('stock')
    dt_now = datetime.datetime.now()
    date = dt_now.strftime('%Y/%m/%d')
    check = 1
    user_id = 1
    conn = sqlite3.connect('2022_03_03.db')
    c = conn.cursor()
    c.execute("INSERT INTO lists VALUES(null,?,?,?,?,?,?,?)", (date, food, category, priority, stock, check, user_id,))
    conn.commit()
    conn.close()
    
    # Todo：ユーザーID 追加、DB にも外部キーで追加必須
    # user_id = session.get('user_id')

    return redirect('/list')
    
@app.route('/list_del/<int:id>/', methods=['POST'])
def food_del(id):
    print(id)
    conn = sqlite3.connect('2022_03_03.db')
    c = conn.cursor()
    c.execute("DELETE FROM lists WHERE id = ?", (id,))

    return redirect('/list')

@app.errorhandler(404)
def notfound(code):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)