import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

import views
import model
import controller


itk = model.Model()


def main():
    application = QtGui.QApplication(sys.argv)
    window = views.MainWindow(itk)
    window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
