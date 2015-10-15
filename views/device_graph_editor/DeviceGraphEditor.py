from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import views
import controller


class DeviceGraphEditor(QtGui.QWidget):
    def __init__(self, itk):
        super(DeviceGraphEditor, self).__init__()
        scene = itk.device_graph_graphics_scene()
        self.deviceTableSplitter = QtGui.QSplitter(Qt.Horizontal)
        self.deviceTable = views.DeviceTableView()
        device_graph_controller = controller.DeviceGraphController(itk, scene)
        self.deviceGraph = views.DeviceGraphView(device_graph_controller)
        self.setup(itk, scene)

    def setup(self, itk, scene):
        self._setup_splitter()
        self._setup_device_table(itk)
        self._setup_device_graph(scene)

    def _setup_splitter(self):
        self.deviceTableSplitter.addWidget(self.deviceTable)
        self.deviceTableSplitter.addWidget(self.deviceGraph)
        self.deviceTableSplitter.setSizes([300, 700])
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
        layout.addWidget(self.deviceTableSplitter)
        self.setLayout(layout)

    def _setup_device_table(self, itk):
        device_table_model = views.DeviceTableModel(itk)
        self.deviceTable.setModel(device_table_model)
        self.deviceTable.resizeRowsToContents()

    def _setup_device_graph(self, scene):
        self.deviceGraph.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.deviceGraph.setRenderHint(QtGui.QPainter.Antialiasing)
        self.deviceGraph.setRenderHint(QtGui.QPainter.TextAntialiasing)
        self.deviceGraph.setScene(scene)
