class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listString = list(s)
        longest = 0
        subString = list()
        for char in listString:
            if char not in subString:
                subString.append(char)
                longest = max(len(subString), longest)
            else:
                subString = subString[subString.index(char)+1:]
                subString.append(char)
        return longest
        