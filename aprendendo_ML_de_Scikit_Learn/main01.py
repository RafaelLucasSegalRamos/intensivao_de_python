from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['num_especie'] = iris.target
iris_df['especies'] = pd.Categorical.from_codes(iris.target, iris.target_names)

iris_df.to_excel('iris.xlsx', index=False)

sns.set_style('whitegrid')
sns.pairplot(iris_df[['sepal length (cm)', 'sepal width (cm)', "petal length (cm)", "petal width (cm)", "especies"]],
             hue='especies', height=3)
# plt.show()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=15)
clf = svm.SVC(C=1)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test)*100, "%")

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=iris.target_names))
