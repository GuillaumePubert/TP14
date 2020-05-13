from PySide2.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layoutV=QGridLayout()
        self.obj1=QLabel("Laissez un commentaire")
        self.obj2=QTextEdit("")
        self.button1=QPushButton("Success")
        self.button2=QPushButton("Cancel")
        self.layoutV.addWidget(self.obj1)
        self.layoutV.addWidget(self.obj2)
        self.layoutV.addWidget(self.button1)
        self.layoutV.addWidget(self.button2)
        self.setLayout(self.layoutV)
        self.setWindowTitle("Le titre")

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   win.show()
   app.exec_()
