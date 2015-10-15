from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class DeviceGraphView(QtGui.QGraphicsView):
    def __init__(self, device_graph_controller, parent=None):
        super(DeviceGraphView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setRenderHint(QtGui.QPainter.TextAntialiasing)
        self._deviceGraphController = device_graph_controller

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        text = mime_data.text()
        index = int(text.split(':')[1])
        position = self.mapToScene(event.pos())
        self._deviceGraphController.add_device(index, position)
        event.accept()
