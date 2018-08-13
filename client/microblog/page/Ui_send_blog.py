#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-12
# Version: v0.1

'''
发布微博页面

'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Blog(object):
    def __init__(self, client):
        self.client = client

    def setupUi(self, Blog):
        Blog.setObjectName("Blog")
        Blog.resize(400, 237)
        self.send_btn = QtWidgets.QPushButton(Blog)
        self.send_btn.setGeometry(QtCore.QRect(300, 0, 100, 40))
        self.send_btn.setStyleSheet("font: 11pt \"Arial\";")
        self.send_btn.setFlat(True)
        self.send_btn.setObjectName("send_btn")
        self.back_btn = QtWidgets.QPushButton(Blog)
        self.back_btn.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.back_btn.setStyleSheet("font: 11pt \"Arial\";")
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.blog_content = QtWidgets.QTextEdit(Blog)
        self.blog_content.setGeometry(QtCore.QRect(0, 40, 401, 200))
        self.blog_content.setStyleSheet("font: 14pt \"Arial\";")
        self.blog_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blog_content.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.blog_content.setObjectName("blog_content")
        self.send_blog = QtWidgets.QLabel(Blog)
        self.send_blog.setGeometry(QtCore.QRect(166, 0, 70, 40))
        self.send_blog.setStyleSheet("font: 14pt \"Arial\";")
        self.send_blog.setObjectName("send_blog")

        self.retranslateUi(Blog)
        QtCore.QMetaObject.connectSlotsByName(Blog)

    def retranslateUi(self, Blog):
        _translate = QtCore.QCoreApplication.translate
        Blog.setWindowTitle(_translate("Blog", "发微博"))
        self.send_btn.setText(_translate("Blog", "发送"))
        self.back_btn.setText(_translate("Blog", "退出"))
        self.send_blog.setText(_translate("Blog", "发微博"))

    # 获取用户输入的微博正文
    def get_input(self):
        msg = self.blog_content.toPlainText()
        return msg

    # 提交消息
    def sendNew(self, userid):
        msg = self.get_input()
        statuscode = self.client.do_publish(userid, msg)
        if statuscode == '0000':
            return
        else:
            self.blog_content.setText(msg+"\n"+"异常错误,请重试!")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Blog = QtWidgets.QDialog()
    ui = Ui_Blog()
    ui.setupUi(Blog)
    Blog.show()
    sys.exit(app.exec_())

