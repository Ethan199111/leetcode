# 123456 sorted array
# find target

def find(a, t):
	left = 0
	right = len(a) - 1
	while left <= right:
		mid = (left + right) // 2
		if t == a[mid]:
			return mid
		elif t > a[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return -1

a = [1,2,3,3,4,5]
print(find(a, 1))
print(find(a, 2))
print(find(a, 5))
