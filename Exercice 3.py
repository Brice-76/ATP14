from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout, QGridLayout,QLabel, QPushButton,QTextEdit,QHBoxLayout


class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle('IMH')

