# -*- coding: utf-8 -*-
# Auther: Kepner Wu
# Date: 2018-06-12
# Version: v0.4

'''
注册页面
注册成功跳转主页或登录页面
注册失败判断原因进一步操作
通过哈希散列对用户密码进行转换,确保安全

'''

import re
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):

    def __init__(self, client):
        self.client = client

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 480)
        self.dialog = Dialog
        self.return_home = QtWidgets.QPushButton(Dialog)
        self.return_home.setGeometry(QtCore.QRect(40, 390, 121, 41))
        self.return_home.setObjectName("return_home")
        self.signup = QtWidgets.QPushButton(Dialog)
        self.signup.setGeometry(QtCore.QRect(240, 390, 121, 41))
        self.signup.setObjectName("signup")
        self.passwd_confirm = QtWidgets.QLineEdit(Dialog)
        self.passwd_confirm.setGeometry(QtCore.QRect(90, 170, 280, 32))
        self.passwd_confirm.setMinimumSize(QtCore.QSize(0, 32))
        self.passwd_confirm.setText("")
        self.passwd_confirm.setObjectName("passwd_confirm")
        self.remind_passwd = QtWidgets.QLabel(Dialog)
        self.remind_passwd.setGeometry(QtCore.QRect(70, 350, 301, 41))
        self.remind_passwd.setText("")
        self.remind_passwd.setObjectName("remind_passwd")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setEnabled(True)
        self.name.setGeometry(QtCore.QRect(90, 40, 280, 32))
        self.name.setMinimumSize(QtCore.QSize(280, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(9)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setObjectName("name")
        self.mail = QtWidgets.QLineEdit(Dialog)
        self.mail.setGeometry(QtCore.QRect(90, 310, 280, 32))
        self.mail.setMinimumSize(QtCore.QSize(0, 30))
        self.mail.setObjectName("mail")
        self.phoneNumber = QtWidgets.QLineEdit(Dialog)
        self.phoneNumber.setGeometry(QtCore.QRect(90, 240, 280, 32))
        self.phoneNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.phoneNumber.setObjectName("phoneNumber")
        self.tip_phone = QtWidgets.QLabel(Dialog)
        self.tip_phone.setGeometry(QtCore.QRect(70, 350, 301, 31))
        self.tip_phone.setText("")
        self.tip_phone.setObjectName("tip_phone")
        self.passwd = QtWidgets.QLineEdit(Dialog)
        self.passwd.setGeometry(QtCore.QRect(90, 110, 280, 32))
        self.passwd.setMinimumSize(QtCore.QSize(0, 32))
        self.passwd.setText("")
        self.passwd.setObjectName("passwd")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 91, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLabel(self.layoutWidget)
        self.username.setBaseSize(QtCore.QSize(0, 3))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setScaledContents(False)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.userpwd = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.userpwd.setFont(font)
        self.userpwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userpwd.setScaledContents(False)
        self.userpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.userpwd.setObjectName("userpwd")
        self.verticalLayout.addWidget(self.userpwd)
        self.userpwd_confirm = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.userpwd_confirm.setFont(font)
        self.userpwd_confirm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userpwd_confirm.setScaledContents(False)
        self.userpwd_confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.userpwd_confirm.setObjectName("userpwd_confirm")
        self.verticalLayout.addWidget(self.userpwd_confirm)
        self.usrphone = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.usrphone.setFont(font)
        self.usrphone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usrphone.setScaledContents(False)
        self.usrphone.setAlignment(QtCore.Qt.AlignCenter)
        self.usrphone.setObjectName("usrphone")
        self.verticalLayout.addWidget(self.usrphone)
        self.usermail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.usermail.setFont(font)
        self.usermail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usermail.setScaledContents(False)
        self.usermail.setAlignment(QtCore.Qt.AlignCenter)
        self.usermail.setObjectName("usermail")
        self.verticalLayout.addWidget(self.usermail)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.setTabOrder(self.name, self.passwd)
        Dialog.setTabOrder(self.passwd, self.passwd_confirm)
        Dialog.setTabOrder(self.passwd_confirm, self.phoneNumber)
        Dialog.setTabOrder(self.phoneNumber, self.mail)
        Dialog.setTabOrder(self.mail, self.return_home)
        Dialog.setTabOrder(self.return_home, self.signup)

        # 设置用户名及密码文本框
        self.name.setPlaceholderText("字母数字,且不为纯数字.长度在3-8之间")
        self.passwd.setPlaceholderText("密码6-9位，数字字母，须以字母开头")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwd_confirm.setEchoMode(QtWidgets.QLineEdit.Password)

        # 输入框输入内容判定关联
        self.name.textChanged[str].connect(self.nameCheck)
        self.passwd.textChanged[str].connect(self.onChanged)
        self.phoneNumber.textChanged[str].connect(self.phoneNumberCheck)
        self.mail.textChanged[str].connect(self.mailCheck)
        self.passwd_confirm.textChanged[str].connect(self.pwdCheck)

        # 需要的函数调用
        self.check_input()

    # 页面内容初始化函数
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.return_home.setText(_translate("Dialog", "返   回"))
        self.signup.setText(_translate("Dialog", "注   册"))
        self.username.setText(_translate("Dialog", "用户名"))
        self.userpwd.setText(_translate("Dialog", "密  码"))
        self.userpwd_confirm.setText(_translate("Dialog", "确认密码"))
        self.usrphone.setText(_translate("Dialog", "电  话"))
        self.usermail.setText(_translate("Dialog", "邮  箱"))

    # 正则表达式判断函数
    def check_input(self):
        regx_name = QtCore.QRegExp(r'^\w{3,8}')
        self.rejudgement(self.name, regx_name)
        regx_pwd = QtCore.QRegExp(r"^[a-zA-Z][0-9A-Za-z]{5,8}$")
        self.rejudgement(self.passwd, regx_pwd)
        regx_phone = QtCore.QRegExp(r'^1\d{10}$')
        self.rejudgement(self.phoneNumber, regx_phone)

    # 正则表达式函数
    def rejudgement(self, text, regx):
        validator = QtGui.QRegExpValidator(regx, text)
        text.setValidator(validator)

    # 获取用户输入的信息
    def usr_input(self):
        self.name_t = self.name.text()
        self.passwd_t = self.passwd.text()
        self.passwd_confirm_t = self.passwd_confirm.text()
        self.phoneNumber_t = self.phoneNumber.text()
        self.mail_t = self.mail.text()

    # 用户名输入为空判定
    def nameCheck(self, text):
        if not text:
            self.tip_phone.setText("您输入的用户名为空， 请重新输入！")
        elif len(text) < 3:
            self.tip_phone.setText("您输入的用户名长度小于3， 请重新输入！")
        else:
            self.tip_phone.setText('')

    # 用户首次输入密码判断
    def onChanged(self, text):
        if not text:
            self.tip_phone.setText("您输入的密码为空， 请重新输入！")
        elif len(text) < 6:
            self.tip_phone.setText("您输入的密码长度小于6， 请重新输入！")
        else:
            self.tip_phone.setText('')

    # 用户输入手机号判断
    def phoneNumberCheck(self, text):
        if not text:
            self.tip_phone.setText("您输入的内容为空， 请重新输入！")
        elif len(text) < 11:
            self.tip_phone.setText('您输入的号码有误， 请重新输入！')
        else:
            self.tip_phone.setText('')

    # 动态检验用户两次输入密码是否一致
    def pwdCheck(self, text):
        self.usr_input()
        if self.passwd_t != text:
            self.remind_passwd.setText("您两次输入的密码不一致，请重新输入！")
        else:
            self.remind_passwd.setText("")

    # 用户输入邮箱是否为空判断
    def mailCheck(self, text):
        if not text:
            self.tip_phone.setText("您输入的邮箱为空， 请重新输入！")
        else:
            self.tip_phone.setText('')

    # 通过正则匹配用户输入,判断是否为邮箱格式,并返回结果
    def get_mail(self):
        self.usr_input()
        try:
            usr_mail = re.search(r'^\w+@\w+(\.(\w)+)+$', self.mail_t).group()
        except:
            usr_mail = None
        finally:
            return usr_mail

    # 用户提交,判定是否可以跳转
    def signup_info(self):
        self.usr_input()
        hash = hashlib.md5()
        hash.update(bytes(self.passwd_t, "utf-8"))
        self.hash_pwd = hash.hexdigest()
        print(self.hash_pwd)
        usr_mail = self.get_mail()
        # 判断是否有空内容, 密码不一致, 邮箱不正确, 无误后提交
        if self.tip_phone.text() or self.remind_passwd.text():
            self.tip_phone.setText('您输入的内容有误, 请检查无误后提交!')
        elif self.passwd_t != self.passwd_confirm_t:
            self.tip_phone.setText("您两次输入的密码不一致，请重新输入！")
        elif usr_mail != self.mail_t:
            self.tip_phone.setText('您输入的邮箱有误， 请重新输入！')
        else:
            info = self.client.do_register(self.name_t, self.hash_pwd,
                                           self.phoneNumber_t, self.mail_t)
            print(self.name_t, self.hash_pwd, self.phoneNumber_t, self.mail_t)
            print(info)
            if info[0] == '0000':
                return (info[1], self.name_t, self.phoneNumber_t, self.mail_t)
            elif info[0] == '0001':
                self.tip_phone.setText('用户名已存在,请重试')
            else:
                self.tip_phone.setText('未知错误,请重试')


# 自测函数
def main():
    client = ClientMsgDeal()
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Signup(client)
    Dialog = QtWidgets.QDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
