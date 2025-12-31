# Finding the Kth Digit from the Right in A^B

**Difficulty:** Easy  
**Time Complexity:** O(B + K)  
**Space Complexity:** O(1)  

---

You are given three integers `A`, `B`, and `K`.  
Your task is to find the **Kth digit from the right** in the number obtained by raising `A` to the power `B` (i.e., `A^B`).

### Example 1
Input:  
A = 3, B = 3, K = 1  

Output:  
7  

**Explanation:**  
3³ = 27, and the 1st digit from the right is `7`.

### Example 2
Input:  
A = 5, B = 2, K = 2  

Output:  
2  

**Explanation:**  
5² = 25, and the 2nd digit from the right is `2`.

### Your Task
Implement the function `kthDigit()` which takes three integers `A`, `B`, and `K` as arguments and returns the Kth digit from the right of the number `A^B`.

### Constraints
- 1 ≤ A, B ≤ 15  
- 1 ≤ K ≤ number of digits in `A^B`  

### Input Format
- A single line containing three space-separated integers `A`, `B`, and `K`.

### Output Format
- Output represents the Kth digit of `A^B` from the right.
