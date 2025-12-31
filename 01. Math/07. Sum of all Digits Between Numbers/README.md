# Sum of all Digits Between Numbers

**Difficulty:** Easy  
**Time Complexity:** O((N2 − N1 + 1) × log₁₀N2)  
**Space Complexity:** O(1)  

---

You are given two integers `N1` and `N2`.  
Your task is to calculate the sum of all the digits of the numbers from `N1` to `N2` (inclusive).

### Example 1
Input:  
N1 = 10  
N2 = 13  

Output:  
10  

**Explanation:**  
The sum of all digits from 10 to 13 is:  
(1 + 0) + (1 + 1) + (1 + 2) + (1 + 3) = 10.

### Example 2
Input:  
N1 = 21  
N2 = 31  

Output:  
70  

**Explanation:**  
The sum of all digits from 21 to 31 is:  
(2 + 1) + (2 + 2) + (2 + 3) + (2 + 4) + (2 + 5) + (2 + 6) + (2 + 7) + (2 + 8) + (2 + 9) + (3 + 0) + (3 + 1) = 70.

### Your Task
Complete the function `calculateDigitSum()` which takes two integers `N1` and `N2` as arguments and returns the sum of all digits present in the numbers from `N1` to `N2` (inclusive).

### Constraints
- 1 ≤ N1, N2 ≤ 10⁵  
- N2 is always greater than N1  

### Input Format
- A single line containing two space-separated integers `N1` and `N2`.

### Output Format
- Print a single integer representing the sum of all digits in the numbers from `N1` to `N2` (inclusive).
