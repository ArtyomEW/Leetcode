class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        maxLen = 0
        for i in range(len(s)):
            st = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in st:
                    st += s[j]
                else:
                    maxLen = max(maxLen, len(st))
                    break
            maxLen = max(maxLen, len(st))
        return maxLen