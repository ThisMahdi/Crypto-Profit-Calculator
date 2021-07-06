# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

# Imports Here
from PyQt5.QtWidgets import QApplication, QMessageBox,QMainWindow
from PyQt5.QtGui import QDoubleValidator
from PyQt5 import QtGui
from PyQt5 import uic
import sys



__version__ = "1"
__author__ = "Mahdi Yaghoubi"

class ProfitCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui.ui', self)
        self.setWindowTitle("Crypto Profit Calculator")
        self.setFixedWidth(429)
        self.setFixedHeight(584)
        self.calculate.clicked.connect(self.check)
        # create validator to force user enter numbers
        self.onlyint = QDoubleValidator()
        self.purchase.setValidator(self.onlyint)
        self.sale.setValidator(self.onlyint)
        self.property.setValidator(self.onlyint)
        link = "<a style='text-decoration: none; color:white;' href='https://github.com/ThisMahdi/'>By Mahdi Yaghoubi</a>"
        self.mahdi.setText(link)
        self.setWindowIcon(QtGui.QIcon("logo/logo.png"))


    def check(self):
        purchase = self.purchase.text()
        sale = self.sale.text()
        property = self.property.text()
        if purchase == "":
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Enter Your Purchase Price.")
            msg.setWindowIcon(QtGui.QIcon("logo/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            # showing msg box
            x = msg.exec_()
        elif sale == "":
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Enter Your Sale Price.")
            msg.setWindowIcon(QtGui.QIcon("logo/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            # showing msg box
            x = msg.exec_()
        elif property == "":
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Enter Your Property In Dollar$.")
            msg.setWindowIcon(QtGui.QIcon("logo/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            # showing msg box
            x = msg.exec_()
        else:
            self.calculator()


    def calculator(self):
        purchase = self.purchase.text()
        sale = self.sale.text()
        property = self.property.text()
        profit1 = float(sale)/float(purchase)
        profit2 = (profit1*float(property))-float(property)
        fixed = format(profit2, '.2f')
        self.profit.setText(f"{fixed} $")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfitCalculator()
    window.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing app...")
        
# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
