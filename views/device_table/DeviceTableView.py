from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class DeviceTableView(QtGui.QTableView):
    def __init__(self):
        QtGui.QTableView.__init__(self)
        self.setSelectionMode(self.SingleSelection)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.verticalHeader().setVisible(False)

    def resizeEvent(self, event):
        width = event.size().width()
        self.setColumnWidth(0, width)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        drag = QtGui.QDrag(self)
        mime_data = QtCore.QMimeData()
        mime_data.setText('device:' + str(index.row()))
        drag.setMimeData(mime_data)
        pixmap = QtGui.QPixmap()
        pixmap = pixmap.grabWidget(self, self.visualRect(index))
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - self.visualRect(index).topLeft())
        dropAction = drag.exec_()
