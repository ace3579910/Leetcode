class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set_num=set(nums)
        new_set=[]

        for i in range(1,len(nums)+1):
            if i not in set_num:
                new_set.append(i)
        return new_set