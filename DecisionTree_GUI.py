import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
import DecisionTree
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import *
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__() # Inheritance from QMainWindow library
        self.title = "Decision Tree Application"
        self.top = 300
        self.left = 600
        self.width = 400
        self.height = 300
        self.iconName = r'H:\Classifier_with_GUI\Icons\DT.JPG'
        self.initUI()

    def initUI(self):               
        self.setWindowTitle(self.title) # Title
        self.setWindowIcon(QtGui.QIcon(self.iconName)) # Icon
        self.setGeometry(self.left, self.top, self.width, self.height)  # Move and resize
        self.splitSize = 20 # test split

        self.drawBrowser()
        self.drawSplit()
        self.drawCriterion()
        self.drawSplitter()
        self.setDefault()
        self.DTButton = self.createButton("Run",self.runDT,330, 240,60, 30)

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
        
    # Third label : Criterion : gini or entropy.
    def drawCriterion(self):
        self.crit_label = QLabel("Criterion: ",self)
        self.split_label.setStyleSheet('background-color: #f0f0f0; color: #333; border: 1px solid #ccc; padding: 5px; border-radius: 3px;')             
        self.crit_label.setGeometry(QtCore.QRect(40,120, 80, 30))
        self.crit_group = QButtonGroup(self)
        self.crit_button1 = QRadioButton("gini",self)
        self.crit_button1.setGeometry(QtCore.QRect(160,125,80,20))
        self.crit_group.addButton(self.crit_button1)
        self.crit_button2 = QRadioButton("entropy",self)
        self.crit_button2.setGeometry(QtCore.QRect(250,125,80,20))
        self.crit_group.addButton(self.crit_button2)

    # Forth label : Splitter : best or random.    
    def drawSplitter(self):
        self.splitter_label = QLabel("Splitter: ",self)
        self.split_label.setStyleSheet('background-color: #f0f0f0; color: #333; border: 1px solid #ccc; padding: 5px; border-radius: 3px;')              
        self.splitter_label.setGeometry(QtCore.QRect(40,160, 80, 30))
        self.splitter_group = QButtonGroup(self)
        self.splitter_button1 = QRadioButton("best",self)
        self.splitter_button1.setGeometry(QtCore.QRect(160,165,80,20))
        self.splitter_group.addButton(self.splitter_button1)
        self.splitter_button2 = QRadioButton("random",self)
        self.splitter_button2.setGeometry(QtCore.QRect(250,165,80,20))
        self.splitter_group.addButton(self.splitter_button2)


    def setDefault(self):
        self.crit_button1.setChecked(True)
        self.splitter_button1.setChecked(True)
        self.splitter = 'best'
        self.criterion = 'gini'

    # Function to run Decition Tree Model.
    def runDT(self):
        if self.fileName != "":
            self.splitSize = int(self.split_lineEdit.text())
            
            if self.splitSize <=40:
                if self.splitter_button1.isChecked() is False:
                    self.splitter = 'random'
                if self.crit_button1.isChecked() is False:
                    self.criterion = 'entropy'
                self.results = DecisionTree.run(self.fileName,self.splitSize,self.criterion,self.splitter)
            else:
                pass  # Can't train on such small dataset.
        else: 
            pass      # incorrect file name. 
        
        # Visualize classification report:
        QMessageBox.about(self,"Results:", self.results)

    def createButton(self,text,fun,x,y,l,w):
        pushButton = QPushButton(text,self) 
        pushButton.setGeometry(QtCore.QRect(x,y,l,w))
        pushButton.clicked.connect(fun) # Connect to run when clicked
        return pushButton
    

def Main():
    m = window()
    m.show()
    return m
if __name__=="__main__":   
    app = QApplication(sys.argv)
    mWin = window()
    sys.exit(app.exec_())