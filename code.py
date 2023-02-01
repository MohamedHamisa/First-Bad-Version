import bisect

class Solution(dict):
    def firstBadVersion(self, n):
        return bisect.bisect_left(self, True, 1, n) #bisect_left(list, num, beg, end) :
    
    def __getitem__(self, key):
        return isBadVersion(key)
