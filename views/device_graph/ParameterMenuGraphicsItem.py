from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui

from ParameterMenuItemGraphicsItem import ParameterMenuItemGraphicsItem


class ParameterMenuGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, device, scene, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self._padding = 5
        self._spacing = 4
        color = QtGui.QColor(Qt.lightGray)
        self._brush = QtGui.QBrush(color)
        self._device = device
        self._create_parameter_menu_items(scene)
        self._boundingRect = self._calculate_bounding_rect()

    def boundingRect(self):
        return self._boundingRect

    def paint(self, painter, item, widget=None):
        painter.setBrush(self._brush)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self._boundingRect, 10, 10)

    def _calculate_bounding_rect(self):
        children = self.childItems()
        height = (len(children) - 1) * self._spacing
        max_width = 0
        for item in children:
            height += item.boundingRect().height()
            if item.boundingRect().width() > max_width:
                max_width = item.boundingRect().width()
        return QtCore.QRectF(0, 0, max_width + 2 * self._padding, height + 2 * self._padding)

    def _create_parameter_menu_items(self, scene):
        x = 0 + self._padding
        y = 0 + self._padding
        for parameter in self._device.available_parameters:
            item = ParameterMenuItemGraphicsItem(parameter, scene, self)
            item.setPos(QtCore.QPointF(x, y))
            y += item.boundingRect().height() + self._spacing
