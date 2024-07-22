import itertools

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = len(tiles)
        result = 0
        while res != 0:
            lst = set(itertools.permutations(tiles, res))
            result += len(list(lst))
            res -= 1
        return result

cl = Solution()
print(cl.numTilePossibilities('AAABBC'))



