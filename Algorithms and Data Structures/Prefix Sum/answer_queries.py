# prefix sums allow us to find the sum of any subarray in 0(1) time complexity
# starts with one element that is iterated over from 1 Index
# Last element of the prefix represents the sum of all elements in input 
# up to but not including the i

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans