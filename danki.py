# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'danki.ui'
#
# UI Created by: PyQt5 UI code generator 5.13.2
#



from PyQt5 import QtCore, QtGui, QtWidgets

counter = 0
word_arr = []
new_arr = []

def read_text_file():
    f = open("words.txt","r",encoding="utf-8")

    fl = f.readlines()
    for x in fl:
        word_arr.append(x)

read_text_file()




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.card_label = QtWidgets.QLabel(self.centralwidget)
        self.card_label.setGeometry(QtCore.QRect(0, 0, 481, 451))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.card_label.setFont(font)
        self.card_label.setText("")
        self.card_label.setObjectName("card_label")
        self.easy_button = QtWidgets.QPushButton(self.centralwidget)
        self.easy_button.setGeometry(QtCore.QRect(0, 450, 241, 151))
        self.easy_button.setObjectName("easy_button")
        self.hard_button = QtWidgets.QPushButton(self.centralwidget)
        self.hard_button.setGeometry(QtCore.QRect(240, 450, 241, 151))
        self.hard_button.setObjectName("hard_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSize = QtWidgets.QAction(MainWindow)
        self.actionSize.setObjectName("actionSize")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionSize)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.easy_button.clicked.connect(self.show_easy)
        self.hard_button.clicked.connect(self.show_hard)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DANKi"))
        self.easy_button.setText(_translate("MainWindow", "Next"))
        self.hard_button.setText(_translate("MainWindow", "Previous"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSize.setText(_translate("MainWindow", "Size"))
        self.actionSize.setStatusTip(_translate("MainWindow", "Sets number of words"))
        self.actionSize.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves current settings and word file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Opens a new file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))


    def show_easy(self,text):
        try:
            self.card_label.setText(word_arr[0])
            new_arr.append(word_arr[0])
            word_arr.remove(word_arr[0])

        except (IndexError):
            pass


    def show_hard(self,text):
        try:
            self.card_label.setText(new_arr[0])
            word_arr.append(new_arr[0])
            new_arr.remove(new_arr[0])

        except (IndexError):
            pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
