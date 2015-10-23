from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

import itk


class ParameterTableModel(QtCore.QAbstractTableModel):
    def __init__(self, device_graph_model):
        QtCore.QAbstractTableModel.__init__(self)
        self._columnHeaders = ['Parameter', 'Value']
        self._selectedDeviceId = None
        self._deviceGraphModel = device_graph_model
        self._availableParameters = None

    def select_device(self, device_id):
        self._selectedDeviceId = device_id
        self._availableParameters = self._deviceGraphModel.device(device_id).device.device.availableParameters
        self.reset()

    def rowCount(self, parent=QtCore.QModelIndex(), *args, **kwargs):
        if self._availableParameters is not None:
            return len(self._availableParameters)
        return 0

    def columnCount(self, parent=QtCore.QModelIndex(), *args, **kwargs):
        return len(self._columnHeaders)

    def data(self, index, role=None):
        if role == Qt.DecorationRole:
            return QtCore.QVariant()
        elif role != Qt.DisplayRole:
            return QtCore.QVariant()
        elif (not index.isValid()) or index.row() < 0 or index.row() >= len(self._availableParameters):
            return QtCore.QVariant()
        else:
            parameter = self._availableParameters[index.row()]
            if index.column() is 0:
                return QtCore.QVariant(parameter.name)
            elif index.column() is 1:
                device_id = self._selectedDeviceId
                parameter_id = parameter.id
                return self._deviceGraphModel.parameter_value(device_id, parameter_id)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole and orientation == Qt.Horizontal:
            return QtCore.QVariant(int(Qt.AlignLeft | Qt.AlignVCenter))
        elif role == Qt.TextAlignmentRole and orientation == Qt.Vertical:
            return QtCore.QVariant(int(Qt.AlignRight | Qt.AlignVCenter))
        elif role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._columnHeaders[section]
        elif role == Qt.DisplayRole and orientation == Qt.Vertical:
            return QtCore.QVariant(int(section + 1))
        return QtCore.QVariant()

    def flags(self, index):
        if index.column() is 1:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsEnabled

    def setData(self, index, variant, role=None):
        if index.column() is 1:
            value = variant.toDouble()
            if value[1] is True:
                parameter = self._availableParameters[index.row()]
                device_id = self._selectedDeviceId
                parameter_id = parameter.id
                self._deviceGraphModel.parameter_value(device_id, parameter_id, value[0])
                self.dataChanged.emit(index, index)
        return False

