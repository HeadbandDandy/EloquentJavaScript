# sets ignore duplicates so we can put all frequency values into a set and check if the length is 1


from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int) # counts frequency within map
        for c in s:
            counts[c] += 1
        
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1 