#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-13
# Version: v0.5

'''
页面调用的主函数
负责全部前端页面的调用及逻辑处理
负责所有页面按钮的监控及按钮相关事件的调用

'''

import sys
import re
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets


# 导入页面相关模块
from page.Ui_signin_signup import Ui_Login
from page.Ui_signup import Ui_Signup
from page.Ui_me import Ui_me
from page.Ui_me_changeinfo import Ui_changeinfo
from page.Ui_me_changepwd import Ui_changepwd
from page.Ui_login_tip import Ui_tip
from page.Ui_home_page import Ui_Home
from page.Ui_send_comment import Ui_SendComment
from page.Ui_details import Ui_Detail
from page.Ui_send_blog import Ui_Blog
from page.Ui_remind import Ui_remind
from page.Ui_search import Ui_Search
from page.news_main import Ui_message1
# 客户端接口模块
from client_deal.client_msg_deal import ClientMsgDeal


# 初始化客户端服务接口
client = ClientMsgDeal()


# 定义主类, 负责页面按钮相关事件的处理及页面间调用
class Main(object):
    """处理页面逻辑调用的类, 包含按钮监控及事件处理"""

    # 初始化全部调用页面
    def __init__(self, client):
        self.client = client
        # 将用到的页面类初始化
        self.tip = Ui_tip()
        self.info = Ui_changeinfo(self.client)
        self.signin = Ui_Login(self.client)
        self.signup = Ui_Signup(self.client)
        self.Me = Ui_me(self.client)
        self.pwd = Ui_changepwd(self.client)
        self.home = Ui_Home(self.client)
        self.sendComment = Ui_SendComment(self.client)
        self.detail = Ui_Detail(self.client)
        self.sendBlog = Ui_Blog(self.client)
        self.remind = Ui_remind()
        self.search = Ui_Search(self.client)
        self.message = Ui_message1(self.client)

    # 注册登录界面
    def LoginTip(self):
        app = QtWidgets.QApplication(sys.argv)
        self.LoginTipWindow = QtWidgets.QMainWindow()
        self.tip.setupUi(self.LoginTipWindow)
        self.Tip_btn()
        self.LoginTipWindow.show()
        sys.exit(app.exec_())


    # 提示登录页面
    def Tip_btn(self):
        self.tip.signup.clicked.connect(self.do_signup)
        self.tip.login.clicked.connect(self.do_login)

    # 登录页面
    def Signin_btn(self):
        self.signin.Signin.clicked.connect(self.judgement)
        self.signin.Signup.clicked.connect(self.signup_page)

    # 注册页面按钮
    def Signup_btn(self):
        self.signup.return_home.clicked.connect(self.back_tip)
        self.signup.signup.clicked.connect(self.go_me)

    # 主页按钮监控
    def Home_btn(self):
        # 四个主按钮
        self.home.message.clicked.connect(self.home_to_msg)
        self.home.new_blog.clicked.connect(self.send_blog)
        self.home.search.clicked.connect(self.search_page)
        self.home.me_.clicked.connect(self.aboutMe)
        # 评论按钮
        self.home.comment1.clicked.connect(self.comment)
        self.home.comment2.clicked.connect(self.comment)
        self.home.comment3.clicked.connect(self.comment)
        # 点赞按钮
        self.home.fabulous1.clicked.connect(self.fabulous)
        self.home.fabulous2.clicked.connect(self.fabulous)
        self.home.fabulous3.clicked.connect(self.fabulous)
        # 转发按钮
        self.home.forward1.clicked.connect(self.forward)
        self.home.forward2.clicked.connect(self.forward)
        self.home.forward3.clicked.connect(self.forward)
        # 查看更多/详情按钮
        self.home.more1.clicked.connect(self.more)
        self.home.more2.clicked.connect(self.more)
        self.home.more3.clicked.connect(self.more)
        # 热门微博,关注,下一页
        self.home.hotBlog.clicked.connect(self.hot_blog)
        self.home.relateBlog.clicked.connect(self.relate_blog)
        self.home.next_page.clicked.connect(self.nextPage)

    def Message_btn(self):
        self.message.home_page.clicked.connect(self.message_to_Home)
        self.message.new_blog.clicked.connect(self.send_blog_msg)
        self.message.search.clicked.connect(self.message_to_search)
        self.message.me_.clicked.connect(self.message_to_me)

    # 搜索页面按钮
    def Search_btn(self):
        self.search.home_page.clicked.connect(self.search_to_Home)
        self.search.message.clicked.connect(self.search_to_message)
        self.search.new_blog.clicked.connect(self.send_blog)
        self.search.me_.clicked.connect(self.search_to_me)
        # 评论按钮
        self.search.comment1.clicked.connect(self.comment1)
        self.search.comment2.clicked.connect(self.comment1)
        self.search.comment3.clicked.connect(self.comment1)
        # 点赞按钮
        self.search.fabulous1.clicked.connect(self.fabulous1)
        self.search.fabulous2.clicked.connect(self.fabulous1)
        self.search.fabulous3.clicked.connect(self.fabulous1)
        # 转发按钮
        self.search.forward1.clicked.connect(self.forward1)
        self.search.forward2.clicked.connect(self.forward1)
        self.search.forward3.clicked.connect(self.forward1)
        # 更多详情
        self.search.more1.clicked.connect(self.more1)
        self.search.more2.clicked.connect(self.more1)
        self.search.more3.clicked.connect(self.more1)
        # 下一页,搜索按钮
        self.search.next_page.clicked.connect(self.search_nextPage)
        self.search.input.clicked.connect(self.search_info)

    # 相关个人信息页面按钮绑定
    def Me_btn(self):
        # 首页
        self.Me.home_page.clicked.connect(self.me_to_Home)
        # 消息页面
        self.Me.message.clicked.connect(self.me_to_message)
        # 发布微博
        self.Me.new_blog.clicked.connect(self.send_blog_me)
        # 搜索
        self.Me.search.clicked.connect(self.me_to_search)
        # 微博及点赞记录页面
        # self.Me.blog.clicked.connect(self.blog.click)
        # self.Me.good.clicked.connect(self.good.click)
        # 个人信息页面按钮
        self.Me.change_pwd.clicked.connect(self.changePwd)
        self.Me.change_info.clicked.connect(self.changeInfo)

    # 修改信息页面按钮
    def Info_btn(self):
        self.info.cancle_btn.clicked.connect(self.cancle_info)
        self.info.confirm_btn.clicked.connect(self.confirm_info)

    # 修改密码页面按钮
    def Pwd_btn(self):
        self.pwd.cancle_btn.clicked.connect(self.cancle_pwd)
        self.pwd.confirm_btn.clicked.connect(self.confirm_pwd)

    # 评论页面按钮
    def sendComment_btn(self):
        self.sendComment.send_btn.clicked.connect(self.send_c)
        self.sendComment.back_btn.clicked.connect(self.back_h)

    # 微博详情页面
    def Detail_btn(self):
        self.detail.fabulous_btn.clicked.connect(self.back_tip)
        self.detail.comment_btn.clicked.connect(self.back_tip)
        self.detail.comment_btn.clicked.connect(self.back_tip)
        self.detail.comment_btn.clicked.connect(self.back_tip)

    # 发布微博页面
    def sendBlog_btn(self):
        self.sendBlog.send_btn.clicked.connect(self.send_new)
        self.sendBlog.back_btn.clicked.connect(self.back_home)

    # 详情页面
    def detail_btn(self):
        self.detail.fabulous_btn.clicked.connect(self.detail_fabulous)
        self.detail.comment_btn.clicked.connect(self.detail_comment)
        self.detail.forward_btn.clicked.connect(self.detail_forward)
        self.detail.back.clicked.connect(self.detail_back_home)

    # 获取用户信息
    def get_info(self):
        statuscode, userinfo = self.client.do_show_userinfo(self.userid)
        self.gender = userinfo.__dict__['gender']
        self.brithday = userinfo.__dict__['birthday']
        self.mail = userinfo.__dict__['email']
        self.phoneno = userinfo.__dict__['phonenumber']
        self.introduction = userinfo.__dict__['introduce']
        self.blog = userinfo.__dict__['publishnum']
        self.good = userinfo.__dict__['laudnum']
        self.stime = userinfo.__dict__['registtime']

    # 登录页面
    def do_login(self):
        self.LoginTipWindow.close()
        self.Go_signin = QtWidgets.QDialog()
        self.signin.setupUi(self.Go_signin)
        self.Signin_btn()
        self.Go_signin.show()

    # 登录页面提交
    def judgement(self):
        self.username, self.userid = self.signin.judgement()
        self.Go_signin.close()
        self.home_page()

    # 登录页面跳转注册页面按钮
    def signup_page(self):
        self.Go_signin.close()
        self.do_signup()

    # 注册页面
    def do_signup(self):
        self.LoginTipWindow.close()
        self.Go_signup = QtWidgets.QDialog()
        self.signup.setupUi(self.Go_signup)
        self.Signup_btn()
        self.Go_signup.show()

    # 注册页面返回按钮
    def back_tip(self):
        self.Go_signup.close()
        self.LoginTipWindow.show()

    # 注册页面提交按钮
    def go_me(self):
        # 将注册信息保存为类属性
        info = self.signup.signup_info()
        print(info)
        if info: 
            self.userid, self.username, self.phoneno, self.mail = info
            self.Go_signup.close()
            try:
                # 直接跳转到主页, 如果发生异常则通过登录跳转
                self.home_page()
            except Exception as e:
                print(e)
                self.Go_signin = QtWidgets.QDialog()
                self.signin.setupUi(self.Go_signin)
                self.Signin_btn()
                self.Go_signin.show()

    # 用于主页面的显示及刷新
    def blog_refresh(self):
        self.home.get_hot()
        self.showed = self.home.get_hotblog()
        self.HomeWindow.show()

    # 以下为主页面相关事件及按钮绑定
    # 主页面
    def home_page(self):
        self.HomeWindow = QtWidgets.QDialog()
        self.home.setupUi(self.HomeWindow)
        self.Home_btn()
        self.get_info()
        self.blog_refresh()

    # 主页面提示窗口
    def remind_info(self):
        self.remindWindow = QtWidgets.QDialog()
        self.remind.setupUi(self.remindWindow)
        self.remindWindow.show()

    # 热门微博按钮事件
    def hot_blog(self):
        self.showed = self.home.get_hotblog()
        self.home.get_hot()
        self.showed = self.home.get_hotblog()
        self.home.next_page.setText('下一页')

    # 关注微博按钮事件
    def relate_blog(self):
        self.home.get_relate(self.userid)
        self.showed = self.home.get_relateblog()
        self.home.next_page.setText('下一页>')

    # 下一页按钮事件
    def nextPage(self):
        # 判断是热门微博的按钮还是关注微博的
        if self.home.next_page.text() == '下一页>':
            self.showed = self.home.get_relateblog()
        else:
            self.showed = self.home.get_hotblog()

    # 微博详情页面
    def more(self):
        # 判断是哪个按钮被触发,并获取此消息类
        sender = self.HomeWindow.sender()
        if sender == self.home.more1:
            msg = self.showed[0]
        elif sender == self.home.more2:
            msg = self.showed[1]
        elif sender == self.home.more3:
            msg = self.showed[2]
        self.detailWindow = QtWidgets.QDialog()
        self.detail.setupUi(self.detailWindow)
        self.detail_btn()
        # 将消息类传入具体处理模块
        self.detail.get_msg(msg, self.userid)
        self.HomeWindow.hide()
        self.detailWindow.show()

    # 详情页面返回调主页面同时刷新信息
    def detail_back_home(self):
        self.detailWindow.close()
        self.blog_refresh()

    # 详细信息页面评论
    def detail_comment(self):
        msgid = self.detail.msg.getmessagesid()
        self.commmentWindow = QtWidgets.QDialog()
        self.sendComment.setupUi(self.commmentWindow)
        self.sendComment_btn()
        self.sendComment.get_msgid(msgid, self.userid)
        self.commmentWindow.show()

    # 详细信息页面点赞
    def detail_fabulous(self):
        self.detail.fabulous()

    # 详细信息页面转发
    def detail_forward(self):
        self.detail.forward()

    # 主页评论
    def comment(self):
        # 判断是哪个评论按钮被触发, 并获取此条消息的ID
        sender = self.HomeWindow.sender()
        if sender == self.home.comment1:
            msgid = self.showed[0].getmessagesid()
        elif sender == self.home.comment2:
            msgid = self.showed[1].getmessagesid()
        elif sender == self.home.comment3:
            msgid = self.showed[2].getmessagesid()
        self.commmentWindow = QtWidgets.QDialog()
        self.sendComment.setupUi(self.commmentWindow)
        self.sendComment_btn()
        self.sendComment.get_msgid(msgid, self.userid)
        self.commmentWindow.show()

    # 发布评论页面取消按钮
    def back_h(self):
        self.commmentWindow.close()

    # 发布评论页面发布按钮
    def send_c(self):
        self.sendComment.do_com()
        self.commmentWindow.close()
        self.remind_info()
        self.remind.info.setText('评论成功!')
        self.blog_refresh()

    # 首页及详情页点赞按钮绑定事件
    def fabulous(self):
        # 判断是哪个点赞按钮被触发, 并获得此消息的ID及发布作者的ID
        sender = self.HomeWindow.sender()
        if sender == self.home.fabulous1:
            msgid = self.showed[0].getmessagesid()
            relateid = self.showed[0].getuserid()
        elif sender == self.home.fabulous2:
            msgid = self.showed[1].getmessagesid()
            relateid = self.showed[1].getuserid()
        elif sender == self.home.fabulous3:
            msgid = self.showed[2].getmessagesid()
            relateid = self.showed[2].getuserid()
        statuscode1 = self.client.do_agree(msgid, self.userid)
        self.remind_info()
        # 判断是不是用户自己为自己的消息点赞
        if self.userid != relateid:
            # 不是用户自己, 则点赞同时关注用户
            statuscode2 = self.client.do_relate(self.userid, relateid)
            print(statuscode1, statuscode2)
            if statuscode1 == '0000':
                if statuscode2 == '0000':
                    self.remind.info.setText('点赞成功, 您已成功关注该用户!')
                    self.home.get_hot()
                    self.showed = self.home.get_hotblog()
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')
        else:
            # 是用户自己, 则只点赞
            if statuscode1 == "0000":
                self.remind.info.setText('为自己点赞成功!')
                self.get_info()
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')

    # 主页转发
    def forward(self):
        # 判断触发按钮, 同时获取消息ID, 内容, 及发布作者
        sender = self.HomeWindow.sender()
        if sender == self.home.forward1:
            msgid = self.showed[0].getmessagesid()
            msg = self.showed[0].getmessagesinfo()
            msg_userid = self.showed[0].getuserid()
        elif sender == self.home.forward2:
            msgid = self.showed[1].getmessagesid()
            msg = self.showed[1].getmessagesinfo()
            msg_userid = self.showed[1].getuserid()
        elif sender == self.home.forward3:
            msgid = self.showed[2].getmessagesid()
            msg = self.showed[2].getmessagesinfo()
            msg_userid = self.showed[2].getuserid()
        self.remind_info()
        # 判断是否是用户自己发布的微博
        if self.userid != msg_userid:
            statuscode = self.client.do_forward(msgid, self.userid)
            if statuscode == '0000':
                code = self.client.do_publish(self.userid, msg)
                print(code)
                if code == '0000':
                    self.remind.info.setText('转发成功!')
                    self.home.get_hot()
                    self.showed = self.home.get_hotblog()
                    self.get_info()
                else:
                    self.remind.info.setText('发生错误, 请稍后重试!')
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')
        else:
            self.remind.info.setText('这是您自己发布的微博哦!')


    # 消息页面相关
    # 主页前往消息页面
    def home_to_msg(self):
        self.MessageWindow = QtWidgets.QDialog()
        self.message.setupUi(self.MessageWindow,self.userid, self.username)
        self.Message_btn()
        self.HomeWindow.hide()
        self.MessageWindow.show()

    def message_to_Home(self):
        self.MessageWindow.close()
        self.HomeWindow.show()

    def message_to_search(self):
        self.SearchWindow = QtWidgets.QDialog()
        self.search.setupUi(self.SearchWindow)
        self.Search_btn()
        self.search.get_hot()
        self.showed = self.search.get_blog()
        self.MessageWindow.close()
        self.SearchWindow.show()

    def message_to_me(self):
        self.MeWindow = QtWidgets.QDialog()
        self.Me.setupUi(self.MeWindow)
        self.Me_btn()
        self.Me.get_info(self.username, self.introduction, self.gender,
                         self.brithday, self.stime, self.blog, self.good)
        self.MessageWindow.close()
        self.MeWindow.show()

    def send_blog_msg(self):
        self.MessageWindow.close()
        self.send_blog()

    # 以下为发布微博页面相关
    # 发布微博页面
    def send_blog(self):
        self.sendBlogWindow = QtWidgets.QDialog()
        self.sendBlog.setupUi(self.sendBlogWindow)
        self.sendBlog_btn()
        self.sendBlogWindow.show()

    # 发布微博页面取消按钮
    def back_home(self):
        self.sendBlogWindow.close()
        self.HomeWindow.show()

    # 发布微博页面发布按钮
    def send_new(self):
        self.sendBlog.sendNew(self.userid)
        self.sendBlogWindow.close()
        self.home.get_hot()
        self.blog_refresh()
        self.get_info()

    # 以下为搜索页面相关的按钮事件
    # 搜索页面
    def search_page(self):
        self.SearchWindow = QtWidgets.QDialog()
        self.search.setupUi(self.SearchWindow)
        self.Search_btn()
        self.search.get_hot()
        self.showed = self.search.get_blog()
        self.HomeWindow.hide()
        self.SearchWindow.show()

    # 搜索页面返回主页
    def search_to_Home(self):
        self.SearchWindow.hide()
        self.HomeWindow.show()
        self.blog_refresh()

    def search_to_message(self):
        self.MessageWindow = QtWidgets.QDialog()
        self.message.setupUi(self.MessageWindow,self.userid, self.username)
        self.Message_btn()
        self.SearchWindow.close()
        self.MessageWindow.show()

    def search_to_me(self):
        self.MeWindow = QtWidgets.QDialog()
        self.Me.setupUi(self.MeWindow)
        self.Me_btn()
        self.Me.get_info(self.username, self.introduction, self.gender,
                         self.brithday, self.stime, self.blog, self.good)
        self.SearchWindow.close()
        self.MeWindow.show()

    # 搜索页面搜索
    def search_info(self):
        self.showed = self.search.input_info()

    # 搜索页面的下一页按钮事件
    def search_nextPage(self):
        # 判断是热门微博的按钮还是关注微博的
        if self.search.next_page.text() == '下一页>':
            self.showed = self.search.get_inputblog()
        else:
            self.showed = self.search.get_blog()

    # 搜索页面评论
    def comment1(self):
        # 判断是哪个按钮被触发, 并获取此消息ID
        sender = self.HomeWindow.sender()
        if sender == self.search.comment1:
            msgid = self.showed[0].getmessagesid()
        elif sender == self.search.comment2:
            msgid = self.showed[1].getmessagesid()
        elif sender == self.search.comment3:
            msgid = self.showed[2].getmessagesid()
        self.commmentWindow = QtWidgets.QDialog()
        self.sendComment.setupUi(self.commmentWindow)
        self.sendComment_btn()
        self.sendComment.get_msgid(msgid, self.userid)
        self.commmentWindow.show()

    # 搜索页点赞按钮绑定事件
    def fabulous1(self):
        # 判断触发按钮, 获取消息ID及作者ID
        sender = self.HomeWindow.sender()
        if sender == self.search.fabulous1:
            msgid = self.showed[0].getmessagesid()
            relateid = self.showed[0].getuserid()
        elif sender == self.search.fabulous2:
            msgid = self.showed[1].getmessagesid()
            relateid = self.showed[1].getuserid()
        elif sender == self.search.fabulous3:
            msgid = self.showed[2].getmessagesid()
            relateid = self.showed[2].getuserid()
        statuscode1 = self.client.do_agree(msgid, self.userid)
        self.remind_info()
        # 判断是不是用户自己为自己的消息点赞
        if self.userid != relateid:
            # 不是用户自己, 则点赞同时关注用户
            statuscode2 = self.client.do_relate(self.userid, relateid)
            print(statuscode1, statuscode2)
            if statuscode1 == '0000':
                if statuscode2 == '0000':
                    self.remind.info.setText('点赞成功, 您已成功关注该用户!')
                    self.search.get_hot()
                    self.showed = self.search.get_blog()
                    self.search_page()
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')
        else:
            # 是用户自己, 则只点赞
            if statuscode1 == "0000":
                self.remind.info.setText('为自己点赞成功!')
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')

    # 搜索页面转发
    def forward1(self):
        # 判断是哪个按钮被触发, 获取此消息相关信息
        sender = self.HomeWindow.sender()
        if sender == self.search.forward1:
            msgid = self.showed[0].getmessagesid()
            msg = self.showed[0].getmessagesinfo()
            msg_userid = self.showed[0].getuserid()
        elif sender == self.search.forward2:
            msgid = self.showed[1].getmessagesid()
            msg = self.showed[1].getmessagesinfo()
            msg_userid = self.showed[1].getuserid()
        elif sender == self.search.forward3:
            msgid = self.showed[2].getmessagesid()
            msg = self.showed[2].getmessagesinfo()
            msg_userid = self.showed[2].getuserid()
        self.remind_info()
        # 判断是否是用户自己发布的微博
        if self.userid != msg_userid:
            statuscode = self.client.do_forward(msgid, self.userid)
            if statuscode == '0000':
                code = self.client.do_publish(self.userid, msg)
                print(code)
                if code == '0000':
                    self.remind.info.setText('转发成功!')
                    self.search.get_hot()
                    self.showed = self.search.get_blog()
                else:
                    self.remind.info.setText('发生错误, 请稍后重试!')
            else:
                self.remind.info.setText('发生错误, 请稍后重试!')
        else:
            self.remind.info.setText('这是您自己发布的微博哦!')

    # 从搜索页面前往微博详情页面
    def more1(self):
        sender = self.HomeWindow.sender()
        if sender == self.search.more1:
            msg = self.showed[0]
        elif sender == self.search.more2:
            msg = self.showed[1]
        elif sender == self.search.more3:
            msg = self.showed[2]
        self.detailWindow = QtWidgets.QDialog()
        self.detail.setupUi(self.detailWindow)
        self.detail_btn()
        self.detail.get_msg(msg, self.userid)
        self.detailWindow.show()

    # 从搜索页面前往个人信息页面
    def search_to_me(self):
        self.MeWindow = QtWidgets.QDialog()
        self.Me.setupUi(self.MeWindow)
        self.Me_btn()
        self.Me.get_info(self.username, self.introduction, self.gender,
                         self.brithday, self.stime, self.blog, self.good)
        self.SearchWindow.close()
        self.MeWindow.show()

    # 以下为个人信息页面
    # 个人信息界面
    def aboutMe(self):
        self.MeWindow = QtWidgets.QDialog()
        self.Me.setupUi(self.MeWindow)
        self.Me_btn()
        self.Me.get_info(self.username, self.introduction, self.gender,
                         self.brithday, self.stime, self.blog, self.good)
        self.HomeWindow.hide()
        self.MeWindow.show()

    # 修改信息界面
    def changeInfo(self):
        self.changeinfoWindow = QtWidgets.QDialog()
        self.info.setupUi(self.changeinfoWindow)
        self.Info_btn()
        self.info.get_info(self.username, self.userid, self.brithday, self.gender,
                           self.stime, self.introduction, self.phoneno, self.mail)
        self.MeWindow.hide()
        self.changeinfoWindow.show()

    # 修改个人信息页面取消按钮
    def cancle_info(self):
        self.changeinfoWindow.close()
        self.MeWindow.show()

    # 修改个人信息页面提交按钮
    def confirm_info(self):
        self.introduction, self.gender, self.brithday = self.info.confirmInfo()
        self.changeinfoWindow.close()
        self.get_info()
        self.Me.get_info(self.username, self.introduction, self.gender,
                         self.brithday, self.stime, self.blog, self.good)
        self.Me.tip.setText("个人信息修改成功!")
        self.MeWindow.show()

    # 修改密码界面
    def changePwd(self):
        self.changepwdWindow = QtWidgets.QDialog()
        self.pwd.setupUi(self.changepwdWindow)
        self.Pwd_btn()
        self.pwd.get_info(self.username, self.stime, self.userid)
        self.MeWindow.hide()
        self.changepwdWindow.show()

    # 修改密码页面取消按钮
    def cancle_pwd(self):
        self.changepwdWindow.close()
        self.MeWindow.show()

    # 修改密码页面提交按钮
    def confirm_pwd(self):
        self.pwd.confirmPwd()
        self.changepwdWindow.close()
        self.Me.tip.setText("密码修改成功!")
        self.MeWindow.show()

    # 返回主页面
    def me_to_Home(self):
        self.MeWindow.close()
        self.blog_refresh()

    # 前往搜索页面
    def me_to_search(self):
        self.SearchWindow = QtWidgets.QDialog()
        self.search.setupUi(self.SearchWindow)
        self.Search_btn()
        self.search.get_hot()
        self.showed = self.search.get_blog()
        self.MeWindow.close()
        self.SearchWindow.show()

    def me_to_message(self):
        self.MessageWindow = QtWidgets.QDialog()
        self.message.setupUi(self.MessageWindow, self.userid, self.username)
        self.Message_btn()
        self.MeWindow.close()
        self.MessageWindow.show()

    def send_blog_me(self):
        self.MeWindow.close()
        self.send_blog()


if __name__ == '__main__':
    main = Main(client)
    main.LoginTip()
