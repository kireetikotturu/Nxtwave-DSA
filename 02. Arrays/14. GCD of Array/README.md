# GCD of Array

**Difficulty:** Easy  
**Time Complexity:** O(N * log(min(arr[i])))  
**Space Complexity:** O(1)  

---

Given an array of `N` positive integers, the task is to find the **greatest common divisor (GCD)** of all the elements in the array.

### Example 1
Input:  
N = 3  
arr = [2, 4, 6]  

Output:  
2  

**Explanation:**  
The GCD of 2, 4, and 6 is 2.

### Example 2
Input:  
N = 1  
arr = [1]  

Output:  
1  

**Explanation:**  
The GCD of a single number is the number itself, so the GCD is 1.

### Your Task
Complete the provided `gcd()` function, which accepts two parameters: an integer `N` and an array `arr`.  
The function should return the greatest common divisor (GCD) of all the elements in the array.

### Constraints
- 1 ≤ N ≤ 10⁵  
- 1 ≤ arr[i] ≤ 10⁵  

### Input Format
- The first line contains a single integer `N`, which represents the number of elements in the array.  
- The second line contains `N` space-separated positive integers, where each integer represents an element of the array.

### Output Format
- The output represents a single integer, which is the greatest common divisor (GCD) of all the elements in the array.

### LeetCode Link
<a href="https://leetcode.com/problems/find-greatest-common-divisor-of-array/" target="_blank">LeetCode – Find Greatest Common Divisor of Array (Problem 1979)</a>
