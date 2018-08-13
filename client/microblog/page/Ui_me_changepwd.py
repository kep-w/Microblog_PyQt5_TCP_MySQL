# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-13
# Version: v0.2

'''
密码修改页面
将用户输入密码通过哈希算法转换成密文传送
'''

import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changepwd(object):
    def __init__(self, client):
        self.client = client

    def setupUi(self, changepwd):
        changepwd.setObjectName("changepwd")
        changepwd.setEnabled(True)
        changepwd.resize(400, 600)
        changepwd.setMinimumSize(QtCore.QSize(400, 600))
        changepwd.setMaximumSize(QtCore.QSize(400, 600))
        changepwd.setMouseTracking(False)
        changepwd.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                "color: rgb(0, 0, 0);")

        self.changepwd = changepwd

        self.centralWidget = QtWidgets.QWidget(changepwd)
        self.centralWidget.setObjectName("centralWidget")
        self.userinfo = QtWidgets.QGroupBox(self.centralWidget)
        self.userinfo.setGeometry(QtCore.QRect(10, 40, 381, 501))
        self.userinfo.setObjectName("userinfo")
        self.uname = QtWidgets.QLabel(self.userinfo)
        self.uname.setGeometry(QtCore.QRect(16, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uname.setFont(font)
        self.uname.setAlignment(QtCore.Qt.AlignCenter)
        self.uname.setObjectName("uname")
        self.stime = QtWidgets.QLabel(self.userinfo)
        self.stime.setGeometry(QtCore.QRect(120, 100, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stime.setFont(font)
        self.stime.setText("")
        self.stime.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.stime.setObjectName("stime")
        self.nickname = QtWidgets.QLabel(self.userinfo)
        self.nickname.setGeometry(QtCore.QRect(120, 40, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickname.setFont(font)
        self.nickname.setText("")
        self.nickname.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nickname.setObjectName("nickname")
        self.confirm_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.confirm_pwd.setGeometry(QtCore.QRect(110, 303, 241, 35))
        self.confirm_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pwd.setObjectName("confirm_pwd")
        self.layoutWidget_2 = QtWidgets.QWidget(self.userinfo)
        self.layoutWidget_2.setGeometry(QtCore.QRect(15, 150, 81, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.old = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.old.setFont(font)
        self.old.setAlignment(QtCore.Qt.AlignCenter)
        self.old.setObjectName("old")
        self.verticalLayout_2.addWidget(self.old)
        self.new = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new.setFont(font)
        self.new.setAlignment(QtCore.Qt.AlignCenter)
        self.new.setObjectName("new")
        self.verticalLayout_2.addWidget(self.new)
        self.confirm = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm.setFont(font)
        self.confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm.setObjectName("confirm")
        self.verticalLayout_2.addWidget(self.confirm)
        self.old_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.old_pwd.setGeometry(QtCore.QRect(110, 163, 241, 35))
        self.old_pwd.setMaxLength(9)
        self.old_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_pwd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.old_pwd.setObjectName("old_pwd")
        self.new_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.new_pwd.setGeometry(QtCore.QRect(110, 234, 241, 35))
        self.new_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pwd.setObjectName("new_pwd")
        self.confirm_btn = QtWidgets.QCommandLinkButton(self.userinfo)
        self.confirm_btn.setGeometry(QtCore.QRect(230, 400, 101, 41))
        self.confirm_btn.setObjectName("confirm_btn")
        self.cancle_btn = QtWidgets.QCommandLinkButton(self.userinfo)
        self.cancle_btn.setGeometry(QtCore.QRect(40, 400, 101, 41))
        self.cancle_btn.setObjectName("cancle_btn")
        self.siguptime = QtWidgets.QLabel(self.userinfo)
        self.siguptime.setGeometry(QtCore.QRect(16, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.siguptime.setFont(font)
        self.siguptime.setAlignment(QtCore.Qt.AlignCenter)
        self.siguptime.setObjectName("siguptime")

        self.tip_pwd = QtWidgets.QLabel(self.changepwd)
        self.tip_pwd.setGeometry(QtCore.QRect(80, 390, 241, 35))
        self.tip_pwd.setText("")
        self.tip_pwd.setObjectName("tip_pwd")

        self.retranslateUi(changepwd)
        self.cancle_btn.clicked.connect(self.changepwd.close)
        self.confirm_btn.clicked.connect(self.confirmPwd)

        self.old_pwd.textChanged[str].connect(self.onChanged)
        self.new_pwd.textChanged[str].connect(self.onChanged)
        self.confirm_pwd.textChanged[str].connect(self.pwdCheck)

        self.checkinput()

    def retranslateUi(self, changepwd):
        _translate = QtCore.QCoreApplication.translate
        changepwd.setWindowTitle(_translate("changepwd", "密码修改"))
        self.userinfo.setTitle(_translate("changepwd", "账号信息"))
        self.uname.setText(_translate("changepwd", "昵    称"))
        self.old.setText(_translate("changepwd", "旧的密码"))
        self.new.setText(_translate("changepwd", "新的密码"))
        self.confirm.setText(_translate("changepwd", "确认密码"))
        self.old_pwd.setPlaceholderText(
            _translate("changepwd", "请输入您旧的的密码"))
        self.new_pwd.setPlaceholderText(
            _translate("changepwd", "密码6-9位，数字字母，必须以字母开头"))
        self.confirm_btn.setText(_translate("changepwd", "确认修改"))
        self.cancle_btn.setText(_translate("changepwd", "取消返回"))
        self.siguptime.setText(_translate("changepwd", "注册时间"))

    # 正则表达式函数判断密码有效性
    def checkinput(self):
        regx_pwd = QtCore.QRegExp(r"^[a-zA-Z][0-9A-Za-z]{5,8}$")
        validator = QtGui.QRegExpValidator(regx_pwd, self.new_pwd)
        self.new_pwd.setValidator(validator)

    # 监控文本框变化
    def onChanged(self, text):
        if not text:
            self.tip_pwd.setText("您输入的密码为空， 请重新输入！")
        elif len(text) < 6:
            self.tip_pwd.setText("您输入的密码长度小于6， 请重新输入！")
        else:
            self.tip_pwd.setText('')

    # 获取用户输入信息
    def usr_input(self):
        self.old_t = self.old_pwd.text()
        self.passwd_t = self.new_pwd.text()
        self.passwd_confirm_t = self.confirm_pwd.text()

    # 判断用户两次输入密码是否一致
    def pwdCheck(self, text):
        self.usr_input()
        if self.passwd_t != text:
            self.tip_pwd.setText("您两次输入的密码不一致，请重新输入！")
        else:
            self.tip_pwd.setText("")
            
    # 页面初始化时获取用户信息
    def get_info(self, username, stime, userid):
        self.nickname.setText(username)
        self.stime.setText(stime)
        self.username = username
        self.userid = userid

    # 用户提交,判定是否可以跳转
    def confirmPwd(self):
        self.usr_input()
        hash = hashlib.md5()
        hash.update(bytes(self.passwd_t,"utf-8"))
        self.hash_pwd = hash.hexdigest()
        hash_old = hashlib.md5()
        hash_old.update(bytes(self.old_t,"utf-8"))
        self.hash_pwd_old = hash_old.hexdigest()
        # 判断是否有空内容, 密码不一致, 无误后提交
        if self.tip_pwd.text():
            self.tip_pwd.setText('您输入的内容有误, 请检查无误后提交!')
        else:
            # 调用方法传入修改的密码
            statuscode = self.client.do_modify_pass(self.userid,self.username,self.hash_pwd_old,self.hash_pwd)
            if statuscode == '0000':
                return
            elif statuscode == '0001':
                self.tip_pwd.setText('原密码不正确,请重试!')
            else:
                self.tip_pwd.setText('发生未知错误, 请重试!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepwd = QtWidgets.QMainWindow()
    ui = Ui_changepwd()
    ui.setupUi(changepwd)
    changepwd.show()
    sys.exit(app.exec_())
