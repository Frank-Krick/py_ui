from PyQt4.QtCore import Qt
from PyQt4 import QtGui

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
        self._deviceList = [
            Device('Device 0', 'Test Device 1', 'Audio', 0),
            Device('Device 1', 'Test Device 2', 'Control', 1),
            Device('Device 2', 'Test Device 3', 'Audio', 2),
            Device('Device 3', 'Test Device 4', 'Audio', 3),
            Device('Device 4', 'Test Device 5', 'Control', 4)
        ]
