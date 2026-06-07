from PyQt5.QtWidgets import (
    QApplication, QWidget, QComboBox, QLabel, QVBoxLayout 
)

from PyQt5.QtCore import Qt

class Language_picker(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox=QVBoxLayout()
        self.setGeometry(500, 400, 300, 200)

        self.dir=QComboBox()
        self.dir.addItems(["Python", "C++", "Java"])
        self.dir.setFixedSize(250,30)
        self.dir.setStyleSheet("font-size: 28px; font-family: Calibri;")
        self.dir.currentTextChanged.connect(self.show_chosen)
        self.vbox.addWidget(self.dir)

        self.label=QLabel("Tanlangan til: Python")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 28px; font-weight: bold; color: #2e7d32; margin-top: 15px;")

        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    def show_chosen(self, a):
        self.label.setText(f"Tanlangan til: {a}")

app=QApplication([])
win=Language_picker()
win.show()
app.exec_()