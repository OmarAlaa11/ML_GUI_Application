import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")

from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit,QHBoxLayout,QPushButton
import DecisionTree_GUI,SVM_GUI


class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "ML Application"
        self.top = 300
        self.left = 700
        self.width = 240
        self.height = 250
        self.iconName = r'H:\Classifier_with_GUI\Icons\python.PNG'
        self.initUI()
        
    def createButton(self,text,fun,x,y,l,w):
        pushButton = QPushButton(text,self) 
        pushButton.setGeometry(QtCore.QRect(x,y,l,w))
        pushButton.clicked.connect(fun)
        return pushButton    
                
    def initUI(self):               
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.svmButton = self.createButton("SVM",self.callSVMRunner,10, 120,100, 100)
        self.dtButton = self.createButton("Decision Tree",self.callDecesionTreeRunner,120, 120,100, 100)
        # self.mlpButton = self.createButton("MLP",self.MLPRunner,230, 120,100, 100)
        
        
        
        self.show()
        
        
    def callSVMRunner(self): 
        self.m = SVM_GUI.Main()
        
    def callDecesionTreeRunner(self): 
        self.m = DecisionTree_GUI.Main()
    
    # def MLPRunner(self): 
    #     self.m = MLPRunner.Main()    
        
        
if __name__=="__main__":   
    import sys
    app = QApplication(sys.argv)
    mWin = mainWindow()
    sys.exit(app.exec_())