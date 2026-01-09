"""
Problem: Group Anagrams
Approach: Character frequency as hash key
Difficulty: Medium
Time Complexity: O(N × K)
Space Complexity: O(N × K)
"""

class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            key = "#".join(map(str, freq))

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
