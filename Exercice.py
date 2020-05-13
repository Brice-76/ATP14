from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout


class Window(QWidget) :
    def __init__(self):
        Window.__init__(self)
        layout=QVBoxLayout()
        for i in range (0,10) :
            k=QWidget()
            layout.addWidget(k)
        self.setLayout(layout)








if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
