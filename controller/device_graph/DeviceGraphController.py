import views


class DeviceGraphController:
    def __init__(self, model, device_graph_scene):
        self._deviceGraphModel = model.deviceGraphModel
        self._model = model
        self._deviceGraphScene = device_graph_scene

    def add_device(self, device_index, position):
        device = self._model.device(device_index)
        item = views.DeviceGraphicsItem(device)
        item.setPos(position)
        self._deviceGraphScene.addItem(item)
        self._deviceGraphModel.add_device(device)
