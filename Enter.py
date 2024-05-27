import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Client import Ui_MainWindow


class Ui_Dialog_3(object):
    def openMainWindow(self):
        self.windowMain = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.windowMain)
        self.windowMain.show()

    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(746, 484)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 761, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\python_proj\\KSIS_Kursovaya\\EnterBackground1.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 120, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 230, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 380, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 380, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)

    def validate_username(self, username):
        return len(username.split()) == 2

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        if not username or not password:
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, не заполнены все поля!")
            msg.exec()
        elif not self.validate_username(username):
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, логин должен содержать ровно 2 слова!")
            msg.exec()
        elif len(password) < 8:
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, пароль должен содержать не менее 8 символов!")
            msg.exec()
        else:
            conn = sqlite3.connect("my_database_enter.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()

            if result:
                self.openMainWindow()
                Dialog.close()
            else:
                msg.setWindowTitle("Ошибка")
                msg.setText("Ошибка, неверно введён логин или пароль!")
                msg.exec()

    def register(self):
        conn = sqlite3.connect("my_database_enter.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        if not username or not password:
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, не заполнены все поля!")
            msg.exec()
        elif not self.validate_username(username):
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, логин должен содержать ровно 2 слова!")
            msg.exec()
        elif len(password) < 8:
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, пароль должен содержать не менее 8 символов!")
            msg.exec()
        else:
            cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            conn.commit()
            msg.setWindowTitle("Успех")
            msg.setText("Вы успешно были зарегистрированы!")
            msg.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.label_2.setText(_translate("Dialog", "Вход  в систему"))
        self.label_3.setText(_translate("Dialog", "Введите логин:"))
        self.label_4.setText(_translate("Dialog", "Введите пароль:"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "Зарегистрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog_3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
