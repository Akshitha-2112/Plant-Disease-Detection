
from PyQt5 import QtCore, QtGui, QtWidgets

from AdminHome import adminhome
from PlantDiseaseDetection import Prediction
import sys


class login_portal(object):
    def __init__(self,Dialog):
        self.dialog=Dialog

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def alertmsg2(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def log_in(self):
        try:
            uid= self.lineEdit.text()
            passw = self.lineEdit_2.text()

            if uid=="" or uid == 'null' or  passw=="" or passw == 'null':
                self.alertmsg2("Failed", "Please Fill the required fields..!")

            else:
                if uid == "admin" and passw == "admin":
                    self.Dialog = QtWidgets.QDialog()
                    self.ui = adminhome()
                    self.ui.setupUi(self.Dialog)
                    self.Dialog.show()
                    self.dialog.hide()
                elif uid == "user" and passw == "user":
                    self.Dialog = QtWidgets.QDialog()
                    self.ui = Prediction()
                    self.ui.setupUi(self.Dialog)
                    self.Dialog.show()
                    self.dialog.hide()
                else:
                    self.alertmsg("Failed", "Please Enter correct UserId and Password")



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 863)
        Dialog.setStyleSheet("QDialog{background-image: url(../PlantDiseaseDetection/image/backfroun.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(880, 260, 381, 482))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 194, 75, 168), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 260, 670, 482))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(180, 180, 180, 135), stop:1 rgba(255, 255, 255, 255));\n"
"background-image: url(../PlantDiseaseDetection/image/login.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1000, 270, 131, 121))
        self.label_3.setStyleSheet("background-image: url(../PlantDiseaseDetection/image/userlogwin.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(960, 470, 231, 41))
        self.lineEdit.setStyleSheet("font: 12pt \"Georgia\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(970, 380, 191, 71))
        self.label_4.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(960, 550, 231, 41))
        self.lineEdit_2.setStyleSheet("font: 12pt \"Georgia\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(991, 627, 163, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-image: url(../PlantDiseaseDetection/image/login_button.png);")
        self.pushButton.setText("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.log_in)
        self.pushButton.clicked.connect(self.clear)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LoginPortal"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "UserID"))
        self.label_4.setText(_translate("Dialog", "Log In"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = login_()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
