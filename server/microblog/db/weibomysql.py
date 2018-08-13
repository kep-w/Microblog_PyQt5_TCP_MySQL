#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：建库建表模块，用于检查库表是否建立

'''


from pymysql import *
from config.conf import *
import warnings
warnings.filterwarnings('ignore')
class WeiBo():
    #初始化建立与数据库连接
    def init_database(self):
        #连接数据库
        L = getdbdic()

        conn  = connect(host= L["host"],port = int(L["port"]),user = L["username"],
            passwd = L["passwd"],charset = L["charset"])
        yb=conn.cursor()
        self.conn = conn
        self.yb = yb
        #weibo库初始化

        self.yb.execute("create database if not exists weibo DEFAULT CHARSET = UTF8;")
        self.yb.execute("use weibo;")
        
        # users用户注册表初始化
        self.yb.execute("""create table if not exists users(
            userid int primary key auto_increment,
            username varchar(60) not null,
            userpasswd varchar(40) not null,
            email varchar(40) not null,
            phonenumber varchar(20) not null,            
            registtime timestamp,
            loginstatus int default 0
            )DEFAULT CHARSET = UTF8;""")
        
        #userinfo用户详细信息表初始化
        self.yb.execute("""create table if not exists userinfo(
            userinfoid int primary key auto_increment,
            nickename varchar(60) default ' ',
            gender varchar(4) default ' ',
            birthday varchar(20) default ' ',
            email varchar(40) not null,
            phonenumber varchar(20) not null,
            introduce varchar(300) default ' ',
            publishnum int default 0,
            laudnum int default 0,
            registtime timestamp,
            userid int,
            foreign key(userid) 
            references users(userid) 
            on delete cascade 
            on update cascade
            )DEFAULT CHARSET = UTF8;""")

        # Relation用户关系表 结构 用户Id user_id : 被关注id user_follow 
        self.yb.execute("""create table if not exists relation(
            relationid int primary key auto_increment,
            userid int,
            userfollow int,
            relationtime timestamp, 
            foreign key(userid) 
            references users(userid) 
            on delete cascade 
            on update cascade,
            foreign key(userfollow) 
            references users(userid) 
            on delete cascade 
            on update cascade
            )DEFAULT CHARSET = UTF8;""")
        

        #messages微博动态表初始化

        self.yb.execute("""create table if not exists messages(
                            messagesid int primary key auto_increment,
                            userid int,
                            messagesinfo varchar(500) not null,
                            messagesagreenum int default 0,
                            messagestranspondnum int default 0,
                            messagestime timestamp,
                            foreign key(userid) 
                            references users(userid) 
                            on delete cascade 
                            on update cascade)DEFAULT CHARSET = UTF8;""")
            
        #comment评论表初始化

        self.yb.execute("""create table if not exists comment(
                        commentid int primary key auto_increment,
                        commentinfo char(100),
                        messagesid int,
                        userid int,
                        commentstime timestamp,
                        foreign key(messagesid)
                        references messages(messagesid) 
                        on delete cascade 
                        on update cascade,
                        foreign key(userid)
                        references users(userid) 
                        on delete cascade 
                        on update cascade)DEFAULT CHARSET = UTF8;""")


        #管理员消息        
        self.yb.execute("""create table if not exists admin(
                        adminid int primary key auto_increment,
                        messagesid int,
                        admintype varchar(20),
                        userid int,
                        acceptuserid int,    
                        adminstime timestamp,
                        commentid int default -1,
                        foreign key(messagesid)
                        references messages(messagesid) 
                        on delete cascade 
                        on update cascade,
                        foreign key(userid)
                        references users(userid) 
                        on delete cascade 
                        on update cascade,
                        foreign key(acceptuserid)
                        references users(userid) 
                        on delete cascade 
                        on update cascade)DEFAULT CHARSET = UTF8;""")
  
        
        self.yb.close()
        self.conn.close()    

if __name__ == '__main__':

    p =WeiBo()
    p.init_database()
