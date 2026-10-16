
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_res = []
        prod_pre = 1

        # Prefix product
        for i in range(len(nums)):
            pre_res.append(prod_pre)  ###Yes, exactly! 🎯 You've understood it correctly.Since we don't want to include the current element in its prefix product, we append the product before multiplying by the current element.
            prod_pre = prod_pre * nums[i]

        res = pre_res.copy()
        prod_suff = 1

        # Suffix product
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * prod_suff
            prod_suff = prod_suff * nums[i]

        return res
