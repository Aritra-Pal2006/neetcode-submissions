class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2="".join(char.lower() for char in s if char.isalnum())
        lis=list(str2)

        last=len(lis)-1

        for i in range(0,len(lis)//2) :
            if (lis[i].casefold() != lis[last].casefold()) :
                return False
            last=last-1

        return True

        