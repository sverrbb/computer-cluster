from node import Node

## Class for representing racks in a cluster.
class Rack:

	## creates a rack where nodes can be placed later
	def __init__(self, maxNodes):
		self._maxNodes = maxNodes
		self._nodeList = []


	## Inserts a new node into the rack
	# @param node - the node to be placed
	def insert(self, node):
		self._nodeList.append(node)


	## Gets the number of nodes in the rack
	# @return number of nodes
	def getNumberOfNodes(self):
		numberOfNodes = len(self._nodeList)
		return numberOfNodes


	# Checks if the rack has capacity for more nodes
	def moreCapacity(self):
		return len(self._nodeList) < self._maxNodes


	## Calculates the total number of processors in the nodes in a rack
	# @return number of processors
	def getnumberOfProcessors(self):
		total = 0
		for node in self._nodeList:
			total += node.numberOfProcessors()
		return total


	## Calculates the number of nodes in the rack with memory above the given limit
	# @param requiredMemory - number of GB of memory required
	# @return number of nodes with sufficient memory
	def sufficientMemory(self, requiredMemory):
		numberOfNoder = 0
		for node in self._nodeList:
			if node.checkMemory(requiredMemory):
				numberOfNoder += 1
		return numberOfNoder
