#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-12
# Version: v0.2

'''
微博详情页面

'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Detail(object):
    # 初始化与服务器通讯的类
    def __init__(self, client):
        self.client = client

    # 页面样式方法
    def setupUi(self, Detail):
        Detail.setObjectName("Detail")
        Detail.resize(400, 600)
        self.fabulous_btn = QtWidgets.QPushButton(Detail)
        self.fabulous_btn.setGeometry(QtCore.QRect(0, 568, 100, 30))
        self.fabulous_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.fabulous_btn.setFlat(True)
        self.fabulous_btn.setObjectName("fabulous_btn")
        self.comment_btn = QtWidgets.QPushButton(Detail)
        self.comment_btn.setGeometry(QtCore.QRect(300, 568, 100, 30))
        self.comment_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.comment_btn.setFlat(True)
        self.comment_btn.setObjectName("comment_btn")
        self.forward_btn = QtWidgets.QPushButton(Detail)
        self.forward_btn.setGeometry(QtCore.QRect(150, 568, 100, 30))
        self.forward_btn.setStyleSheet("font: 14pt \"Arial\";")
        self.forward_btn.setFlat(True)
        self.forward_btn.setObjectName("forward_btn")
        self.back = QtWidgets.QPushButton(Detail)
        self.back.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.back.setStyleSheet("font: 12pt \"Arial\";")
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.content = QtWidgets.QTextBrowser(Detail)
        self.content.setGeometry(QtCore.QRect(10, 30, 380, 180))
        self.content.setStyleSheet(
            "font: 12pt \"Arial\";background-color:rgba(253,253,253,0.5);")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setObjectName("content")
        self.weibo = QtWidgets.QLabel(Detail)
        self.weibo.setGeometry(QtCore.QRect(150, 0, 100, 30))
        self.weibo.setStyleSheet("font: 14pt \"Arial\";")
        self.weibo.setObjectName("weibo")
        self.comment_list = QtWidgets.QTextBrowser(Detail)
        self.comment_list.setGeometry(QtCore.QRect(10, 260, 380, 301))
        self.comment_list.setStyleSheet(
            "font: 12pt \"Arial\";background-color:rgba(253,253,253,0.5);")
        self.comment_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.comment_list.setObjectName("comment_list")
        self.count_comment = QtWidgets.QLabel(Detail)
        self.count_comment.setGeometry(QtCore.QRect(30, 232, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.count_comment.setFont(font)
        self.count_comment.setAlignment(QtCore.Qt.AlignCenter)
        self.count_comment.setObjectName("count_comment")
        self.count_fabulous = QtWidgets.QLabel(Detail)
        self.count_fabulous.setGeometry(QtCore.QRect(170, 232, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.count_fabulous.setFont(font)
        self.count_fabulous.setAlignment(QtCore.Qt.AlignCenter)
        self.count_fabulous.setObjectName("count_fabulous")
        self.count_forward = QtWidgets.QLabel(Detail)
        self.count_forward.setGeometry(QtCore.QRect(300, 232, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.count_forward.setFont(font)
        self.count_forward.setAlignment(QtCore.Qt.AlignCenter)
        self.count_forward.setObjectName("count_forward")

        self.tip_info = QtWidgets.QLabel(Detail)
        self.tip_info.setGeometry(QtCore.QRect(30, 530, 241, 20))
        self.tip_info.setText("")
        self.tip_info.setObjectName("tip_info")

        self.retranslateUi(Detail)
        QtCore.QMetaObject.connectSlotsByName(Detail)

    def retranslateUi(self, Detail):
        _translate = QtCore.QCoreApplication.translate
        Detail.setWindowTitle(_translate("Detail", "Dialog"))
        self.fabulous_btn.setText(_translate("Detail", "点赞"))
        self.comment_btn.setText(_translate("Detail", "评论"))
        self.forward_btn.setText(_translate("Detail", "转发"))
        self.back.setText(_translate("Detail", "返回"))
        self.weibo.setText(_translate("Detail", "微博正文"))
        self.count_comment.setText(_translate("Detail", "被评论数"))
        self.count_fabulous.setText(_translate("Detail", "点赞数量"))
        self.count_forward.setText(_translate("Detail", "转发数量"))

    # 获取此消息的相关信息, 保存为属性
    def get_msg(self, msg, userid):
        self.msg = msg
        self.userid = userid
        self.msgid = msg.getmessagesid()
        self.relateid = msg.getuserid()
        self.msginfo = msg.getmessagesinfo()
        self.set_count()
        self.set_commentContent()
        self.set_weiboContent()

    # 点赞相关
    def fabulous(self):
        statuscode1 = self.client.do_agree(self.msgid, self.userid)
        # 判断是不是用户自己为自己的消息点赞
        if self.userid != self.msg.getuserid():
            # 不是用户自己, 则点赞同时关注用户
            statuscode2 = self.client.do_relate(self.userid, self.relateid)
            print(statuscode1, statuscode2)
            if statuscode1 == '0000':
                if statuscode2 == '0000':
                    self.tip_info.setText('点赞成功, 您已成功关注该用户!')
            else:
                self.tip_info.setText('发生错误, 请稍后重试!')
        else:
            # 是用户自己, 则只点赞
            if statuscode1 == "0000":
                self.tip_info.setText('为自己点赞成功!')
            else:
                self.tip_info.setText('发生错误, 请稍后重试!')

    # 转发相关的方法
    def forward(self):
        if self.userid != self.msg.getuserid():
            statuscode = self.client.do_forward(self.msgid, self.userid)
            if statuscode == '0000':
                code = self.client.do_publish(self.userid, self.msginfo)
                if code == '0000':
                    self.tip_info.setText('转发成功!')
                else:
                    self.tip_info.setText('发生错误, 请稍后重试!')
            else:
                self.tip_info.setText('发生错误, 请稍后重试!')
        else:
            self.tip_info.setText('这是您自己发布的微博哦!')

    # 修改设置数量
    def set_count(self):
        self.count_comment.setText("评论" + str(len(self.msg.getcommentlist())))
        self.count_fabulous.setText("点赞" + str(self.msg.getmessagesagreenum()))
        self.count_forward.setText(
            "转发" + str(self.msg.getmessagestranspondnum()))

    # 设置评论内容
    def set_commentContent(self):
        commentList = self.msg.getcommentlist()
        show = ""
        for cm in commentList:
            show += cm.getusername() + "\t" + cm.getcommentstime() + \
                "\n" + cm.getcommentinfo()+'\n' + '\n'
        self.comment_list.setText(show)

    # 设置微博正文
    def set_weiboContent(self):
        self.content.setText(self.msg.username + '\n' +
                             self.msg.getmessagestime() + '\n' + self.msg.getmessagesinfo())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detail = QtWidgets.QDialog()
    ui = Ui_Detail()
    ui.setupUi(Detail)
    Detail.show()
    sys.exit(app.exec_())
