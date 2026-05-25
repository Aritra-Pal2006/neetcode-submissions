class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find={}
        for i in range(0,len(nums)):
            to_find=target-nums[i]
            if  to_find in find :
                if find[to_find] != i :
                    return [find[to_find],i]

            find[nums[i]]=i

        
        