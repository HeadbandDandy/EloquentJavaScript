# solution below declares variable seen as set
# Once character is seen for first time it is placed within a set
# Iterate over input and if character has already been seen it needs to print repeated character


class Solution:
    def repeatedCharacter(self, s: str) -> str:

        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "
