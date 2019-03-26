# 290. Word Pattern
# Easy

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not str: return False
        # split str into word array
        words = str.split(' ')
        if len(words) != len(pattern): return False
        # use dict to keep track of pattern
        ptnmap = {}
        for i, word in enumerate(words):
            if pattern[i] in ptnmap:
                if word != ptnmap[pattern[i]]:
                    return False
            else:
                if word in ptnmap.values():
                    return False
                ptnmap[pattern[i]] = word
        return True

sol = Solution()
print(sol.wordPattern('abba', "dog cat cat dog"))
print(sol.wordPattern("abba", "dog cat cat fish"))