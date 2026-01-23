# String to Integer Conversion (atoi)

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Uber, Amazon, Google, Microsoft, Bloomberg  

---

Implement the function `stringToInteger(s)` that converts a string into a **32-bit signed integer**.

The conversion follows these rules:

1. **Leading Whitespace**  
   Ignore any leading whitespace characters `' '`.

2. **Sign Handling**  
   If the next character is `'-'`, the number is negative.  
   If the next character is `'+'`, the number is positive.  
   If no sign is present, assume the number is positive.

3. **Digit Parsing**  
   Read digits until a non-digit character is encountered or the string ends.  
   Ignore leading zeros.  
   If no digits are found, return `0`.

4. **32-bit Integer Range Handling**  
   Clamp the result within the range:
   - Minimum: `-2³¹`
   - Maximum: `2³¹ - 1`

---

### Example 1
Input:  
s = " -0037"

Output:  
-37

Explanation:  
- Leading spaces are ignored  
- '-' indicates negative number  
- Digits read: "0037" → 37  
- Final result: -37

---

### Example 2
Input:  
s = "279fg024"

Output:  
279

Explanation:  
- Digits are read until non-digit `'f'`  
- Remaining characters are ignored  

---

### Your Task
Implement the function `stringToInteger(s)` that returns the converted integer.

---

### Constraints
- 0 ≤ length of `s` ≤ 200  
- `s` contains letters, digits, spaces, `'+'`, `'-'`, and `'.'`

---

### Input Format
- A single line containing the string `s`

---

### Output Format
- A single integer after conversion

---

### LeetCode Link
https://leetcode.com/problems/string-to-integer-atoi/
