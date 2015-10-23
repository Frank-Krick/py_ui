from PyQt4.QtCore import Qt
from PyQt4 import QtGui
from PyQt4 import QtCore

import math


class TimeSeriesView(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self._padding = 10
        self._data = []
        self._stepWidth = 0
        self._test_data()
        self._update_parameter()
        self.setSizePolicy(
            QtGui.QSizePolicy(
                QtGui.QSizePolicy.MinimumExpanding,
                QtGui.QSizePolicy.Fixed))

    def sizeHint(self):
        return self.maximumWidth()

    def minimumSizeHint(self):
        return QtCore.QSize(300, 200)

    def paintEvent(self, event):
        QtGui.QWidget.paintEvent(self, event)
        painter = QtGui.QPainter()
        painter.begin(self)
        width = self.width()
        height = self.height()
        color = QtGui.QColor(Qt.black)
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        painter.drawRect(0, 0, width, height)
        color = QtGui.QColor(Qt.blue)
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        self._draw_data(painter)
        painter.setPen(Qt.lightGray)
        middle = height / 2
        painter.drawLine(0, middle, width, middle)
        painter.end()

    def resizeEvent(self, event):
        QtGui.QWidget.resizeEvent(self, event)
        self._update_parameter()

    def _update_parameter(self):
        self._stepWidth = self._calculate_step_width()

    def _draw_data(self, painter):
        painter.setPen(Qt.blue)
        x = self._padding
        y_start = self.height() / 2
        y_delta_max = (self.height() - self._padding * 2) / 2
        for sample in self._data:
            y = y_start + y_delta_max * sample
            painter.drawLine(x, y_start, x, y)
            x += self._stepWidth

    def _calculate_step_width(self):
        number_of_samples = len(self._data)
        if number_of_samples is not 0:
            return (self.width() - 2.0 * self._padding) / number_of_samples
        else:
            return 0

    def _test_data(self):
        for i in range(0, 55):
            self._data.append(math.sin(i))
