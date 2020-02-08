class ListNode:
	def __init__(self, val=0):
		self.val = val
		self.next = None

l = ListNode(0)

print(l.val)

def buildList(arr):
	dummy = ListNode()
	head = dummy
	for i in arr:
		dummy.next = ListNode(i)
		dummy = dummy.next
	return head.next

def printList(head):
	while head is not None:
		print(head.val, end='->')
		head = head.next

r = buildList([99,2,4])
printList(r)




