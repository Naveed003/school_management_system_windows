
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fees_Details(object):
    def setupUi(self, Fees_Details):
        Fees_Details.setObjectName("Fees_Details")
        Fees_Details.resize(667, 447)
        Fees_Details.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                   "font-family: Times New Roman\n"
                                   "\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(Fees_Details)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR: WHITE;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 110, 291, 101))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border: 2px solid white;\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtcheckroll = QtWidgets.QLineEdit(self.frame)
        self.txtcheckroll.setGeometry(QtCore.QRect(20, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtcheckroll.setFont(font)
        self.txtcheckroll.setStyleSheet("QLineEdit {\n"
                                        "    border: 2px solid gray;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 0 8px;\n"
                                        "    background: white;\n"
                                        "    selection-background-color: darkgray;\n"
                                        "}")
        self.txtcheckroll.setObjectName("txtcheckroll")
        self.btn_enter = QtWidgets.QToolButton(self.frame)
        self.btn_enter.setGeometry(QtCore.QRect(90, 60, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_enter.setFont(font)
        self.btn_enter.setStyleSheet("QToolButton { \n"
                                     "    background-color: #33ff39;\n"
                                     "    border: 2px;\n"
                                     "    border-radius: 8px;\n"
                                     "    FONT: 12PX;\n"
                                     "    COLOR: BLACK;\n"
                                     "\n"
                                     "                    \n"
                                     " }\n"
                                     "\n"
                                     "QToolButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_enter.setObjectName("btn_enter")
        self.txtcheckname = QtWidgets.QLineEdit(self.frame)
        self.txtcheckname.setGeometry(QtCore.QRect(160, 20, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtcheckname.setFont(font)
        self.txtcheckname.setStyleSheet("QLineEdit {\n"
                                        "    border: 2px solid gray;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 0 8px;\n"
                                        "    background: white;\n"
                                        "    selection-background-color: darkgray;\n"
                                        "}")
        self.txtcheckname.setObjectName("txtcheckname")
        self.tblfees = QtWidgets.QTableWidget(self.centralwidget)
        self.tblfees.setGeometry(QtCore.QRect(30, 250, 611, 161))
        self.tblfees.setStyleSheet("\n"
                                   "\n"
                                   "\n"
                                   "QWidget {\n"
                                   "    background-color: black;\n"
                                   "    color: #fffff8;\n"
                                   "    font-family:Times New Roman;\n"
                                   "}\n"
                                   "\n"
                                   "QHeaderView::section {\n"
                                   "    background-color: black;\n"
                                   "    padding: 4px;\n"
                                   "    font-size:10pt;\n"
                                   "     border: 1px solid white;\n"
                                   "   \n"
                                   "    \n"
                                   "}\n"
                                   "\n"
                                   "QTableWidget {\n"
                                   "    gridline-color: white;\n"
                                   "      font-size:12pt;\n"
                                   "}\n"
                                   "\n"
                                   "QTableWidget QTableCornerButton::section {\n"
                                   "    background-color: black;\n"
                                   "    border: 1px solid white\n"
                                   ";\n"
                                   "}\n"
                                   "\n"
                                   "QTableWidget {\n"
                                   "    gridline-color: white;\n"
                                   "      font-size:12pt;\n"
                                   "}\n"
                                   "\n"
                                   "QTableWidget QTableCornerButton::section {\n"
                                   "    background-color: black;\n"
                                   "    border: 1px solid white\n"
                                   ";\n"
                                   "}")
        self.tblfees.setObjectName("tblfees")
        self.tblfees.setColumnCount(6)
        self.tblfees.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tblfees.setHorizontalHeaderItem(5, item)
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(390, 110, 161, 32))
        self.btn_return.setStyleSheet("QToolButton { \n"
                                      "    background-color: #33ff39;\n"
                                      "    border: 2px;\n"
                                      "    border-radius: 8px;\n"
                                      "    FONT: 12PX;\n"
                                      "    COLOR: BLACK;\n"
                                      "\n"
                                      "                    \n"
                                      " }\n"
                                      "\n"
                                      "QToolButton:pressed {\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_return.setObjectName("btn_return")
        self.btn_returnmain = QtWidgets.QToolButton(self.centralwidget)
        self.btn_returnmain.setGeometry(QtCore.QRect(390, 160, 161, 32))
        self.btn_returnmain.setStyleSheet("QToolButton { \n"
                                          "    background-color: #33ff39;\n"
                                          "    border: 2px;\n"
                                          "    border-radius: 8px;\n"
                                          "    FONT: 12PX;\n"
                                          "    COLOR: BLACK;\n"
                                          "\n"
                                          "                    \n"
                                          " }\n"
                                          "\n"
                                          "QToolButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_returnmain.setObjectName("btn_returnmain")
        Fees_Details.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fees_Details)
        QtCore.QMetaObject.connectSlotsByName(Fees_Details)

    def retranslateUi(self, Fees_Details):
        _translate = QtCore.QCoreApplication.translate
        Fees_Details.setWindowTitle(_translate("Fees_Details", "MainWindow"))
        self.label.setText(_translate("Fees_Details", "FEE DETAILS"))
        self.txtcheckroll.setPlaceholderText(
            _translate("Fees_Details", "ROLL NO"))
        self.btn_enter.setText(_translate("Fees_Details", "ENTER"))
        self.txtcheckname.setPlaceholderText(
            _translate("Fees_Details", "NAME"))
        item = self.tblfees.horizontalHeaderItem(0)
        item.setText(_translate("Fees_Details", "ROLL NO"))
        item = self.tblfees.horizontalHeaderItem(1)
        item.setText(_translate("Fees_Details", "NAME"))
        item = self.tblfees.horizontalHeaderItem(2)
        item.setText(_translate("Fees_Details", "GRADE"))
        item = self.tblfees.horizontalHeaderItem(3)
        item.setText(_translate("Fees_Details", "TOTAL FEES"))
        item = self.tblfees.horizontalHeaderItem(4)
        item.setText(_translate("Fees_Details", "AMOUNT PAID"))
        item = self.tblfees.horizontalHeaderItem(5)
        item.setText(_translate("Fees_Details", "AMOUNT PENDING"))
        self.btn_return.setText(_translate("Fees_Details", "RETURN"))
        self.btn_returnmain.setText(_translate(
            "Fees_Details", "RETURN TO MAIN MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fees_Details = QtWidgets.QMainWindow()
    ui = Ui_Fees_Details()
    ui.setupUi(Fees_Details)
    Fees_Details.show()
    sys.exit(app.exec_())
