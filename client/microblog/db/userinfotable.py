#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：详细信息模块，详细信息用到的方法

'''

from pymysql import *
from mainaction import *
from traceback import *


# user_id int primary key auto_increment,
#             user_nikename varchar(60) not null,
#             user_passwd varchar(40) not null,
#             user_email varchar(80),
#             user_time timestamp
class UserInfo(MainAction):

    #详细信息id
    def setuserinfoid(self, userinfoid):
        self.userinfoid = userinfoid
    def getuserinfoid(self):
        return self.userinfoid
    
    #昵称
    def setnickename(self,nickename):
        self.nickename = nickename

    def getnickename(self):
        return self.nickename   
   
    #性别
    def setgender(self,gender):
        self.gender = gender

    def getgender(self):
        return self.gender
    
    #生日
    def setbirthday(self,birthday):
        self.birthday = birthday

    def getbirthday(self):
        return self.birthday
   
    #个人介绍
    def getintroduce(self):
        return self.introduce
    
    def setintroduce(self,introduce):
        self.introduce = introduce
   
    #邮箱
    def setemail(self,email):
        self.email = email

    def getemail(self):
        return self.email

    #手机号
    def setphonenumber(self,phonenumber):
        self.phonenumber = phonenumber

    def getphonenumber(self):
        return self.phonenumber    
    #发表微博数
    def setpublishnum(self,publishnum):
        self.publishnum = publishnum

    def getpublishnum(self):
        return self.publishnum

     #点赞数
    def setlaudnum(self,laudnum):
        self.laudnum = laudnum

    def getlaudnum(self):
        return self.laudnum        

    #注册时间
    def setregisttime(self,registtime):
        self.registtime = registtime

    def getregisttime(self):
        return self.registtime        

    #用户ID
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid       

    #新建用户详细信息
    def insert_info(self,yb,userid,email,phonenumber):
       
       sql_yuju = """insert into userinfo(email,phonenumber,userid) 
       values('{}','{}',{});""".format(escape_string(email),escape_string(phonenumber),userid)
       yb.execute(sql_yuju)

    #更新信息
    def update_info(self):
        try:    
            L = self.__dict__
            userid = L['userid']            
            del L['userid']
            print(L)
            l = ''
            
            for k in L:
                l += '{}='.format(k)
                l += '"'+escape_string(L[k])+'",'
            l = l[0:-1]
            s = len(l)
            sql_yuju = "update userinfo set " + l +" where userid={};".format(userid)
            print(sql_yuju)
            self.mysql_link()
            self.yb.execute(sql_yuju)
            self.conn.commit()
            return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0002'
        finally:
            self.close_conn()

   #查询用户详细信息
    def select_userinfo(self):
        self.mysql_link()

        try:
            sql_yu="select * from userinfo where userid={};".format(self.getuserid())
            self.yb.execute(sql_yu)
            
            L = self.yb.fetchone()
            if not L:
                return '0001'
           
            self.setuserinfoid (L[0])
            self.setnickename(L[1])
            self.setgender(L[2])
            self.setbirthday(L[3])
            self.setemail(L[4])
            self.setphonenumber(L[5])
            self.setintroduce(L[6])
            self.setpublishnum(L[7])
            self.setlaudnum(L[8])
            self.setregisttime(L[9])
            self.setuserid(L[10])
            return '0000'
        except Exception as e:
            print_exc()

            return '0002' 
        finally:

            self.close_conn()
            del self.conn,self.yb

        





        

