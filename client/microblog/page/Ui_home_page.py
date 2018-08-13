# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-13
# Version: v0.5

'''
微博展示主页面
包含热门微博和关注人的动态微博两部分

'''


from PyQt5 import QtCore, QtGui, QtWidgets
from client_msg_deal import ClientMsgDeal
# 页面图标资源文件导入
import imgs_rc


class Ui_Home(object):
    # 初始化通讯的类
    def __init__(self, client):
        self.client = client

    # 页面样式方法
    def setupUi(self, home):
        home.setObjectName("home")
        home.setEnabled(True)
        home.resize(400, 600)
        home.setMinimumSize(QtCore.QSize(400, 600))
        home.setMaximumSize(QtCore.QSize(400, 600))
        home.setMouseTracking(False)
        home.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                           "color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(home)
        self.centralWidget.setObjectName("centralWidget")
        self.aboutme = QtWidgets.QLabel(self.centralWidget)
        self.aboutme.setGeometry(QtCore.QRect(330, 575, 41, 20))
        self.aboutme.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutme.setObjectName("aboutme")
        self.search_ = QtWidgets.QLabel(self.centralWidget)
        self.search_.setGeometry(QtCore.QRect(260, 575, 41, 20))
        self.search_.setObjectName("search_")
        self.home = QtWidgets.QLabel(self.centralWidget)
        self.home.setGeometry(QtCore.QRect(30, 575, 41, 20))
        self.home.setObjectName("home")
        self.message = QtWidgets.QPushButton(self.centralWidget)
        self.message.setGeometry(QtCore.QRect(88, 535, 75, 41))
        self.message.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/imgs/white_information.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message.setIcon(icon)
        self.message.setIconSize(QtCore.QSize(30, 30))
        self.message.setFlat(True)
        self.message.setObjectName("message")
        self.me_ = QtWidgets.QPushButton(self.centralWidget)
        self.me_.setGeometry(QtCore.QRect(320, 540, 61, 31))
        self.me_.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/imgs/white.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me_.setIcon(icon1)
        self.me_.setIconSize(QtCore.QSize(30, 30))
        self.me_.setFlat(True)
        self.me_.setObjectName("me_")
        self.search = QtWidgets.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(240, 540, 61, 31))
        self.search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/imgs/white_search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.home_page = QtWidgets.QPushButton(self.centralWidget)
        self.home_page.setGeometry(QtCore.QRect(10, 530, 71, 51))
        self.home_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/imgs/black_house.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_page.setIcon(icon3)
        self.home_page.setIconSize(QtCore.QSize(30, 30))
        self.home_page.setFlat(True)
        self.home_page.setObjectName("home_page")
        self.msg = QtWidgets.QLabel(self.centralWidget)
        self.msg.setGeometry(QtCore.QRect(110, 575, 41, 20))
        self.msg.setObjectName("msg")
        self.new_blog = QtWidgets.QPushButton(self.centralWidget)
        self.new_blog.setGeometry(QtCore.QRect(144, 540, 111, 51))
        self.new_blog.setAutoFillBackground(False)
        self.new_blog.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/imgs/plus_sign.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_blog.setIcon(icon4)
        self.new_blog.setIconSize(QtCore.QSize(50, 50))
        self.new_blog.setFlat(True)
        self.new_blog.setObjectName("new_blog")
        self.relate_blog = QtWidgets.QGroupBox(self.centralWidget)
        self.relate_blog.setGeometry(QtCore.QRect(200, 20, 191, 41))
        self.relate_blog.setTitle("")
        self.relate_blog.setObjectName("relate_blog")
        self.relateBlog = QtWidgets.QPushButton(self.relate_blog)
        self.relateBlog.setGeometry(QtCore.QRect(20, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.relateBlog.setFont(font)
        self.relateBlog.setFlat(True)
        self.relateBlog.setObjectName("relateBlog")
        self.hot_blog = QtWidgets.QGroupBox(self.centralWidget)
        self.hot_blog.setGeometry(QtCore.QRect(10, 20, 191, 41))
        self.hot_blog.setTitle("")
        self.hot_blog.setObjectName("hot_blog")
        self.hotBlog = QtWidgets.QPushButton(self.hot_blog)
        self.hotBlog.setGeometry(QtCore.QRect(20, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.hotBlog.setFont(font)
        self.hotBlog.setFlat(True)
        self.hotBlog.setObjectName("hotBlog")
        self.forward1 = QtWidgets.QPushButton(self.centralWidget)
        self.forward1.setGeometry(QtCore.QRect(130, 190, 71, 31))
        self.forward1.setFlat(True)
        self.forward1.setObjectName("forward1")
        self.comment1 = QtWidgets.QPushButton(self.centralWidget)
        self.comment1.setGeometry(QtCore.QRect(240, 190, 71, 31))
        self.comment1.setFlat(True)
        self.comment1.setObjectName("comment1")
        self.fabulous1 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous1.setGeometry(QtCore.QRect(30, 190, 71, 31))
        self.fabulous1.setFlat(True)
        self.fabulous1.setObjectName("fabulous1")
        self.text_box1 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box1.setGeometry(QtCore.QRect(10, 80, 380, 111))
        self.text_box1.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text_box1.setObjectName("text_box1")
        self.next_page = QtWidgets.QPushButton(self.centralWidget)
        self.next_page.setGeometry(QtCore.QRect(310, 490, 80, 31))
        self.next_page.setFlat(True)
        self.next_page.setObjectName("next_page")
        self.fabulous3 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous3.setGeometry(QtCore.QRect(20, 489, 71, 31))
        self.fabulous3.setFlat(True)
        self.fabulous3.setObjectName("fabulous3")
        self.forward3 = QtWidgets.QPushButton(self.centralWidget)
        self.forward3.setGeometry(QtCore.QRect(120, 489, 71, 31))
        self.forward3.setFlat(True)
        self.forward3.setObjectName("forward3")
        self.comment3 = QtWidgets.QPushButton(self.centralWidget)
        self.comment3.setGeometry(QtCore.QRect(230, 489, 71, 31))
        self.comment3.setFlat(True)
        self.comment3.setObjectName("comment3")
        self.comment2 = QtWidgets.QPushButton(self.centralWidget)
        self.comment2.setGeometry(QtCore.QRect(240, 340, 71, 31))
        self.comment2.setFlat(True)
        self.comment2.setObjectName("comment2")
        self.text_box2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box2.setGeometry(QtCore.QRect(10, 230, 380, 111))
        self.text_box2.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box2.setObjectName("text_box2")
        self.fabulous2 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous2.setGeometry(QtCore.QRect(30, 340, 71, 31))
        self.fabulous2.setFlat(True)
        self.fabulous2.setObjectName("fabulous2")
        self.forward2 = QtWidgets.QPushButton(self.centralWidget)
        self.forward2.setGeometry(QtCore.QRect(130, 340, 71, 31))
        self.forward2.setFlat(True)
        self.forward2.setObjectName("forward2")
        self.text_box3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box3.setGeometry(QtCore.QRect(10, 378, 380, 111))
        self.text_box3.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box3.setObjectName("text_box3")

        self.more1 = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.more1.setGeometry(QtCore.QRect(320, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.more1.setFont(font)
        self.more1.setIconSize(QtCore.QSize(15, 15))
        self.more1.setObjectName("more1")
        self.more2 = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.more2.setGeometry(QtCore.QRect(320, 230, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.more2.setFont(font)
        self.more2.setIconSize(QtCore.QSize(15, 15))
        self.more2.setObjectName("more2")
        self.more3 = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.more3.setGeometry(QtCore.QRect(320, 379, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.more3.setFont(font)
        self.more3.setIconSize(QtCore.QSize(15, 15))
        self.more3.setDefault(False)
        self.more3.setObjectName("more3")

        self.retranslateUi(home)

        QtCore.QMetaObject.connectSlotsByName(home)


    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "微博"))
        self.aboutme.setText(_translate("home", "我"))
        self.search_.setText(_translate("home", "发 现"))
        self.home.setText(_translate("home", "微 博"))
        self.msg.setText(_translate("home", "消 息"))
        self.relateBlog.setText(_translate("home", "我的关注"))
        self.hotBlog.setText(_translate("home", "热门微博"))
        self.forward1.setText(_translate("home", "转发"))
        self.comment1.setText(_translate("home", "评论"))
        self.fabulous1.setText(_translate("home", "点赞"))
        self.next_page.setText(_translate("home", "下一页"))
        self.fabulous3.setText(_translate("home", "点赞"))
        self.forward3.setText(_translate("home", "转发"))
        self.comment3.setText(_translate("home", "评论"))
        self.comment2.setText(_translate("home", "评论"))
        self.fabulous2.setText(_translate("home", "点赞"))
        self.forward2.setText(_translate("home", "转发"))
        self.more1.setText(_translate("home", "更多"))
        self.more2.setText(_translate("home", "更多"))
        self.more3.setText(_translate("home", "更多"))

    # 获取微博列表同时展示热门微博
    def get_hotblog(self):
        if self.hotcode == '0000':
            # 调用展示函数, 并更新展示后的待展示列表和已展示的3条消息id
            self.hotlist, self.showed = self.show_content(self.hotlist)
            return self.showed
        else:
            self.text_box1.setText('暂时没有动态消息,过一会儿再来吧!!!')
            self.text_box2.setText('')
            self.text_box3.setText('')

    # 与服务器链接, 获取全部的消息列表
    def get_hot(self):
        self.hotcode, self.hotlist = self.client.do_find()
        self.text_box1.setText('')
        self.text_box2.setText('')
        self.text_box3.setText('')

    # 与服务器链接. 获取全部已关注人发布的消息
    def get_relate(self, userid):
        self.relatecode, self.relatelist = self.client.do_relate_msg(userid)
        self.text_box1.setText('')
        self.text_box2.setText('')
        self.text_box3.setText('')

    # 查看关注消息列表是否有有消息显示, 有调显示方法, 没有提示用户
    def get_relateblog(self):
        if self.relatecode == '0000':
            self.relatelist, self.showed = self.show_content(self.relatelist)
            return self.showed
        else:
            self.text_box1.setText('暂时没有动态消息,过一会儿再来吧!!!')
            self.text_box2.setText('')
            self.text_box3.setText('')
        self.next_page.setText('下一页>')

    # 用于将消息列表展示的方法
    def show_content(self, msglist):
        print('微博展示列表')
        # 创建空列表,最多存放3条展示的消息,用于后面点赞评论及转发获取相关的消息信息
        showed = []
        if msglist:
            # 显示内容为用户名, 发布时间, 微博内容
            # 判断列表长度,显示完后将此消息从msglist删除, 并存入showed
            if len(msglist) == 1:
                self.text_box1.setText(msglist[0].username + '\t' + msglist[0].getmessagestime() +'\n' +'\n' + msglist[0].getmessagesinfo())
                # 将展示的消息添加到展示后列表
                showed.append(msglist[0])
                # 删除为展示列表中此条消息
                msglist.pop(0)
                # 将两个没有展示的文本框设置为空
                self.text_box2.setText('')
                self.text_box3.setText('')
            elif len(msglist) == 2:
                self.text_box1.setText(msglist[0].username + '\t' + msglist[0].getmessagestime() +'\n' +'\n' + msglist[0].getmessagesinfo())
                showed.append(msglist[0])
                self.text_box2.setText(msglist[1].username + '\t' + msglist[1].getmessagestime() +'\n' +'\n' + msglist[1].getmessagesinfo())
                showed.append(msglist[1])
                msglist.pop(0)
                msglist.pop(0)
                self.text_box3.setText('')
            else:
                self.text_box1.setText(msglist[0].username + '\t' + msglist[0].getmessagestime() +'\n' +'\n' + msglist[0].getmessagesinfo())
                showed.append(msglist[0])
                self.text_box2.setText(msglist[1].username + '\t' + msglist[1].getmessagestime() +'\n' +'\n' + msglist[1].getmessagesinfo())
                showed.append(msglist[1])
                self.text_box3.setText(msglist[2].username + '\t' + msglist[2].getmessagestime() +'\n' +'\n' + msglist[2].getmessagesinfo())
                showed.append(msglist[2])
                msglist.pop(0)
                msglist.pop(0)
                msglist.pop(0)
        else:
            self.text_box1.setText('没有更多消息了...')
            self.text_box2.setText('')
            self.text_box3.setText('')
        # 将展示后剩余的列表, 和展示的消息列表返回
        return [msglist, showed]


if __name__ == "__main__":
    import sys
    client = ClientMsgDeal()
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_Home(client)
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
