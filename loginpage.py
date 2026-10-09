import os
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox
)
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt, pyqtSignal

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    import sys, os
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LoginPage(QWidget):
    loginSuccess = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

        if parent:
            self.loginSuccess.connect(parent.checkwho)

    def initUI(self):
        # Window Settings
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 1200, 700)

        # Set background gradient
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #f3f4f6, stop: 1 #d4d8e2
                );
            }
        """)

        # Main Layout
        main_layout = QHBoxLayout(self)

        # Left Panel (Image)
        left_panel = QLabel()
        pixmap = QPixmap(resource_path('Pictures/display.jpeg'))
        left_panel.setPixmap(pixmap.scaled(600, 700, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_panel.setAlignment(Qt.AlignCenter)

        # Right Panel
        right_panel = QVBoxLayout()
        right_panel.setContentsMargins(50, 50, 50, 50)
        right_panel.setSpacing(20)
        right_panel.setAlignment(Qt.AlignCenter)

        # Login Form Title
        login_title = QLabel("Sign In")
        login_title.setFont(QFont("Arial", 24, QFont.Bold))
        login_title.setStyleSheet("color: #2C3E50;")
        login_title.setAlignment(Qt.AlignCenter)
        right_panel.addWidget(login_title)

        # Login Form Layout
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)

        # Username Field
        username_label = QLabel("Username or Email:")
        username_label.setFont(QFont("Arial", 12))
        form_layout.addWidget(username_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username or email")
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setFixedWidth(350)
        self.username_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
        """)
        form_layout.addWidget(self.username_input)

        # Password Field
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 12))
        form_layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setFixedWidth(350)
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
        """)
        form_layout.addWidget(self.password_input)

        # Remember Me and Forgot Password
        options_layout = QHBoxLayout()
        remember_me = QCheckBox("Remember me")
        remember_me.setFont(QFont("Arial", 10))
        options_layout.addWidget(remember_me)

        forgot_password = QLabel("<a href='#'>Forgot password?</a>")
        forgot_password.setFont(QFont("Arial", 10))
        forgot_password.setStyleSheet("color: #3498db;")
        forgot_password.setOpenExternalLinks(True)
        options_layout.addWidget(forgot_password, alignment=Qt.AlignRight)
        form_layout.addLayout(options_layout)

        # Login Button
        login_button = QPushButton("Sign In")
        login_button.setFont(QFont("Arial", 14, QFont.Bold))
        login_button.setFixedWidth(200)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #217dbb;
            }
        """)
        login_button.clicked.connect(self.on_login_button_click)
        form_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # Create Account Link
        create_account_label = QLabel("<a href='#'>New here? Create an Account</a>")
        create_account_label.setFont(QFont("Arial", 10))
        create_account_label.setStyleSheet("color: #3498db;")
        create_account_label.setAlignment(Qt.AlignCenter)
        create_account_label.setOpenExternalLinks(True)
        form_layout.addWidget(create_account_label)

        # Add Form to Right Panel
        right_panel.addLayout(form_layout)

        # Add Panels to Main Layout
        main_layout.addWidget(left_panel, stretch=1)
        main_layout.addLayout(right_panel, stretch=1)
        self.setLayout(main_layout)

    def on_login_button_click(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.loginSuccess.emit(username, password)

    


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())
