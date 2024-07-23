class Solution(object):
    def sortByLength(self, inputStr):
        return len(inputStr)

    def longestCommonPrefix(self, strs):
        strs.sort(key=self.sortByLength)
        first = [i for i in strs.pop(0)]
        ind_f = 0
        while ind_f < len(strs):
            if strs[ind_f].startswith(''.join(first)):
                ind_f += 1
            else:
                first.pop()
                ind_f = 0
        return ''.join(first)

a = Solution()
print(a.longestCommonPrefix(["dog","racecar","car"]))

