from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import views


class DeviceGraphEditor(QtGui.QWidget):
    def __init__(self, itk):
        super(DeviceGraphEditor, self).__init__()
        self.deviceTableSplitter = QtGui.QSplitter(Qt.Horizontal)
        self.deviceTable = QtGui.QTableView()
        self.deviceGraph = QtGui.QGraphicsView()
        self.setup(itk)

    def setup(self, itk):
        self._setup_splitter()
        self._setup_device_table(itk)
        self._setup_device_graph(itk)

    def _setup_splitter(self):
        self.deviceTableSplitter.addWidget(self.deviceTable)
        self.deviceTableSplitter.addWidget(self.deviceGraph)
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
        layout.addWidget(self.deviceTableSplitter)
        self.setLayout(layout)

    def _setup_device_table(self, itk):
        device_table_model = views.DeviceTableModel(itk)
        self.deviceTable.setModel(device_table_model)

    def _setup_device_graph(self, itk):
        self.deviceGraph.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.deviceGraph.setRenderHint(QtGui.QPainter.Antialiasing)
        self.deviceGraph.setRenderHint(QtGui.QPainter.TextAntialiasing)
        scene = itk.device_graph_graphics_scene(0)
        self.deviceGraph.setScene(scene)
