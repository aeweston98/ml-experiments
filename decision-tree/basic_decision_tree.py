from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
d_tree_gini = tree.DecisionTreeClassifier(criterion='gini', min_samples_split = 5)
d_tree_gini = d_tree_gini.fit(iris.data, iris.target)

from pydotplus import graphviz

dot_data = tree.export_graphviz(d_tree_gini, out_file= 'results/tree_gini.dot') 
graph = graphviz.graph_from_dot_file('results/tree_gini.dot') 
graph.write_pdf("results/iris_gini.pdf") 

d_tree_entropy = tree.DecisionTreeClassifier(criterion='entropy', min_samples_split = 5)
d_tree_entropy = d_tree_entropy.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(d_tree_entropy, out_file= 'results/tree_entropy.dot') 
graph = graphviz.graph_from_dot_file('results/tree_entropy.dot') 
graph.write_pdf("results/iris_entropy.pdf") 
