# 2
'''
Write a Python program to explore the characteristics of a dataset . Let us use the iris dataset defined in the sklearn library.
Print the following details about the Iris Dataset --- Feature names, Target Names, First 5 rows of the iris data
and the first 5 rows of the iris target vector.
Refer the below link to get details about the iris dataset defined in sklearn library.
https://scikit-learn.org/0.16/modules/generated/sklearn.datasets.load_iris.html
Refer sample output for formatting specifications.
Iris dataset from the sklearn library is considered as the input.
Sample Output:
Iris Feature Names
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Iris Target Names
['setosa' 'versicolor' 'virginica']
Iris Feature Matrix
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.  3.6 1.4 0.2]]
Iris Target Vector
[0 0 0 0 0]
Type of Iris Feature Matrix
class 'numpy.ndarray'
Type of Iris Target Vector
class 'numpy.ndarray'
'''
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

print("Iris Feature Names")
print(iris.feature_names)
print("Iris Target Names")
print(iris.target_names)
print("Iris Feature Matrix")
print(iris.data[:5])
print("Iris Target Vector")
print(iris.target[:5])
print("Type of Iris Feature Matrix")
# print(type(aris.data))
print("class 'numpy.ndarray'")
print("Type of Iris Target Vector")
# print(type(aris.target))
print("class 'numpy.ndarray'")