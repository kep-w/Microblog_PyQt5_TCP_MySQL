#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：用于储存管理员要发送的消息

'''
from pymysql import *
from mainaction import *
from messagestable import *
from traceback import *
class Admin(MainAction):
    #管理员id
    def setadminid(self,adminid):
        self.adminid = adminid
    
    def getadminid(self):
        return self.adminid
    
    #动态id
    def setmessagesid(self,messagesid):
        self.messagesid = messagesid

    def getmessagesid(self):
        return self.messagesid   
   
    #发送用户用户名
    def setusername(self,username):
        self.username = username

    def getusername(self):
        return self.username
    
    #消息类型
    def setadmintype(self,admintype):
        self.admintype = admintype

    def getadmintype(self):
        return self.admintype
    
    #发送消息的用户
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid
    #用户自己的ID
    def setacceptuserid(self,acceptuserid):
        self.acceptuserid = acceptuserid

    def getacceptuserid(self):
        return self.acceptuserid
    #消息时间
    def getadminstime(self):
        return self.adminstime
    
    def setadminstime(self,adminstime):
        self.adminstime = adminstime
    
    #设置用户对象
    def setmessagesobject(self,messagesobject):
        self.messagesobject = messagesobject

    def getmessagesobject(self):
        return self.messagesobject
    #设置评论内容
    def setcommentinfo(self,commentinfo):
        self.commentinfo = commentinfo

    def getcommentinfo(self):
        return self.commentinfo

    #评论id
    def setcommentid(self,commentid):
        self.commentid = commentid

    def getcommentid(self):
        return self.commentid

    # #查寻点赞转发消息
    # def select_mess(self,adminlist,):
    #     self.mysql_link()
    #     try:
    #         acceptuserid = self.getacceptuserid()
    #         sql_yuju1 = """select * from admin where acceptuserid={}
    #          and admintype='{}' order by adminid desc;""".format(acceptuserid,strtype)
    #         self.yb.execute(sql_yuju1)
    #         lst = self.yb.fetchall()
    #         if not lst:
    #             return '0001'  #没有点赞消息
    #         for i in lst:
    #             P = Admin()
    #             P.setadminid(i[0])
    #             P.setmessagesid(i[1])
    #             P.setuserid(i[3])
    #             P.setacceptuserid(i[4])
    #             P.setadminstime(i[5])
    #             mes = Messages()
    #             mes.select_messagesid(P.messagesid)
    #             P.setmissagesobject(mes)
    #             sql_yu = "select username from users where userid = {};".format(P.userid)
    #             self.yb.execute(sql_yu)
    #             Y = self.yb.fetchone()
    #             P.setusername(Y[0])
    #             adminlist.append(P)
    #             return "0000"
    #     except Exception:
    #         print_exc()
    #         return "0002"
    #     finally:
    #         self.close_conn()

    #查询评论消息
    def select_admin_info(self,adminlist):
        self.mysql_link()
        try:
            acceptuserid = self.getacceptuserid()
            sql_yuju1 = """select * from admin where acceptuserid={}
             and admintype='{}' order by adminid desc limit 10;""".format(acceptuserid,self.getadmintype())
            self.yb.execute(sql_yuju1)
            lst = self.yb.fetchall()
            if not lst:
                return '0001'  #没有点赞消息
            for i in lst:
                P = Admin()
                P.setadminid(i[0])
                P.setmessagesid(i[1])
                P.setadmintype(i[2])
                P.setuserid(i[3])
                P.setacceptuserid(i[4])
                P.setadminstime(i[5])
                mes = Messages()
                mes.select_messagesid(P.getmessagesid())
                P.setmessagesobject(mes)
                sql1 = "select username from users where userid = {} ;".format(P.getuserid())
                self.yb.execute(sql1)
                Y = self.yb.fetchone()
                P.setusername(Y[0])
                P.setcommentinfo('')
                

                if i[6] != -1:
                    P.setcommentid(i[6])
                    sql2 = """select commentinfo from comment where commentid={} 
                    ;""".format(P.getcommentid())
                    print("**************", sql2)
                    self.yb.execute(sql2)
                    Y = self.yb.fetchone()
                    P.setcommentinfo(Y[0])
                    
                adminlist.append(P)
            return "0000"
        except Exception:
            print_exc()
            return "0002"
        finally:
            self.close_conn()


