from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class DeviceTableView(QtGui.QTableView):
    def __init__(self):
        QtGui.QTableView.__init__(self)

    def resizeEvent(self, event):
        width = event.size().width()
        self.setColumnWidth(0, width)
