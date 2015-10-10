from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import itk


class Device:
    def __init__(self, name, description, device_type, id):
        self.name = name
        self.description = description
        self.deviceType = device_type
        self._id = id


class Model:
    def __init__(self):
        self._create_device_list()

    def device_list(self):
        return self._deviceList

    def device_graph_graphics_scene(self, device_graph_index):
        scene = QtGui.QGraphicsScene()
        scene.addRect(0, 0, 300, 300)
        return scene

    def _create_device_list(self):
        device_registry = itk.DeviceRegistry()
        self._deviceList = device_registry.registeredDevices()
