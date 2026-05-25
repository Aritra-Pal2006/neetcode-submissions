from collections import defaultdict
class Solution:    
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final=[]
        newstrs=[]
        hashmap=defaultdict(list)
        for i in strs :
            newstrs.append(''.join(sorted(i)))

        for i,n in enumerate(newstrs) :
            hashmap[n].append(i)

        for key in hashmap :
            lis=[]
            for item in hashmap[key] :
                
                lis.append(strs[item])
            final.append(lis)
        return final

            

            



        