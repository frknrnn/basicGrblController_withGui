import sys
from main_functions import AppFunctions
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppFunctions()
    window.show()
    sys.exit(app.exec_())