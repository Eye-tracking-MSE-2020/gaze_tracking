import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QHBoxLayout, QVBoxLayout, QToolTip, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt
from qtconsole.qt import QtGui

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.quit_sig = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Eye Tracking')
        self.setWindowIcon(QIcon('eye.png'))

        self.start_btn = QPushButton('Start', self)
        self.start_btn.setCheckable(True)
        self.start_btn.toggled.connect(self.start_end)

        #question guide line
        self.lbl = QLabel(self)
        self.lbl.resize(50, 50)
        pixmap = QPixmap("question_mark.png")
        pixmap = pixmap.scaledToWidth(50)
        self.lbl.setPixmap(QPixmap(pixmap))
        self.lbl.setToolTip('Eyt Tracking Guide <br><b>Click Start button</b></br><br>Put your face on the guide line</br>')

        self.face_label = QtWidgets.QLabel(self)
        self.face_label.setGeometry(150, 100, 500, 500)
        self.face_label.setFrameShape(QtWidgets.QFrame.Box)
        self.face_label.setObjectName("face_label")

        '''
        self.quit_btn = QPushButton('Quit', self)
        self.quit_btn.move(50, 50)
        self.quit_btn.resize(self.quit_btn.sizeHint())
        self.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        '''

        #horizontal layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.start_btn)
        hbox.addStretch(1)
        #vertical layout
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(20)

        self.setLayout(vbox)

        self.resize(800, 700)
        self.center()
        self.show()

    def start_end(self, state):
        if state:
            self.start_btn.setText("End")
            return 1
        else:
            self.start_btn.setText("Start")
            return 0

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.quit_sig = True
            event.accept()
        else:
            self.quit_sig = False
            event.ignore()


'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''