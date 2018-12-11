from flask import Flask, jsonify, request
import json
from flask_cors import *
from flask_restful import reqparse, abort, Api, Resource
import pymysql


app = Flask(__name__)


@app.route('/HelloWorld',methods=['GET','POST'])
def hello_world():
    print(request.method);
    print(request.form);
    print(request.headers.get('X-Real-Ip'));
    return "Hello World!";

@app.route('/sso',methods=['GET','POST'])
def sso():
    print(request.method);
    print(request.form);
    print(request.headers.get('X-Real-Ip'));
    return "Hello World!SSO";

@app.route('/demo',methods=['GET','POST'])
def demo():
    print(request.method);
    print(request.form);
    print(request.headers);
    print(request.headers.get('X-Real-Ip'));
    return "Hello World!DEMO";

def run():
    app.run(debug=True)

if __name__ == "__main__":
# 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True,host='178.22.22.239',port=5000)
