class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        non=list(freq.keys())
        result=sorted(non, key = lambda x: freq[x],reverse=True)

        return result[:k]

    