

class simple_knowledge_graph_node:
	def __init__(self, name, uid, parent_node):
		self._name = name
		self._uid = uid
		#initialize a list of VEdges and HEdges
		#add the original parent node to the list of VEdges
		