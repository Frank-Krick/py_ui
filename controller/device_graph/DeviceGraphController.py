from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import views
import utility


class DeviceGraphController(QtCore.QObject):
    def __init__(self, model, device_graph_scene):
        QtCore.QObject.__init__(self)
        self._deviceGraphModel = model.deviceGraphModel
        self._model = model
        self._deviceGraphScene = device_graph_scene
        self._addConnectionMode = False
        self._selectedDeviceId = None
        device_graph_scene.deviceGraphController = self
        model.deviceGraphModel.deviceGraphController = self
        model.deviceGraphModel.deviceGraphScene = device_graph_scene
        self.parameterTableModel = None

    def add_device(self, device_index, position):
        device = self._model.device(device_index)
        device_id = self._deviceGraphModel.add_device(device)
        item = views.DeviceGraphicsItem(device_id, device, self, self._deviceGraphScene)
        item.setPos(position)
        self._deviceGraphScene.addItem(item)
        self.emit(QtCore.SIGNAL('deviceHasBeenAdded'), utility.DeviceItem(item, device))

    def connect_devices(self, source, target, parameter=None):
        self._deviceGraphModel.connect_devices(source, target, parameter)
        if parameter is None:
            connection = views.ConnectionGraphicsItem(
                source, target, self._deviceGraphModel, views.ConnectionType.Audio)
            self._deviceGraphScene.addItem(connection)
            self._deviceGraphScene.device_item(source).add_connection(connection)
            self._deviceGraphScene.device_item(target).add_connection(connection)
        else:
            connection = views.ConnectionGraphicsItem(
                source, target, self._deviceGraphModel, views.ConnectionType.Control)
            self._deviceGraphScene.addItem(connection)
            self._deviceGraphScene.device_item(source).add_connection(connection)
            self._deviceGraphScene.device_item(target).add_connection(connection)

    def start_add_connection(self, position, source_device_id):
        self._deviceGraphScene.start_add_connection(position, source_device_id)

    def select_device(self, device_id):
        if self._selectedDeviceId is not device_id:
            self._deviceGraphScene.select_inspected_item(device_id)
            self._selectedDeviceId = device_id
            device = self._deviceGraphModel.device(device_id)
            if self.parameterTableModel is not None:
                self.parameterTableModel.select_device(device_id)
            self.emit(QtCore.SIGNAL('selectedDeviceChanged'), device)
