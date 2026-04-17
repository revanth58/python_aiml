class Node:
	def __init__(self,value):
		self.value = value
		self.prev = None
		self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)
n10 = Node(100)
n11 = Node(110)




n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11



n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

def print_forward(head):
	x = head

	while x is not None:
		print(x.value)
		x = x.next

#print_forward(n1)

def print_reverse(tail):
	x = tail

	while x is not None:
		print(x.value)
		x = x.prev

#print_reverse(n3)

def length_of_list(head):
	count = 0
	x = head

	while x is not None:
		count +=1
		x=x.next

	return count

#print(length_of_list(n2))

def lastkthnode(head,k):
	if length_of_list(head)<k :
		print("invalud list:djffnbgkjbjnrfb")
		return None

	x = head
	y = head

	for a in range(0,k):
		y = y.next
	
	while y is not None:
		x = x.next
		y = y.next

	return x.value

print(lastkthnode(n2,4))