class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = Counter(nums).most_common(1)[0][0]
        return s
