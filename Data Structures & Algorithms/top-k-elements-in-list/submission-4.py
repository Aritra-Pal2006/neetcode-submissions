class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums2=set(nums)
        hashmap={}
        lis=[]
        for i in nums2 :
            count=0
            for j in nums :
                if i == j :
                    count=count+1
            hashmap[i]=count

        for i in range (0,k) :
            max1=0
            maxkey=0
            for key in hashmap :
                if hashmap[key]>=max1 :
                    maxkey=key
                    max1=hashmap[key]
            
            lis.append(maxkey)
            hashmap.pop(maxkey)


        return lis   
            
        