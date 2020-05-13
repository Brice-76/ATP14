from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout, QGridLayout,QLabel, QPushButton,QTextEdit,QHBoxLayout,QProgressBar,QLineEdit
from PySide2 import QtGui
from PySide2 import QtCore


class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle('IMH')
        icon=QtGui.QIcon('../fr-flag.png')
        self.setWindowIcon(icon)
        label=QLabel('Hello World')
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout=QVBoxLayout()
        barre_chargement=QProgressBar()
        barre_chargement.setValue(30)
        line=QLineEdit()
        button=QPushButton('push_me')
        label.setToolTip(('SALUT'))
        layout.addWidget(label)
        layout.addWidget(barre_chargement)
        layout.addWidget(line)
        layout.addWidget(button)
        self.setLayout(layout)





if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
