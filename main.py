import sys
from random_image import main
from convert import convert_to_srgb
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click on the button to see a random picture\nIt will take a couple of second!")
        self.setWindowTitle("My App")
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(1280, 720)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Push me!")
        button.setFixedSize(500, 35)

        button.clicked.connect(self.clicked_button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def clicked_button(self):
        dlg2 = QMessageBox()
        dlg2.setWindowTitle("Wait")
        dlg2.setText("Wait a couple of seconds please!")

        dlg2.exec()

        result = main()

        dlg = QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("Something went wrong!\nTry to restart the app..")

        dlg1 = QMessageBox()
        dlg1.setWindowTitle("Error")
        dlg1.setText("Internet connection lost!\nCheck connection..")

        if result == 'correct':
            convert_to_srgb('random_image.png')
            pixmap = QPixmap('random_image.png')
            self.label.adjustSize()
            self.label.setPixmap(pixmap)
        elif result == 'something':
            dlg.exec()
            app.exit()
        elif result == 'connection':
            dlg1.exec()
            app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    app.exec()
