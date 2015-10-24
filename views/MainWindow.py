from PyQt4 import QtGui
from PyQt4 import QtCore

import views
import model
import controller


class MainWindow(QtGui.QMainWindow):
    def __init__(self, itk):
        super(MainWindow, self).__init__()
        self._setup_window()
        self._create_tabs(itk)

    def _create_tabs(self, itk):
        device_graph_editor = views.DeviceGraphEditor(itk)
        self.setCentralWidget(device_graph_editor)

    def _setup_window(self):
        self.setWindowTitle('Instrument Tool Kit')
        self.resize(1200, 600)
        self.move(70, 50)

    def create_button(self):
        button = QtGui.QPushButton('Quit', self)
        button.resize(button.sizeHint())
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QtCore.QCoreApplication.instance().quit()
