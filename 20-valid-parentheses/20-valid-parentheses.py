class Solution:
    def isValid(self, s: str) -> bool:
        stringList = list(s)
        startBracket = ["(", "{", "["]
        endBracket = [")", "}", "]"]
        stack = []
        
        for bracket in stringList:
            if len(stack) == 0:
                if bracket in startBracket:
                    
                    stack.append(bracket)
                else:
                    return False
                
                continue
                
            if bracket in startBracket:
                stack.append(bracket)
            
            else:
                if startBracket.index(stack[-1]) != endBracket.index(bracket):
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        