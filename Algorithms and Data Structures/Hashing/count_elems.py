# need to declare a set of numbers
# if the set of numbers contains follows as such x + 1 print result
# if set of numbers does not contain x + 1 print zero

class Solution:
    def countElements(self, arr: list[int]) -> int:

        num_set = set(arr)
        count = 0

        for x in arr:
            if x + 1 in num_set:
                count += 1

        return count
            