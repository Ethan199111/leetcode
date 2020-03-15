# 123456 sorted array
# find target

# 确定mid不是target时，就可以去[left, mid-1], [mid+1, right]区间搜索

def find(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 # python // 2是不带小数点的
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1


a = [1, 2, 3, 3, 4, 5]
#print(find(a, 4))

b = [1, 2, 2, 2, 3, 3, 4, 5]

c = [1, 3, 5, 6]


def left_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def right_bound(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return right - 1


#print(left_bound(b, 2))
#print(left_bound(c, 7))
print(right_bound(b, 2))
print(right_bound(b, 5))
print(right_bound(b, 1))
print(right_bound(b, 0.5))

