#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：动态模块，动态用到的方法

'''

from pymysql import *
from mainaction import *
from commentstable import *
from traceback import *
class Messages(MainAction):

    #动态id
    def setmessagesid(self,messagesid):
        self.messagesid = messagesid

    def getmessagesid(self):
        return self.messagesid

    #发送用户id
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid
    #发送用户用户名
    def setusername(self,username):
        self.username = username

    def getusername(self):
        return self.username


    #动态内容
    def setmessagesinfo(self,messagesinfo):
        self.messagesinfo = messagesinfo

    def getmessagesinfo(self):
        return self.messagesinfo

    #点赞次数
    def setmessagesagreenum(self,messagesagreenum):
        self.messagesagreenum = messagesagreenum

    def getmessagesagreenum(self):
        return self.messagesagreenum

    #转发次数
    def setmessagestranspondnum(self,messagestranspondnum):
        self.messagestranspondnum = messagestranspondnum

    def getmessagestranspondnum(self):
        return self.messagestranspondnum

    #发送时间
    def setmessagestime(self,messagestime):
        self.messagestime = messagestime

    def getmessagestime(self):
        return self.messagestime
    
    def setcommentlist(self,commentlist):
        self.commentlist = commentlist

    def getcommentlist(self):
        return self.commentlist    

    # def set(self,):
    #     self. = 

    # def get(self):
    #     return self.

    # 时间顺序返回动态
    def select_time_order(self,messagelist):
        self.mysql_link()
        try:
            self.yb.execute("select * from messages order by messagesid desc;")
            
            L = self.yb.fetchall()
            if not L:
                return '0001'
            for i in L:
                p = Messages()
                p.setmessagesid(i[0])
                p.setuserid(i[1])
                p.setmessagesinfo(i[2])
                p.setmessagesagreenum(i[3])
                p.setmessagestranspondnum(i[4])
                p.setmessagestime(i[5])
                sql_yu = "select username from users where userid = {};".format(p.getuserid())
                self.yb.execute(sql_yu)
                Y = self.yb.fetchone()
                p.setusername(Y[0])
                s = Comments()
                p.setcommentlist([])
                s.select_comment(p.getmessagesid(),p.getcommentlist())
                
                messagelist.append(p)
            return '0000'
        except Exception as e:
            print_exc()
            messagelist = []

            return '0002'
        finally:
            self.close_conn()

    #热度
    def select_heat_order(self,messagelist):
        self.mysql_link()
        try:
            self.yb.execute("select * from messages order by messagesagreenum desc;")
            
            L = self.yb.fetchall()
            if not L:
                return 
            for i in L:
                p = Messages()
                p.setmessagesid(i[0])
                p.setuserid(i[1])
                p.setmessagesinfo(i[2])
                p.setmessagesagreenum(i[3])
                p.setmessagestranspondnum(i[4])
                p.setmessagestime(i[5])
                sql_yu = "select username from users where userid = {};".format(p.getuserid())
                self.yb.execute(sql_yu)
                Y = self.yb.fetchone()
                p.setusername(Y[0])
                p.setcommentlist([])
                s = Comments()
                s.select_comment(p.getmessagesid(),p.getcommentlist())
                
                messagelist.append(p)
            return '0000'
        except Exception as e:
            print_exc()
            messagelist = []

            return '0002'
        finally:
            self.close_conn()

    #按id查询
    def select_messagesid(self,messagesid):
        self.mysql_link()
        try:
            sql_yuju = "select * from messages where messagesid ={};".format(messagesid)
            self.yb.execute(sql_yuju)
            
            L = self.yb.fetchone()
            
            self.setmessagesid(L[0])
            self.setuserid(L[1])
            self.setmessagesinfo(L[2])
            self.setmessagesagreenum(L[3])
            self.setmessagestranspondnum(L[4])
            self.setmessagestime(L[5])
            sql_yu = "select username from users where userid = {};".format(self.getuserid())
            self.yb.execute(sql_yu)
            Y = self.yb.fetchone()
            self.setusername(Y[0])
            self.setcommentlist([])
            s = Comments()
            s.select_comment(self.getmessagesid(),self.getcommentlist())
                
            return '0000'
        except Exception as e:
            print_exc()
            return '0002'
        finally:
            self.close_conn()


    #关注动态
    def select_follow_order(self,user,messagelist):
        self.mysql_link()
        try:
            sql_yu = "select * from relation where userid= {};".format(int(user.getuserid()))
            self.yb.execute(sql_yu)
            H = self.yb.fetchall()
            if not H:
                return "0001"
            foll = []
            l = 0
            for x in H:
                l += 1
                foll.append(x[2])
            
            fo = ("{},"*l).format(*foll)
            fo = fo[0:-1]
            sql_yu = ("select * from messages where userid in("+'{}'+") order by messagesagreenum desc;").format(fo)
            self.yb.execute(sql_yu)
            L = self.yb.fetchall()
            if not L:
                return '0001'
            for i in L:
                p = Messages()
                p.setmessagesid(i[0])
                p.setuserid(i[1])
                p.setmessagesinfo(i[2])
                p.setmessagesagreenum(i[3])
                p.setmessagestranspondnum(i[4])
                p.setmessagestime(i[5])
                sql_yu = "select username from users where userid = {};".format(p.getuserid())
                self.yb.execute(sql_yu)
                Y = self.yb.fetchone()
                p.setusername(Y[0])
                p.setcommentlist([])
                s = Comments()
                s.select_comment(p.getmessagesid(),p.getcommentlist())
                
                messagelist.append(p)
            return '0000'
        except Exception as e:
            print_exc()
            messagelist = []

            return '0002'
        finally:
            self.close_conn()

    #模糊查寻
    def select_vague_time(self,strin,messagelist):
        self.mysql_link()

        try:
            sql_yu="select * from messages where messagesinfo like '%"+strin+"%' order by messagesid desc;"
            print(sql_yu)
            self.yb.execute(sql_yu)
            
            L = self.yb.fetchall()
            if not L:
                self.close_conn()
                state = self.select_time_order(messagelist)
                return state
            for i in L:
                p = Messages()
                p.setmessagesid(i[0])
                p.setuserid(i[1])
                p.setmessagesinfo(i[2])
                p.setmessagesagreenum(i[3])
                p.setmessagestranspondnum(i[4])
                p.setmessagestime(i[5])
                sql_yu = "select username from users where userid = {};".format(p.userid)
                self.yb.execute(sql_yu)
                Y = self.yb.fetchone()
                p.setusername(Y[0])
                p.setcommentlist([])
                s = Comments()
                s.select_comment(p.getmessagesid(),p.getcommentlist())
                
                messagelist.append(p)
            self.close_conn()
            return '0000'
        except Exception as e:
            print_exc()
            messagelist = []

            self.close_conn()
            return '0002'
        
    #写入动态
    def write_dynamic(self):
        self.mysql_link()
        userid = self.getuserid()
        messagesinfo = self.getmessagesinfo()
        sql_yuju = """insert into messages(userid,messagesinfo) values(
        {},'{}');""".format(int(userid),escape_string(messagesinfo))
        sql = """update userinfo set phonenumber=phonenumber+1 where userid={};""".format(int(userid))
        try:
            self.yb.execute(sql_yuju)
            self.yb.execute(sql)
            self.conn.commit()
            return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0001'
        finally:
            self.close_conn()

    #点赞
    def agree_with(self):
        self.mysql_link()
        messagesid = self.getmessagesid()
        userid = self.getuserid()

        sql_yuju1 = """update messages set messagesagreenum=messagesagreenum+1 where messagesid={};""".format(messagesid)
        sql_yuju2 = """update userinfo set laudnum=laudnum+1 where userid={};""".format(userid)
        self.yb.execute("""select userid from messages where messagesid = {};""".format(messagesid))
        acceptuserid = self.yb.fetchone()[0]
        sql_yuju3 = """insert into admin(messagesid,admintype,userid,acceptuserid)
         value({},{},{},{})""".format(messagesid,'0',userid,acceptuserid)
        try:
            self.yb.execute(sql_yuju1)
            self.yb.execute(sql_yuju2)
            self.yb.execute(sql_yuju3)
            self.conn.commit()
            return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0001'
        finally:
            self.close_conn()

    #转发
    def forward(self):
        self.mysql_link()
        try:
            messagesid = self.getmessagesid()
            userid = self.getuserid()
            sql_yuju1 = """update messages set messagestranspondnum=messagestranspondnum+1 where messagesid={};""".format(int(messagesid))
            self.yb.execute("""select userid from messages where messagesid = {};""".format(messagesid))
            acceptuserid = self.yb.fetchone()[0]
            sql_yuju2 = """insert into admin(messagesid,admintype,userid,acceptuserid)
             value({},'{}',{},{})""".format(messagesid,"1",userid,acceptuserid)
            self.yb.execute(sql_yuju1)
            self.yb.execute(sql_yuju2)
            self.conn.commit()
            return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0001'
        finally:
            self.close_conn()





