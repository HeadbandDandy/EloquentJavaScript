def find_best_subarray(nums, k):
    # finds sum of first window/k element
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    # answer set to value and iterate over rest of windows
    # each window sum can be found by adding next element and removing previous element
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans