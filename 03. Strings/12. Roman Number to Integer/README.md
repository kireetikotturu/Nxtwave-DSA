# Roman Number to Integer

**Difficulty:** Easy  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Oracle, Amazon, Google, Microsoft, Bloomberg  

---

Roman numerals are represented by the following symbols and values:

- I → 1  
- V → 5  
- X → 10  
- L → 50  
- C → 100  
- D → 500  
- M → 1000  

Roman numerals are usually written from **largest to smallest** from left to right.  
However, in some cases, **subtraction is used** instead of addition.

### Subtraction Rules
- `I` before `V` or `X` → 4 or 9  
- `X` before `L` or `C` → 40 or 90  
- `C` before `D` or `M` → 400 or 900  

You are given a Roman numeral string `s`.  
Your task is to **convert it into its corresponding integer value**.

---

### Example 1
Input:  
s = "II"

Output:  
2

**Explanation:**  
`II = 1 + 1 = 2`

---

### Example 2
Input:  
s = "XLVII"

Output:  
47

**Explanation:**  
`XL = 40`  
`VII = 7`  
Total = `40 + 7 = 47`

---

### Example 3
Input:  
s = "CMXC"

Output:  
990

**Explanation:**  
`CM = 900`  
`XC = 90`  
Total = `900 + 90 = 990`

---

### Your Task
Complete the function `romanToInteger()` that converts a Roman numeral string into an integer.

---

### Constraints
- 1 ≤ s.length ≤ 15  
- `s` contains only characters `I, V, X, L, C, D, M`  
- The Roman numeral is guaranteed to be valid  
- 1 ≤ result ≤ 3999  

---

### Input Format
- A single Roman numeral string `s`

---

### Output Format
- A single integer representing the converted value

---

### LeetCode Link
https://leetcode.com/problems/roman-to-integer/
