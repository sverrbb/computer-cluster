## Class for representation of nodes in a cluster
class Node:

	## Creates a node with a given memory size and number of processors
	# @param memory - GB memory in the new node
	# @param processors - number of processors in the new node
	def __init__(self, memory, processors):
		self._memory = memory
		self._processors = processors


	## Gets the total number of processors in the node
	# @return number of processors in the node
	def numberOfProcessors(self):
		return self._processors


	## Checks if the node has sufficient memory for a program
	# @param requiredMemory - GB memory required for the application
	# @return True if the node has at least that much memory
	def checkMemory(self, requiredMemory):
		if self._memory >= requiredMemory:
			return True
		else:
			return False
