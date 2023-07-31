from sklearn.datasets import load_iris
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import random

iris = load_iris()
X, y = load_iris(return_X_y=True)

iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['target'] = y
iris_df['target names'] = pd.Categorical.from_codes(iris.target, iris.target_names)

iris_df.to_excel('iris.xlsx', index=False)
#print(iris_df)

#iris_df = pd.read_excel('iris.xlsx')

iris_df.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', c='target', colormap='viridis')
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)