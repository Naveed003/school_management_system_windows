# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs/NEW_USER_PAGE.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup_Page(object):
    def setupUi(self, Signup_Page):
        Signup_Page.setObjectName("Signup_Page")
        Signup_Page.resize(452, 462)
        Signup_Page.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"font-family: Times New Roman\n"
"")
        self.centralwidget = QtWidgets.QWidget(Signup_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(110, 380, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_signup.setObjectName("btn_signup")
        self.txtemail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtemail.setGeometry(QtCore.QRect(110, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtemail.setFont(font)
        self.txtemail.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtemail.setCursorPosition(0)
        self.txtemail.setObjectName("txtemail")
        self.txtusername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(QtCore.QRect(110, 190, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtusername.setFont(font)
        self.txtusername.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtusername.setObjectName("txtusername")
        self.txtpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpass.setGeometry(QtCore.QRect(112, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtpass.setFont(font)
        self.txtpass.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtpass.setObjectName("txtpass")
        self.txtconfirmpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtconfirmpass.setGeometry(QtCore.QRect(112, 310, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtconfirmpass.setFont(font)
        self.txtconfirmpass.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtconfirmpass.setObjectName("txtconfirmpass")
        Signup_Page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signup_Page)
        QtCore.QMetaObject.connectSlotsByName(Signup_Page)

    def retranslateUi(self, Signup_Page):
        _translate = QtCore.QCoreApplication.translate
        Signup_Page.setWindowTitle(_translate("Signup_Page", "MainWindow"))
        self.label.setText(_translate("Signup_Page", "<html><head/><body><p><span style=\" color:#ffffff;\">SIGN-UP</span></p></body></html>"))
        self.btn_signup.setText(_translate("Signup_Page", "SIGN-UP"))
        self.txtemail.setPlaceholderText(_translate("Signup_Page", "ENTER EMAIL ID"))
        self.txtusername.setPlaceholderText(_translate("Signup_Page", "ENTER USERNAME"))
        self.txtpass.setPlaceholderText(_translate("Signup_Page", "ENTER PASSWORD"))
        self.txtconfirmpass.setPlaceholderText(_translate("Signup_Page", "CONFIRM PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup_Page = QtWidgets.QMainWindow()
    ui = Ui_Signup_Page()
    ui.setupUi(Signup_Page)
    Signup_Page.show()
    sys.exit(app.exec_())
