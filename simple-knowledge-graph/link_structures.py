

#class for containing all the links between
#a parent node and a child node
class VEdges:
	def __init__(self, parent_uid, child_uid, original_edge):
		self._parent_uid = parent_uid 		#the uid of the parent node
		self._child_uid = child_uid 		#the uid of the child node
		_edges = []							#list of edges
		_edges.append(original_edge)		#presumably we will only initialize this when we want to store a vertical edge
											#so we can make it the first link in the list of edges					
		_strength = 1 						#initialize the strength at 1 (can't be zero because it will change by multiplication)
		_num_edges = 1						#counter for number of edges


class HEdges:
		def __init__(self, parent_uid, child_uid, original_edge):
		self._parent_uid = parent_uid 		#the uid of the parent node
		self._child_uid = child_uid 		#the uid of the child node
		_edges = []							#list of edges
		_edges.append(original_edge)		#presumably we will only initialize this when we want to store a vertical edge
											#so we can make it the first link in the list of edges					
		_strength = 1 						#initialize the strength at 1 (can't be zero because it will change by multiplication)
		_num_edges = 1						#counter for number of edges


class Edge:
	def __init__(self, description, strength):
		self._keywords = keywords 			#hold the keywords so the set of edges can be searched
		self._strength = strength 			#strength of the particular connection
		self._fulltext = fulltext 			#record the fulltext pertaining to a connection