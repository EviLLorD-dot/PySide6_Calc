import sys
import math

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_calc import Ui_w_calc

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_w_calc()
        self.ui.setupUi(self)
        self.press()

    # Pressed btn
    def press(self):
        # Numbers
        self.ui.btn_0.clicked.connect(lambda: self.click(input_el="0"))
        self.ui.btn_1.clicked.connect(lambda: self.click(input_el="1"))
        self.ui.btn_2.clicked.connect(lambda: self.click(input_el='2'))
        self.ui.btn_3.clicked.connect(lambda: self.click(input_el='3'))
        self.ui.btn_4.clicked.connect(lambda: self.click(input_el='4'))
        self.ui.btn_5.clicked.connect(lambda: self.click(input_el='5'))
        self.ui.btn_6.clicked.connect(lambda: self.click(input_el='6'))
        self.ui.btn_7.clicked.connect(lambda: self.click(input_el='7'))
        self.ui.btn_8.clicked.connect(lambda: self.click(input_el='8'))
        self.ui.btn_9.clicked.connect(lambda: self.click(input_el='9'))
        self.ui.btn_dot.clicked.connect(lambda: self.click(input_el='.'))

        # Operations
        self.ui.btn_add.clicked.connect(lambda: self.click(input_el=' + '))
        self.ui.btn_sub.clicked.connect(lambda: self.click(input_el=' - '))
        self.ui.btn_mul.clicked.connect(lambda: self.click(input_el=' * '))
        self.ui.btn_div.clicked.connect(lambda: self.click(input_el=' / '))

        self.ui.btn_clear.clicked.connect(lambda: self.clear())
        self.ui.btn_rmlst.clicked.connect(lambda: self.rmv_lst())

        # Equals
        self.ui.btn_squar.clicked.connect(lambda: self.square())
        self.ui.btn_sqrt.clicked.connect(lambda: self.sqrt())


        self.ui.btn_equ.clicked.connect(lambda: self.equals())

    #show from display
    def click(self, input_el="0"):
        self.display(input_el)

    def display(self, output_text="0"):
        old_text = self.ui.l_display.text()

        if old_text == "0":
            old_text = ""

        output_text = old_text + output_text
        self.ui.l_display.setText(output_text)

    def clear(self):
        self.ui.l_display.setText("0")

    def rmv_lst(self):
        text = self.ui.l_display.text()[:-1]

        if text == "":
            text = "0"

        self.ui.l_display.setText(text)

    #solution
    def equals(self):
        input_text = self.ui.l_display.text()
        output_text = eval(input_text)
        self.ui.l_display.setText(str(output_text))

    def square(self):
        input_text = self.ui.l_display.text()
        if not ('+' or '-' or '*' or '/') in input_text:
            self.ui.l_display.setText(str(math.pow(float(input_text), 2)))

    def sqrt(self):
        input_text = self.ui.l_display.text()
        if not ('+' or '-' or '*' or '/') in input_text:
            self.ui.l_display.setText(str(math.sqrt(float(input_text))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

