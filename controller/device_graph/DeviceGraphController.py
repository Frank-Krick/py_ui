import views


class DeviceGraphController:
    def __init__(self, model, device_graph_scene):
        self._deviceGraphModel = model.deviceGraphModel
        self._model = model
        self._deviceGraphScene = device_graph_scene
        self._addConnectionMode = False
        device_graph_scene.deviceGraphController = self
        model.deviceGraphModel.deviceGraphController = self
        model.deviceGraphModel.deviceGraphScene = device_graph_scene

    def add_device(self, device_index, position):
        device = self._model.device(device_index)
        device_id = self._deviceGraphModel.add_device(device)
        item = views.DeviceGraphicsItem(device_id, device, self, self._deviceGraphScene)
        item.setPos(position)
        self._deviceGraphScene.addItem(item)

    def connect(self, source, target, parameter=None):
        self._deviceGraphModel.connect(source, target, parameter)
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
