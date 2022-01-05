class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 1
        hashtable = {}
        for num in nums:
            hashtable[num] = 1
            
            
        for num in nums:
            i=1
            while hashtable.get(num-1) == None and hashtable.get(num+i) and hashtable.get(num+i) - hashtable.get(num) is not i:
                hashtable[num+i] = hashtable[num] + i
                
                ans = max(hashtable[num+i], ans)
                i+=1
                
        return ans
                