import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import SVM

class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "SVM Application"
        self.top = 300
        self.left = 600
        self.width = 400
        self.height = 300
        self.iconName = r'H:\Classifier_with_GUI\Icons\SVM.PNG'
        self.initUI()
        
        
    def initUI(self):               
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setDefault()        
        self.drawBrowser()
        self.drawSplit()                
        self.drawKernel()       
        self.drawDegree()       
        self.svmButton = self.createButton("Run",self.runSVM,330, 240,60, 30)

        self.show()
        
    def getFileName(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\' , '*.csv') # default path with filtering csv extensions files.
        self.csv_lineEdit.setText(fileName) # set text on text box
        self.fileName = self.csv_lineEdit.text()
            
    # First label with Button : upload csv file label with Text.
    def drawBrowser(self):
       self.centralwidget = QWidget(self) # window
       self.csv_label = QLabel(self.centralwidget) # label
       self.csv_label.setGeometry(QtCore.QRect(10, 10, 80, 30))
       self.csv_label.setText("csv file: ")
       self.csv_lineEdit = QLineEdit(self) # Creat text box on window
       self.csv_lineEdit.setGeometry(QtCore.QRect(90,10,300,30))
       self.DTButton = self.createButton("Browse",self.getFileName,330, 50,60, 30) # getFile when click Browse Button.

    # Second label : test Split label. 
    def drawSplit(self):
        self.split_label = QLabel("test_data size(%): ",self)
        self.split_label.setStyleSheet('background-color: #f0f0f0; color: #333; border: 1px solid #ccc; padding: 5px; border-radius: 3px;')              
        self.split_label.setGeometry(QtCore.QRect(40,80, 110, 30))
        self.split_lineEdit = QLineEdit(self)
        self.split_lineEdit.setGeometry(QtCore.QRect(160,80,50,30))
        self.split_lineEdit.setText(str(self.splitSize))

    def drawKernel(self):
        self.kernel_label = QLabel("Kernel Type: ",self)
        self.split_label.setStyleSheet('background-color: #f0f0f0; color: #333; border: 1px solid #ccc; padding: 5px; border-radius: 3px;')  
        self.kernel_label.setGeometry(QtCore.QRect(40,120, 110, 30))
        
        self.kernel_cb = QComboBox(self)
        self.kernel_cb.setGeometry(QtCore.QRect(160,120,80,30))
        self.kernel_cb.addItems(["Linear", "rbf", "poly","sigmoid"])
        self.kernel_cb.currentIndexChanged.connect(self.selectionChange)

    def selectionChange(self):
        self.kernelType = self.kernel_cb.currentText()

    def drawDegree(self):
        self.degree_label = QLabel("Degree: ",self)
        self.split_label.setStyleSheet('background-color: #f0f0f0; color: #333; border: 1px solid #ccc; padding: 5px; border-radius: 3px;')              
        self.degree_label.setGeometry(QtCore.QRect(40,160, 110, 30))
        
        self.degree_lineEdit = QLineEdit(self)
        self.degree_lineEdit.setGeometry(QtCore.QRect(160,160,50,30))
        self.degree_lineEdit.setText(str(self.degree))

    def setDefault(self):
        self.splitSize = 20
        self.kernelType = 'rbf'
        self.degree = 3

    # Function to run SVM Model.
    def runSVM(self):
        if self.fileName != "":
            self.splitSize = int(self.split_lineEdit.text())
            self.kernelType = self.kernel_cb.currentText()
            self.degree = int(self.degree_lineEdit.text())
            if self.splitSize <=40:
                self.results = SVM.run(self.fileName,self.splitSize,self.kernelType,self.degree,self.tol,self.regParam)
            else:
                pass # Can't train on such small dataset.
        else: 
            pass     # incorrect file name.             

        # Visualize classification report:
        QMessageBox.about(self,"Results:", self.results)
        

    def createButton(self, text, fun, x, y, l, w):
        pushButton = QPushButton(text, self) 
        pushButton.setGeometry(QtCore.QRect(x, y, l, w))
        pushButton.clicked.connect(fun) # Connect to run when clicked
        return pushButton
        
        
def Main():
    m = mainWindow()
    m.show()
    return m
    
if __name__=="__main__":   
    import sys
    app = QApplication(sys.argv)
    mWin = mainWindow()
    sys.exit(app.exec_())