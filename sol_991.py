# leetcode contest 123 question 991: Broken Calculator
# On a broken calculator that has a number showing on its display, we can perform two operations:
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.

# Return the minimum number of operations needed to display the number Y.

# 1 <= X <= 10^9
# 1 <= Y <= 10^9

# Note: started off the problem by using recursion to compute the answer
# after doubling first against subtracting one first. This is a trap I fell into
# because the number of recursive calls grow exponentially and it does not work well on large
# numbers.

# The problem is best solved by working backwards. Divide Y by 2 until Y is less than X, 
# if Y is odd, we +1 to Y if Y is even we divide by 2
# Time complexity: O(log(Y))

class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        ans = 0
        while (Y > X):
            ans += 1
            if Y%2: Y+=1
            else: Y/=2
        
        return int(ans + X - Y)

if __name__ == "__main__":
    sol = Solution()
    
    # Input: X = 2, Y = 3
    # Output: 2
    # Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
    print(sol.brokenCalc(2,3))

    # Input: X = 5, Y = 8
    # Output: 2
    # Explanation: Use decrement and then double {5 -> 4 -> 8}.
    print(sol.brokenCalc(5,8))

    # Input: X = 3, Y = 10
    # Output: 3
    # Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
    print(sol.brokenCalc(3,10))

    # Input: X = 1024, Y = 1
    # Output: 1023
    # Explanation: Use decrement operations 1023 times.
    print(sol.brokenCalc(1024,1))

    print(sol.brokenCalc(1,1000000000))