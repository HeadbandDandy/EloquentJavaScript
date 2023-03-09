def find_length(nums, k):
    # left pointer, current number, and answer set to zero
    left = curr = ans = 0
    # need to iterate and loop over the input
    for right in range(len(nums)):
        # at each number increment current number and add each number to the right
        curr += nums[right]
        # as long as sum is greater than limit move to left and increment left
        while curr > k:
            curr -= nums[left]
            left += 1
            # below is length of the window
        ans = max(ans, right - left + 1)
    
    return ans


# Second implemntation

def find_length(s):
    # below initializes variables to zero
    left = curr = ans = 0 
    # iterates over the input
    for right in range(len(s)):
        # if character is zero it will update window curr variable
        if s[right] == "0":
            curr += 1
            # if more than one zero, window needs to shrink by moving
            # left one spot in index
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
            # if window not breaking constraint the answer should be updated
        ans = max(ans, right - left + 1)
    
    return ans