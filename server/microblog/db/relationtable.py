#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：关注模块，关注用到的方法

'''

from pymysql import *
from mainaction import *


class Relation(MainAction):

    #用户关系id
    def setrelationid(self,relationid):
        self.relationid = relationid

    def getrelationid(self):
        return self.relationid

    #用户id
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid        
        
    #被关注用户id
    def setuserfollow(self,userfollow):
        self.userfollow = userfollow

    def getuserfollow(self):
        return self.userfollow       

    
    #关注时间
    def setrelationtime(self,relationtime):
        self.relationtime = relationtime

    def getrelationtime(self):
        return self.relationtime

    def insert_relation(self):
        self.mysql_link()
        userid = self.getuserid()
        userfollow = self.getuserfollow()
        sql_yuju = """insert into relation(userid,userfollow) values(
        {},{});""".format(int(userid),int(userfollow))
        try:
            self.yb.execute(sql_yuju)
            self.conn.commit()
            return '0000'
        except Exception:
            self.conn.rollback()
            return '0001'
        finally:
            self.close_conn()