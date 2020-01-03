from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("app.conf")  # 加载app的初始化文件

from PhotoShare import views, models


@app.route('/default')  # default页面
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()