from rack import Rack
from node import Node

## Class for representation of cluster with racks and nodes
class Cluster:

	## Creates empty calculation cluster for racks with specified maximum number of nodes / rack
	# @param nodesInRack - max number of nodes that can be placed in a rack
	def __init__(self, nodesInRack):
		self._rackList = []
		self._nodesInRack = nodesInRack
		self._index = 0
		self._rackList.append(Rack(nodesInRack))


	## Insert node into the rackList in the cluster. Checks if rack has capasity
	# @param node - node to insert into the rackList
	def insertNode(self, node):
		if not self._rackList[self._index].moreCapacity():
			self._rackList.append(Rack(self._nodesInRack))
			self._index += 1
		self._rackList[self._index].insert(node)



	## Calculates the total number of processors in the entire calculation cluster
	# @return total number of processors
	def numberOfProcessors(self):
		total = 0
		for rack in self._rackList:
			total += rack.getnumberOfProcessors()
		return total


	## Calculates the number of nodes in the cluster with memory above the specified limit
	# @param requiredMemory - how much memory should nodes that are counted have
	# @return number of nodes with sufficient memory
	def sufficientMemory(self, requiredMemory):
		numberOfNodes = 0
		for rack in self._rackList:
			numberOfNodes += rack.sufficientMemory(requiredMemory)
		return numberOfNodes


	## Retrieves the number of racks in the cluster
	# @return number of racks
	def numberOfRacks(self):
		return len(self._rackList)
