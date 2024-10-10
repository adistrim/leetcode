class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sseett = set()
        for i in nums:
            if i in sseett:
                return True
            sseett.add(i)
        return False