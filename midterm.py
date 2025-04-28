from PyQt5 import QtCore, QtGui, QtWidgets
import random

lists = []
for i in range(100):
    l = []
    for i in range(3):
        l.append(random.randrange(1,200))
    lists.append(l)

class Trapezoid:
    def __init__(self, values):
        self.base1 = values[0]
        self.base2 = values[1]
        self.height = values[2]

    def area(self):
        return (self.base1 + self.base2) * self.height / 2 
    
    def __str__(self):
        return f"Trapezoid first base is: {self.base1}, second base: {self.base2} and its height is: {self.height}"

class Rectangle(Trapezoid):
    def __init__(self, values):
        super().__init__([values[0], values[1], 0])

    def area(self):
        return self.base1 * self.base2

    def __str__(self):
        return f"Rectangles width is: {self.base1} and height: {self.base2}"
    
class Triangle(Rectangle):
    def __init__(self, values):
        super().__init__([values[0], values[1], 0])

    def area(self):
        return self.base1 * self.base2 / 2
    
    def __str__(self):
        return f"Triangles width is: {self.base1} and height: {self.base2}"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 400, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 400, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 461, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../puthon_midterm/trapezoid.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 300, 491, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewTrapezoid = QtWidgets.QAction(MainWindow)
        self.actionNewTrapezoid.setObjectName("actionNewTrapezoid")
        self.actionNewRectangle = QtWidgets.QAction(MainWindow)
        self.actionNewRectangle.setObjectName("actionNewRectangle")
        self.actionNewTriangle = QtWidgets.QAction(MainWindow)
        self.actionNewTriangle.setObjectName("actionNewTriangle")
        self.menuFile.addAction(self.actionNewTrapezoid)
        self.menuFile.addAction(self.actionNewRectangle)
        self.menuFile.addAction(self.actionNewTriangle)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.trapezoid)
        self.pushButton_2.clicked.connect(self.rectangle)
        self.pushButton_3.clicked.connect(self.triangle)
        self.pushButton_4.clicked.connect(self.show_area)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.actionNewRectangle.triggered.connect(self.rectangle)
        self.actionNewTrapezoid.triggered.connect(self.trapezoid)
        self.actionNewTriangle.triggered.connect(self.triangle)

    def rectangle(self):
        values = random.choice(lists)
        self.current_shape = Rectangle(values)
        self.label_2.setText(str(self.current_shape))
        self.label.setPixmap(QtGui.QPixmap("../puthon_midterm/rectangle.png"))

    def triangle(self):
        values = random.choice(lists)
        self.current_shape = Triangle(values)
        self.label_2.setText(str(self.current_shape))
        self.label.setPixmap(QtGui.QPixmap("../puthon_midterm/triangle.png"))

    def trapezoid(self):
        values = random.choice(lists)
        self.current_shape = Trapezoid(values)
        self.label_2.setText(str(self.current_shape))
        self.label.setPixmap(QtGui.QPixmap("../puthon_midterm/trapezoid.jpg"))

    def show_area(self):
        area_value = self.current_shape.area()
        self.label_2.setText(f"The area is: {area_value}")




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "trapezoid"))
        self.pushButton_2.setText(_translate("MainWindow", "rectangle"))
        self.pushButton_3.setText(_translate("MainWindow", "triangle"))
        self.pushButton_4.setText(_translate("MainWindow", "area"))
        self.pushButton_5.setText(_translate("MainWindow", "close"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNewTrapezoid.setText(_translate("MainWindow", "NewTrapezoid"))
        self.actionNewRectangle.setText(_translate("MainWindow", "NewRectangle"))
        self.actionNewTriangle.setText(_translate("MainWindow", "NewTriangle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
