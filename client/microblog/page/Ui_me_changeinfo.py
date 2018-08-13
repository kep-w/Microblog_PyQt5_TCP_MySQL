# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-14
# Version: v0.2

'''
个人信息修改页面
其中用户名手机号邮箱不可以修改
'''

import re
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeinfo(object):
    def __init__(self, client):
        self.client = client

    def setupUi(self, changeinfo):
        changeinfo.setObjectName("changeinfo")
        changeinfo.setEnabled(True)
        changeinfo.resize(400, 600)
        changeinfo.setMinimumSize(QtCore.QSize(400, 600))
        changeinfo.setMaximumSize(QtCore.QSize(400, 600))
        changeinfo.setMouseTracking(False)
        changeinfo.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                 "color: rgb(0, 0, 0);")

        self.changeinfo = changeinfo

        self.centralWidget = QtWidgets.QWidget(changeinfo)
        self.centralWidget.setObjectName("centralWidget")
        self.userinfo = QtWidgets.QGroupBox(self.centralWidget)
        self.userinfo.setGeometry(QtCore.QRect(10, 50, 381, 251))
        self.userinfo.setObjectName("userinfo")
        self.intro = QtWidgets.QLabel(self.userinfo)
        self.intro.setGeometry(QtCore.QRect(16, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intro.setFont(font)
        self.intro.setAlignment(QtCore.Qt.AlignCenter)
        self.intro.setObjectName("intro")
        self.uname = QtWidgets.QLabel(self.userinfo)
        self.uname.setGeometry(QtCore.QRect(15, 40, 140, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.uname.setFont(font)
        self.uname.setAlignment(QtCore.Qt.AlignCenter)
        self.uname.setObjectName("uname")
        self.intro_change = QtWidgets.QTextEdit(self.userinfo)
        self.intro_change.setGeometry(QtCore.QRect(110, 130, 241, 111))
        self.intro_change.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.intro_change.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.intro_change.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.intro_change.setTabChangesFocus(False)
        self.intro_change.setObjectName("intro_change")
        self.stime = QtWidgets.QLabel(self.userinfo)
        self.stime.setGeometry(QtCore.QRect(120, 80, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stime.setFont(font)
        self.stime.setText("")
        self.stime.setObjectName("stime")
        self.nickname = QtWidgets.QLabel(self.userinfo)
        self.nickname.setGeometry(QtCore.QRect(120, 40, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickname.setFont(font)
        self.nickname.setText("")
        self.nickname.setObjectName("nickname")
        self.siguptime = QtWidgets.QLabel(self.userinfo)
        self.siguptime.setGeometry(QtCore.QRect(16, 82, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.siguptime.setFont(font)
        self.siguptime.setAlignment(QtCore.Qt.AlignCenter)
        self.siguptime.setObjectName("siguptime")

        self.userinfo_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.userinfo_2.setGeometry(QtCore.QRect(10, 310, 381, 221))
        self.userinfo_2.setObjectName("userinfo_2")
        self.mail_t = QtWidgets.QLabel(self.userinfo_2)
        self.mail_t.setGeometry(QtCore.QRect(110, 175, 241, 26))
        self.mail_t.setObjectName("mail_t")
        self.phoneno_t = QtWidgets.QLabel(self.userinfo_2)
        self.phoneno_t.setGeometry(QtCore.QRect(110, 127, 241, 26))
        self.phoneno_t.setObjectName("phoneno_t")
        self.birthday_t = QtWidgets.QLineEdit(self.userinfo_2)
        self.birthday_t.setGeometry(QtCore.QRect(110, 79, 241, 26))
        self.birthday_t.setMaxLength(10)
        self.birthday_t.setObjectName("birthday_t")
        self.layoutWidget = QtWidgets.QWidget(self.userinfo_2)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 20, 81, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gender = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender.setFont(font)
        self.gender.setAlignment(QtCore.Qt.AlignCenter)
        self.gender.setObjectName("gender")
        self.verticalLayout.addWidget(self.gender)
        self.birthday = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birthday.setFont(font)
        self.birthday.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday.setObjectName("birthday")
        self.verticalLayout.addWidget(self.birthday)
        self.phoneno = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneno.setFont(font)
        self.phoneno.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneno.setObjectName("phoneno")
        self.verticalLayout.addWidget(self.phoneno)
        self.mail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mail.setFont(font)
        self.mail.setAlignment(QtCore.Qt.AlignCenter)
        self.mail.setObjectName("mail")
        self.verticalLayout.addWidget(self.mail)
        self.genderBox = QtWidgets.QLineEdit(self.userinfo_2)
        self.genderBox.setGeometry(QtCore.QRect(110, 32, 241, 26))
        self.genderBox.setObjectName("genderBox")
        self.cancle_btn = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.cancle_btn.setGeometry(QtCore.QRect(150, 10, 101, 41))
        self.cancle_btn.setObjectName("cancle_btn")
        self.confirm_btn = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.confirm_btn.setGeometry(QtCore.QRect(280, 10, 101, 41))
        self.confirm_btn.setObjectName("confirm_btn")

        self.tip_info = QtWidgets.QLabel(self.changeinfo)
        self.tip_info.setGeometry(QtCore.QRect(80, 540, 260, 35))
        self.tip_info.setText("")
        self.tip_info.setObjectName("tip_info")

        self.retranslateUi(changeinfo)

        self.birthday_t.textChanged[str].connect(self.onChanged)

        self.check_input()

    def retranslateUi(self, changeinfo):
        _translate = QtCore.QCoreApplication.translate
        changeinfo.setWindowTitle(_translate("changeinfo", "修改信息"))
        self.userinfo.setTitle(_translate("changeinfo", "账号信息"))
        self.intro.setText(_translate("changeinfo", "简    介"))
        self.uname.setText(_translate("changeinfo", "昵    称"))
        self.intro_change.setPlaceholderText(
            _translate("changeinfo", "输入您的个人简介"))
        self.siguptime.setText(_translate("changeinfo", "注册时间"))
        self.userinfo_2.setTitle(_translate("changeinfo", "个人信息"))
        self.birthday_t.setPlaceholderText(
            _translate("changeinfo", "2018-08-08"))
        self.gender.setText(_translate("changeinfo", "性    别"))
        self.birthday.setText(_translate("changeinfo", "生    日"))
        self.phoneno.setText(_translate("changeinfo", "手机号码"))
        self.mail.setText(_translate("changeinfo", "邮    箱"))
        self.genderBox.setText(_translate("changeinfo", "输入您的性别"))
        self.cancle_btn.setText(_translate("changeinfo", "取消返回"))
        self.confirm_btn.setText(_translate("changeinfo", "确认修改"))

    # 对文本框变化的监控
    def onChanged(self, text):
        if not text:
            self.tip_info.setText("您输入的内容为空， 请重新输入！")
        else:
            self.tip_info.setText("")

    # 获取用户输入信息, 并保存为属性
    def usr_input(self):
        self.cintroduction = self.intro_change.toPlainText()
        self.gender = self.genderBox.text()
        # self.cphoneno = self.phoneno_t.text()
        self.cbrithday = self.birthday_t.text()
        # self.cmail = self.mail_t.text()

    # 检查用户输入的生日是否合法
    def check_input(self):
        # regx_phone = QtCore.QRegExp(r'^1\d{10}$')
        # validator = QtGui.QRegExpValidator(regx_phone, self.phoneno_t)
        # self.phoneno_t.setValidator(validator)
        regx_brithday = QtCore.QRegExp(
            r"^(19|20)\d{2}-(1[0-2]|0?[1-9])-(0?[1-9]|[1-2][0-9]|3[0-1])$")
        validator = QtGui.QRegExpValidator(regx_brithday, self.birthday_t)
        self.birthday_t.setValidator(validator)

    # 判断邮箱有效性
    # def get_mail(self):
    #     self.usr_input()
    #     try:
    #         usr_mail = re.search(r'^\w+@\w+(\.(\w)+)+$', self.mail_t).group()
    #     except:
    #         usr_mail = None
    #     finally:
    #         return usr_mail

    # 确认提交按钮
    def confirmInfo(self):
        self.usr_input()
        # usr_mail = self.get_mail()
        if self.tip_info.text():
            self.tip_info.setText('您输入的内容有误, 请检查无误后提交!')
        # elif usr_mail != self.cmail and usr_mail != None:
        #     self.tip_info.setText('您输入的邮箱有误，请重新输入！')
        else:
            # 调用方法传入修改的数据
            statuscode = self.client.do_modify_userinfo(self.userid,self.username, self.gender,self.cbrithday,self.cintroduction)
            if statuscode == '0000':
                return (self.cintroduction, self.gender,
                   self.cbrithday)
            else:
                self.tip_info.setText('发生未知错误, 请重试!')

    # 从主模块获取用户信息, 并保存为属性
    def get_info(self, username, userid, brithday, gender, stime, introduction, phoneno, mail):
        self.uname.setText(username)
        self.username = username
        self.userid = userid
        self.birthday_t.setText(brithday)
        self.genderBox.setText(gender)
        self.stime.setText(stime)
        self.intro_change.setText(introduction)
        self.phoneno_t.setText(phoneno)
        self.mail_t.setText(mail)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changeinfo = QtWidgets.QMainWindow()
    ui = Ui_changeinfo()
    ui.setupUi(changeinfo)
    changeinfo.show()
    sys.exit(app.exec_())