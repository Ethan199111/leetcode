class Tree:
	def __init__(self, val=0):
		self.val = val
		self.right = None
		self.left = None


t = Tree(2)

t.left = Tree(3)
t.right = Tree(4)

print(t.val)
print(t.left.val)


