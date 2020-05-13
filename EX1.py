from PySide2.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layoutV=QVBoxLayout()
        self.obj1=QLabel("Ceci est un QLabel")
        self.obj2=QPushButton("Ceci est un QPushButton")
        self.layoutV.addWidget(self.obj1)
        self.layoutV.addWidget(self.obj2)
        self.setLayout(self.layoutV)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
