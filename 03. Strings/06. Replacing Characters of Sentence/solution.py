"""
Problem: Replacing Characters of Sentence
Approach: Character-by-character replacement using ASCII values
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def replaceCharacters(self, s):
        result = []

        for ch in s:
            if ch == " ":
                result.append(ch)
            elif ch == "z":
                result.append("a")
            elif ch == "Z":
                result.append("A")
            else:
                result.append(chr(ord(ch) + 1))

        return "".join(result)
