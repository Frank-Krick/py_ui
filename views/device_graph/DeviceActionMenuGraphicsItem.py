from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class DeviceActionMenuGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self._addIcon = QtGui.QPixmap("resources/device_table_icons/add.png")
        self._removeIcon = QtGui.QPixmap("resources/device_table_icons/remove.png")
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self._width = 40
        self._height = 2 * 32 + 8 * 2

    def paint(self, painter, style_options, widget=None):
        self._paint_action_menu(painter)

    def boundingRect(self):
        return QtCore.QRectF(0.0, 0.0, self._width, self._height)

    def _paint_action_menu(self, painter):
        pen = QtGui.QPen(Qt.black, 1)
        painter.setPen(pen)
        painter.drawPixmap(4, 4, self._addIcon)
        painter.drawPixmap(4, 4 + 32 + 8, self._removeIcon)
