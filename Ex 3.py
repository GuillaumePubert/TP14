from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2 import QtCore
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle("IHM")
        self.layoutV=QVBoxLayout()
        self.icon=QtGui.QIcon('C:/Users/guill/Documents/Python/fr-flag.png')
        self.setWindowIcon(self.icon)
        self.label=QLabel("Hello world")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.barre=QProgressBar()
        self.barre.setValue(50)
        self.ligne=QLineEdit("")
        self.bouton=QPushButton("Click me !")
        self.bouton.setToolTip("hello")
        self.layoutV.addWidget(self.label)
        self.layoutV.addWidget(self.barre)
        self.layoutV.addWidget(self.ligne)
        self.layoutV.addWidget(self.bouton)
        self.setLayout(self.layoutV)
if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   win.show()
   app.exec_()
