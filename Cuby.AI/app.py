import cv2
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtCore import Qt
import startup_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("CUBY.AI")
        self.setGeometry(100, 100, 1366, 720)

        # Center the main window on the screen
        self.center()

        # Create a label for the background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap("interface_files//image.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())
        self.background_label.setPixmap(pixmap)

        # Create a label to show the camera feed
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 500, 934, 120)
        self.image_label.setScaledContents(True)

        # Create a button with custom styling and label
        self.button = QPushButton(self)
        self.button.setGeometry(self.width() // 2 - 150, self.height() // 2 - 150, 300, 300)
        self.button.setStyleSheet("QPushButton { border-radius: 150px;  }")
        self.button.clicked.connect(startup_file.startup)

        # Create a button with custom styling and label
        self.button = QPushButton(self)
        self.button.setGeometry(self.width() // 2 - 150, self.height() // 2 - 150, 300, 300)
        self.button.setStyleSheet("QPushButton { border-radius: 150px; }")
        self.button.clicked.connect(startup_file.startup)

        # Create a label for the button text with custom font
        label = QLabel("Cuby", self.button)
        label.setGeometry(0, self.button.height() - 140, self.button.width(), 100)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white;")
        font = QFont("Times New Roman", 30, QFont.Bold)
        label.setFont(font)

        # Open the camera using OpenCV
        self.camera = cv2.VideoCapture('interface_files//waves.mp4')

        # Create a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)

    def center(self):
        # Calculate the center coordinates of the screen
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center of the screen
        self.move(x, y)

    def update_image(self):
        # Read the image from the camera
        ret, image = self.camera.read()

        # Convert the image to the RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a QImage from the image
        qimage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(qimage)

        # Set the pixmap on the label
        self.image_label.setPixmap(pixmap)

    def main(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
