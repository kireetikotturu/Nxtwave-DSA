"""
Problem: First Non-Repeating Character in a String
Approach: Frequency Count + Queue
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import deque

class Solution:
    def firstUniqueCharacter(self, n, s):
        freq = [0] * 26
        q = deque()

        for i, ch in enumerate(s):
            freq[ord(ch) - ord('a')] += 1
            q.append(i)

        while q and freq[ord(s[q[0]]) - ord('a')] > 1:
            q.popleft()

        return q[0] if q else -1
