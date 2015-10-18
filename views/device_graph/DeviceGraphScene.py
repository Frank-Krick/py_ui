from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

import math
import random
import views
import itk
from DeviceGraphicsItem import DeviceGraphicsItem


class DeviceGraphScene(QtGui.QGraphicsScene):
    def __init__(self, device_graph_model):
        QtGui.QGraphicsScene.__init__(self)
        self._deviceGraphModel = device_graph_model
        self._addConnectionMode = False
        self._selectParameterMode = False
        self._addConnectionItem = QtGui.QGraphicsLineItem()
        self._addConnectionItem.setPen(Qt.green)
        self._addConnectionItem.setZValue(0)
        self._addConnectionStartPosition = QtCore.QPointF(0, 0)
        self._addConnectionSourceDeviceId = 0
        self._addConnectionTargetDeviceId = 0
        self.deviceGraphController = None

    def device_item(self, device_id):
        for item in self.items():
            if isinstance(item, views.DeviceGraphicsItem):
                if item.deviceId is device_id:
                    return item
        return None

    def start_add_connection(self, position, source_device_id):
        if self._addConnectionMode is False:
            self._addConnectionMode = True
            self._addConnectionItem.setPos(position)
            self._addConnectionItem.setLine(0, 0, 10, 10)
            self.addItem(self._addConnectionItem)
            self._addConnectionStartPosition = position
            self._addConnectionSourceDeviceId = source_device_id

    def end_add_connection(self, position):
        if self._addConnectionMode is True:
            item = self.itemAt(position)
            if item is not None:
                if isinstance(item, DeviceGraphicsItem):
                    target = item.deviceId
                    source = self._addConnectionSourceDeviceId
                    source_device = self._deviceGraphModel.device(source)
                    if source_device.device.device.deviceType is itk.DeviceType.Audio:
                        self._add_connection(source, target)
                    elif source_device.device.device.deviceType is itk.DeviceType.Control:
                        item.display_parameter_menu()
                        self._addConnectionSourceDeviceId = source
                        self._addConnectionTargetDeviceId = target
                        self._selectParameterMode = True

    def end_parameter_selection(self, parameter):
        target = self._addConnectionTargetDeviceId
        source = self._addConnectionSourceDeviceId
        self._add_connection(source, target, parameter)

    def _add_connection(self, source, target, parameter=None):
        self._addConnectionMode = False
        self._selectParameterMode = False
        self.removeItem(self._addConnectionItem)
        self.deviceGraphController.connect(source, target, parameter)

    def mouseMoveEvent(self, event):
        if self._selectParameterMode is True and self._addConnectionMode is True:
            QtGui.QGraphicsScene.mouseMoveEvent(self, event)
        elif self._addConnectionMode is True:
            position = event.scenePos()
            x = [self._addConnectionStartPosition.x(), position.x()]
            y = [self._addConnectionStartPosition.y(), position.y()]
            self._move_line_to_origin(x, y)
            self._addConnectionItem.setLine(x[0], y[0], x[1], y[1])
        else:
            QtGui.QGraphicsScene.mouseMoveEvent(self, event)

    def mousePressEvent(self, event):
        if self._addConnectionMode is True and self._selectParameterMode is True:
            QtGui.QGraphicsScene.mousePressEvent(self, event)
        if self._addConnectionMode is True:
            self.end_add_connection(event.scenePos())
            self.update()
        else:
            QtGui.QGraphicsScene.mousePressEvent(self, event)

    def _move_line_to_origin(self, x, y):
        x[1] = x[1] - x[0]
        y[1] = y[1] - y[0]
        x[0] = 0
        y[0] = 0
        return x, y
