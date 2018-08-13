#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：数据库连接模块，用于建立数据库连接和关闭
'''

from pymysql import *
from config.conf import *
class MainAction():


    #数据库连接
    def mysql_link(self):
        L = getdbdic()
        conn  = connect(host= L["host"],port = int(L["port"]),user = L["username"],
            passwd = L["passwd"],db = L["database"],charset = L["charset"])
        yb=conn.cursor()
        self.conn = conn
        self.yb = yb

    #数据库关闭
    def close_conn(self):
        self.yb.close()
        self.conn.close()
    
