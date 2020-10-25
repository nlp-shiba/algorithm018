class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1