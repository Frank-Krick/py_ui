from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import math


class ConnectionGraphicsItem(QtGui.QGraphicsItem):
    def __init__(self, source_id, target_id, graph_model, parent=None):
        QtGui.QGraphicsItem.__init__(self, parent)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape, True)
        self._sourceId = source_id
        self._targetId = target_id
        self._model = graph_model
        self._radianToDegreeFactor = 180 / math.pi
        self._start = None
        self._end = None
        self._distance = 0
        self._angle = 0
        self._background_brush = self._setup_background_brush()
        self._upper_pattern_brush = self._setup_upper_pattern_brush()
        self._lower_pattern_brush = self._setup_lower_pattern_brush()
        self._update_parameters()

    def paint(self, painter, style_options, widget=None):
        self._paint_connection(painter)

    def boundingRect(self):
        return self._rect

    def update_device_position(self):
        self.prepareGeometryChange()
        self._update_parameters()

    def _update_parameters(self):
        source_device_item = self._model.device(self._sourceId)
        target_device_item = self._model.device(self._targetId)
        source_item = source_device_item.item
        target_item = target_device_item.item
        source_item_center = self._item_bounding_rect_center_in_scene_coordinates(source_item)
        target_item_center = self._item_bounding_rect_center_in_scene_coordinates(target_item)
        self._distance = self._calc_distance(source_item_center, target_item_center)
        self._angle = self._calc_angle(source_item_center, target_item_center)
        if source_item_center.x() <= target_item_center.x():
            self._start = source_item_center
            self._end = target_item_center
        else:
            self._start = target_item_center
            self._end = source_item_center
        self.setRotation(self._angle)
        self.setPos(self._start)
        self._rect = QtCore.QRectF(0, -10, self._distance, 20)

    def _paint_connection(self, painter):
        painter.setBrush(self._background_brush)
        painter.drawRect(self._rect)
        painter.setBrush(self._upper_pattern_brush)
        painter.setPen(Qt.blue)
        painter.drawRect(
            QtCore.QRectF(self._rect.x(), self._rect.y(),
                          self._rect.width(), self._rect.height() / 2))
        painter.setBrush(self._lower_pattern_brush)
        painter.drawRect(
            QtCore.QRectF(self._rect.x() + self._rect.height() / 2,
                          self._rect.y() + self._rect.height() / 2,
                          self._rect.width(), self._rect.height() / 2))

    def _calc_distance(self, A, B):
        a = abs(A.x() - B.x())
        b = abs(A.y() - B.y())
        return math.sqrt(a * a + b * b)

    def _calc_angle(self, A, B):
        if A.x() == B.x():
            return 90
        if A.y() == B.y():
            return 0
        a = abs(A.y() - B.y())
        b = abs(A.x() - B.x())
        tangens = a / b
        angle_in_radians = math.atan(tangens)
        angle_in_degrees = angle_in_radians * self._radianToDegreeFactor
        if A.x() < B.x() and A.y() < B.y():
            return angle_in_degrees
        elif A.x() < B.x() and A.y() > B.y():
            return -angle_in_degrees
        elif A.x() > B.x() and A.y() < B.y():
            return -angle_in_degrees
        elif A.x() > B.x() and A.y() > B.y():
            return angle_in_degrees

    def _item_bounding_rect_center_in_scene_coordinates(self, item):
        bounding_rect = item.mapRectToScene(item.boundingRect())
        x = bounding_rect.x() + bounding_rect.width() / 2
        y = bounding_rect.y() + bounding_rect.height() / 2
        return QtCore.QPointF(x, y)

    def _setup_upper_pattern_brush(self):
        color = QtGui.QColor(Qt.blue)
        brush = QtGui.QBrush(color)
        brush.setStyle(Qt.FDiagPattern)
        return brush

    def _setup_lower_pattern_brush(self):
        color = QtGui.QColor(Qt.blue)
        brush = QtGui.QBrush(color)
        brush.setStyle(Qt.BDiagPattern)
        return brush

    def _setup_background_brush(self):
        color = QtGui.QColor(Qt.darkBlue)
        brush = QtGui.QBrush(color)
        brush.setStyle(Qt.SolidPattern)
        return brush
