import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


import numpy as np
import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns


def run(file_name, testing_percentage, kernel_name, poly_degree, tol_val, reg):

    df = pd.read_csv(file_name)

    ts = (testing_percentage)/100
    
    # Data processing
    x = df.drop(columns=['Class'])
    y = pd.DataFrame(df['Class'])
    X = x.iloc[:, :].values
    Y = y.iloc[:, :].values
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=ts,random_state=109)
    
    # Normalization
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    # Model
    clf = SVC(kernel=kernel_name,degree = poly_degree, tol = tol_val,C = reg)
    clf.fit(X_train,Y_train)

    # Predict and visualize confusion_matrix and classification_report
    Y_predict = clf.predict(X_test)
    cm = np.array(confusion_matrix(Y_test, Y_predict, labels=[0,1]))
    confusion = pd.DataFrame(cm, index = ['actual 0', 'actual 1'], columns = ['predicted 0','predicted 1'])
    
    sns.heatmap(confusion, annot = True)
    plt.show()
    results = classification_report(Y_test, Y_predict)
    return results