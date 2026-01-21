class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        total_value = sum(range(n + 1))
        current_sum = sum(nums)

        print("Expected sum:", total_value)
        print("Actual sum:", current_sum)

        return total_value - current_sum
