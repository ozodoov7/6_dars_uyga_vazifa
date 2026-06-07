from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
)

from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("Background-color: #AABCAA")
        self.hbox=QHBoxLayout()
        self.vbox=QVBoxLayout()

        self.setWindowTitle('QHBoxLayout va QLabel Misoli')
        self.setGeometry(300, 300, 400, 150)
        
        self.btn1=QPushButton("Chapga")
        self.btn2=QPushButton("Ortga")
        self.btn3=QPushButton("O'ngga")

        self.btn1.setStyleSheet("Background-color: #777777; color: #CCCCCC")
        self.btn2.setStyleSheet("Background-color: #777777; color: #CCCCCC")
        self.btn3.setStyleSheet("Background-color: #777777; color: #CCCCCC")
        
        self.btn1.clicked.connect(self.func)
        self.btn2.clicked.connect(self.func)
        self.btn3.clicked.connect(self.func)

        self.label=QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-top: 15px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.btn_layout=QHBoxLayout()
        self.btn_layout.addWidget(self.btn1)
        self.btn_layout.addWidget(self.btn2)
        self.btn_layout.addWidget(self.btn3)
        
        self.vbox.addLayout(self.btn_layout)
        self.vbox.addWidget(self.label)

        self.setLayout(self.vbox)


    def func(self):
        a=self.sender()
        self.label.setText(a.text())

    
app=QApplication([])
win=App()
win.show()
app.exec_()