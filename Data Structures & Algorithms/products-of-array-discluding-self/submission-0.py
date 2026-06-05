class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        

        for i in range (0,len(nums)) :
            new=nums.copy()
            mul=1
            new.pop(i)
            for j in new :
                mul=mul*j
            arr.append(mul)
        return arr
        


        