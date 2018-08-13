#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-14
# Version: v0.1

'''
搜索页面
根据用户输入内容,检索相关消息展示

'''

from PyQt5 import QtCore, QtGui, QtWidgets
import imgs_search_rc


class Ui_Search(object):
    # 初始化通讯的类对象
    def __init__(self, client):
        self.client = client

    def setupUi(self, search):
        search.setObjectName("search")
        search.setEnabled(True)
        search.resize(400, 600)
        search.setMinimumSize(QtCore.QSize(400, 600))
        search.setMaximumSize(QtCore.QSize(400, 600))
        search.setMouseTracking(False)
        search.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(search)
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
        icon.addPixmap(QtGui.QPixmap(":/search/imgs/white_information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message.setIcon(icon)
        self.message.setIconSize(QtCore.QSize(30, 30))
        self.message.setFlat(True)
        self.message.setObjectName("message")
        self.me_ = QtWidgets.QPushButton(self.centralWidget)
        self.me_.setGeometry(QtCore.QRect(320, 540, 61, 31))
        self.me_.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/search/imgs/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me_.setIcon(icon1)
        self.me_.setIconSize(QtCore.QSize(30, 30))
        self.me_.setFlat(True)
        self.me_.setObjectName("me_")
        self.search = QtWidgets.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(240, 540, 61, 31))
        self.search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/search/imgs/black_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.home_page = QtWidgets.QPushButton(self.centralWidget)
        self.home_page.setGeometry(QtCore.QRect(10, 530, 71, 51))
        self.home_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/search/imgs/white_house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon4.addPixmap(QtGui.QPixmap(":/search/imgs/plus_sign.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_blog.setIcon(icon4)
        self.new_blog.setIconSize(QtCore.QSize(50, 50))
        self.new_blog.setFlat(True)
        self.new_blog.setObjectName("new_blog")
        self.search_box = QtWidgets.QLineEdit(self.centralWidget)
        self.search_box.setEnabled(True)
        self.search_box.setGeometry(QtCore.QRect(10, 10, 270, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setMinimumSize(QtCore.QSize(270, 40))
        self.search_box.setMaximumSize(QtCore.QSize(247, 50))
        self.search_box.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.search_box.setMouseTracking(True)
        self.search_box.setAcceptDrops(True)
        self.search_box.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.search_box.setObjectName("search_box")
        self.input = QtWidgets.QPushButton(self.centralWidget)
        self.input.setGeometry(QtCore.QRect(290, 9, 91, 43))
        self.input.setObjectName("input")
        self.fabulous3 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous3.setGeometry(QtCore.QRect(30, 500, 71, 31))
        self.fabulous3.setFlat(True)
        self.fabulous3.setObjectName("fabulous3")
        self.next_page = QtWidgets.QPushButton(self.centralWidget)
        self.next_page.setGeometry(QtCore.QRect(320, 501, 80, 30))
        self.next_page.setFlat(True)
        self.next_page.setObjectName("next_page")
        self.comment3 = QtWidgets.QPushButton(self.centralWidget)
        self.comment3.setGeometry(QtCore.QRect(240, 500, 71, 31))
        self.comment3.setFlat(True)
        self.comment3.setObjectName("comment3")
        self.forward3 = QtWidgets.QPushButton(self.centralWidget)
        self.forward3.setGeometry(QtCore.QRect(130, 500, 71, 31))
        self.forward3.setFlat(True)
        self.forward3.setObjectName("forward3")
        self.text_box3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box3.setGeometry(QtCore.QRect(10, 380, 380, 121))
        self.text_box3.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box3.setObjectName("text_box3")
        self.comment1 = QtWidgets.QPushButton(self.centralWidget)
        self.comment1.setGeometry(QtCore.QRect(240, 180, 71, 31))
        self.comment1.setFlat(True)
        self.comment1.setObjectName("comment1")
        self.text_box1 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box1.setGeometry(QtCore.QRect(10, 60, 380, 121))
        self.text_box1.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box1.setObjectName("text_box1")
        self.fabulous1 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous1.setGeometry(QtCore.QRect(30, 180, 71, 31))
        self.fabulous1.setFlat(True)
        self.fabulous1.setObjectName("fabulous1")
        self.forward1 = QtWidgets.QPushButton(self.centralWidget)
        self.forward1.setGeometry(QtCore.QRect(130, 180, 71, 31))
        self.forward1.setFlat(True)
        self.forward1.setObjectName("forward1")
        self.forward2 = QtWidgets.QPushButton(self.centralWidget)
        self.forward2.setGeometry(QtCore.QRect(130, 340, 71, 31))
        self.forward2.setFlat(True)
        self.forward2.setObjectName("forward2")
        self.fabulous2 = QtWidgets.QPushButton(self.centralWidget)
        self.fabulous2.setGeometry(QtCore.QRect(30, 340, 71, 31))
        self.fabulous2.setFlat(True)
        self.fabulous2.setObjectName("fabulous2")
        self.comment2 = QtWidgets.QPushButton(self.centralWidget)
        self.comment2.setGeometry(QtCore.QRect(240, 340, 71, 31))
        self.comment2.setFlat(True)
        self.comment2.setObjectName("comment2")
        self.text_box2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.text_box2.setGeometry(QtCore.QRect(10, 220, 380, 121))
        self.text_box2.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(253,253,253,0.6);")
        self.text_box2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box2.setObjectName("text_box2")

        self.more1 = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.more1.setGeometry(QtCore.QRect(320, 65, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.more1.setFont(font)
        self.more1.setIconSize(QtCore.QSize(15, 15))
        self.more1.setObjectName("more1")
        self.more2 = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.more2.setGeometry(QtCore.QRect(320, 219, 61, 31))
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

        self.retranslateUi(search)
        
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslateUi(self, me):
        _translate = QtCore.QCoreApplication.translate
        me.setWindowTitle(_translate("search", "搜索"))
        self.aboutme.setText(_translate("search", "我"))
        self.search_.setText(_translate("search", "发 现"))
        self.home.setText(_translate("search", "微 博"))
        self.msg.setText(_translate("search", "消 息"))
        self.input.setText(_translate("search", "搜  索"))
        self.fabulous3.setText(_translate("search", "点赞"))
        self.next_page.setText(_translate("search", "下一页"))
        self.comment3.setText(_translate("search", "评论"))
        self.forward3.setText(_translate("search", "转发"))
        self.comment1.setText(_translate("search", "评论"))
        self.fabulous1.setText(_translate("search", "点赞"))
        self.forward1.setText(_translate("search", "转发"))
        self.forward2.setText(_translate("search", "转发"))
        self.fabulous2.setText(_translate("search", "点赞"))
        self.comment2.setText(_translate("search", "评论"))
        self.more1.setText(_translate("home", "更多"))
        self.more2.setText(_translate("home", "更多"))
        self.more3.setText(_translate("home", "更多"))

    # 与服务器链接, 获取全部的消息列表
    def get_hot(self):
        self.hotcode, self.hotlist = self.client.do_find()
        self.text_box1.setText('')
        self.text_box2.setText('')
        self.text_box3.setText('')

    # 将全部消息进行展示
    def get_blog(self):
        self.hotlist, self.showed = self.show_content(self.hotlist)
        return self.showed

    # 根据用户输入内容进行查询并调用展示函数展示, 返回展示后的列表
    def input_info(self):
        self.input = self.search_box.text()
        if self.input:
            print('查询内容是:',self.input)
            self.relatecode, self.relatelist = self.client.do_find(self.input)
            self.text_box1.setText('')
            self.text_box2.setText('')
            self.text_box3.setText('')
            self.next_page.setText('下一页>')
            self.showed = self.get_inputblog()
            return self.showed
        else:
            self.search_box.setText("请输入您要搜索的内容!")

    # 查看关注消息列表是否有有消息显示, 有调显示方法, 没有提示用户
    def get_inputblog(self):
        if self.relatecode == '0000':
            self.relatelist, self.showed = self.show_content(self.relatelist)
            return self.showed
        else:
            self.text_box1.setText('暂时您所查找的消息,过一会儿再来吧!!!')
            self.text_box2.setText('')
            self.text_box3.setText('')

    # 用于将消息列表展示的方法
    def show_content(self, msglist):
        # 创建空列表,最多存放3条展示的消息,用于后面点赞评论及转发获取相关的消息信息
        showed = []
        if msglist:
            # 显示内容为用户名, 发布时间, 微博内容
            # 判断列表长度,显示完后将此消息从msglist删除, 并存入showed
            if len(msglist) == 1:
                self.text_box1.setText(msglist[0].username + '\t' + msglist[0].getmessagestime() +'\n' +'\n' + msglist[0].getmessagesinfo())
                showed.append(msglist[0])
                msglist.pop(0)
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
    app = QtWidgets.QApplication(sys.argv)
    me = QtWidgets.QMainWindow()
    ui = Ui_me()
    ui.setupUi(search)
    me.show()
    sys.exit(app.exec_())

