from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic1 ={}
        for i in strs:
            temp = sorted(list(i))
            temp = ''.join(temp)
            if temp not in dic1.keys():
                dic1[temp] = i
            else:
                dic1[temp] += ","+i
        return [v.split(",") for v in dic1.values()]

 
            
        