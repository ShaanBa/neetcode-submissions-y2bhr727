class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1] * len(nums)
        prefix = [1] * len(nums)
        output = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[0] = 1
            else:
                prefix[i] = prefix[i-1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1,):
            if i == len(nums) - 1:
                postfix[len(nums) - 1] = 1 
            else:
                postfix[i] = postfix[i+1] * nums[i + 1]

        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]
        
        return output


            


            