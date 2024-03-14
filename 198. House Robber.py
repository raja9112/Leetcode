class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
        
obj = Solution()
print(obj.rob([2,3,2]))