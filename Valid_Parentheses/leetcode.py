class Solution(object):
    def isValid(self, n, t):
        left = 0
        right = len(n)
        while right >= left:
            middle = (left + right) // 2
            if n[middle] == t:
                return middle
            elif n[middle] > t:
                right -= middle
            else:
                left += middle

a = Solution()
print(a.isValid([1,2,3,4,5,6,7,7,8,9], 3))