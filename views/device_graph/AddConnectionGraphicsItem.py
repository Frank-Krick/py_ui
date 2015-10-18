from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class AddConnectionGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, device_graph_controller, parent):
        QtGui.QGraphicsItem.__init__(self, parent)
        self._icon = QtGui.QPixmap("resources/device_table_icons/add.png")
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self._padding = 5
        self._boundingRect = self._calculate_size(self._icon.rect())
        self._deviceGraphController = device_graph_controller

    def paint(self, painter, style_options, widget=None):
        pen = QtGui.QPen(Qt.black, 1)
        painter.setPen(pen)
        painter.drawPixmap(self._padding, self._padding, self._icon)

    def boundingRect(self):
        return self._boundingRect

    def mousePressEvent(self, event):
        position = self.mapToScene(event.pos())
        source_device_id = self.parentItem().deviceId
        self._deviceGraphController.start_add_connection(position, source_device_id)

    def _calculate_size(self, rect):
        return QtCore.QRectF(
            rect.x(),
            rect.y(),
            rect.width() + self._padding * 2,
            rect.height() + self._padding * 2)
