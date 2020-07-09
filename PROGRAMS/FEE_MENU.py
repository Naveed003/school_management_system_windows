
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fee_Menu(object):
    def setupUi(self, Fee_Menu):
        Fee_Menu.setObjectName("Fee_Menu")
        Fee_Menu.resize(506, 275)
        Fee_Menu.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                               "font-family: Times New Roman\n"
                               "")
        self.centralwidget = QtWidgets.QWidget(Fee_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
                                 "")
        self.label.setObjectName("label")
        self.btn_fee_deposit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fee_deposit.setGeometry(QtCore.QRect(18, 129, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_fee_deposit.setFont(font)
        self.btn_fee_deposit.setStyleSheet("QPushButton { \n"
                                           "    background-color: #33ff39;\n"
                                           "    border: 2px;\n"
                                           "    border-radius: 10px;\n"
                                           "                    \n"
                                           " }\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                           "")
        self.btn_fee_deposit.setObjectName("btn_fee_deposit")
        self.btn_fees_details = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fees_details.setGeometry(QtCore.QRect(258, 129, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_fees_details.setFont(font)
        self.btn_fees_details.setStyleSheet("QPushButton { \n"
                                            "    background-color: #33ff39;\n"
                                            "    border: 2px;\n"
                                            "    border-radius: 10px;\n"
                                            "                    \n"
                                            " }\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                            "")
        self.btn_fees_details.setObjectName("btn_fees_details")
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(18, 199, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("QPushButton { \n"
                                      "    background-color: #33ff39;\n"
                                      "    border: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "                    \n"
                                      " }\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                      "")
        self.btn_return.setObjectName("btn_return")
        Fee_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fee_Menu)
        QtCore.QMetaObject.connectSlotsByName(Fee_Menu)

    def retranslateUi(self, Fee_Menu):
        _translate = QtCore.QCoreApplication.translate
        Fee_Menu.setWindowTitle(_translate("Fee_Menu", "MainWindow"))
        self.label.setText(_translate(
            "Fee_Menu", "<html><head/><body><p>FEE MENU</p></body></html>"))
        self.btn_fee_deposit.setText(_translate("Fee_Menu", "FEE DEPOSIT"))
        self.btn_fees_details.setText(_translate("Fee_Menu", "FEE DETAILS"))
        self.btn_return.setText(_translate("Fee_Menu", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fee_Menu = QtWidgets.QMainWindow()
    ui = Ui_Fee_Menu()
    ui.setupUi(Fee_Menu)
    Fee_Menu.show()
    sys.exit(app.exec_())
