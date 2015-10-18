from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

import math
import views


class DeviceItem:
    def __init__(self, item, device):
        self.device = device
        self.item = item


class ConnectionItem:
    def __init__(self, source_id, target_it, item):
        self.sourceId = source_id
        self.targetId = target_it
        self.item = item


class DeviceGraphModel:
    def __init__(self, device_graph):
        self.scene = None
        self._deviceGraph = device_graph
        self._deviceItemMap = {}
        self._radianToDegreeFactor = 180 / math.pi
        self.deviceGraphController = None
        self.deviceGraphScene = None

    def device(self, device_id):
        device = self._deviceGraph.device(device_id)
        item = self.deviceGraphScene.device_item(device_id)
        return DeviceItem(item, device)

    def add_device(self, device):
        return self._deviceGraph.add_device(device)

    def connect(self, source, target, parameter=None):
        if parameter is None:
            self._deviceGraph.connect(source, target)
        else:
            self._deviceGraph.connect(source, target, parameter)

    def device_graph_graphics_scene(self):
        if self.scene is None:
            self.scene = views.DeviceGraphScene(self)
            self._create_graphics_scene(self.scene)
        return self.scene

    def _create_graphics_scene(self, scene):
        brush = QtGui.QBrush(Qt.black)
        self.scene.setBackgroundBrush(brush)
        self._add_devices_to_scene(self._deviceGraph, scene)
        self._add_connections_to_scene(self._deviceGraph, scene)

    def _add_connections_to_scene(self, device_graph, scene):
        for connection in device_graph.audioConnections:
            self._add_connection(connection, views.ConnectionType.Audio, scene)
        for connection in device_graph.controlConnections:
            self._add_connection(connection, views.ConnectionType.Control, scene)

    def _add_connection(self, connection, connection_type, scene):
        item = views.ConnectionGraphicsItem(connection.source, connection.target, self, connection_type)
        item.setZValue(0)
        scene.addItem(item)
        source_item = self._deviceItemMap[connection.source]
        target_item = self._deviceItemMap[connection.target]
        source_item.add_connection(
            ConnectionItem(connection.source, connection.target, item))
        target_item.add_connection(
            ConnectionItem(connection.source, connection.target, item))

    def _add_devices_to_scene(self, device_graph, scene):
        x = [-300, 0, 300, 600, -300, 600]
        y = [-100, 150, 100, 200, 200, 0]
        for device in device_graph.devices:
            item = views.DeviceGraphicsItem(device)
            self._deviceItemMap[device.deviceId] = item
            menu = views.DeviceActionMenuGraphicsItem(item)
            menu.setPos(QtCore.QPointF(154, 39))
            position = QtCore.QPointF(x[device.deviceId], [device.deviceId])
            item.setPos(position)
            item.setZValue(1.0)
            scene.addItem(item)
