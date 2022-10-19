import sys
import os
from random_image import main
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout


def on_click():
    main()
    os.system('random_image.png')


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(1200, 100, 440, 280)

        label = QLabel("Click on the button to see a random picture")

        button = QPushButton("Push me!")
        button.clicked.connect(on_click)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    app.exec()
