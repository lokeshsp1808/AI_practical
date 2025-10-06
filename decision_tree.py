from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load dataset
X, y = load_iris(return_X_y=True)

# Create Decision Tree (classification)
tree = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=0)
tree.fit(X, y)

# Print decision rules
rules = export_text(tree, feature_names=load_iris().feature_names)
print(rules)
