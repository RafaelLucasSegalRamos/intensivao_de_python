from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# df = px.data.iris()
# fig = px.scatter_3d(df, x="sepal_length", y="sepal_width", z='petal_width', color="species") --> esse mostra um plot 3D
# fig.show()

iris = load_iris()
X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=22)

clf = KNeighborsClassifier(n_neighbors=10)

clf.fit(X_train, y_train)

x_pred = clf.predict(X_test)

print(classification_report(y_test, x_pred, target_names=iris.target_names))


