"""
Problem: Reverse Words in a String
Approach: Split words, reverse list, and join with single spaces
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverseWords(self, text):
        words = text.split()
        return " ".join(reversed(words))
