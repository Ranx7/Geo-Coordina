from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import *
import sys
import os

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSNM - Login")
        self.resize(900, 560)

        central = QWidget()
        self.setCentralWidget(central)

        
        self.bg_label = QLabel(central) #gay ass aero watcher
        self.bg_label.setObjectName("bg_label")
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        image_path = os.path.join(os.path.dirname(__file__), "bg.jpg")
        self.original_pixmap = QPixmap(image_path)
        if self.original_pixmap.isNull():
            print("background image not found:", image_path)
        else:
            print("background image loaded.")

 
        blur = QGraphicsBlurEffect(self.bg_label)
        blur.setBlurRadius(18)   
        self.bg_label.setGraphicsEffect(blur)

    
        self.overlay = QWidget(central)
        self.overlay.setStyleSheet("background-color: rgba(0,0,0,120);")
        self.overlay.setGeometry(0, 0, self.width(), self.height())

      
        self.container = QWidget(central)

        self.container.setGeometry(0, 0, self.width(), self.height())
        container_layout = QVBoxLayout(self.container)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        card = QWidget()
        card.setFixedWidth(380)
        card.setStyleSheet("""
            background-color: rgba(255,255,255,230);
            border-radius: 12px;
        """)

        shadow = QGraphicsDropShadowEffect(card)
        shadow.setBlurRadius(18)
        shadow.setOffset(0, 6)
        shadow.setColor(Qt.GlobalColor.black)
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)
        card_layout.setContentsMargins(24, 20, 24, 20)

        title = QLabel("Welcome to CSNM!")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        subtitle = QLabel("Please log your admin credentials")
        subtitle.setStyleSheet("color: gray; font-size: 12px;")

        department = QLineEdit()
        department.setPlaceholderText("Department code (eg. 0011A)")
        department.setStyleSheet("padding:8px; border-radius:6px;")

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setStyleSheet("padding:8px; border-radius:6px;")

        submit = QPushButton("Submit")
        submit.setStyleSheet("""
            QPushButton {
                padding:8px;
                border-radius:6px;
                background-color: black;
                color: white;
            }
                             
            QPushButton:hover {
                background-color: gray;
            }
        """)
        submit.setCursor(Qt.CursorShape.PointingHandCursor)
    

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(4)
        card_layout.addWidget(department)
        card_layout.addWidget(password)
        card_layout.addWidget(submit)

        container_layout.addWidget(card)
        self.container.setLayout(container_layout)
 
        self._widgets = (self.bg_label, self.overlay, self.container, card)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()

        self.bg_label.setGeometry(0, 0, w, h)
        self.overlay.setGeometry(0, 0, w, h)
        self.container.setGeometry(0, 0, w, h)

        if not self.original_pixmap.isNull():
            scaled = self.original_pixmap.scaled(
                w, h,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )

            x = (scaled.width() - w) // 2
            y = (scaled.height() - h) // 2
            cropped = scaled.copy(x, y, w, h)

            self.bg_label.setPixmap(cropped)

        super().resizeEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec())
