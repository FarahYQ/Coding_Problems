"""
3Sum
Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which 
gives the sum of zero.
"""

from collections import defaultdict

class Solution:
    def threeSum( self, nums ):
        nums.sort()
        nums_counts = defaultdict( int )
        for i in nums:
            nums_counts[i] += 1
        visited_nums = set()
        unique_triplets = set()
        for b in nums:
            nums_counts[ b ] -= 1
            for a in visited_nums:
                if -(a+b) in nums_counts and nums_counts[-(a+b)] > 0 :
                    unique_triplets.add( ( a, b, -( a + b ) ) )
            visited_nums.add( b )
        return list( unique_triplets )