from model.device_graph import DeviceGraphModel
import itk


class Model:
    def __init__(self):
        self._create_device_list()
        device_graph = itk.DeviceGraph()
        self.deviceGraphModel = DeviceGraphModel.DeviceGraphModel(device_graph)

    def device_list(self):
        return self._deviceList

    def device(self, device_index):
        return self._deviceList[device_index]

    def device_graph_graphics_scene(self):
        return self.deviceGraphModel.device_graph_graphics_scene()

    def _test_setup(self):
        audio_device_ids = [
            self.deviceGraphModel.add_device(self._audioDevices[0]),
            self.deviceGraphModel.add_device(self._audioDevices[0]),
            self.deviceGraphModel.add_device(self._audioDevices[0]),
            self.deviceGraphModel.add_device(self._audioDevices[0]),
        ]
        control_device_ids = [
            self.deviceGraphModel.add_device(self._controlDevices[0]),
            self.deviceGraphModel.add_device(self._controlDevices[0]),
        ]
        self.deviceGraphModel.connect_devices(audio_device_ids[0], audio_device_ids[1])
        self.deviceGraphModel.connect_devices(audio_device_ids[2], audio_device_ids[3])
        self.deviceGraphModel.connect_devices(audio_device_ids[0], audio_device_ids[3])
        self.deviceGraphModel.connect_devices(audio_device_ids[1], audio_device_ids[2])
        self.deviceGraphModel.connect_devices(control_device_ids[0], audio_device_ids[1], 0)
        self.deviceGraphModel.connect_devices(control_device_ids[1], audio_device_ids[2], 0)

    def _create_device_list(self):
        device_registry = itk.DeviceRegistry()
        self._deviceList = device_registry.registeredDevices
        self._audioDevices = [device for device in self._deviceList if device.deviceType == itk.DeviceType.Audio]
        self._controlDevices = [device for device in self._deviceList if device.deviceType == itk.DeviceType.Control]
