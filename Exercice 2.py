from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout, QGridLayout,QLabel, QPushButton,QTextEdit,QHBoxLayout

class Window(QWidget) :
    def __init__(self):
        Window.__init__(self)
        self.setWindowTitle('IHM')
        layout=QGridLayout()

        label=QLabel('Laisser un commentaire')
        button_1=QPushButton('Succes')
        button_2=QPushButton('Cancel')
        textEdit=QTextEdit()
        layout.addWidget(label,0,0,1,0,allignement=0)
        layout.addWidget(textEdit,1,1)
        layout.addWidget(button_1,3,0)
        layout.addWidget(button_2,3,1)


        self.setLayout(layout)



if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
