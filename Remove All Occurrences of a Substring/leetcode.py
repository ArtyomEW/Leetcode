from icecream import ic
class Solution(object):
    def removeStars(self, s):
        s = [i for i in s]
        res = ''
        for i in s:
            if i == '*':
               res = res[:-1]
            else:
                res += i
        return res

ob = Solution()
ic(ob.removeStars(s = "leet**cod*e"))