from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from model import Model
import itk


class DeviceTableModel(QtCore.QAbstractTableModel):
    def __init__(self, itk):
        super(DeviceTableModel, self).__init__()
        self.columnHeaders = ['Device']
        self.devices = itk.device_list()
        self._controlDeviceIcon = QtGui.QImage("resources/device_table_icons/control_device.png")
        self._audioDeviceIcon = QtGui.QImage("resources/device_table_icons/audio_device.png")

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DecorationRole:
            device = self.devices[index.row()]
            if device.deviceType == itk.DeviceType.Audio:
                return QtCore.QVariant(self._audioDeviceIcon)
            elif device.deviceType == itk.DeviceType.Control:
                return QtCore.QVariant(self._controlDeviceIcon)
        elif role == Qt.SizeHintRole:
            return QtCore.QVariant(QtCore.QSize(0, 100))
        elif role != Qt.DisplayRole:
            return QtCore.QVariant()
        elif (not index.isValid()) or index.row() < 0 or index.row() >= len(self.devices):
            return QtCore.QVariant()
        else:
            device = self.devices[index.row()]
            if index.column() == 0:
                return QtCore.QVariant(device.name)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole and orientation == Qt.Horizontal:
            return QtCore.QVariant(int(Qt.AlignLeft | Qt.AlignVCenter))
        elif role == Qt.TextAlignmentRole and orientation == Qt.Vertical:
            return QtCore.QVariant(int(Qt.AlignRight | Qt.AlignVCenter))
        elif role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.columnHeaders[section]
        elif role == Qt.DisplayRole and orientation == Qt.Vertical:
            return QtCore.QVariant(int(section + 1))
        elif role == Qt.SizeHintRole and orientation == Qt.Horizontal:
            if section == 0:
                return QtCore.QVariant(QtCore.QSize(0, 50))
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex(), *args, **kwargs):
        return len(self.devices)

    def columnCount(self, parent=QtCore.QModelIndex(), *args, **kwargs):
        return len(self.columnHeaders)
