from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout, QGridLayout,QLabel, QPushButton,QTextEdit

class Window(QWidget) :
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('IHM')
        layout=QGridLayout()
        label=QLabel('Laisser un commentaire')
        button_1=QPushButton('Succes')
        button_2=QPushButton('Cancel')
        textEdit=QTextEdit()
        layout.addWidget(label)
        layout.addWidget(textEdit)
        layout.addWidget(button_1)
        layout.addWidget(button_2)


