import sys
import os
from random_image import main
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QMessageBox


def on_click():
    main()

    dlg = QMessageBox()
    dlg.setWindowTitle("Error")
    dlg.setText("Something went wrong!\nTry to restart the app..")

    if os.path.exists('random_image.png'):
        os.system('random_image.png')
    else:
        dlg.exec()
        app.exit()


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
