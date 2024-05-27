import sys
import socket
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

port = 12347

class Ui_MainWindow(object):
    def openWindowAbout_me(self):
        self.window_1 = QtWidgets.QMainWindow()
        self.ui = AboutAuthorLogic()
        self.ui.setupUi(self.window_1)
        self.window_1.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 508)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddKey = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AddKey.setGeometry(QtCore.QRect(90, 240, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddKey.setFont(font)
        self.AddKey.setObjectName("AddKey")
        self.DeleteKey = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DeleteKey.setGeometry(QtCore.QRect(90, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DeleteKey.setFont(font)
        self.DeleteKey.setObjectName("DeleteKey")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 50, 181, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.UserName = QtWidgets.QLabel(parent=self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(80, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("color: rgb(255, 255, 255);")
        self.UserName.setObjectName("UserName")
        self.OpenKey = QtWidgets.QLabel(parent=self.centralwidget)
        self.OpenKey.setGeometry(QtCore.QRect(80, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OpenKey.setFont(font)
        self.OpenKey.setStyleSheet("color: rgb(255, 255, 255);")
        self.OpenKey.setObjectName("OpenKey")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 110, 181, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.ClosedKey = QtWidgets.QLabel(parent=self.centralwidget)
        self.ClosedKey.setGeometry(QtCore.QRect(80, 170, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClosedKey.setFont(font)
        self.ClosedKey.setStyleSheet("color: rgb(255, 255, 255);")
        self.ClosedKey.setObjectName("ClosedKey")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 170, 181, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.ShowKey = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ShowKey.setGeometry(QtCore.QRect(320, 240, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowKey.setFont(font)
        self.ShowKey.setObjectName("ShowKey")
        self.Edit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Edit.setGeometry(QtCore.QRect(320, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.Exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(200, 380, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -270, 651, 1021))
        self.label.setMaximumSize(QtCore.QSize(651, 16777215))
        self.label.setStyleSheet("background-image: ;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("KeyBackGround5.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.AddKey.raise_()
        self.DeleteKey.raise_()
        self.lineEdit.raise_()
        self.UserName.raise_()
        self.OpenKey.raise_()
        self.lineEdit_2.raise_()
        self.ClosedKey.raise_()
        self.lineEdit_3.raise_()
        self.ShowKey.raise_()
        self.Edit.raise_()
        self.Exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Exit.clicked.connect(MainWindow.close)
        self.AddKey.clicked.connect(self.add_key_clicked)
        self.DeleteKey.clicked.connect(self.delete_key_clicked)
        self.ShowKey.clicked.connect(self.show_keys_clicked)
    def validate_keys(self, public_key, description):
        if len(public_key) < 8 or len(description) < 8:
            QMessageBox.warning(None, "Warning", "Keys must have at least 8 characters.")
            return False
        return True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Управление открытыми ключами"))
        self.AddKey.setText(_translate("MainWindow", "Добавить ключ"))
        self.DeleteKey.setText(_translate("MainWindow", "Удалить ключ"))
        self.UserName.setText(_translate("MainWindow", "Имя пользователя"))
        self.OpenKey.setText(_translate("MainWindow", "Открытый ключ"))
        self.ClosedKey.setText(_translate("MainWindow", "Закрытый ключ"))
        self.ShowKey.setText(_translate("MainWindow", "Вывести ключ"))
        self.Edit.setText(_translate("MainWindow", "Редактировать"))
        self.Exit.setText(_translate("MainWindow", "Выход"))

    def send_request(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', port))
            s.sendall(message.encode())
            response = s.recv(1024).decode()
        return response

    def add_key_clicked(self):
        username = self.lineEdit.text()
        public_key = self.lineEdit_2.text()
        description = self.lineEdit_3.text()

        if not username:
            QMessageBox.warning(None, "Warning", "Please enter a username.")
            return

        if not public_key and not description:
            QMessageBox.warning(None, "Warning", "Please enter at least one key.")
            return

        if not self.validate_keys(public_key, description):
            return

        message = f"ADD;{username};{public_key};{description}"
        response = self.send_request(message)
        QMessageBox.information(None, "Information", response)

    def delete_key_clicked(self):
        username = self.lineEdit.text()

        if not username:
            QMessageBox.warning(None, "Warning", "Please enter a username.")
            return

        message = f"DELETE;{username}"
        response = self.send_request(message)
        QMessageBox.information(None, "Information", response)

    def show_keys_clicked(self):
        username = self.lineEdit.text()
        message = f"SHOW;{username}"
        response = self.send_request(message)

        keys = response.split(';') if response else []

        if keys:
            key_text = "\n".join(keys)
            QMessageBox.information(None, "Keys", key_text)
        else:
            QMessageBox.information(None, "Information", "No keys found for the user.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
