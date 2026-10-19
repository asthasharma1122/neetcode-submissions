class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        count=0
        num_set=set(nums)

        for num in num_set:
            if num-1 not in num_set:
                current=num
                count=1
                while current+1 in num_set:
                    current=current+1
                    count+=1
                max_len=max(max_len,count)
        return max_len
            