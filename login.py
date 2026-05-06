# from flask import Flask, render_template, request, redirect, session
# import pymysql
# import hashlib

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'


# def get_db_connection():
#     return pymysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         database='flask_auth',
#         cursorclass=pymysql.cursors.DictCursor
#     )

# # Home
# @app.route('/')
# def home():
#     if 'loggedin' in session:
#         return render_template('home.html', username=session['username'])
#     return redirect('/login')

# # Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = hashlib.sha256(request.form['password'].encode()).hexdigest()

#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
#             (username, email, password)
#         )

#         conn.commit()
#         conn.close()

#         return redirect('/login')

#     return render_template('register.html')

# # Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = hashlib.sha256(request.form['password'].encode()).hexdigest()

#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT * FROM users WHERE email=%s AND password=%s",
#             (email, password)
#         )

#         account = cursor.fetchone()
#         conn.close()

#         if account:
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             return redirect('/')
#         else:
#             return "Invalid credentials"

#     return render_template('login.html')

# # Logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, session, url_for
import pymysql
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='flask_auth',
        cursorclass=pymysql.cursors.DictCursor
    )

# Root (decides where to go)
@app.route('/')
def index():
    if 'loggedin' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        account = cursor.fetchone()
        conn.close()

        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

# Home (after login)
@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)