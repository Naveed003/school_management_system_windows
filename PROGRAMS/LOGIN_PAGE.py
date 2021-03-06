
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_Login_page(object):
    def ShowMessageBox(self, title, message):
        self.mydb.close()
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()

    def ShowMessageBox_(self, title, message):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()

    def cleartxt(self):
        self.txtusername.clear()
        self.txtpass.clear()

    def login(self):
        self.mydb = mysql.connector.connect(
            host='localhost', user='root', passwd='logon@123', database="school_management_system")
        self.mycursor = self.mydb.cursor()
        temp_username = self.txtusername.text()
        temp_password = self.txtpass.text()
        checklist = [temp_username.lower(), temp_password]
        if temp_username == "" or temp_password == "":
            self.ShowMessageBox_(
                "FAILED", "ENTER USERNAME/EMAIL ID AND PASSWORD")
            return
        else:
            if "@" in temp_username:
                email_query = "select email_id,password from users where email_id='{}'".format(
                    temp_username)
                self.mycursor.execute(email_query)
                email_id = self.mycursor.fetchall()
                if email_id == []:
                    self.ShowMessageBox_(
                        "LOGIN FAILEd", "The email id you entered doesn't belong to an account. Please check your email id and try again.".upper())
                    self.cleartxt()
                    return
                else:
                    list = []
                    for i in email_id:
                        for j in i:
                            list.append(j)
                    if checklist == list:
                        self.ShowMessageBox("SUCCESSFULL", "LOGIN SUCCESSFULL")

                    else:
                        self.ShowMessageBox_(
                            "LOGIN FAILED", "INCORRECT EMAIL ID OR PASSWORD")
                        self.cleartxt()
                        return

            else:
                query = "select username,password from users where username='{}'".format(
                    temp_username)
                self.mycursor.execute(query)
                username = self.mycursor.fetchall()
                if username == []:
                    self.ShowMessageBox_(
                        "LOGIN FAILED", "The USERNAME you entered doesn't belong to an account. Please check your username and try again.".upper())
                    self.cleartxt()
                    return
                else:
                    list = []
                    for i in username:
                        for j in i:
                            list.append(j)
                    if checklist == list:
                        self.ShowMessageBox("SUCCESSFULL", "LOGIN SUCCESSFULL")
                    else:
                        self.ShowMessageBox_(
                            "LOGIN FAILED", "INCORRECT USERNAME OR PASSWORD")
                        self.cleartxt()
                        return

    def setupUi(self, Login_page):
        Login_page.setObjectName("Login_page")
        Login_page.resize(447, 413)
        Login_page.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                 "font-family: Times New Roman\n"
                                 "\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(Login_page)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtusername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(QtCore.QRect(110, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtusername.setFont(font)
        self.txtusername.setStyleSheet("QLineEdit {\n"
                                       "    border: 2px solid gray;\n"
                                       "    border-radius: 10px;\n"
                                       "    padding: 0 8px;\n"
                                       "    background: white;\n"
                                       "    selection-background-color: darkgray;\n"
                                       "}")
        self.txtusername.setText("")
        self.txtusername.setObjectName("txtusername")
        self.txtpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpass.setGeometry(QtCore.QRect(110, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtpass.setFont(font)
        self.txtpass.setStyleSheet("QLineEdit {\n"
                                   "    border: 2px solid gray;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 0 8px;\n"
                                   "    background: white;\n"
                                   "    selection-background-color: darkgray;\n"
                                   "}\n"
                                   "\n"
                                   "QLineEdit[echoMode=\"1\"] {\n"
                                   "    lineedit-password-character: 9679;\n"
                                   "}")
        self.txtpass.setText("")
        self.txtpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtpass.setObjectName("txtpass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(110, 270, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton { \n"
                                     "    background-color: #33ff39;\n"
                                     "    border: 2px;\n"
                                     "    border-radius: 10px;\n"
                                     "                    \n"
                                     " }\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                     "")
        self.btn_login.setObjectName("btn_login")
        self.btn_login.clicked.connect(self.login)
        self.btn_new_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_user.setGeometry(QtCore.QRect(110, 340, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_new_user.setFont(font)
        self.btn_new_user.setStyleSheet("QPushButton { \n"
                                        "    background-color: #33ff39;\n"
                                        "    border: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "                    \n"
                                        " }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_new_user.setObjectName("btn_new_user")
        Login_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_page)
        QtCore.QMetaObject.connectSlotsByName(Login_page)

    def retranslateUi(self, Login_page):
        _translate = QtCore.QCoreApplication.translate
        Login_page.setWindowTitle(_translate("Login_page", "MainWindow"))
        self.label.setText(_translate(
            "Login_page", "<html><head/><body><p><span style=\" color:#ffffff;\">LOGIN</span></p></body></html>"))
        self.txtusername.setPlaceholderText(
            _translate("Login_page", "ENTER USERNAME/EMAIL ID"))
        self.txtpass.setPlaceholderText(
            _translate("Login_page", "ENTER PASSWORD"))
        self.btn_login.setText(_translate("Login_page", "LOGIN"))
        self.btn_new_user.setText(_translate("Login_page", "NEW-USER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_page = QtWidgets.QMainWindow()
    ui = Ui_Login_page()
    ui.setupUi(Login_page)
    Login_page.show()
    sys.exit(app.exec_())
