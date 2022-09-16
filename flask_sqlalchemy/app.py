from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zl_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
