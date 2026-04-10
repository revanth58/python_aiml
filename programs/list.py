class Node :
	def __init__(self, value):
		self.value = value
		self.next = None

n1 = Node(30)
n2 = Node(46)
n3 = Node(65)
n4 = Node(57)
n5 = Node(80)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def print_list(head):
	x = head
	while x is not None:
		print(x.value)
		x = x.next

print_list(n2)