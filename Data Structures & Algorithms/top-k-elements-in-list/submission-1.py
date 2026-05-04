class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        apr = {}

        for n in nums:
            if n in apr:
                apr[n] = apr[n] + 1
            else:
                apr[n] = 1

        res = []
        sorted_dict = dict(sorted(apr.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)
        for value, aprCount in sorted_dict.items():
            print(value, aprCount)
            res.append(value)

        return res[:k]

