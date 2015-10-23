from PyQt4.QtCore import Qt
from PyQt4 import QtGui

from DeviceGraphInspectorView import DeviceGraphInspectorView
from FrequencyDomainView import FrequencyDomainView


class ToolBoxView(QtGui.QWidget):
    def __init__(self, device_graph_controller, device_graph_model):
        QtGui.QWidget.__init__(self)
        self._deviceGraphInspector = DeviceGraphInspectorView(device_graph_controller, device_graph_model)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self._deviceGraphInspector)
        self.setLayout(layout)
