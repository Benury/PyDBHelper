#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pyodbc
class DB(object):
    conn = None;
    def __init__(self):
        print('aa')
        self.conn = pyodbc.connect(DRIVER='{SQL Server}', SERVER='localhost', DATABASE='LSQuesLib', UID='sa', PWD='123456')
        # self.conn = pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="article_splider",port=3306,charset="utf8")
    def getBySql(self,sql,*param):
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        self.conn.commit()
        return result
    def exeprocedure(self,sql,*param):
        cursor = self.conn.cursor()
        cursor.execute(sql,param)
        rows = cursor.fetchall()
        while rows:
            print(rows)
            if cursor.nextset():
                rows = cursor.fetchall()
            else:
                rows = None
    def executeOne(self,sql,*param):
        cursor = self.conn.cursor()
        effect_row = cursor.execute(sql,param)
        self.conn.commit()
        return effect_row
    def executeMany(self,sql,arr):
        cursor = self.conn.cursor()
        effect_row = cursor.executemany(sql,arr)
        self.conn.commit()
        return effect_row
    def executeGetOneID(self,sql,*param):
        cursor = self.conn.cursor()
        rowid = cursor.execute(sql, param)
        self.conn.commit()
        return cursor.lastrowid
    def executeGetManyID(self,sql,arr):
        cursor = self.conn.cursor()
        effect_row = cursor.executemany(sql, arr)
        self.conn.commit()
        return cursor.lastrowid

    def __del__(self):
        self.conn.close()
# import datetime
# start = datetime.datetime.now()
#
# db = DB()
# con = ("14","02",25)
# sql = """\
# DECLARE @out nvarchar(max);
# exec getQuesInit  '{0}','{1}',{2};
# SELECT @out;
# """.format(*con)
#
# db.exeprocedure(sql)
#
# end = datetime.datetime.now()
# print(end-start)