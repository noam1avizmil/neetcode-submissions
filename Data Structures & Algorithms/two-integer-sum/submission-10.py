import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            temp = copy.deepcopy(nums)
            temp.pop(i)
            if diff in temp:
                idx = temp.index(diff) +1
                return [i,idx]
        
