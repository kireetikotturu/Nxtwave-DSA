"""
Problem: Isomorphic Strings
Approach: Bidirectional character mapping using hash maps
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def helperFunction(self, s1, s2):
        mapping = {}

        for i in range(len(s1)):
            if s1[i] in mapping:
                if mapping[s1[i]] != s2[i]:
                    return False
            mapping[s1[i]] = s2[i]

        return True

    def isomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False

        return self.helperFunction(s1, s2) and self.helperFunction(s2, s1)
