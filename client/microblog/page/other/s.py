# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\kep\aid1803\microblog\microblog\page\s.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_me(object):
    def setupUi(self, me):
        me.setObjectName("me")
        me.setEnabled(True)
        me.resize(400, 600)
        me.setMinimumSize(QtCore.QSize(400, 600))
        me.setMaximumSize(QtCore.QSize(400, 600))
        me.setMouseTracking(False)
        me.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
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
        me.setCentralWidget(self.centralWidget)

        self.retranslateUi(me)
        self.home_page.clicked.connect(self.home_page.click)
        self.message.clicked.connect(self.message.click)
        self.new_blog.clicked.connect(self.new_blog.click)
        self.search.clicked.connect(self.search.click)
        self.me_.clicked.connect(self.me_.click)
        QtCore.QMetaObject.connectSlotsByName(me)

    def retranslateUi(self, me):
        _translate = QtCore.QCoreApplication.translate
        me.setWindowTitle(_translate("me", "weibo"))
        self.aboutme.setText(_translate("me", "我"))
        self.search_.setText(_translate("me", "发 现"))
        self.home.setText(_translate("me", "微 博"))
        self.msg.setText(_translate("me", "消 息"))

import imgs_search_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    me = QtWidgets.QMainWindow()
    ui = Ui_me()
    ui.setupUi(me)
    me.show()
    sys.exit(app.exec_())

