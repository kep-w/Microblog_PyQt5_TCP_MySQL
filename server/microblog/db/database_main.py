#!/usr/bin/env python3
#coding = utf-8
'''
name：谢康
功能：主控制流程

'''

from messagestable import *
from weibomysql import *
from userstable import *
from admin import *
from relationtable import *
class MyDatabase():
    #检查库表
    def update_database(self):
        lib = WeiBo()
        lib.init_database()
    
    #注册
    def weibo_register(self,user):
        '''
        0000 注册成功
        0001 该账号以注册
        0002 系统错误
        '''
        state = user.register_user()

        return state


    #用户登录
    def weibo_login(self,user):
        '''
        0000　登录成功
        0001 用户以登录
        0002 账号错误
        0003 密码错误
        0004 系统错误
        '''
        state = user.user_login()
        return state

    #退出登录　修改登录状态
    def wei_quit(self,user):
        user.exit_logon()

    #更新用户信息
    def update_userinfo(self,user):
        '''
        0000　更新成功
        0001 更新失败
        不需要全部更新
        '''
        state = user.update_info()
        return state

    #修改密码
    def modify_passwd(self,user,strin):
        '''
        0000 修改成功
        0001 密码输入错误
        0003 系统错误

        '''

        state = user.modify_passwd(strin)
        return state



    #按时间顺序返回动态信息
    def time_order(self):
        '''
        查看全部动态调用
        0000　成功
        0001 无动态
        0002 系统错误
        '''
        messagelist = []
        p = Messages()

        state = p.select_time_order(messagelist)
        return state,messagelist

    #按热度顺序返回动态信息
    def heat_order(self):
        '''
        查看热度顺序动态调用
        0000　成功
        0001 无动态
        0002 系统错误
        '''
        messagelist = []
        p = Messages()

        state = p.select_heat_order(messagelist)
        return state,messagelist

    # 返回关注的好友动态
    def follow_time_oder(self,user):
        '''传入ｕｓｅｒ对象要有userid属性
            0000　成功
            0001 无动态
            0002 系统错误
        '''
        messagelist = []
        p = Messages()

        state = p.select_follow_order(user,messagelist)
        return state,messagelist

    #返回模糊查询动态
    def vague_query(self,strin):
        '''传入字符串
            0000　成功
            0001 无动态
            0002 系统错误
        '''
        messagelist = []
        p = Messages()

        state = p.select_vague_time(strin,messagelist)
        return state,messagelist



    #写入动态
    def publish_dynamic(self,mes):
        '''传入绑定属性动态类对象'''
        state = mes.write_dynamic()
        return state
    #点赞
    def agree_with(self,mes):
        "传入带有动态ｉｄ的动态类对象"
        state = mes.agree_with()
        return state
    #转发
    def forward(self,mes):
        """传入带有动态ｉｄ的
                  和用户id属性对象"""
        state = mes.forward()
        return state
    #评论
    def write_comment(self,comm):
        "传入绑定属性的评论类对象"
        state = comm.insert_comment()
        return state

    #关注用户
    def follow_user(self,rel):
        "传入绑定两个用户ｉｄ的关注类对象"
        state = rel.insert_relation()
        return state

    #查寻用户详细信息
    def main_select_userinfo(self,user):
        """传入用户id
        　　　0000 查询成功
        　　　0001 无此用户信息
        　　　0002 系统错误"""
        start=user.select_userinfo()
        return start

    # #查询点赞管理员消息
    # def main_select_agree(self,adm):
    #     """传入带用户id的对像
    #     　　　0000 成功
    #        0001 无消息
    #        0002 系统错误"""
    #     adminlist=[]
    #     start = adm.select_mess(adminlist,'0')
    #     return start,adminlist

    # #查询点赞管理员消息
    # def main_select_forward(self,adm):
    #     """传入带用户id的对像
    #     　　　0000 成功
    #        0001 无消息
    #        0002 系统错误"""
    #     adminlist=[]
    #     start = adm.select_mess(adminlist,'1')
    #     return start,adminlist

    #查询已发微博的动态
    def main_select_admin_info(self,adm):
        """传入带用户id的对像
        　　　0000 成功
           0001 无消息
           0002 系统错误"""
        adminlist=[]
        start = adm.select_admin_info(adminlist)
        return start,adminlist




if __name__ == "__main__":
    P = MyDatabase()
    P.update_database()
    # P.update_database()
    # s,L = P.time_order()
    # print(s)
    # for i in L:
    #     print(i.username)
    # user = Admin()
    # user.setacceptuserid(18)
    # user.setmessagesid(2)
    # user.setcommentinfo('123456')
    # user.setmessagesid(2)
    # s = '1234456'
    # user.email='sadaa'
    # user.phonenumber='sdsdsaa'
    # user.setuserid(18)
    # user.setmessagesid(1)
    # s,L = P.main_select_comment(user)
    # print(L[0].__dict__)
    # print(L[0].missagesobject.__dict__)
    # print(L[0].missagesobject.commentlist[0].__dict__)
    # print(user.__dict__)