# Finding the Missing Number in an Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Apple, Amazon, Google, Microsoft, Adobe, Nvidia, Bloomberg  

---

You are given an array of n-1 unique integers from 1 to n, where n is a positive integer. The array is missing one of the integers from the range [1, n]. Your task is to find the missing integer in the array.

### Example 1
Input:  
n = 5  
arr = [1, 2, 4, 5]  

Output:  
3  

**Explanation:**  
The missing number from the given array in the range [1, 5] is 3.

### Example 2
Input:  
n = 10  
arr = [2, 5, 9, 1, 10, 6, 4, 3, 8]  

Output:  
7  

**Explanation:**  
The missing number from the given array in the range [1, 10] is 7.

### Your Task
Complete the provided `missingNumber` function that takes an array of integers `arr` and an integer `n` as arguments and returns an integer representing the missing integer in the array within the range [1, n].

### Constraints
- 2 ≤ n ≤ 10⁵  
- Elements are unique and lie in the range [1, n]

### Input Format
- The first line contains an integer `n`, denoting the size of the array.  
- The second line contains `n` space-separated integers, representing the elements of the array `arr`.

### Output Format
- The output represents a single integer denoting the missing number in the array.

### LeetCode Link  
<a href="https://leetcode.com/problems/missing-number/" target="_blank">LeetCode – Missing Number (Problem 268)</a>
