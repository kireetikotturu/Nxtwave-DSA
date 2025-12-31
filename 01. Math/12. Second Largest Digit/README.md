# Second Largest Digit

**Difficulty:** Medium  
**Time Complexity:** O(log₁₀N)  
**Space Complexity:** O(1)  

---

You are given an integer `num` that may contain repeating digits.  
Your task is to return the **second largest digit** in the number.

If there is no second largest digit, return `-1`.

### Example 1
Input:  
num = 4052  

Output:  
4  

**Explanation:**  
The digits in the number are {0, 4, 5, 2}.  
The largest digit is `5` and the second largest digit is `4`.

### Example 2
Input:  
num = 7998852  

Output:  
8  

**Explanation:**  
The digits in the number are {7, 9, 9, 8, 8, 5, 2}.  
The largest digit is `9` and the second largest digit is `8`.

### Your Task
Complete the function `secondLargestDigit()` that takes an integer `num` as an argument and returns the second largest digit present in the number.

### Constraints
- 0 ≤ num ≤ 10⁹  

### Input Format
- Input is a single line consisting of an integer `num`.

### Output Format
- Output is a single integer representing the second largest digit of `num`.
