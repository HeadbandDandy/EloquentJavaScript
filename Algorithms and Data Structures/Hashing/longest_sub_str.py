from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    # map for characters and sliding window set above
    
    # iterate over input
    for right in range(len(s)):
        # each character add to window
        counts[s[right]] += 1
        # while length of the count is greater than k remove from the left
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                # after decrementing if count is 0 all chars have been removed from the window
                del counts[s[left]]
            left += 1
        # answer set below
        ans = max(ans, right - left + 1)
    
    return ans