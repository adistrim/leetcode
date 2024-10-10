class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        ans = [int(i) for i in str(num)]
        return ans