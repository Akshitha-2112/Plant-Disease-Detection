

from PyQt5 import QtCore, QtGui, QtWidgets

from Login import login_portal


class home(object):
    def admin(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = login_portal(self.Dialog)
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def user(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = login_portal(self.Dialog)
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 865)
        Dialog.setStyleSheet("QDialog{background-image: url(../PlantDiseaseDetection/image/backfroun.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 170, 521, 631))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(26, 138, 13, 94), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(697, 570, 211, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 63 14pt \"Lucida Fax\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 145, 0, 90), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(697, 400, 211, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 63 14pt \"Lucida Fax\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 145, 0, 90), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(486, 177, 508, 91))
        self.label_2.setStyleSheet("font: 29pt \"Britannic Bold\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 160, 14, 239), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(905, 181, 91, 91))
        self.label_3.setStyleSheet("background-image: url(../PlantDiseaseDetection/image/admin.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(580, 370, 101, 91))
        self.label_4.setStyleSheet("background-image: url(../PlantDiseaseDetection/image/admin_login.jpg);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(579, 547, 101, 99))
        self.label_5.setStyleSheet("background-image: url(../PlantDiseaseDetection/image/user.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1501, 111))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 239, 56, 138), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 85, 0);\n"
"font: 26pt \"Algerian\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.admin)
        self.pushButton_2.clicked.connect(self.user)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.pushButton_2.setText(_translate("Dialog", "USER"))
        self.pushButton.setText(_translate("Dialog", "ADMIN"))
        self.label_2.setText(_translate("Dialog", "Home"))
        self.label_6.setText(_translate("Dialog", "CLASSIFICATION OF PLANT LEAF DISEASES USING\n"
"DEEP LEARNING TECHNIQUES "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

