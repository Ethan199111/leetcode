# 456123 45123
# find 4

# 核心点是 知道中间跟右边的对比，比右边大，意味着左边是有序的，否则右边是有序的
# 二分查找的关键点就是找到有序的序列，然后利用二分查找

def find(a, t):
	left = 0
	right = len(a) - 1
	while left <= right:
		mid = (left + right) // 2
		if t == a[mid]:
			return mid
		if a[mid] > a[right]:
			if  t  < a[mid] and t >= a[left]:
				right = mid -1
			else:
				left = mid +1		
		else:
			if t > a[mid] and t <= a[right]:
				left = mid + 1
			else:
				right = mid -1
	return -1

a = [4,5,6,1,2,3]
print(find(a, 4))
print(find(a, 5))
print(find(a, 6))
print(find(a, 1))
print(find(a, 2))
print(find(a, 3))



			