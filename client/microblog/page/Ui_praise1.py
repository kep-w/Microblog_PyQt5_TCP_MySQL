# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\xiangmu\项目\comment_second\praise\praise.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Praise(object):
    def setupUi2(self, Dialog_praise):

        self.Dialog_praise=Dialog_praise
        Dialog_praise.setObjectName("Dialog_praise")
        Dialog_praise.resize(400, 600)
        Dialog_praise.setMinimumSize(QtCore.QSize(400, 600))
        Dialog_praise.setMaximumSize(QtCore.QSize(400, 600))
        Dialog_praise.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog_praise)
        self.label.setGeometry(QtCore.QRect(195, 10, 81, 18))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QPushButton(Dialog_praise)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 52, 24))
        self.toolButton.setMinimumSize(QtCore.QSize(52, 24))
        self.toolButton.setMaximumSize(QtCore.QSize(52, 24))
        self.toolButton.setObjectName("toolButton")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog_praise)
        self.textBrowser.setGeometry(QtCore.QRect(2, 60, 395, 531))
        self.textBrowser.setMinimumSize(QtCore.QSize(395, 531))
        self.textBrowser.setMaximumSize(QtCore.QSize(395, 531))
        self.textBrowser.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(235,237,244,0.8);")
        self.textBrowser.setObjectName("textBrowser1")
        self.toolButton.setFlat(True)

        self.retranslateUi(Dialog_praise)
        # self.toolButton.clicked.connect(Dialog_praise.close)
        # QtCore.QMetaObject.connectSlotsByName(Dialog_praise)

    def retranslateUi(self, Dialog_praise):
        _translate = QtCore.QCoreApplication.translate
        Dialog_praise.setWindowTitle(_translate("Dialog_praise", "Dialog"))
        self.label.setText(_translate("Dialog_praise", "赞"))
        self.toolButton.setText(_translate("Dialog_praise", "返回"))

    def pra_news(self,m):
        l=''
        for i in m:
            l+=i
            l+='\n'
            l+='******************************************'
            l+='\n'
        self.textBrowser.setText(l)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_praise = QtWidgets.QDialog()
    ui = Praise()
    ui.setupUi2(Dialog_praise)
    Dialog_praise.show()
    sys.exit(app.exec_())

