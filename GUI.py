# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ece656.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import os
import config
from PyQt5.QtWidgets import (QWidget, QToolTip,QLCDNumber,QSlider,QVBoxLayout,QHBoxLayout,QFrame,QSplitter,
                             QPushButton, QLineEdit,QApplication,QWidget, QLabel,QGridLayout,QVBoxLayout,QGroupBox)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 280, 160, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 320, 161, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 360, 161, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 101, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 70, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 160, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(250, 140, 121, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 80)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(260, 10, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(260, 70, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 90, 131, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(380, 140, 31, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(420, 140, 16, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(260, 120, 81, 16))
        self.label_11.setObjectName("label_11")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(260, 40, 121, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 190, 91, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 250, 151, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(360, 160, 81, 16))
        self.label_13.setObjectName("label_13")

        db = config.DB_info()
        ur = config.user_info()

        self.lineEdit.setText(db.user)
        self.lineEdit_2.setText(db.password)
        self.lineEdit_3.setText(db.host)
        self.lineEdit_4.setText(str(db.port))
        self.lineEdit_5.setText(db.db)
        self.lineEdit_6.setText(ur.business_id)
        self.lineEdit_6.resize(200,20)
        print(str(100-int(ur.test_size)*100))
        # self.horizontalSlider.value(str(100-int(ur.test_size)*100))

        self.retranslateUi(Form)
        self.horizontalSlider.sliderMoved['int'].connect(self.label_9.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.business_trend)
        self.pushButton_2.clicked.connect(self.predict)
        self.pushButton_3.clicked.connect(self.length)
        self.pushButton_4.clicked.connect(self.reload_module)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ECE656 Project"))
        self.pushButton.setText(_translate("Form", "Business Rating Trend"))
        self.pushButton_2.setText(_translate("Form", "Predict Rate"))
        self.pushButton_3.setText(_translate("Form", "Review Length"))
        self.label.setText(_translate("Form", "Connection Config:"))
        self.label_2.setText(_translate("Form", "user:"))
        self.label_3.setText(_translate("Form", "passwrod:"))
        self.label_4.setText(_translate("Form", "port:"))
        self.label_5.setText(_translate("Form", "DB IP address:"))
        self.label_6.setText(_translate("Form", "DataBase Name:"))
        self.label_7.setText(_translate("Form", "Data Mining Parameter:"))
        self.label_8.setText(_translate("Form", "Business ID:"))
        self.label_9.setText(_translate("Form", "80"))
        self.label_10.setText(_translate("Form", "%"))
        self.label_11.setText(_translate("Form", "Data Split:"))
        self.checkBox.setText(_translate("Form", "Data Cleaning"))
        self.pushButton_4.setText(_translate("Form", "Save"))
        self.label_12.setText(_translate("Form", "Data Mining Function:"))
        self.label_13.setText(_translate("Form", "Training Set"))

    def business_trend(self):
        os.system("python3 2_PlotRatingTrend.py")
    def predict(self):
        os.system("python3 3_DecisionTree.py")
    def length(self):
        os.system("python3 4_ReviewLenEffect.py")

    def reload_module(self):

        db = config.DB_info()
        self.alter("config.py", "user='%s'" % db.user, "user='%s'" % self.lineEdit.text())
        # print(self.lineEdit.text())
        self.alter("config.py", "password='%s'" % db.password, "password='%s'" % self.lineEdit_2.text())
        self.alter("config.py", "port=%s" % db.port, "port=%s" % self.lineEdit_4.text())
        self.alter("config.py", "host='%s'" % db.host, "host='%s'" % self.lineEdit_3.text())
        self.alter("config.py", "db='%s'" % db.db, "db='%s'" % self.lineEdit_5.text())

        ur = config.user_info()
        self.alter("config.py", "business_id = '%s'" % ur.business_id, "business_id = '%s'" % self.lineEdit_6.text())
        # self.alter("config.py", "user_id = '%s'" % ur.user_id, "user_id = '%s'" % self.uid_textbox.text())
        splitRatio=str((100-int(self.label_9.text()))/100)
        self.alter("config.py", "test_size = '%s'" % ur.test_size, "test_size = '%s'" % splitRatio)
        # print(str((100-int(self.label_9.text()))/100))


        # python = sys.executable
        # file_name = sys.argv[0]
        #
        # os.execl(python, python, file_name)

    def alter(self, file, old_str, new_str):
        file_data = ""
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if old_str in line:
                    line = line.replace(old_str, new_str)
                file_data += line
        with open(file, "w", encoding="utf-8") as f:
            f.write(file_data)


class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        # self.text_edit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
