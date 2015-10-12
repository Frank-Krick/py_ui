from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

import itk

import views


class Model:
    def __init__(self):
        self._deviceGraph = itk.DeviceGraph()
        self._create_device_list()
        self._deviceGraph.add_device(self._deviceList[2])
        self._deviceGraph.add_device(self._deviceList[1])
        self._deviceGraph.add_device(self._deviceList[5])
        self._deviceGraph.add_device(self._deviceList[6])
        self._deviceGraph.add_device(self._deviceList[0])

    def device_list(self):
        return self._deviceList

    def device_graph_graphics_scene(self):
        scene = QtGui.QGraphicsScene()
        self._add_devices_to_scene(self._deviceGraph, scene)
        brush = QtGui.QBrush(Qt.black)
        scene.setBackgroundBrush(brush)
        return scene

    def _create_device_list(self):
        device_registry = itk.DeviceRegistry()
        self._deviceList = device_registry.registeredDevices()

    def _add_devices_to_scene(self, device_graph, scene):
        x = 0
        y = 0
        width = 200.0
        height = 125.0
        padding = 5
        for device in device_graph.devices:
            item = views.DeviceGraphicsItem(device)
            menu = views.DeviceActionMenuGraphicsItem(item)
            menu.setPos(QtCore.QPointF(154, 39))
            position = QtCore.QPointF(x, y)
            item.setPos(position)
            scene.addItem(item)
            y = y + height + padding
