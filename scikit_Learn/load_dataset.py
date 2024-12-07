#This is a classification dataset used to predict whether a tumor is malignant or benign based on features derived from a digitized image of a fine-needle aspirate (FNA) of a breast mass.

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer() 
print("Feature names:", cancer.feature_names)
print("Target names:", cancer.target_names)

#A multivariate regression dataset involving physical exercise and physiological measurements.

from sklearn.datasets import load_linnerud

linnerud = load_linnerud()
print("Features (exercise data):", linnerud.data[:5])
print("Targets (physiological data):", linnerud.target[:5])

#A classification dataset for predicting the class of wine based on its chemical analysis.

from sklearn.datasets import load_wine

wine = load_wine()
print("Feature names:", wine.feature_names)
print("Target names:", wine.target_names)

#A regression dataset used to predict house prices based on various features.

# This will raise an error in Scikit-learn >= 1.0
from sklearn.datasets import load_boston

boston = load_boston()
print("Feature names:", boston.feature_names)
print("Target values:", boston.target[:5])

#A classification dataset for predicting the species of iris flowers based on their measurements.

from sklearn.datasets import load_iris

iris = load_iris()
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("First 5 samples:\n", iris.data[:5])

