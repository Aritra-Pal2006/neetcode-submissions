class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        index=None
        while(left <= right ) :
            mid=(left+right)//2
            if target == nums[mid] :
                index=mid
                break
            elif target > nums[mid] :
                left=mid+1
                
            elif target < nums[mid] :
                right=mid-1
        if index == None :
            return -1 
        else :
            return index


        