import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QGridLayout
from PyQt5.QtWidgets import QPushButton,QSizePolicy,QLineEdit

class Calculator(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calc')
        self.setFixedSize(300,300)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        # Display #
        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: #FFF; color: 000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)
        self.add_bt(QPushButton('7'),1,0,1,1)
        self.add_bt(QPushButton('8'), 1, 1, 1, 1)
        self.add_bt(QPushButton('9'), 1, 2, 1, 1)
        self.add_bt(QPushButton('+'), 1, 3, 1, 1)
        self.add_bt(QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
        'background: #d5580d; color: #FFF; font-weight: 800'
                    )

        self.add_bt(QPushButton('4'), 2, 0, 1, 1)
        self.add_bt(QPushButton('5'), 2, 1, 1, 1)
        self.add_bt(QPushButton('6'), 2, 2, 1, 1)
        self.add_bt(QPushButton('-'), 2, 3, 1, 1)
        self.add_bt(QPushButton('Del'), 2, 4, 1, 1,
        lambda: self.display.setText(self.display.text()[:-1]),
                    'background: green; color: #FFF; font-weight: 800'
                    )

        self.add_bt(QPushButton('1'), 3, 0, 1, 1)
        self.add_bt(QPushButton('2'), 3, 1, 1, 1)
        self.add_bt(QPushButton('3'), 3, 2, 1, 1)
        self.add_bt(QPushButton('/'), 3, 3, 1, 1)
        self.add_bt(QPushButton(''), 3, 4, 1, 1)

        self.add_bt(QPushButton('0'), 4, 0, 1, 1)
        self.add_bt(QPushButton('.'), 4, 1, 1, 1)
        self.add_bt(QPushButton(''), 4, 2, 1, 1)
        self.add_bt(QPushButton('*'), 4, 3, 1, 1)
        self.add_bt(QPushButton('='), 4, 4, 1, 1,
        self.equal,
                    'background: blue; color: #FFF; font-weight: 800'
                    )

        self.setCentralWidget(self.cw)

        # create a button #
    def add_bt(self,bt,row,col,rowspan,colspan,func = None,style = None):
        self.grid.addWidget(bt,row,col,rowspan,colspan)
        if not func:
            bt.clicked.connect(
                lambda: self.display.setText(
                    self.display.text()+bt.text()
                )
            )
        else:
            bt.clicked.connect(func)
        bt.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if style:
            bt.setStyleSheet(style)


    def equal(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Conta Inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()