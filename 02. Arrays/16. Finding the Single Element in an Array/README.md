# Finding the Single Element in an Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Airbnb, Amazon, Google, Microsoft, Bloomberg  

---

You are given an array of integers `arr` of size `n`, where every element appears exactly twice except for one element, which appears only once.  

Your task is to find the element that occurs only once in the array.

### Example 1
Input:  
n = 7  
arr = [3, 5, 2, 1, 2, 5, 3]  

Output:  
1  

**Explanation:**  
In the given array, all elements occur twice except for `1`.

### Example 2
Input:  
n = 5  
arr = [2, 2, 3, 3, 1]  

Output:  
1  

**Explanation:**  
In the given array, all elements occur twice except for `1`.

### Your Task
Complete the provided `findSingleElement` function that takes an array of integers `arr` and an integer `n` as arguments and returns an integer representing the element that occurs only once in the array.

### Constraints
- 2 ≤ n ≤ 10⁵  

### Input Format
- The first line contains an integer `n`, denoting the size of the array.  
- The second line contains `n` space-separated integers, representing the elements of the array `arr`.

### Output Format
- The output represents a single integer denoting the element that appears only once in the array.

### LeetCode Link
<a href="https://leetcode.com/problems/single-number/" target="_blank">LeetCode – Single Number (Problem 136)</a>
