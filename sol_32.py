# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        
        # O(n^2) : for each letter in the string, go through every possible substring starting from
        # itself, return the longest one
        valid = set()
        longestValid = 0
        def validParen(s, k):
            longest = 0
            count = 0
            for i in range(k, len(s)):
                if s[i] == '(':
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    if (i - k + 1 > longest):
                        longest = i - k + 1
                elif count == -1:
                    return longest
            return longest
        for j in range(len(s)):
            tmp = validParen(s, j)
            if tmp > longestValid:
                longestValid = tmp
        return longestValid

sol = Solution()
print(sol.longestValidParentheses("())"))
print(sol.longestValidParentheses("()()(())()())"))
print(sol.longestValidParentheses(")("))