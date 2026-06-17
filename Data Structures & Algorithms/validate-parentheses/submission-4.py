class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        count=-1
        brack={
            ']':'[',
            '}':'{',
            ')':'('
        }

        for i in s :
            if i == ']' or i=='}' or i==')' :
                if brack[i] not in stack :
                    return False
                if stack[count] != brack[i] :
                    return False 
                stack.pop(count)
                count=count-1

            elif i == '[' or i=='{' or i=='(':
                count=count+1
                stack.append(i)  
        if len(stack) > 0 :
            return False
        return True













































        