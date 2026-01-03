"""
Problem: Palindrome of a String
Approach: Recursion with Two-Pointer Comparison
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def helperCheckPalindrome(self, s, i, N):
        if i >= N // 2:
            return True
        if s[i] != s[N - i - 1]:
            return False
        return self.helperCheckPalindrome(s, i + 1, N)

    def checkPalindrome(self, s):
        return self.helperCheckPalindrome(s, 0, len(s))
