

class simple_knowledge_graph:
	def __init__(self, name, head_node):
		self._name = name 				#give the graph a name :)
		self._head_node = head_node 	#head node of the graph must be passed in
										#it will be the only node of level 1
 		self._size = 1 					#constructor takes the head node

	#this function will be for building a graph from some
	#kind of remote storage structure
	#so that a graph can be passed around
	def build_from_existing(graph_data):


	#this function will be for creating the storage structure
	#to save the graph as previously mentionend
	def save_graph():

	#this function will add a node to the graph
	#it relies on the parent node of the node
	#you wish to add 
	#each node can have multiple parents, but they 
	#get added with only one
	def add_node(name, level, parent_node_id):


	#add a link between two nodes of different levels
	#note that child nodes know about their parent nodes
	def create_vertical_link(parent_node_id, child_node_id):


	#add a link between two nodes on the same level
	def create_horizontal_link()




