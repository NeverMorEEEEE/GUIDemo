#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9

from flask import Flask, jsonify, request
import json
from flask_cors import *
from flask_restful import reqparse, abort, Api, Resource
import pymysql

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
# 创建连接
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wac', db='test', charset='utf8')
# # 创建游标
# cursor = conn.cursor()
import contextlib
#定义上下文管理器，连接后自动关闭连接
# @contextlib.contextmanager
# def mysql(host='127.0.0.1', port=3306, user='root', passwd='wac', db='test', charset='utf8'):
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# try:
#     yield cursor
# finally:
#     conn.commit()
#     cursor.close()
#     conn.close()

app = Flask(__name__)


@app.route('/HelloWorld',methods=['GET','POST'])
def hello_world():
    return "Hello World!"

@app.route('/user/<id>',methods=['GET','POST'])
def querUser(id):
    print(request.form)
    datax = request.form.to_dict()
    content = str(datax)
    print(datax)
    print(datax['userid']);
    cursor.execute('select * from user where id = ' + datax['userid'])
    user = cursor.fetchone()
    print(user)

    cursor.execute('select * from user where id = ' + id)
    list = cursor.fetchall()
    cursor.close()
    return  json.dumps(list)

@app.route('/user',methods=['DELETE'])
def delUser():
    print(request.form)
    datax = request.form.to_dict()
    content = str(datax)
    cursor.execute('delet from user where id = ' + id)
    list = cursor.fetchall()
    cursor.close()
    return  json.dumps(list)
# 查询博客
@app.route('/blog',methods=['GET','POST'])
def queryBlog(id):
    print(id)
    print(request.form)
    datax = request.form.to_dict()

    cursor.execute('select * from user where id = ' + id)
    list = cursor.fetchall()
    cursor.close()
    return  json.dumps(list)


def run():
    app.run(debug=True)

if __name__ == "__main__":
# 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)
