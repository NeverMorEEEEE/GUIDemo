#!/usr/bin/python
#conding=utf-8
#-*-coding:utf-8-*-
import os
import re
import time
import sys
import uuid

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

def pushClxx():
    rs = sqlSelect("select * from sxxx where xzqh = '330482'", db=db)

    for row in rs:
        print(type(row))

    print(type(rs))

def addSxWarrant(sxid,bsc001,bsc010,type):
    id = str(uuid.uuid1());
    print('UUID : ' + id);
    record = {'id':id,'sxid':sxid,'bsc001':bsc001,'bsc001':bsc010,'type':type};
    sqlDML("insert into sx_warrant(id,sxid,bsc001,bsc010,warrant_type) values('" + id + "','" + sxid + "','" + bsc001
            + "','" + bsc010 + "','" + type + "')",db);


if __name__ == '__main__':
  #  rs = sqlSelect('select * from sxxx where bljg in (\'321\',\'324\',\'325\',\'326\')',db);
  rs = sqlSelect('select * from sxxx where bljg in (321,324,325,326)', db);

  for row in rs:
        print(row[0]);
        # cur = db.cursor();
        # cur.prepare('select count(1) from sx_warrant where sxid=:sxid');
        # result = cur.execute(None,{'sxid':row[0]});
        # print(result)
        # for res in result:
        #     print(res)

        result = sqlSelect("select count(1) from sx_warrant where sxid='"  + row[0] + "' and bsc010='1324'",db);

        print(result[0][0])
        if(result[0][0] == 0):
            addSxWarrant(row[0], '', '1324', '2');


