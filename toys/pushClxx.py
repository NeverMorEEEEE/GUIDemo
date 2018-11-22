#!/usr/bin/python
#conding=utf-8
import os
import re
import time
import sys

import cx_Oracle as oracle


db=oracle.connect('tz_yth/oracle@10.80.79.12:1521/zjtz')
cr=db.cursor()

#查询include:select
def sqlSelect(sql,db):
        cr=db.cursor()
        cr.execute(sql)
        rs=cr.fetchall()
        cr.close()
        return rs

#插入、更新、删除操作之后需要提交include:insert、update、delete
def sqlDML(sql,db):
        cr=db.cursor()
        cr.execute(sql)
        cr.close()
        db.commit()

#execute DML with parameters
def sqlDML2(sql,params,db):
    cr = db.cursor()
    cr.execute(sql,params)
    cr.close()
    db.commit()



rs = sqlSelect("select * from sxxx where xzqh = '330482'",db=db)

for row in rs:
    print (type(row))

print(type(rs))

db.close()
