class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1) != m:
            nums1.pop()
        while len(nums2) != n:
            nums2.pop()
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        return nums1

a = Solution()
print(a.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))