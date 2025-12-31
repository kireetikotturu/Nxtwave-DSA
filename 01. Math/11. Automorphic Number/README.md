# Automorphic Number

**Difficulty:** Medium  
**Time Complexity:** O(log₁₀N)  
**Space Complexity:** O(1)  

---

You are given an integer `num`.  
Your task is to determine whether it is an **Automorphic number** or not.

### Note
A number is said to be **Automorphic** if the square of the number ends with the same digits as the number itself.

### Example 1
Input:  
num = 76  

Output:  
true  

**Explanation:**  
Square of the number is `5776`, which ends with the same digits as the number itself.  
Hence, `76` is an Automorphic number.

### Example 2
Input:  
num = 382  

Output:  
false  

**Explanation:**  
Square of the number is `145924`, which does not end with the same digits as the number itself.  
Hence, `382` is not an Automorphic number.

### Your Task
Complete the function `checkAutomorphicNumber()` that takes an integer `num` as an argument and returns `true` if the number is Automorphic, otherwise `false`.

### Constraints
- 1 ≤ num ≤ 10⁴  

### Input Format
- Input is a single line consisting of an integer `num`.

### Output Format
- Output is a single line containing `true` if `num` is an Automorphic number, otherwise `false`.
