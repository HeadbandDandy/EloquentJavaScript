def check_for_target(nums, target):
    # checks for two pointers
    left = 0
    right = len(nums) - 1

    # loops through array until pointers meet eaach other
    while left < right:
        # if current number is equal to target returns true
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        # if current number is greater than target the right 
        #  index will decrement one and the next will increment 
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False