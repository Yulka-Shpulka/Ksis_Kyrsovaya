import socket
import sqlite3
import threading
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMessageBox, QLineEdit

class IpInputDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter IP Address")
        self.layout = QtWidgets.QVBoxLayout()

        self.ip_label = QtWidgets.QLabel("IP Address:")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Enter IP Address")

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        self.layout.addWidget(self.ip_label)
        self.layout.addWidget(self.ip_input)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

    def get_ip(self):
        return self.ip_input.text()


def handle_client(client_socket, cursor, conn):
    with client_socket:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            command, *params = data.split(';')
            if command == "ADD":
                username, public_key, description = params
                cursor.execute("INSERT INTO keys (username, public_key, description) VALUES (?, ?, ?)",
                               (username, public_key, description))
                conn.commit()
                client_socket.sendall(b"Key added successfully.")
            elif command == "DELETE":
                username = params[0]
                cursor.execute("DELETE FROM keys WHERE username=?", (username,))
                conn.commit()
                client_socket.sendall(b"Key deleted successfully.")
            elif command == "SHOW":
                username = params[0]
                cursor.execute("SELECT public_key FROM keys WHERE username=?", (username,))
                rows = cursor.fetchall()
                if rows:
                    keys = ";".join(row[0] for row in rows)
                    client_socket.sendall(keys.encode())
                else:
                    client_socket.sendall(b"No keys found for the specified username.")


def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server listening on {ip}:{port}")

    conn = sqlite3.connect('keys.db', check_same_thread=False)
    cursor = conn.cursor()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, cursor, conn))
        client_handler.start()


def get_ip_address():
    app = QtWidgets.QApplication([])
    dialog = IpInputDialog()
    if dialog.exec():
        ip = dialog.get_ip()
        if ip.strip() == "":
            QMessageBox.warning(None, "Warning", "Пожалуйста, введите значение.")
        else:
            return ip
    return None


if __name__ == "__main__":
    conn = sqlite3.connect('keys.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS keys
                      (username TEXT, public_key TEXT, description TEXT)''')
    conn.commit()

    ip = get_ip_address()
    if ip:
        port = 12347
        start_server(ip, port)
    else:
        print("No IP address provided. Exiting...")
