from PyQt4 import QtCore
from PyQt4 import QtGui
# generated with pyuic4 mainwindow.ui -o ui_mainwindow.py
from ui_mainwindow import Ui_MainWindow
# generated with pyrcc4 -o resources_rc.py resources.qrc
#import resources_rc
from database import RpiControlDB

class MainWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        #uic.loadUi(os.path.dirname(os.path.realpath(__file__))+'/mainwindow.ui', self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # connect signals to slots
        self.connect(self.ui.buttonBack, QtCore.SIGNAL("clicked(bool)"), self.switchToMain)
        # main
        self.connect(self.ui.buttonDrinks, QtCore.SIGNAL("clicked(bool)"), self.switchToUsers)
        # radio
        # users
        self.connect(self.ui.buttonUser1, QtCore.SIGNAL("clicked(bool)"), self.handleUser1)
        # drinks
        self.connect(self.ui.buttonPay, QtCore.SIGNAL("clicked(bool)"), self.switchToPayment)
        # payment
        self.connect(self.ui.buttonNum0, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad0)
        self.connect(self.ui.buttonNum1, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad1)
        self.connect(self.ui.buttonNum2, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad2)
        self.connect(self.ui.buttonNum3, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad3)
        self.connect(self.ui.buttonNum4, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad4)
        self.connect(self.ui.buttonNum5, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad5)
        self.connect(self.ui.buttonNum6, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad6)
        self.connect(self.ui.buttonNum7, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad7)
        self.connect(self.ui.buttonNum8, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad8)
        self.connect(self.ui.buttonNum9, QtCore.SIGNAL("clicked(bool)"), self.paymentNumPad9)
        self.connect(self.ui.buttonNumDel, QtCore.SIGNAL("clicked(bool)"), self.paymentNumDel)

    def switchToMain(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.buttonBack.setEnabled(False)

    def switchToUsers(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.buttonBack.setEnabled(True)

    def switchToDrinks(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.buttonBack.setEnabled(True)

    def switchToPayment(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.buttonBack.setEnabled(True)
        self.ui.lcdPayment.display(0)

    def paymentNumPad0(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        if value == 0:
            return
        self.ui.lcdPayment.display(value*10+0)

    def paymentNumPad1(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+1)

    def paymentNumPad2(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+2)

    def paymentNumPad3(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+3)

    def paymentNumPad4(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+4)

    def paymentNumPad5(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+5)

    def paymentNumPad6(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+6)

    def paymentNumPad7(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+7)

    def paymentNumPad8(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+8)

    def paymentNumPad9(self):
        value = self.ui.lcdPayment.intValue()
        # prevent values longer than 3 digits
        if value >= 100:
            return
        self.ui.lcdPayment.display(value*10+9)

    def paymentNumDel(self):
        self.ui.lcdPayment.display(0)

    def handleUser1(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.buttonBack.setEnabled(True)

    def doStuff(self):
        hlayout = QtGui.QHBoxLayout()
        label = QtGui.QLabel("test")
        button = QtGui.QPushButton()
        lcd = QtGui.QLCDNumber()
        hlayout.addWidget(label)
        hlayout.addWidget(button)
        hlayout.addWidget(lcd)
        self.ui.verticalLayout.insertLayout(2, hlayout)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    db = RpiControlDB()
    if not db.connect():
        sys.exit(1)
    db.createTables()
    db.getUsers()
    db.getDrinks()

    mainwidget = MainWidget()
    mainwidget.show()

    mainwidget.doStuff()

    sys.exit(app.exec_())