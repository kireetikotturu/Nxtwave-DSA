# Valid Variable Name

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  

---

You are given a string `S` representing a variable name.  
Your task is to check whether `S` is a **valid variable name**.

A variable name is considered valid if it contains **only**:
- Uppercase letters (A–Z)
- Lowercase letters (a–z)
- Digits (0–9)

### Note
Unicode value ranges:
- A–Z → 65 to 90  
- a–z → 97 to 122  
- 0–9 → 48 to 57  

### Example 1
Input:  
S = "eachNumber"

Output:  
True

**Explanation:**  
All characters are alphabetic letters.

### Example 2
Input:  
S = "is even"

Output:  
False

**Explanation:**  
The string contains a space, which is not allowed.

### Your Task
Check whether the given string `S` is a valid variable name and print `True` or `False`.

### Input Format
- A single line containing the string `S`

### Output Format
- Print `True` if valid, otherwise print `False`
