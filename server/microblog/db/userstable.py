#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：登录信息模块，登录退出用到的方法
'''



from pymysql import *
from mainaction import *
from messagestable import *
from userinfotable import *
from traceback import *
class Users(MainAction):

    #用户ID
    def setuserid(self,userid):
        self.userid = userid

    def getuserid(self):
        return self.userid   

    #用户名
    def setusername(self,username):
        self.username = username

    def getusername(self):
        return self.username   

    #密码
    def setuserpasswd(self,userpasswd):
        self.userpasswd = userpasswd

    def getuserpasswd(self):
        return self.userpasswd  

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


    #注册时间
    def setregisttime(self,registtime):
        self.registtime = registtime

    def getregisttime(self):
        return self.registtime   

    #登录状态
    def setloginstatus(self,loginstatus):
        self.loginstatus = loginstatus

    def getloginstatus(self):
        return self.loginstatus
 


    # def set(self,):
    #     self. = 

    # def get(self):
    #     return self. 
    



    #用户注册
    def register_user(self):
        '''
        0000 注册成功
        0001 该账号以注册
        0002 系统错误
        '''
        try:
            
            self.mysql_link()

            username = self.getusername()
            

            sql_yuju ="select * from users where username = '{}';".format(escape_string(username))
            s = self.yb.execute(sql_yuju)
            if s == 0:
                
                self.inset_users()
                self.yb.execute(sql_yuju)
                L=self.yb.fetchone()
                self.setuserid(L[0])
                uinfo=UserInfo()
                uinfo.insert_info(self.yb,self.getuserid(),self.getemail(),self.getphonenumber())
                self.conn.commit()
                
                return "0000"

            return "0001"
        except Exception as e:
            print_exc()
            self.conn.rollback()
            # self.conn.commit()
            return "0002"
        finally:
           self.close_conn()

    
    #用户登录 
    def user_login(self):
        '''
        0000　登录成功
        0001 用户以登录
        0002 账号错误
        0003 密码错误
        0004 系统错误
        '''
        try:
            self.mysql_link()
            username = self.getusername()
            passwd = self.getuserpasswd()

            sql_yuju ="select * from users where username = '{}';".format(escape_string(username))
            s = self.yb.execute(sql_yuju)
            if s == 0:
                return "0002"
            else:
                y = self.yb.fetchone()
                if self.userpasswd != y[2]:
                    return "0003"
            #设置用户id
            self.setuserid(y[0])
            #设置注册时间
            self.setregisttime(y[5])
            #设置登录状态
            self.setloginstatus(y[-1])
            #设置邮箱
            self.setemail(y[3])
            #设置在手机号
            self.setphonenumber(y[4])
            # if self.loginstatus == 1:
            #     return '0001'

            # #修改登录状态
            # self.land_state()
            return "0000"
        except Exception as e:
            print_exc()
            return '0004'
        finally:
            #关闭数据库链接
            self.close_conn()

    
    def inset_users(self):
        '''
        存储数据　
        不能主动调用
        '''
        username = self.getusername()
        passwd = self.getuserpasswd()
        email = self.getemail()
        phonenumber = self.getphonenumber()
        sql_yuju = """insert into users(username,userpasswd,email,phonenumber) values(
        '{}','{}','{}','{}');""".format(escape_string(username),escape_string(passwd),escape_string(email),escape_string(phonenumber))
           
        self.yb.execute(sql_yuju)


    #登录
    def land_state(self):
        '''
        设置为登录状态
        不能主动调用
        '''
        userid = self.getuserid()
        sql_yuju = 'update users set loginstatus = 1 where userid = {};'.format(int(userid))
        self.yb.execute(sql_yuju)
        self.setloginstatus(1)
        self.conn.commit()

    #退出登录
    def exit_logon(self):
        '''
        用户下线调用
        '''
        self.mysql_link()

        userid = self.getuserid()
        sql_yuju = 'update users set loginstatus = 0 where userid = {};'.format(int(userid))
        self.yb.execute(sql_yuju)
        self.setloginstatus(0)
        self.conn.commit()
        self.close_conn()

    def attribute_setting(self):

        self.mysql_link()
        userid = self.getuserid()
        sql_yuju ="select * from users where userid = {};".format(int(userid))
        self.yb.execute(sql_yuju)
        y = self.yb.fetchone()
         #设置用户名
        self.setusername(y[1])
        #设置邮箱
        self.setemail(y[3])
        #设置在手机号
        self.setphonenumber(y[4])
        #设置登录时间
        self.setregisttime(y[5])
        #设置登录状态
        self.setloginstatus(y[-1])
        #关闭数据库链接
        self.close_conn()
    #修改密码
    def modify_passwd(self,strin):

        try:
            self.mysql_link()
            username = self.getusername()
            passwd = self.getuserpasswd()

            sql_yuju ="select * from users where username = '{}' and userpasswd='{}';".format(escape_string(username),escape_string(passwd))
            s = self.yb.execute(sql_yuju)
            if s == 0:
                return "0001"
            else:
                sql_yuju ="update users set userpasswd='{}' where username = '{}';".format(escape_string(strin),escape_string(username))
                self.yb.execute(sql_yuju)
                self.conn.commit()
                return '0000'
        except Exception as e:
            print_exc()
            self.conn.rollback()
            return '0002'
        finally:
            #关闭数据库链接
            self.close_conn()







            
