from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import argparse
from second_window import Second 
import sys
from skimage.io import imread_collection

#transfer color window
class Third(object):
    def setupUi(self, Third):
        Third.setObjectName("Third")
        Third.resize(658, 594)
        self.centralwidget = QtWidgets.QWidget(Third)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(150, 10, 481, 541))
        self.imageLbl.setMouseTracking(False)
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setScaledContents(False)
        self.imageLbl.setObjectName("imageLbl")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 90, 51, 31))
        self.spinBox.setObjectName("spinBox")
        self.selectImageBtn.raise_()
        self.pushButton.raise_()
        self.imageLbl.raise_()
        self.pushButton_2.raise_()
        self.spinBox.raise_()
        Third.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Third)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        Third.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Third)
        self.statusbar.setObjectName("statusbar")
        Third.setStatusBar(self.statusbar)

        self.retranslateUi(Third)
        QtCore.QMetaObject.connectSlotsByName(Third)
        Third.setTabOrder(self.selectImageBtn, self.pushButton_2)
        Third.setTabOrder(self.pushButton_2, self.spinBox)
        Third.setTabOrder(self.spinBox, self.pushButton)
        ###
        self.selectImageBtn.clicked.connect(self.setImage)
        self.pushButton_2.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.clicked.connect(self.transferColor)
        ###
        self.dialogs = list()
        ###
       

    def retranslateUi(self, Third):
        _translate = QtCore.QCoreApplication.translate
        Third.setWindowTitle(_translate("Third", "Chỉnh màu"))
        self.selectImageBtn.setText(_translate("Third", "Open"))
        self.pushButton.setText(_translate("Third", "Next"))
        self.pushButton_2.setText(_translate("Third", "Effects"))

    def on_pushButton_clicked(self):  # show the 2nd window
        import sys
        self.window = QtWidgets.QMainWindow()
        self.ui = Second()  # ------------->creating an object
        self.ui.setupUi(self.window)
        self.window.show()

# image processing
    def setImageName(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)")  # Ask for file
        return fileName

    def setImage(self):
        
        fileName = 'output.jpg'
        if fileName:  # If the user gives a file
            # Setup pixmap with the provided image
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(
            ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            # Align the label to center
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def transferColor(self):
        
        temp = self.spinBox.value()
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        if temp == 0:
            src = 'source.jpg'

        src = covertStr2Int(temp) 
        source = cv2.imread(src)
        
        fileName = 'output.jpg'
        target = cv2.imread(fileName)
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()

        ap.add_argument("-c", "--clip", type=str2bool, default='t',
                        help="Should np.clip scale L*a*b* values before final conversion to BGR? "
                        "Approptiate min-max scaling used if False.")
        ap.add_argument("-p", "--preservePaper", type=str2bool, default='t',
                        help="Should color transfer strictly follow methodology layed out in original paper?")
        ap.add_argument("-o", "--output",
                        help="Path to the output image (optional)")

        args = vars(ap.parse_args())
        transfer = color_transfer(
            source, target, clip=args["clip"], preserve_paper=args["preservePaper"])
        cv2.imshow("Transfer", transfer)
        cv2.waitKey(0)


# transfer color processing
def covertStr2Int(_Int):
    string = str(_Int)
    return string + ".jpg"


def image_stats(image):

    # compute the mean and standard deviation of each channel
    (l, a, b) = cv2.split(image)
    (l_Mean, l_Std) = (l.mean(), l.std())
    (a_Mean, a_Std) = (a.mean(), a.std())
    (b_Mean, b_Std) = (b.mean(), b.std())

    # return the color statistics
    return (l_Mean, l_Std, a_Mean, a_Std, b_Mean, b_Std)


def color_transfer(source, target, clip=True, preserve_paper=True):

    # convert the images from the RGB to L*ab* color space, being
    # sure to utilizing the floating point data type (note: OpenCV
    # expects floats to be 32-bit, so use that instead of 64-bit)
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

    # compute color statistics for the source and target images
    (l_Mean_Src, l_Std_Src, a_Mean_Src, a_Std_Src,
     b_Mean_Src, b_Std_Src) = image_stats(source)
    (l_Mean_Tar, l_Std_Tar, a_Mean_Tar, a_Std_Tar,
     b_Mean_Tar, b_Std_Tar) = image_stats(target)

    # subtract the means from the target image
    (l, a, b) = cv2.split(target)
    l -= l_Mean_Tar
    a -= a_Mean_Tar
    b -= b_Mean_Tar

    if preserve_paper:
        # scale by the standard deviations using paper proposed factor
        l = (l_Std_Tar / l_Std_Src) * l
        a = (a_Std_Tar / a_Std_Src) * a
        b = (b_Std_Tar / b_Std_Src) * b
    else:
        # scale by the standard deviations using reciprocal of paper proposed factor
        l = (l_Std_Src / l_Std_Tar) * l
        a = (a_Std_Src / a_Std_Tar) * a
        b = (b_Std_Src / b_Std_Tar) * b

    # add in the source mean
    l += l_Mean_Src
    a += a_Mean_Src
    b += b_Mean_Src

    # clip/scale the pixel intensities to [0, 255] if they fall
    # outside this range
    l = _scale_array(l, clip=clip)
    a = _scale_array(a, clip=clip)
    b = _scale_array(b, clip=clip)

    # merge the channels together and convert back to the RGB color
    # space, being sure to utilize the 8-bit unsigned integer data
    # type
    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)

    # return the color transferred image
    return transfer


def _min_max_scale(arr, new_range=(0, 255)):

    # get array's current min and max
    mn = arr.min()
    mx = arr.max()

    # check if scaling needs to be done to be in new_range
    if mn < new_range[0] or mx > new_range[1]:
        # perform min-max scaling
        scaled = (new_range[1] - new_range[0]) * \
            (arr - mn) / (mx - mn) + new_range[0]
    else:
        # return array if already in range
        scaled = arr

    return scaled


def _scale_array(arr, clip=True):

    if clip:
        scaled = np.clip(arr, 0, 255)
    else:
        scale_range = (max([arr.min(), 0]), min([arr.max(), 255]))
        scaled = _min_max_scale(arr, new_range=scale_range)

    return scaled


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


