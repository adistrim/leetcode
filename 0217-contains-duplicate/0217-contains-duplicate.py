class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # create a hashmap (called set in python)
        # iterate through the elements of the nums array
        # check if the current element is present in the hashmap or not
        # if not present then add that element into the hashmap
        # if present then return True because that indicates duplicate

        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False

