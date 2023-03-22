# Straight forward solution...ans placed in an array. Nums are matched in a set
# the problem will iterate over set to see if any numbers match x + 1 or x - 1


def find_numbers(nums):
    
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    
    return ans