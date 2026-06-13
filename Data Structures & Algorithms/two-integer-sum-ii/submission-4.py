class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp=0
        lp=len(numbers)-1

        while(fp!=lp) :
            if numbers[fp]+numbers[lp] == target :
                return [fp+1,lp+1]
            elif  numbers[fp]+numbers[lp] > target :
                lp=lp-1
            elif numbers[fp]+numbers[lp]< target :
                fp=fp+1

        return 