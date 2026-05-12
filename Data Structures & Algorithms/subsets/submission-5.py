class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.lst =[]
        lst1= []
        def helper(idx):
                if idx == len(nums):
                     return self.lst.append(lst1[:])
                helper(idx+1)

                lst1.append(nums[idx])
                helper(idx+1)
                lst1.pop()
        helper(0)
        return self.lst
        



