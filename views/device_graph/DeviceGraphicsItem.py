from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class DeviceGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, device, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self._device = device
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self.setAcceptsHoverEvents(True)
        self._hover = False
        self._padding = 5

    def boundingRect(self):
        return QtCore.QRectF(0.0, 0.0, 200.0, 125.0)

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
        painter.drawText(text_position, self._device.name, text_option)
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

