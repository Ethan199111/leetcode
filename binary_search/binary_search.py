# 123456 sorted array
# find target


def find(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a = [1, 2, 3, 3, 4, 5]
print(find(a, 1))
print(find(a, 2))
print(find(a, 5))
print(find(a, 3))
