from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import argparse


#effect window
class Second(object):
    def setupUi(self, Second):
        Second.setObjectName("Second")
        Second.resize(1116, 624)
        self.centralwidget = QtWidgets.QWidget(Second)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(10, 10, 211, 281))
        self.imageLbl.setMouseTracking(False)
        self.imageLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl.setText("")
        self.imageLbl.setScaledContents(False)
        self.imageLbl.setObjectName("imageLbl")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.imageLbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_2.setGeometry(QtCore.QRect(230, 10, 211, 281))
        self.imageLbl_2.setMouseTracking(False)
        self.imageLbl_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_2.setText("")
        self.imageLbl_2.setScaledContents(False)
        self.imageLbl_2.setObjectName("imageLbl_2")
        self.imageLbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_3.setGeometry(QtCore.QRect(450, 10, 211, 281))
        self.imageLbl_3.setMouseTracking(False)
        self.imageLbl_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_3.setText("")
        self.imageLbl_3.setScaledContents(False)
        self.imageLbl_3.setObjectName("imageLbl_3")
        self.imageLbl_4 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_4.setGeometry(QtCore.QRect(670, 10, 211, 281))
        self.imageLbl_4.setMouseTracking(False)
        self.imageLbl_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_4.setText("")
        self.imageLbl_4.setScaledContents(False)
        self.imageLbl_4.setObjectName("imageLbl_4")
        self.imageLbl_5 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_5.setGeometry(QtCore.QRect(890, 10, 211, 281))
        self.imageLbl_5.setMouseTracking(False)
        self.imageLbl_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_5.setText("")
        self.imageLbl_5.setScaledContents(False)
        self.imageLbl_5.setObjectName("imageLbl_5")
        self.imageLbl_6 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_6.setGeometry(QtCore.QRect(10, 300, 211, 281))
        self.imageLbl_6.setMouseTracking(False)
        self.imageLbl_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_6.setText("")
        self.imageLbl_6.setScaledContents(False)
        self.imageLbl_6.setObjectName("imageLbl_6")
        self.imageLbl_7 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_7.setGeometry(QtCore.QRect(230, 300, 211, 281))
        self.imageLbl_7.setMouseTracking(False)
        self.imageLbl_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_7.setText("")
        self.imageLbl_7.setScaledContents(False)
        self.imageLbl_7.setObjectName("imageLbl_7")
        self.imageLbl_8 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_8.setGeometry(QtCore.QRect(450, 300, 211, 281))
        self.imageLbl_8.setMouseTracking(False)
        self.imageLbl_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_8.setText("")
        self.imageLbl_8.setScaledContents(False)
        self.imageLbl_8.setObjectName("imageLbl_8")
        self.imageLbl_9 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_9.setGeometry(QtCore.QRect(670, 300, 211, 281))
        self.imageLbl_9.setMouseTracking(False)
        self.imageLbl_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_9.setText("")
        self.imageLbl_9.setScaledContents(False)
        self.imageLbl_9.setObjectName("imageLbl_9")
        self.imageLbl_10 = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl_10.setGeometry(QtCore.QRect(890, 300, 211, 281))
        self.imageLbl_10.setMouseTracking(False)
        self.imageLbl_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl_10.setText("")
        self.imageLbl_10.setScaledContents(False)
        self.imageLbl_10.setObjectName("imageLbl_10")
        Second.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Second)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        Second.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Second)
        self.statusbar.setObjectName("statusbar")
        Second.setStatusBar(self.statusbar)

        self.retranslateUi(Second)
        QtCore.QMetaObject.connectSlotsByName(Second)
        ###
        self.pushButton.clicked.connect(self.setImage)

        ###
    def retranslateUi(self, Second):
        _translate = QtCore.QCoreApplication.translate
        Second.setWindowTitle(_translate("Second", "hiệu ứng mẫu"))
        self.pushButton.setText(_translate("Second", "Click here!"))

    def setImage(self):
        fileName = '1.PNG'
        fileName_2 = '2.PNG'
        fileName_3 = '3.PNG'
        fileName_4 = '4.PNG'
        fileName_5 = '5.PNG'
        fileName_6 = '6.PNG'
        fileName_7 = '7.PNG'
        fileName_8 = '8.PNG'
        fileName_9 = '9.PNG'
        fileName_10 = '10.PNG'

        # Setup pixmap with the provided image 1
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        # 2
        pixmap_2 = QtGui.QPixmap(fileName_2)
        pixmap_2 = pixmap_2.scaled(self.imageLbl_2.width(), self.imageLbl_2.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_2.setPixmap(pixmap_2)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_2.setAlignment(QtCore.Qt.AlignCenter)
        # 3
        pixmap_3 = QtGui.QPixmap(fileName_3)
        pixmap_3 = pixmap.scaled(self.imageLbl_3.width(), self.imageLbl_3.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_3.setPixmap(pixmap_3)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_3.setAlignment(QtCore.Qt.AlignCenter)
        # 4
        pixmap_4 = QtGui.QPixmap(fileName_4)
        pixmap_4 = pixmap.scaled(self.imageLbl_4.width(), self.imageLbl_4.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_4.setPixmap(pixmap_4)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_4.setAlignment(QtCore.Qt.AlignCenter)
        # 5
        pixmap_5 = QtGui.QPixmap(fileName_5)
        pixmap_5 = pixmap_5.scaled(self.imageLbl_5.width(), self.imageLbl_5.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_5.setPixmap(pixmap_5)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_5.setAlignment(QtCore.Qt.AlignCenter)
        # 6
        pixmap_6 = QtGui.QPixmap(fileName_6)
        pixmap_6 = pixmap.scaled(self.imageLbl_6.width(), self.imageLbl_6.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_6.setPixmap(pixmap_6)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_6.setAlignment(QtCore.Qt.AlignCenter)
        # 7
        pixmap_7 = QtGui.QPixmap(fileName_7)
        pixmap_7 = pixmap_7.scaled(self.imageLbl_7.width(), self.imageLbl_7.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_7.setPixmap(pixmap_7)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_7.setAlignment(QtCore.Qt.AlignCenter)
        # 8
        pixmap_8 = QtGui.QPixmap(fileName_8)
        pixmap_8 = pixmap_8.scaled(self.imageLbl_8.width(), self.imageLbl_8.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_8.setPixmap(pixmap_8)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_8.setAlignment(QtCore.Qt.AlignCenter)
        # 9
        pixmap_9 = QtGui.QPixmap(fileName_9)
        pixmap_9 = pixmap.scaled(self.imageLbl_9.width(), self.imageLbl_9.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_9.setPixmap(pixmap_9)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_9.setAlignment(QtCore.Qt.AlignCenter)
        # 10
        pixmap_10 = QtGui.QPixmap(fileName_10)
        pixmap_10 = pixmap.scaled(self.imageLbl_10.width(), self.imageLbl_10.height(
        ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl_10.setPixmap(pixmap_10)  # Set the pixmap onto the label
        # Align the label to center
        self.imageLbl_10.setAlignment(QtCore.Qt.AlignCenter)

