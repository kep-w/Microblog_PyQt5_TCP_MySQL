#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：评论模块，评论用到的方法

'''

from pymysql import *
from mainaction import *
from traceback import *

class Comments(MainAction):

    #评论id
    def setcommentid(self,commentid):
        self.commentid = commentid

    def getcommentid(self):
        return self.commentid

    #评论内容
    def setcommentinfo(self,commentinfo):
        self.commentinfo = commentinfo

    def getcommentinfo(self):
        return self.commentinfo

    #被评论动态id
    def setmessagesid(self,messagesid):
        self.messagesid = messagesid

    def getmessagesid(self):
        return self.messagesid

    #评论用户id
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid

    #评论时间
    def setcommentstime(self,commentstime):
        self.commentstime = commentstime

    def getcommentstime(self):
        return self.commentstime

    #发送用户用户名
    def setusername(self,username):
        self.username = username

    def getusername(self):
        return self.username

    # def setcommentlist(self,commentlist):
    #     self.commentlist = commentlist

    # def getcommentlist(self):
    #     return self.commentlist

    # def set(self,):
    #     self. = 

    # def get(self):
    #     return self.    
    def select_comment(self,messagesid,commentlist):
            self.mysql_link()
            self.yb.execute("select * from comment where messagesid = {};".format(messagesid))
            
            L = self.yb.fetchall()
            if not L:
                return
            for i in L:
                comm = Comments()
                comm.setcommentid(i[0])
                comm.setcommentinfo(i[1])
                comm.setmessagesid(i[2])
                comm.setuserid(i[3])
                comm.setcommentstime(i[4])
                sql_yu = "select username from users where userid = {};".format(comm.getuserid())
                self.yb.execute(sql_yu)
                Y = self.yb.fetchone()
                comm.setusername(Y[0])
                commentlist.append(comm)
            self.close_conn()


    #插入评论
    def insert_comment(self):
        try:
            self.mysql_link()
            messagesid = self.getmessagesid()
            messagesinfo = self.getcommentinfo()
            userid = self.getuserid()
            sql_yuju1 = """insert into comment(messagesid,commentinfo,userid) values(
            {},'{}',{});""".format(int(messagesid),escape_string(messagesinfo),int(userid))
            self.yb.execute(sql_yuju1)
            self.yb.execute("select commentid from comment where userid = {} order by messagesid desc limit 1;".format(userid))
            commentid = self.yb.fetchone()[0]
            self.yb.execute("""select userid from messages where messagesid = {};""".format(messagesid))
            acceptuserid = self.yb.fetchone()[0]
            sql_yuju2 = """insert into admin(messagesid,admintype,userid,acceptuserid,commentid)
             value({},'{}',{},{},{})""".format(messagesid,"2",userid,acceptuserid,commentid)
            self.yb.execute(sql_yuju2)
            self.conn.commit()
            return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0001'
        finally:
            self.close_conn()