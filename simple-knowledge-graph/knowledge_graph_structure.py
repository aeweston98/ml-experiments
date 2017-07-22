#include node_structure

class simple_knowledge_graph:
	def __init__(self, name, head_node):
		self._name = name 				#give the graph a name :)
		self._head_node = head_node 	#head node of the graph must be passed in
										#it will be the only node of level 1
 		self._size = 1 					#constructor takes the head node
 		self._array_of_level_arrays = []
 		level_one = []
 		level_one.append(head_node)
 		_array_of_level_arrays.append(level_one)
 		self._bin_sizes = [1]			#these values will have to be set as you get to each new level

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
		uid = hash(name, _bin_sizes[level])
		new = simple_knowledge_graph_node(name, ,parent_node_id)

	#add a link between two nodes of different levels
	#note that child nodes know about their parent nodes
	def create_vertical_link(parent_node_id, child_node_id):


	#add a link between two nodes on the same level
	def create_horizontal_link(left_node_id, right_node_id):


	def hash(s, num_bins):
  		int intLength = s.length() / 4
  		long sum = 0

  		for (int j = 0; j < intLength; j++) :
    		char c[] = s.substring(j * 4, (j * 4) + 4).toCharArray()
    		long mult = 1

    		for (int k = 0; k < c.length; k++):
      			sum += c[k] * mult
      			mult *= 256

  		char c[] = s.substring(intLength * 4).toCharArray()
  		long mult = 1
  		
  		for (int k = 0; k < c.length; k++) 
    		sum += c[k] * mult
    		mult *= 256

		return(Math.abs(sum) % num_bins)

