# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\xiangmu\项目\comment_second\comment\_eric6project/comment.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Comment(object):
    def setupUi1(self, Dialog):
        
        self.Dialog=Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 600)
        self.Dialog.setMinimumSize(QtCore.QSize(400, 600))
        self.Dialog.setMaximumSize(QtCore.QSize(400, 600))
        self.Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 91, 18))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(4, 50, 391, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(235,237,244,0.8);")
        self.toolButton = QtWidgets.QPushButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 52, 24))
        self.toolButton.setMinimumSize(QtCore.QSize(52, 24))
        self.toolButton.setMaximumSize(QtCore.QSize(52, 24))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setFlat(True)

        self.retranslateUi(Dialog)
        #self.toolButton.clicked.connect(self.back)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "评论"))
        self.toolButton.setText(_translate("Dialog", "返回"))
    
    def com_news(self,m):
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
    Dialog = QtWidgets.QDialog()
    ui = Comment()
    ui.setupUi1(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

