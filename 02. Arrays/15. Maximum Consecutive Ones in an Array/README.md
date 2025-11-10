# Maximum Consecutive Ones in an Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Amazon, Google, Bloomberg  

---

You are given an array `arr` of size `n` consisting of integers, where each integer can be either `0` or `1`.  
Your task is to find the **maximum number of consecutive 1s** in the array.

### Example 1
Input:  
n = 9  
arr = [0, 1, 0, 1, 1, 0, 1, 1, 1]  

Output:  
3  

**Explanation:**  
The maximum number of consecutive ones in the given array is `3`.

### Example 2
Input:  
n = 5  
arr = [0, 1, 1, 0, 1]  

Output:  
2  

**Explanation:**  
The maximum number of consecutive ones in the given array is `2`.

### Your Task
Complete the provided `maxConsecutiveOnes` function that takes an array of integers `arr` and an integer `n` as arguments and returns an integer representing the maximum number of consecutive 1s in the array.

### Constraints
- 2 ≤ n ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵  

### Input Format
- The first line contains an integer `n`, denoting the size of the array.  
- The second line contains `n` space-separated integers, representing the elements of the array `arr`.  
  Each element is either `0` or `1`.  

### Output Format
- The output represents a single integer denoting the maximum number of consecutive 1s in the array.

### LeetCode Link
<a href="https://leetcode.com/problems/max-consecutive-ones/" target="_blank">LeetCode – Max Consecutive Ones (Problem 485)</a>
