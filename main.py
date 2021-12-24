from cluster import Cluster
from node import Node

def main():

    # Create a cluster
    abel = Cluster(12)

    # Default values - 650 nodes with 64 GB memeory and 1 processor
    for i in range(650):
        abel.insertNode(Node(64, 1))

    # Default values - 16 nodes with 1024 GB memeory and 2 processor
    for j in range(16):
        abel.insertNode(Node(1024, 2))

    # Print out information about the cluster
    print("Nodes with at least 32 GB:", abel.sufficientMemory(32))
    print("Nodes with at least 64 GB: ", abel.sufficientMemory(64))
    print("Nodes with at least 128 GB: ", abel.sufficientMemory(128))
    print("Number of processors: ", abel.numberOfProcessors())
    print("Number of racks: ", abel.numberOfRacks())

main()
