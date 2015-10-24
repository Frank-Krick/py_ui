from PyQt4.QtCore import Qt
from PyQt4 import QtGui
from PyQt4 import QtCore

from TimeSeriesView import TimeSeriesView
import model


class DeviceGraphInspectorView(QtGui.QWidget):
    def __init__(self, device_graph_controller, device_graph_model):
        QtGui.QWidget.__init__(self)
        group_box = QtGui.QGroupBox(self)
        layout = QtGui.QVBoxLayout()
        group_box.setLayout(layout)
        self._inspectedDeviceComboBox = None
        self._deviceGraphController = device_graph_controller
        self._deviceGraphModel = device_graph_model
        self._parameterTableModel = model.ParameterTableModel(self._deviceGraphModel)
        self._deviceGraphController.parameterTableModel = self._parameterTableModel
        self._create_device_selector(layout)
        self._create_parameter_table(layout)
        self._connect_signals()

    def _connect_signals(self):
        self.connect(self._deviceGraphController,
                     QtCore.SIGNAL('deviceHasBeenAdded'),
                     self._add_device)
        self.connect(self._deviceGraphController,
                     QtCore.SIGNAL('selectedDeviceChanged'),
                     self._selected_device_changed)
        self.connect(self._inspectedDeviceComboBox,
                     QtCore.SIGNAL('currentIndexChanged(int)'),
                     self._inspected_device_current_index_changed)

    def _inspected_device_current_index_changed(self, index):
        device_id = self._inspectedDeviceComboBox.itemData(index)
        self._deviceGraphController.select_device(device_id.toInt()[0])

    def _create_device_selector(self, group_box_layout):
        label = QtGui.QLabel('Device')
        self._inspectedDeviceComboBox = QtGui.QComboBox()
        layout = QtGui.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self._inspectedDeviceComboBox)
        group_box_layout.addLayout(layout)
        for device in self._deviceGraphModel.devices:
            self._add_device(device)

    def _create_parameter_table(self, group_box_layout):
        table = QtGui.QTableView()
        table.setModel(self._parameterTableModel)
        group_box_layout.addWidget(table)

    def _add_device(self, device):
        self._inspectedDeviceComboBox.addItem(device.device.name, device.item.deviceId)

    def _selected_device_changed(self, device_item):
        index = self._find_device_in_combo_box(device_item)
        self._inspectedDeviceComboBox.setCurrentIndex(index)

    def _find_device_in_combo_box(self, device_item):
        device_ids = [self._inspectedDeviceComboBox.itemData(i) for i in range(0, self._inspectedDeviceComboBox.count())]
        index = 0
        for device_id in device_ids:
            if device_id.toInt()[0] is device_item.device.deviceId:
                return index
            index += 1
        return None
