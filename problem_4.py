from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QComboBox, 
    QVBoxLayout, QHBoxLayout
)

from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 150)
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.input=QLineEdit()
        self.input.setAlignment(Qt.AlignHCenter)
        self.input.setPlaceholderText("....")
        self.hbox.addWidget(self.input)

        self.btn=QPushButton("+")
        self.btn.clicked.connect(self.func)
        self.hbox.addWidget(self.btn)
        self.vbox.addLayout(self.hbox)
        self.combo=QComboBox()
        self.combo.setStyleSheet("Background-color: #888888; color: black")
        self.vbox.addWidget(self.combo)
        self.setLayout(self.vbox)

    def func(self):
        a=self.input.text()
        self.combo.addItem(a)


app=QApplication([])
win=App()
win.show()
app.exec_()