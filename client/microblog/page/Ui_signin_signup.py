# -*- coding: utf-8 -*-
# Auther: Kepner Wu
# Date: 2018-06-012
# Version: v0.4

'''
登录页面
登录成功进入下一页
登录失败判断原因进一步操作
通过哈希散列对用户密码进行转换,确保安全

'''

import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_signup import Ui_Signup


class Ui_Login(object):
    def __init__(self, client):
        self.client = client

    def setupUi(self, Login):
        # self.s = Ui_Signup(self.client)
        # self.dialog = QtWidgets.QDialog()
        # self.s.setupUi(self.dialog)
        Login.setObjectName("Login")
        Login.resize(400, 480)
        self.login = Login
        self.Signin = QtWidgets.QPushButton(Login)
        self.Signin.setGeometry(QtCore.QRect(50, 360, 110, 41))
        self.Signin.setObjectName("Signin")
        self.Signup = QtWidgets.QPushButton(Login)
        self.Signup.setGeometry(QtCore.QRect(240, 360, 110, 41))
        self.Signup.setObjectName("Signup")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username = QtWidgets.QLabel(Login)
        self.username.setGeometry(QtCore.QRect(25, 120, 91, 51))
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setScaledContents(False)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userpwd = QtWidgets.QLabel(Login)
        self.userpwd.setGeometry(QtCore.QRect(25, 210, 91, 51))
        self.userpwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userpwd.setScaledContents(False)
        self.userpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.userpwd.setObjectName("userpwd")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome = QtWidgets.QLabel(Login)
        self.welcome.setGeometry(QtCore.QRect(40, 20, 201, 71))
        self.welcome.setObjectName("welcome")
        self.name = QtWidgets.QLineEdit(Login)
        self.name.setGeometry(QtCore.QRect(95, 130, 260, 31))
        self.name.setObjectName("name")
        self.passwd = QtWidgets.QLineEdit(Login)
        self.passwd.setGeometry(QtCore.QRect(95, 220, 260, 31))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(60, 300, 281, 31))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Login)

        QtCore.QMetaObject.connectSlotsByName(Login)
        # 设置密码密文
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # 调用保存设置文件查看用户名密码
        self.check_info()

        self.name.textChanged[str].connect(self.nameCheck)
        self.passwd.textChanged[str].connect(self.onChanged)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录/注册"))
        self.Signin.setText(_translate("Login", "登   录"))
        self.Signup.setText(_translate("Login", "注   册"))
        self.username.setText(_translate("Login", "用户名："))
        self.userpwd.setText(_translate("Login", "密  码："))
        self.welcome.setText(_translate("Login", "欢迎您登录/注册微博！"))

    # 用户名输入为空判定
    def nameCheck(self, text):
        if not text:
            self.label.setText("您输入的用户名为空， 请重新输入！")
        elif len(text) < 3:
            self.label.setText("您输入的用户名长度小于3， 请重新输入！")
        else:
            self.label.setText('')

    # 用户输入密码判断
    def onChanged(self, text):
        if not text:
            self.label.setText("您输入的密码为空， 请重新输入！")
        elif len(text) < 6:
            self.label.setText("您输入的密码长度小于6， 请重新输入！")
        else:
            self.label.setText('')

    # 获取用户输入信息
    def signin_info(self):
        self.name_text = self.name.text()
        self.passwd_text = self.passwd.text()
        hash = hashlib.md5()
        hash.update(bytes(self.passwd_text, "utf-8"))
        self.hash_pwd = hash.hexdigest()
        print(self.hash_pwd)

    # 检查登录配置用户信息文件
    def check_info(self):
        try:
            with open('user_information.txt', 'rb') as f:
                uname = f.readline().decode().strip()
                upwd = f.readline().decode().strip()
        except:
            pass
        else:
            self.name.setText(uname)
            self.passwd.setText(upwd)
            self.label.setText('')

     # 将用户信息保存到登录配置文件
    def save_info(self):
        try:
            with open('user_information.txt', 'rb') as f:
                f.writeline(self.name_text+'\n')
                f.writeline(self.passwd_text+'\n')
        except:
            pass

    # 判断用户输入信息同时提交
    def judgement(self):
        self.signin_info()
        self.save_info()
        if not self.label.text():
            info = self.client.do_login(self.name_text, self.hash_pwd)
            print(info)
            if info[0] == '0000':
                self.save_info()
                # 登录成功, 返回用户名和uid
                return (self.name_text, info[1])
            elif info[0] == '0002':
                self.label.setText('用户名不存在, 请重新输入或点击注册!')
            elif info[0] == '0003':
                self.label.setText('您输入的密码不正确!')
            else:
                self.label.setText('未知错误, 请重试!')
        else:
            self.label.setText("请输入您的用户名及密码...")


if __name__ == "__main__":
    import sys
    client = ClientMsgDeal()
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    Login = QtWidgets.QDialog()
    ui = Ui_Login(client)
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
