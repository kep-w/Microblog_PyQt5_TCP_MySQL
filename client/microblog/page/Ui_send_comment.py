#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-10
# Version: v0.1

'''
评论发布页面

'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SendComment(object):
    def __init__(self, client):
        self.client = client

    def setupUi(self, Send_com):
        Send_com.setObjectName("Send_com")
        Send_com.resize(400, 237)
        self.send_btn = QtWidgets.QPushButton(Send_com)
        self.send_btn.setGeometry(QtCore.QRect(300, 0, 100, 40))
        self.send_btn.setStyleSheet("font: 11pt \"Arial\";")
        self.send_btn.setFlat(True)
        self.send_btn.setObjectName("send_btn")
        self.back_btn = QtWidgets.QPushButton(Send_com)
        self.back_btn.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.back_btn.setStyleSheet("font: 11pt \"Arial\";")
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.comment = QtWidgets.QTextEdit(Send_com)
        self.comment.setGeometry(QtCore.QRect(0, 40, 401, 200))
        self.comment.setStyleSheet("font: 14pt \"Arial\";")
        self.comment.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.comment.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.comment.setObjectName("comment")
        self.send_comment = QtWidgets.QLabel(Send_com)
        self.send_comment.setGeometry(QtCore.QRect(166, 0, 70, 40))
        self.send_comment.setStyleSheet("font: 14pt \"Arial\";")
        self.send_comment.setObjectName("send_comment")

        self.retranslateUi(Send_com)
        QtCore.QMetaObject.connectSlotsByName(Send_com)

    def retranslateUi(self, Send_com):
        _translate = QtCore.QCoreApplication.translate
        Send_com.setWindowTitle(_translate("Send_com", "Dialog"))
        self.send_btn.setText(_translate("Send_com", "发送"))
        self.back_btn.setText(_translate("Send_com", "退出"))
        self.send_comment.setText(_translate("Send_com", "发评论"))

    # 获取用户输入内容
    def get_input(self):
        msg = self.comment.toPlainText()
        return msg

    # 初始化时获取用户消息及所评论消息
    def get_msgid(self, msgid, userid):
        print(msgid,"进入评论页面")
        self.msgid = msgid
        self.userid = userid

    # 发布评论
    def do_com(self):
        comminfo = self.get_input()
        print('发布评论页面',comminfo)
        statuscode = self.client.do_comment(self.userid,self.msgid,comminfo)
        print(statuscode)
        if statuscode == '0000':
            print('发布评论成功')
        else:
            self.comment.setText(comminfo+"\n"+"出现错误,请重试!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Send_com = QtWidgets.QDialog()
    ui = Ui_SendComment()
    ui.setupUi(Send_com)
    Send_com.show()
    sys.exit(app.exec_())

