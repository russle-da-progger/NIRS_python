import sys

from PyQt5 import QtGui, QtWidgets

import paths
import texts
from new_ui import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    buffer_images: list[str]
    buffer_texts: list[str]

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.ui.radioButton_ground_launch.clicked.connect(self.choose_f1)
        self.ui.radioButton_ARM.clicked.connect(self.choose_f2)
        self.ui.radioButton_ARMtoRM.clicked.connect(self.choose_f3)
        self.ui.radioButton_RMtoARM.clicked.connect(self.choose_f4)

        self.ui.pushButton_forward.clicked.connect(self.show_next)
        self.ui.pushButton_backward.clicked.connect(self.show_prev)
        self.ui.pushButton_full_scheme.clicked.connect(self.show_full)

    def show_full(self):
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap("images/full/full description.png"))

    def choose_f1(self):
        self.i = 0
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(paths.ground_launch[0]))
        self.ui.textBrowser_description.setText(texts.ground_launch[0])

        self.buffer_images = paths.ground_launch
        self.buffer_texts = texts.ground_launch

        self.ui.label_text_counter.setText(str(self.i + 1) + "/" + str(len(self.buffer_images)))

    def choose_f2(self):
        self.i = 0
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(paths.b[0]))

        self.buffer_images = paths.b

        self.ui.label_text_counter.setText(str(self.i + 1) + "/" + str(len(self.buffer_images)))

    def choose_f3(self):
        self.i = 0
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(paths.c[0]))

        self.buffer_images = paths.c

        self.ui.label_text_counter.setText(str(self.i + 1) + "/" + str(len(self.buffer_images)))

    def choose_f4(self):
        self.i = 0
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(paths.d[0]))

        self.buffer_images = paths.d

        self.ui.label_text_counter.setText(str(self.i + 1) + "/" + str(len(self.buffer_images)))

    def show_prev(self):
        array_images = self.buffer_images
        array_texts = self.buffer_texts
        self.i -= 1
        if self.i < 0:
            self.i = len(array_images) - 1
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(array_images[self.i]))
        self.ui.textBrowser_description.setText(array_texts[self.i])
        self.ui.label_text_counter.setText(str(self.i+1) + "/" + str(len(array_images)))

    def show_next(self):
        array_images = self.buffer_images
        array_texts = self.buffer_texts
        self.i += 1
        if self.i == len(self.buffer_images):
            self.i: int = 0
        self.ui.label_image_overlay.setPixmap(QtGui.QPixmap(array_images[self.i]))
        self.ui.textBrowser_description.setText(array_texts[self.i])
        self.ui.label_text_counter.setText(str(self.i+1) + "/" + str(len(array_images)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
