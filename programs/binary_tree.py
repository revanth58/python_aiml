class Node:
	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None

n25 = Node(25)
n20 = Node(20)
n36 = Node(36)
n10 = Node(10)
n22 = Node(22)
n30 = Node(30)
n40 = Node(40)
n5 = Node(5)
n12 = Node(12)
n28 = Node(28)
n38 = Node(38)
n48 = Node(48)
n1 = Node(1)
n8 = Node(8)
n15 = Node(15)
n45 = Node(45)
n50 = Node(50)

n25.left = n20
n25.right = n36

n20.left = n10
n20.right = n22

n36.left = n30
n36.right = n40

n10.left = n5
n10.right = n12

n30.left = n28

n40.left = n38
n40.right = n48

n5.left = n1
n5.right = n8

n12.right = n15

n48.left = n45
n48.right = n50

def height(root):
	if root is None:
		return 0
	return 1 + max(height(root.left), height(root.right))

#print(height(n25))

def search(root, key):
	if root is None:
		return 0
	if root.data == key:
		return 1

	return search(root.left, key) or search(root.right, key)

#while True:
#	x = int(input("enter value : "))
#	print(search(n25,x))

def count_nodes(root):
	if root is None:
		return 0

	return 1 + count_nodes(root.left) + count_nodes(root.right)

#print("total nodes : ", count_nodes(n25))

def leaves(root):
	if root is None:
		return 0

	if root.left is None and root.right is None:
		return 1

	return leaves(root.left) + leaves(root.right)

#print("no. of leaves ", leaves(n25))

def sum_tree(root):
	if root is None:
		return 0

	return root.data + sum_tree(root.left) + sum_tree(root.right)

#print("sum of tree", sum_tree(n25))

def return_max(root):
	if root is None:
		return 0

	return max(root.data, return_max(root.left), return_max(root.right))

print("max of tree ", return_max(n25))