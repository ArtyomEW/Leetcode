from collections import Counter
from copy import deepcopy
class Solution(object):
    def func(self, nums):
        Ans = []
        n = len(nums)

        def func2(op, start_index):
            if start_index == n:
                Ans.append(list(op))
                return

            op.append(nums[start_index])
            func2(op, start_index + 1)
            op.pop()

            func2(op, start_index+1)

        func2([], 0)

        return Ans


a = Solution()
print(a.func([1,2,3]))
