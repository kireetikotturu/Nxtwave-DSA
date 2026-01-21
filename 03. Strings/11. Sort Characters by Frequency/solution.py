"""
Problem: Sort Characters by Frequency
Approach: Frequency Array + Sorting
Difficulty: Medium
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

class Solution:
    def sortCharactersByFrequency(self, s):
        freq = [(0, "") for _ in range(123)]  # ASCII range

        for ch in s:
            freq[ord(ch)] = (freq[ord(ch)][0] + 1, ch)

        freq.sort(reverse=True, key=lambda x: x[0])

        result = ""
        for count, ch in freq:
            result += count * ch

        return result
