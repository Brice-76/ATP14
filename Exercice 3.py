from PySide2.QtWidgets import QWidget,QVBoxLayout,QApplication,QBoxLayout, QGridLayout,QLabel, QPushButton,QTextEdit,QHBoxLayout,QProgressBar,QLineEdit
from PySide2 import QtGui
from PySide2 import QtCore


class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle('GUI')
        self.setWindowIcon(QtGui.QIcon('/Users/brice/PycharmProjects/ATP14/fr-flag.png'))
        self.label=QLabel('Hello World')
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout=QVBoxLayout()
        self.barre_chargement=QProgressBar()
        self.barre_chargement.setValue(30)
        self.line=QLineEdit()
        self.button=QPushButton('Push Me')
        self.button.setIcon(QtGui.QIcon('/Users/brice/PycharmProjects/ATP14/fr-flag.png'))
        self.button.setToolTip(('SALUT'))
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre_chargement)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)





if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
