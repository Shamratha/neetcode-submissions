class Solution:
    def twoSum(self,arr,target):
        nums=[(x,i)for i, x in enumerate(arr)]
        nums.sort()
        l,r=0,len(nums)-1
        while l<r:
            s=nums[l][0]+nums[r][0]
            if s==target:
                indices = [nums[l][1],nums[r][1]]
                indices.sort()
                return indices
            elif s<target:
                l+=1
            else:
                r-=1
        return[-1,-1]
