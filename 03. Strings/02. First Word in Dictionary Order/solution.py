"""
Problem: First Word in Dictionary Order
Approach: Compare words using lowercase for dictionary comparison
Difficulty: Easy
Time Complexity: O(N × M)
Space Complexity: O(N)
"""

class Solution:
    def firstWordInDictionaryOrder(self, s):
        words = s.split()
        smallest = words[0]

        for word in words:
            if word.lower() < smallest.lower():
                smallest = word

        return smallest
