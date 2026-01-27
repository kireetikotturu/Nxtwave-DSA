# Minimum Length Subarray with Sum at Least K

**Difficulty:** Medium  
**Approach:** Sliding Window (Two Pointers)  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Google, Microsoft, ByteDance, Goldman Sachs, Bloomberg, Facebook, Oracle, Apple, Wish, SAP  

---

You are given an array `A` of `N` positive integers and an integer `K`.

Your task is to find the **minimum length of a contiguous subarray** whose **sum is greater than or equal to `K`**.

If no such subarray exists, return `0`.

---

### Example 1
Input:  
N = 7, K = 9  
A = [5, 3, 1, 2, 4, 3, 6]

Output:  
2

**Explanation:**  
Subarrays with sum ≥ 9 are:
- [5, 3, 1] → sum = 9 (length 3)
- [2, 4, 3] → sum = 9 (length 3)
- [3, 6] → sum = 9 (length 2)

Minimum length is **2**.

---

### Example 2
Input:  
N = 10, K = 8  
A = [7, 5, 9, 3, 6, 2, 6, 7, 5, 10]

Output:  
1

**Explanation:**  
Single element subarrays like `[9]` and `[10]` already satisfy the condition.  
Minimum length is **1**.

---

### Your Task
Implement a solution to find the **minimum length subarray** with sum ≥ `K`.

---

### Constraints
- 1 ≤ N ≤ 3 × 10⁵  
- 1 ≤ K ≤ 3 × 10⁶  
- 1 ≤ A[i] ≤ 10⁵  

---

### Input Format
- First line: two space-separated integers `N` and `K`
- Second line: `N` space-separated integers representing array `A`

---

### Output Format
- Print a single integer representing the minimum subarray length  
- Print `0` if no such subarray exists

---

### LeetCode Link
https://leetcode.com/problems/minimum-size-subarray-sum/
