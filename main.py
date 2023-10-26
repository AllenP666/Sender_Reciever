import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import socket


class SenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sender Window")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Send Signal", self)
        self.button.setGeometry(150, 130, 100, 30)
        self.button.clicked.connect(self.send_signal)

        self.con_btn = QPushButton("Connect", self)
        self.con_btn.setGeometry(305, 50, 60, 30)
        self.con_btn.clicked.connect(self.connect_to_server)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(100, 50, 200, 30)
        self.textbox.setText("localhost")

    def send_signal(self):
        self.socket.sendall(b"signal")

    def connect_to_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.textbox.text(), 12345))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sender_window = SenderWindow()
    sender_window.show()
    sys.exit(app.exec())