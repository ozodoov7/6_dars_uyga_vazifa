from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #AAAAAA")
        self.vbox=QVBoxLayout()

        self.btn1=QPushButton("bir")
        self.btn2=QPushButton("ikki")
        self.btn3=QPushButton("uch")

        self.btn1.clicked.connect(self.func1)
        self.btn2.clicked.connect(self.func2)
        self.btn3.clicked.connect(self.func3)

        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)

        self.setLayout(self.vbox)

        self.show()        
    def func1(self):
        print(f"{self.btn1.text()}")
    
    def func2(self):
        print(f"{self.btn2.text()}")
    
    def func3(self):
        print(f"{self.btn3.text()}")
        

app=QApplication([])
window=App()
app.exec_()
