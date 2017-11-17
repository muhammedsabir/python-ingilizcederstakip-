from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class Course(QMainWindow):
      def __init__(self,ebeveyn_None):
          QWidget.__init__(self,ebeveyn)
          self.ui=uic.loadUi('course.ui',self)

uyg=QApplication([])
pencere = Course()
pencere.show()
uyg.exec_()
