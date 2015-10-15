from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

import math
import random
import views


class DeviceGraphScene(QtGui.QGraphicsScene):
    def __init__(self, graph_model):
        QtGui.QGraphicsScene.__init__(self)
        self._graphModel = graph_model
