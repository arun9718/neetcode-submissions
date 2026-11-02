class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]*len(nums)
        suffix_mul = [1]*len(nums)
        prefix_mul[0]=nums[0]
        suffix_mul[len(nums)-1]=nums[len(nums)-1]

        for i in range(1,len(nums)):
            prefix_mul[i]=prefix_mul[i-1]*nums[i]

        for i in range(len(nums)-2,0,-1):
            suffix_mul[i]=suffix_mul[i+1]*nums[i]
        

        res=[1]*len(nums)
        res[0]=suffix_mul[1]
        res[len(nums)-1]=prefix_mul[len(nums)-2]
        for i in range(1,len(nums)-1):
            res[i]=prefix_mul[i-1]*suffix_mul[i+1]
        
        return res
        


        