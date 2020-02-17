# 输入:
# n: 13   k: 2
#
# 输出:
# 10
#
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。


class Solution:
    def findkthnumber(self, n, k) -> int:
        cur = 1
        prefix = 1

        while cur < k:
            cnt = self.get_count(prefix, n)
            if cur + cnt > k:
                prefix *= 10
                cur += 1
            else:
                prefix += 1
                cur += cnt
        return prefix

    def get_count(self, i, n):

        if i <= n:
            cnt = 1
        else:
            return 0

        a = i
        b = i + 1

        while True:
            a = a * 10
            b = b * 10
            if n >= b:
                cnt += b - a
            elif n >= a:
                cnt += n - a + 1
            else:
                break
        return cnt

r = Solution().findkthnumber(13, 2)
print(r)