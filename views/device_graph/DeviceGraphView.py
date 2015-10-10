from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class DeviceGraphView(QtGui.QGraphicsView):
    def __init__(self, itk, graph_index, parent=None):
        super(DeviceGraphView, self).__init__(parent)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setRenderHint(QtGui.QPainter.TextAntialiasing)
        self.itk = itk
        self.graphIndex = graph_index

