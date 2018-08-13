# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yangtf\Desktop\page_ui\me.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from fuwuduan import *
from Ui_pinglun import *
from Ui_fasongpinglun import *


class Discover_page(object):

    def __init__(self):
        self.l=message_('')

    def discover_page(self, me):

        self.pinglun=Find_comments()
        self.pingluncanshu=QtWidgets.QDialog()
        self.pinglun.find_comments(self.pingluncanshu)

        # self.fasong=Send_comment()
        # self.fasongcanshu=QtWidgets.QDialog()
        # self.fasong.send_comment(self.fasongcanshu)

        self.me=me
        self.me.setObjectName("me")
        self.me.setEnabled(True)
        self.me.resize(400, 600)
        self.me.setMinimumSize(QtCore.QSize(400, 600))
        self.me.setMaximumSize(QtCore.QSize(400, 600))
        self.me.setMouseTracking(False)
        self.me.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.center() #调用居中的函数
        self.centralWidget = QtWidgets.QWidget(me)
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
        icon.addPixmap(QtGui.QPixmap("imgs/white information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message.setIcon(icon)
        self.message.setIconSize(QtCore.QSize(30, 30))
        self.message.setFlat(True)
        self.message.setObjectName("message")
        self.me_ = QtWidgets.QPushButton(self.centralWidget)
        self.me_.setGeometry(QtCore.QRect(320, 540, 61, 31))
        self.me_.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me_.setIcon(icon1)
        self.me_.setIconSize(QtCore.QSize(30, 30))
        self.me_.setFlat(True)
        self.me_.setObjectName("me_")
        self.search = QtWidgets.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(240, 540, 61, 31))
        self.search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/black search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.home_page = QtWidgets.QPushButton(self.centralWidget)
        self.home_page.setGeometry(QtCore.QRect(10, 530, 71, 51))
        self.home_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/white house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon4.addPixmap(QtGui.QPixmap("imgs/plus sign.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_blog.setIcon(icon4)
        self.new_blog.setIconSize(QtCore.QSize(50, 50))
        self.new_blog.setFlat(True)
        self.new_blog.setObjectName("new_blog")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 50, 401, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 399, 479))
        self.scrollAreaContents.setAutoFillBackground(False)
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.blog2 = QtWidgets.QGroupBox(self.scrollAreaContents)
        self.blog2.setGeometry(QtCore.QRect(0, 0, 401, 160))
        self.blog2.setTitle("")
        self.blog2.setObjectName("blog2")
        self.comment1 = QtWidgets.QPushButton(self.blog2)
        self.comment1.setGeometry(QtCore.QRect(240, 129, 71, 31))
        self.comment1.setFlat(True)
        self.comment1.setObjectName("comment1")
        self.forward1 = QtWidgets.QPushButton(self.blog2)
        self.forward1.setGeometry(QtCore.QRect(130, 129, 71, 31))
        self.forward1.setFlat(True)
        self.forward1.setObjectName("forward1")
        self.fabulous1 = QtWidgets.QPushButton(self.blog2)
        self.fabulous1.setGeometry(QtCore.QRect(30, 129, 71, 31))
        self.fabulous1.setFlat(True)
        self.fabulous1.setObjectName("fabulous1")
        self.text_box1 = QtWidgets.QTextBrowser(self.blog2)
        self.text_box1.setGeometry(QtCore.QRect(0, 0, 401, 130))
        self.text_box1.setStyleSheet("font: 11pt \"Arial\";")
        self.text_box1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box1.setObjectName("text_box1")
        self.blog2_2 = QtWidgets.QGroupBox(self.scrollAreaContents)
        self.blog2_2.setGeometry(QtCore.QRect(0, 160, 401, 160))
        self.blog2_2.setTitle("")
        self.blog2_2.setObjectName("blog2_2")
        self.comment2 = QtWidgets.QPushButton(self.blog2_2)
        self.comment2.setGeometry(QtCore.QRect(240, 129, 71, 31))
        self.comment2.setFlat(True)
        self.comment2.setObjectName("comment2")
        self.forward2 = QtWidgets.QPushButton(self.blog2_2)
        self.forward2.setGeometry(QtCore.QRect(130, 129, 71, 31))
        self.forward2.setFlat(True)
        self.forward2.setObjectName("forward2")
        self.fabulous2 = QtWidgets.QPushButton(self.blog2_2)
        self.fabulous2.setGeometry(QtCore.QRect(30, 129, 71, 31))
        self.fabulous2.setFlat(True)
        self.fabulous2.setObjectName("fabulous2")
        self.text_box2 = QtWidgets.QTextBrowser(self.blog2_2)
        self.text_box2.setGeometry(QtCore.QRect(0, 0, 401, 130))
        self.text_box2.setStyleSheet("font: 11pt \"Arial\";")
        self.text_box2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box2.setObjectName("text_box2")
        self.blog2_3 = QtWidgets.QGroupBox(self.scrollAreaContents)
        self.blog2_3.setGeometry(QtCore.QRect(0, 320, 401, 160))
        self.blog2_3.setTitle("")
        self.blog2_3.setObjectName("blog2_3")
        self.comment3 = QtWidgets.QPushButton(self.blog2_3)
        self.comment3.setGeometry(QtCore.QRect(240, 129, 71, 31))
        self.comment3.setFlat(True)
        self.comment3.setObjectName("comment3")
        self.forward3 = QtWidgets.QPushButton(self.blog2_3)
        self.forward3.setGeometry(QtCore.QRect(130, 129, 71, 31))
        self.forward3.setFlat(True)
        self.forward3.setObjectName("forward3")
        self.fabulous3 = QtWidgets.QPushButton(self.blog2_3)
        self.fabulous3.setGeometry(QtCore.QRect(30, 129, 71, 31))
        self.fabulous3.setFlat(True)
        self.fabulous3.setObjectName("fabulous3")
        self.text_box3 = QtWidgets.QTextBrowser(self.blog2_3)
        self.text_box3.setGeometry(QtCore.QRect(0, 0, 401, 130))
        self.text_box3.setStyleSheet("font: 11pt \"Arial\";")
        self.text_box3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box3.setObjectName("text_box3")
        self.next_page = QtWidgets.QPushButton(self.blog2_3)
        self.next_page.setGeometry(QtCore.QRect(320, 130, 80, 30))
        self.next_page.setFlat(True)
        self.next_page.setObjectName("next_page")
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.search_2 = QtWidgets.QToolButton(self.centralWidget)
        self.search_2.setGeometry(QtCore.QRect(275, 4, 107, 45))
        self.search_2.setMinimumSize(QtCore.QSize(107, 45))
        self.search_2.setMaximumSize(QtCore.QSize(107, 45))
        self.search_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/white search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_2.setIcon(icon5)
        self.search_2.setObjectName("search_2")
        self.search_box = QtWidgets.QLineEdit(self.centralWidget)
        self.search_box.setEnabled(True)
        self.search_box.setGeometry(QtCore.QRect(13, 4, 260, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setMinimumSize(QtCore.QSize(260, 45))
        self.search_box.setMaximumSize(QtCore.QSize(247, 50))
        self.search_box.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.search_box.setMouseTracking(True)
        self.search_box.setAcceptDrops(True)
        self.search_box.setStyleSheet("font: 11pt \"Arial\";")
        self.search_box.setObjectName("search_box")
        me.setCentralWidget(self.centralWidget)

        self.retranslateUi(me)
        #把搜索按钮关联事件
        self.search_2.clicked.connect(self.get_message)
        #把下一页按钮关联事件
        self.next_page.clicked.connect(self.get_content)
        self.home_page.clicked.connect(self.home_page.click)
        self.message.clicked.connect(self.message.click)
        self.new_blog.clicked.connect(self.new_blog.click)
        self.search.clicked.connect(zhuyemian)
        self.me_.clicked.connect(self.me_.click)

        self.comment1.clicked.connect(self.call_discovery)
        self.comment2.clicked.connect(self.call_discovery)
        self.comment3.clicked.connect(self.call_discovery)
        self.pinglun.comment_return.clicked.connect(self.discovery_back)

        QtCore.QMetaObject.connectSlotsByName(me)

    def retranslateUi(self, me):
        _translate = QtCore.QCoreApplication.translate
        me.setWindowTitle(_translate("me", "weibo"))
        self.aboutme.setText(_translate("me", "我"))
        self.search_.setText(_translate("me", "发 现"))
        self.home.setText(_translate("me", "微 博"))
        self.msg.setText(_translate("me", "消 息"))
        self.comment1.setText(_translate("me", "评论"))
        self.forward1.setText(_translate("me", "转发"))
        self.fabulous1.setText(_translate("me", "点赞"))
        self.comment2.setText(_translate("me", "评论"))
        self.forward2.setText(_translate("me", "转发"))
        self.fabulous2.setText(_translate("me", "点赞"))
        self.comment3.setText(_translate("me", "评论"))
        self.forward3.setText(_translate("me", "转发"))
        self.fabulous3.setText(_translate("me", "点赞"))
        self.next_page.setText(_translate("me", "下一页"))


     #从搜索栏获取信息
    def get_message(self):
        #这个text方法是用来获取搜素栏信息的
        msg=self.search_box.text()
        self.l=message_(msg)
        # print(msg) 
        #这个clear是清空2搜索栏内容的
        self.search_box.clear()
        self.get_content()

    #把内容写入到内容框
    def get_content(self):
        if len(self.l)==1:
            n=''
            for i in self.l[0]:
                # print(i)
                n+=i+'\n'
            self.text_box3.setText(n)
        elif len(self.l)==2:
            m=''
            for i in self.l[0]:
                # print(i)
                m+=i+'\n'
            self.text_box2.setText(m)
            n=''
            for i in self.l[1]:
                # print(i)
                n+=i+'\n'
            self.text_box3.setText(n)
        else:
            k=''
            for i in self.l[0]:
                # print(i)
                k+=i+'\n'
            self.text_box1.setText(k)
            print(k)
            m=''
            for i in self.l[1]:
                # print(i)
                m+=i+'\n'
            self.text_box2.setText(m)
            n=''
            for i in self.l[2]:
                # print(i)
                n+=i+'\n'
            self.text_box3.setText(n)
            # dianzan=n[8]
            # print(dianzan)
            del self.l[0]
            del self.l[0]
            del self.l[0]


    def call_discovery(self):
        self.pingluncanshu.show()
        self.me.hide()

    def discovery_back(self):
        self.me.show()
        self.pingluncanshu.hide()

    def call_send(self):
        self.fasongcanshu.show()
        self.me.hide()

    def send_back(self):
        self.me.show()
        self.fasongcanshu.hide()

    #屏幕居中显示
    def center(self):
        qr = self.me.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.me.move(qr.topLeft())


def zhuyemian():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    me = QtWidgets.QMainWindow()
    ui = Discover_page()
    ui.discover_page(me)
    #点击发现就调用一次 get_massage函数
    ui.get_message()
    me.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    zhuyemian()
