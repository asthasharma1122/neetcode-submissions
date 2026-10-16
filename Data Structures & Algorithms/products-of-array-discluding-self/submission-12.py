class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_res = []
        prod_pre = 1

        for i in range(len(nums)):
            pre_res.append(prod_pre)
            prod_pre = prod_pre * nums[i]

        res = pre_res.copy()
        prod_suff = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * prod_suff
            prod_suff = prod_suff * nums[i]

        return res