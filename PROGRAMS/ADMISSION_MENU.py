

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admission_Menu(object):
    def setupUi(self, Admission_Menu):
        Admission_Menu.setObjectName("Admission_Menu")
        Admission_Menu.resize(999, 578)
        Admission_Menu.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"font-family: Times New Roman;\n"
"")

                                     "font-family: Times New Roman;\n"

        self.centralwidget = QtWidgets.QWidget(Admission_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.table_adm = QtWidgets.QTableWidget(self.centralwidget)
        self.table_adm.setGeometry(QtCore.QRect(380, 160, 601, 331))
        self.table_adm.setStyleSheet("QWidget {\n"
                                     "    background-color: black;\n"
                                     "    color: #fffff8;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section {\n"
                                     "    background-color: black;\n"
                                     "    padding: 4px;\n"
                                     "    font-size:12pt;\n"
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
                                     "}")
        self.table_adm.setObjectName("table_adm")
        self.table_adm.setColumnCount(6)
        self.table_adm.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(5, item)
        self.btnModify = QtWidgets.QToolButton(self.centralwidget)
        self.btnModify.setGeometry(QtCore.QRect(271, 500, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnModify.setFont(font)
        self.btnModify.setStyleSheet("QToolButton { \n"
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
        self.btnModify.setObjectName("btnModify")
        self.btDelete = QtWidgets.QToolButton(self.centralwidget)
        self.btDelete.setGeometry(QtCore.QRect(190, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btDelete.setFont(font)
        self.btDelete.setStyleSheet("QToolButton { \n"
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
        self.btDelete.setObjectName("btDelete")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("COLOR: WHITE;\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(28, 160, 341, 331))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border: 2px solid white;\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "    border: 2px white;\n"
                                 "\n"
                                 "}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
<< << << < HEAD
"    border: 2px white;\n"
"\n"
"}")


== == == =
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.label_4.setObjectName("label_4")
        self.label_5=QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 101, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
<< << << < HEAD
"    border: 2px white;\n"
"\n"
"}")
== == == =
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")

        self.label_5.setObjectName("label_5")
        self.frame_2=QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(140, 140, 181, 41))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.maleradio=QtWidgets.QRadioButton(self.frame_2)
        self.maleradio.setGeometry(QtCore.QRect(10, 10, 100, 20))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        self.maleradio.setFont(font)
        self.maleradio.setStyleSheet("color: white;\n"
<< << << < HEAD
"BACKGROUND: ")
== == == =
                                     "BACKGROUND: ")

        self.maleradio.setObjectName("maleradio")
        self.femaleradio=QtWidgets.QRadioButton(self.frame_2)
        self.femaleradio.setGeometry(QtCore.QRect(90, 10, 81, 20))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        self.femaleradio.setFont(font)
        self.femaleradio.setStyleSheet("color: white;")
        self.femaleradio.setObjectName("femaleradio")
        self.label_6=QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 71, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
<< << << < HEAD
"    border: 2px white;\n"
"\n"
"}")
== == == =
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.label_6.setObjectName("label_6")
        self.age_val=QtWidgets.QSpinBox(self.frame)
        self.age_val.setGeometry(QtCore.QRect(140, 240, 191, 22))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        self.age_val.setFont(font)
        self.age_val.setMinimum(3)
        self.age_val.setMaximum(20)
        self.age_val.setObjectName("age_val")
        self.label_8=QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 111, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
<< << << < HEAD
"    border: 2px white;\n"
"\n"
"}")
== == == =
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.label_8.setObjectName("label_8")
        self.txtrollno=QtWidgets.QLineEdit(self.frame)
        self.txtrollno.setGeometry(QtCore.QRect(140, 20, 181, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtrollno.setFont(font)
        self.txtrollno.setStyleSheet("QLineEdit {\n"
<< << << < HEAD
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
== == == =
                                     "    border: 2px solid gray;\n"
                                     "    border-radius: 10px;\n"
                                     "    padding: 0 8px;\n"
                                     "    background: white;\n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.txtrollno.setObjectName("txtrollno")
        self.txtname=QtWidgets.QLineEdit(self.frame)
        self.txtname.setGeometry(QtCore.QRect(140, 60, 181, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtname.setFont(font)
        self.txtname.setStyleSheet("QLineEdit {\n"
<< << << < HEAD
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
== == == =
                                   "    border: 2px solid gray;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 0 8px;\n"
                                   "    background: white;\n"
                                   "    selection-background-color: darkgray;\n"
                                   "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.txtname.setObjectName("txtname")
        self.txtphone=QtWidgets.QLineEdit(self.frame)
        self.txtphone.setGeometry(QtCore.QRect(140, 100, 181, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtphone.setFont(font)
        self.txtphone.setStyleSheet("QLineEdit {\n"
<< << << < HEAD
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
== == == =
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: white;\n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.txtphone.setObjectName("txtphone")
        self.txtemail=QtWidgets.QLineEdit(self.frame)
        self.txtemail.setGeometry(QtCore.QRect(140, 280, 181, 31))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtemail.setFont(font)
        self.txtemail.setStyleSheet("QLineEdit {\n"
<< << << < HEAD
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
== == == =
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: white;\n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.txtemail.setObjectName("txtemail")
        self.division=QtWidgets.QComboBox(self.frame)
        self.division.setGeometry(QtCore.QRect(240, 190, 81, 41))
        self.division.setStyleSheet("border: 1px solid white;\n"
<< << << < HEAD
"color: white\n"
"")
== == == =
                                    "color: white\n"
                                    "")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.division.setObjectName("division")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.grade=QtWidgets.QComboBox(self.frame)
        self.grade.setGeometry(QtCore.QRect(140, 189, 91, 41))
        self.grade.setStyleSheet("border: 1px solid white;\n"
<< << << < HEAD
"color: white\n"
"")
== == == =
                                 "color: white\n"
                                 "")
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.grade.setObjectName("grade")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.btn_return=QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(910, 500, 61, 22))
        self.btn_return.setStyleSheet("QToolButton { \n"
<< << << < HEAD
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
== == == =
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
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.btn_return.setObjectName("btn_return")
        self.btnAdd=QtWidgets.QToolButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(110, 500, 71, 20))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("QToolButton { \n"
<< << << < HEAD
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
== == == =
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
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.btnAdd.setObjectName("btnAdd")
        self.btnShowAll=QtWidgets.QToolButton(self.centralwidget)
        self.btnShowAll.setGeometry(QtCore.QRect(820, 500, 71, 22))
        self.btnShowAll.setStyleSheet("QToolButton { \n"
<< << << < HEAD
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
== == == =
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
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.btnShowAll.setObjectName("btnShowAll")
        self.btnShow=QtWidgets.QToolButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(30, 500, 71, 21))
        font=QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnShow.setFont(font)
        self.btnShow.setStyleSheet("QToolButton { \n"
<< << << < HEAD
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
== == == =
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
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.btnShow.setObjectName("btnShow")
        self.table_adm.raise_()
        self.btnModify.raise_()
        self.btDelete.raise_()
        self.label_7.raise_()
        self.frame.raise_()
        self.btn_return.raise_()
        self.btnAdd.raise_()
        self.btnShowAll.raise_()
        self.btnShow.raise_()
        self.label_9.raise_()
        Admission_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Admission_Menu)
        QtCore.QMetaObject.connectSlotsByName(Admission_Menu)

    def retranslateUi(self, Admission_Menu):
        _translate=QtCore.QCoreApplication.translate
<< << << < HEAD
        Admission_Menu.setWindowTitle(
            _translate("Admission_Menu", "MainWindow"))
== == == =
        Admission_Menu.setWindowTitle(
            _translate("Admission_Menu", "MainWindow"))
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        item=self.table_adm.horizontalHeaderItem(0)
        item.setText(_translate("Admission_Menu", "ROLL NO"))
        item=self.table_adm.horizontalHeaderItem(1)
        item.setText(_translate("Admission_Menu", "NAME"))
        item=self.table_adm.horizontalHeaderItem(2)
        item.setText(_translate("Admission_Menu", "AGE"))
        item=self.table_adm.horizontalHeaderItem(3)
        item.setText(_translate("Admission_Menu", "SEX"))
        item=self.table_adm.horizontalHeaderItem(4)
        item.setText(_translate("Admission_Menu", "CLASS"))
        item=self.table_adm.horizontalHeaderItem(5)
        item.setText(_translate("Admission_Menu", "EMAIL ID"))
        self.btnModify.setText(_translate("Admission_Menu", "MODIFY"))
        self.btDelete.setText(_translate("Admission_Menu", "DELETE"))
        self.label_9.setText(_translate("Admission_Menu", " STUDENT DETAILS "))
<< << << < HEAD
        self.label_7.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">ADMISSION MENU</span></p></body></html>"))
        self.label.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">ROLL NO:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">SEX: </span></p></body></html>"))
        self.label_3.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">PHONE NO:</span></p></body></html>"))
        self.label_4.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">NAME: </span></p></body></html>"))
        self.label_5.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">CLASS :</span></p></body></html>"))
        self.maleradio.setText(_translate("Admission_Menu", "MALE"))
        self.femaleradio.setText(_translate("Admission_Menu", "FEMALE"))
        self.label_6.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">AGE :</span></p></body></html>"))
        self.label_8.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">EMAIL ID: </span></p></body></html>"))
        self.txtrollno.setPlaceholderText(
            _translate("Admission_Menu", "ROLL NO"))
        self.txtname.setPlaceholderText(_translate("Admission_Menu", "NAME"))
        self.txtphone.setText(_translate("Admission_Menu", "+971"))
        self.txtphone.setPlaceholderText(
            _translate("Admission_Menu", "PHONE NO"))
        self.txtemail.setPlaceholderText(
            _translate("Admission_Menu", "EMAIL ID"))
== == == =
        self.label_7.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">ADMISSION MENU</span></p></body></html>"))
        self.label.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">ROLL NO:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">SEX: </span></p></body></html>"))
        self.label_3.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">PHONE NO:</span></p></body></html>"))
        self.label_4.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">NAME: </span></p></body></html>"))
        self.label_5.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">CLASS :</span></p></body></html>"))
        self.maleradio.setText(_translate("Admission_Menu", "MALE"))
        self.femaleradio.setText(_translate("Admission_Menu", "FEMALE"))
        self.label_6.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">AGE :</span></p></body></html>"))
        self.label_8.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">EMAIL ID: </span></p></body></html>"))
        self.txtrollno.setPlaceholderText(
            _translate("Admission_Menu", "ROLL NO"))
        self.txtname.setPlaceholderText(_translate("Admission_Menu", "NAME"))
        self.txtphone.setText(_translate("Admission_Menu", "+971"))
        self.txtphone.setPlaceholderText(
            _translate("Admission_Menu", "PHONE NO"))
        self.txtemail.setPlaceholderText(
            _translate("Admission_Menu", "EMAIL ID"))
>> >>>> > 55e2ba4d0146ed1c3cdbf32b41103096fb482bea
        self.division.setItemText(0, _translate("Admission_Menu", "A"))
        self.division.setItemText(1, _translate("Admission_Menu", "B"))
        self.division.setItemText(2, _translate("Admission_Menu", "C"))
        self.division.setItemText(3, _translate("Admission_Menu", "D"))
        self.division.setItemText(4, _translate("Admission_Menu", "E"))
        self.division.setItemText(5, _translate("Admission_Menu", "F"))
        self.division.setItemText(6, _translate("Admission_Menu", "G"))
        self.division.setItemText(7, _translate("Admission_Menu", "H"))
        self.grade.setItemText(0, _translate("Admission_Menu", "KG-1"))
        self.grade.setItemText(1, _translate("Admission_Menu", "KG-2"))
        self.grade.setItemText(2, _translate("Admission_Menu", "1"))
        self.grade.setItemText(3, _translate("Admission_Menu", "2"))
        self.grade.setItemText(4, _translate("Admission_Menu", "3"))
        self.grade.setItemText(5, _translate("Admission_Menu", "4"))
        self.grade.setItemText(6, _translate("Admission_Menu", "5"))
        self.grade.setItemText(7, _translate("Admission_Menu", "6"))
        self.grade.setItemText(8, _translate("Admission_Menu", "7"))
        self.grade.setItemText(9, _translate("Admission_Menu", "8"))
        self.grade.setItemText(10, _translate("Admission_Menu", "9"))
        self.grade.setItemText(11, _translate("Admission_Menu", "10"))
        self.grade.setItemText(12, _translate("Admission_Menu", "11"))
        self.grade.setItemText(13, _translate("Admission_Menu", "12"))
        self.btn_return.setText(_translate("Admission_Menu", "RETURN"))
        self.btnAdd.setText(_translate("Admission_Menu", "ADD"))
        self.btnShowAll.setText(_translate("Admission_Menu", "SHOW ALL"))
        self.btnShow.setText(_translate("Admission_Menu", "SHOW"))


if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Admission_Menu=QtWidgets.QMainWindow()
    ui=Ui_Admission_Menu()
    ui.setupUi(Admission_Menu)
    Admission_Menu.show()
    sys.exit(app.exec_())
