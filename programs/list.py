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

#print_list(n1)

def arrtolist(nums):
	head = None
	prev = None

	for x in nums :
		p = Node(x)
		if head is None:
			head = p
		else :
			prev.next = p

		prev = p

	return head

z = arrtolist([123,345,67,3,23,6,7,4,6,7,3,125,333,4])

def return_last(head):
	if head is None:
		print("invalid : empty list")
		return None
	x = head
	while x.next is not None:
		x = x.next
	return x

print(return_last(z).value)
