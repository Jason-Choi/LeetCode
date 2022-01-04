class Solution:      
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            subtracted = target - num
            if subtracted in hashmap:
                return [hashmap[subtracted], idx]
            hashmap[num] = idx