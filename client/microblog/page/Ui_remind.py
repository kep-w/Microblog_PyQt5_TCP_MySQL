# -*- coding: utf-8 -*-

'''
用于提示的小窗口页面
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remind(object):
    def setupUi(self, remind):
        remind.setObjectName("remind")
        remind.setEnabled(True)
        remind.resize(323, 101)
        remind.setMouseTracking(False)
        remind.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(remind)
        self.centralWidget.setObjectName("centralWidget")
        self.info = QtWidgets.QLabel(self.centralWidget)
        self.info.setGeometry(QtCore.QRect(20, 30, 281, 41))
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")

        self.retranslateUi(remind)

    def retranslateUi(self, remind):
        _translate = QtCore.QCoreApplication.translate
        remind.setWindowTitle(_translate("remind", "提示"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remind = QtWidgets.QMainWindow()
    ui = Ui_remind()
    ui.setupUi(remind)
    remind.show()
    sys.exit(app.exec_())

