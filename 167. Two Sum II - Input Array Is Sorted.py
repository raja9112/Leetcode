class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Using two pointers, Time: 109ms
        # l = 0
        # r = len(numbers) - 1

        # while l < r:
        #     current = numbers[l] + numbers[r]

        #     if current < target:
        #         l += 1
        #     elif current > target:
        #         r -= 1
        #     else:
        #         return [l+1, r+1]

        # Using hash, Time: 93ms
        _hash = {}
        for index, i in enumerate(numbers):
            complement = target - i
            if complement in _hash:
                return [_hash[complement] + 1, index+1]
            _hash[i] = index