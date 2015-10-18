from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui

from AddConnectionGraphicsItem import AddConnectionGraphicsItem
from ParameterMenuGraphicsItem import ParameterMenuGraphicsItem


class DeviceGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, device_id, device, device_graph_controller, scene, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self._addConnectionControl = AddConnectionGraphicsItem(device_graph_controller, self)
        self._addConnectionControl.setPos(QtCore.QPointF(
            200 - self._addConnectionControl.boundingRect().width(),
            125 - self._addConnectionControl.boundingRect().height()
        ))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self.setAcceptsHoverEvents(True)
        self._hover = False
        self._padding = 5
        self._connections = []
        self.setZValue(1)
        self.deviceId = device_id
        self._device = device
        self._parameterMenu = self._create_parameter_menu(scene)
        self._parameterMenu.setVisible(False)

    def add_connection(self, connection):
        self._connections.append(connection)

    def display_parameter_menu(self):
        self._parameterMenu.setVisible(True)
        self.update()

    def mouseMoveEvent(self, event):
        QtGui.QGraphicsItem.mouseMoveEvent(self, event)
        for connection in self._connections:
            connection.update_device_position()

    def boundingRect(self):
        return QtCore.QRectF(-10, -10, 200 + 10, 125 + 10)

    def paint(self, painter, style_options, widget=None):
        color = QtGui.QColor(Qt.darkYellow)
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        painter.drawRoundedRect(0 + self._padding, 0 + self._padding, 200 - self._padding, 125 - self._padding, 10, 10)
        painter.setPen(QtGui.QPen(Qt.black, 1))
        font = painter.font()
        font.setPointSize(14)
        font.setBold(True)
        painter.setFont(font)
        text_option = QtGui.QTextOption()
        text_option.setAlignment(QtCore.Qt.AlignCenter)
        text_position = QtCore.QRectF(0, 0 + self._padding, 200, 35)
        painter.drawText(text_position, 'device', text_option)
        painter.drawLine(0 + self._padding, 34, 200, 34)

    def hoverEnterEvent(self, event):
        QtGui.QGraphicsItem.hoverEnterEvent(self, event)
        effect = QtGui.QGraphicsDropShadowEffect()
        color = QtGui.QColor(Qt.red)
        color.setAlpha(0.4 * 255)
        effect.setColor(color)
        effect.setBlurRadius(10)
        self.setGraphicsEffect(effect)
        self._hover = True

    def hoverLeaveEvent(self, event):
        QtGui.QGraphicsItem.hoverLeaveEvent(self, event)
        self._hover = False
        self.setGraphicsEffect(None)
        self.update()

    def _create_parameter_menu(self, scene):
        item = ParameterMenuGraphicsItem(self._device, scene, self)
        item.setPos(QtCore.QPointF(-10, -10))
        return item
