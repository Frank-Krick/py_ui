import DeviceGraphModel
import itk


class Model:
    def __init__(self):
        self._deviceGraph = itk.DeviceGraph()
        self._create_device_list()
        self._test_setup()
        self._deviceGraphModel = DeviceGraphModel.DeviceGraphModel(self._deviceGraph)

    def device_list(self):
        return self._deviceList

    def device_graph_graphics_scene(self):
        return self._deviceGraphModel.device_graph_graphics_scene()

    def _test_setup(self):
        audio_device_ids = [
            self._deviceGraph.add_device(self._audioDevices[0]),
            self._deviceGraph.add_device(self._audioDevices[0]),
            self._deviceGraph.add_device(self._audioDevices[0]),
            self._deviceGraph.add_device(self._audioDevices[0]),
        ]
        control_device_ids = []
        self._deviceGraph.connect(audio_device_ids[0], audio_device_ids[1])
        self._deviceGraph.connect(audio_device_ids[2], audio_device_ids[3])
        self._deviceGraph.connect(audio_device_ids[0], audio_device_ids[3])
        #self._deviceGraph.connect(control_device_ids[1], audio_device_ids[1], 0)

    def _create_device_list(self):
        device_registry = itk.DeviceRegistry()
        self._deviceList = device_registry.registeredDevices()
        self._audioDevices = [device for device in self._deviceList if device.deviceType == itk.DeviceType.Audio]
        self._controlDevices = [device for device in self._deviceList if device.deviceType == itk.DeviceType.Control]
