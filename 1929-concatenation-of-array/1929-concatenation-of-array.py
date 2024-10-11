class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        extension = nums.copy()
        nums.extend(extension)
        return nums
        
