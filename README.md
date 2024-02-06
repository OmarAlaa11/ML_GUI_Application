# ML_GUI_Application
This is a GUI application for Machine Learning. This application is made purely with python. The main libraries used are used are: PyQt5,Keras,Pandas,Nump,Sklearn and Scikit learn,
It allows a user to make ML classification models.
## Eeasy for Users
The user can select a CSV file containing the dataset. Enter the hyperparameters (which are filled by default (for ease) and hit the run button.The application will give you classification report and confusion matrix on the test data.
## Decision Tree Algorithm
A decision tree is a flowchart-like tree structure where an internal node represents a feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome.

The topmost node in a decision tree is known as the root node. It learns to partition on the basis of the attribute value. It partitions the tree in a recursive manner called recursive partitioning. This flowchart-like structure helps you in decision-making. It's visualization like a flowchart diagram which easily mimics the human level thinking. That is why decision trees are easy to understand and interpret.
A software that allows the user to make ML classification models without writing a single line of code.

### Decision Tree Hyperparameters
1) criterion parameter: determines the function to measure the quality of a split. It could be 'gini' for Gini impurity or 'entropy' for information gain.

   Gini impurity: Gini impurity is a measure of how often a randomly chosen element would be incorrectly classified.
   
   Entropy: Entropy measures the degree of disorder or uncertainty in a set of samples.

3) splitter parameter: chooses the strategy used to choose the split at each node. It could be 'best' to choose the best split or 'random' to choose the best random split.

   Best Split: refers to the strategy of selecting the optimal feature and corresponding threshold that maximizes the information gain (or minimizes impurity) at each split.
   
   Random Split: involves randomly selecting a feature and threshold at each node to create a split.
   
![DT](https://github.com/OmarAlaa11/ML_GUI_Application/assets/142521907/44af4eaf-d642-4dff-aa12-dbd4147d3102)

## SVM Algorithm
SVM constructs a hyperplane in multidimensional space to separate different classes. SVM generates optimal hyperplane in an iterative manner, which is used to minimize an error. The core idea of SVM is to find a maximum marginal hyperplane(MMH) that best divides the dataset into classes.

Support vectors are the data points, which are closest to the hyperplane. These points will define the separating line better by calculating margins. These points are more relevant to the construction of the classifier.

### Hyperplane
A hyperplane is a decision plane which separates between a set of objects having different class memberships.

### Margin
A margin is a gap between the two lines on the closest class points. This is calculated as the perpendicular distance from the line to support vectors or closest points. If the margin is larger in between the classes, then it is considered a good margin, a smaller margin is a bad margin.

![SVM](https://github.com/OmarAlaa11/ML_GUI_Application/assets/142521907/5977cb20-63f1-40f8-b640-3b0dd94c5e30)

The main objective is to segregate the given dataset in the best possible way. The distance between the either nearest points is known as the margin. The objective is to select a hyperplane with the maximum possible margin between support vectors in the given dataset. SVM searches for the maximum marginal hyperplane in the following steps:

1.Generate hyperplanes which segregates the classes in the best way. Left-hand side figure showing three hyperplanes black, blue and orange. Here, the blue and orange have higher classification error, but the black is separating the two classes correctly.

2.Select the right hyperplane with the maximum segregation from the either nearest data points.

### SVM Hyperparameters (Kernels) :
Linear Kernel A linear kernel can be used as normal dot product any two given observations. The product between two vectors is the sum of the multiplication of each pair of input values.
Polynomial Kernel A polynomial kernel is a more generalized form of the linear kernel. The polynomial kernel can distinguish curved or nonlinear input space.
RBF Kernel The Radial basis function kernel is a popular kernel function commonly used in support vector machine classification. RBF can map an input space in infinite dimensional space.
Gaussian Kernel and finally Sigmoid Kernel.


