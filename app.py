import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Chad Clevenger in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://chad_hello_postgres_user:nvjjZl7kwrlAL6CxwJSiBTozpVf3Ahfx@dpg-d46kpaili9vc73aspd4g-a/chad_hello_postgres")
    conn.close()
    return "Database Connection Successful"

