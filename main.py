from __future__ import print_function
from PyQt5 import QtCore, QtGui, QtWidgets
from builtins import input
import cv2
import numpy as np
from second_window import Second
from third_window import Third
import pygame
import sys
from PIL import Image
pygame.init()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(0, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(150, 10, 501, 551))
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(70, 80, 51, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(71, 110, 51, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 560, 91, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.selectImageBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn_2.setGeometry(QtCore.QRect(0, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn_2.setFont(font)
        self.selectImageBtn_2.setObjectName("selectImageBtn_2")
        self.selectImageBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn_3.setGeometry(QtCore.QRect(0, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn_3.setFont(font)
        self.selectImageBtn_3.setObjectName("selectImageBtn_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.selectImageBtn, self.doubleSpinBox)
        MainWindow.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_2)
        MainWindow.setTabOrder(self.doubleSpinBox_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        ###
        self.selectImageBtn.clicked.connect(self.setImage)
        self.pushButton.clicked.connect(self.ImageProcess)
        self.pushButton_2.clicked.connect(self.on_pushButton_click)
        self.pushButton_3.clicked.connect(self.Cut_Image)
        ###

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImageBtn.setText(_translate("MainWindow", "Select Image"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Next..."))
        self.pushButton_3.setText(_translate("MainWindow", "Cut Image"))
        self.selectImageBtn_2.setText(_translate("MainWindow", "contrast"))
        self.selectImageBtn_3.setText(_translate("MainWindow", "brightness"))

    def on_pushButton_click(self):  # show the 3st window
        import sys
        self.window = QtWidgets.QMainWindow()
        self.ui = Third()  # ------------->creating an object
        self.ui.setupUi(self.window)
        self.window.show()

    def setImage(self):
    
        fileName = self.setImageName()
        if fileName:  # If the user gives a file
            # Setup pixmap with the provided image
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(
            ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            # Align the label to center
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        temp = cv2.imread(fileName)
        cv2.imwrite('example.jpg', temp)

    def setImageName(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)")  # Ask for file
        return fileName

    def ImageProcess(self):

        fileName = 'example.jpg'
        image = cv2.imread(fileName)

        new_image = np.zeros(image.shape, image.dtype)
        alpha = 1.0  # Simple contrast control
        beta = 50    # Simple brightness control
        print('done!')

        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(3.0)
        alpha = self.doubleSpinBox.value()

        self.doubleSpinBox_2.setMinimum(0.0)
        self.doubleSpinBox_2.setMaximum(100)
        beta = self.doubleSpinBox_2.value()

        new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        cv2.imshow('New Image', new_image)
        cv2.imwrite('output.jpg', new_image)
        # Wait until user press some key
        cv2.waitKey()

    def Cut_Image(self):
        input_loc = 'output.jpg'
        output_loc = 'output.jpg'
        screen, px = setup(input_loc)
        left, upper, right, lower = mainLoop(screen, px)

        # ensure output rect always has positive width, height
        if right < left:
            left, right = right, left
        if lower < upper:
            lower, upper = upper, lower
        im = Image.open(input_loc)
        im = im.crop((left, upper, right, lower))

        pygame.display.quit()
        im.save(output_loc)
        img = cv2.imread('output.jpg')
        cv2.imshow('cut_image', img)
        cv2.waitKey()


def displayImage(screen, px, topleft, prior):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width = pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn't moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    # return current box extents
    return (x, y, width, height)


def setup(path):
    px = pygame.image.load(path)
    screen = pygame.display.set_mode(px.get_rect()[2:])
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px


def mainLoop(screen, px):
    topleft = bottomright = prior = None
    n = 0
    while n != 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    n = 1
        if topleft:
            prior = displayImage(screen, px, topleft, prior)
    return (topleft + bottomright)


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
