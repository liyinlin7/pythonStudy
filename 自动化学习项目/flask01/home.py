from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/index')
def index_xxx():
    return render_template('/html/home.html')


@app.route('/commit')
def commit():
    return "交互成功"


app.debug = True
app.run()
