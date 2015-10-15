import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

import views
import model
import controller


itk = model.Model()


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._deviceGraphEditor = views.DeviceGraphEditor(itk)
        self.setup()

    def setup(self):
        self.resize(900, 600)
        self.move(70, 50)
        self.setWindowTitle('Instrument Tool Kit')
        self.setCentralWidget(self._deviceGraphEditor)

    def create_button(self):
        button = QtGui.QPushButton('Quit', self)
        button.resize(button.sizeHint())
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QtCore.QCoreApplication.instance().quit()


def main():
    application = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
