from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class ParameterMenuItemGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, parameter_description, scene, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, False)
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self.setAcceptsHoverEvents(True)
        self._parameterDescription = parameter_description
        self._textItem = self._create_parameter_name_text_item()
        color = QtGui.QColor(Qt.lightGray)
        self._brush = QtGui.QBrush(color)
        self._scene = scene

    def boundingRect(self):
        return self._textItem.boundingRect()

    def paint(self, painter, item, widget=None):
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush)
        painter.drawRect(self._textItem.boundingRect())

    def _create_parameter_name_text_item(self):
        item = QtGui.QGraphicsSimpleTextItem(self._parameterDescription.name, self)
        font = item.font()
        font.setPointSize(14)
        font.setBold(True)
        item.setFont(font)
        item.setPos(QtCore.QPointF(0, 0))
        return item

    def hoverEnterEvent(self, event):
        color = QtGui.QColor(Qt.gray)
        self._brush = QtGui.QBrush(color)
        self.update()

    def hoverLeaveEvent(self, event):
        color = QtGui.QColor(Qt.lightGray)
        self._brush = QtGui.QBrush(color)

    def mousePressEvent(self, event):
        parameter_id = self._parameterDescription.id
        self._scene.end_parameter_selection(parameter_id)
        self.parentItem().setVisible(False)
