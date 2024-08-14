from ZGame import ZGame 
from PyQt5 import QtWidgets
from Form import Ui_MainWindow
import sys

#pyrcc5 images.qrc -o Images_rc.py

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.GoNext)
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_4.clicked.connect(self.Create_server)
    
    
    def Create_server(self):
        if self.ui.radioButton.isChecked():
            self.ui.stackedWidget.setCurrentIndex(2)
        elif self.ui.radioButton_2.isChecked():
            self.ui.stackedWidget.setCurrentIndex(3)


    def GoNext(self):
        try:
            Nickname = str(self.ui.lineEdit.text())
            Ip = str(self.ui.lineEdit_2.text())
            Port = int(self.ui.lineEdit_3.text())
            if Nickname == "" or Ip == "" or Port == "":
                print("LOG: ERROR: The value is not correct"); return
            self.ui.stackedWidget.setCurrentIndex(2)
        except Exception as exp:
            print("LOG: ERROR:", exp)


def main():
    TheGame = ZGame()
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
 
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
