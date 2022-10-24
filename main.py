import sys
import os
from random_image import main
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click on the button to see a random picture")
        self.setWindowTitle("My App")
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(1280, 720)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Push me!")
        button.setFixedSize(500, 35)

        button.clicked.connect(self.clicked_button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def clicked_button(self):
        main()

        dlg = QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("Something went wrong!\nTry to restart the app..")

        if os.path.exists('random_image.png'):
            pixmap = QPixmap('random_image.png')
            self.label.adjustSize()
            self.label.setPixmap(pixmap)
        else:
            dlg.exec()
            app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    app.exec()
