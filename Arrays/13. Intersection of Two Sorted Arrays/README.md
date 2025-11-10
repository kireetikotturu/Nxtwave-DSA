# Intersection of Two Sorted Arrays

**Difficulty:** Easy  
**Time Complexity:** O(m + n)  
**Space Complexity:** O(min(m, n))  

---

You are given two sorted arrays `a` and `b` of integers of length `m` and `n` respectively.  
Your task is to find the intersection of the arrays.

### Note
The intersection of two sorted arrays is a set of elements that are common to both arrays.

### Example 1
Input:  
m = 6, n = 6  
a = [1, 2, 3, 3, 4, 4]  
b = [3, 4, 4, 5, 6, 6]  

Output:  
3 4 4  

**Explanation:**  
3, 4 and 4 are the elements common in both the arrays.

### Example 2
Input:  
m = 6, n = 7  
a = [1, 3, 3, 7, 9, 11]  
b = [2, 3, 4, 6, 6, 10, 12]  

Output:  
3  

**Explanation:**  
3 is the only element common in both the arrays.

### Your Task
Complete the provided `intersectionSortedArrays` function that takes two arrays of integers `a` and `b` as arguments and returns the array containing the intersection of these arrays.

### Constraints
- 1 ≤ m, n ≤ 10⁵  
- 0 ≤ a[i], b[i] ≤ 10⁵  

### Input Format
- The first line of input contains two integers `m` and `n`.  
- The second line of input contains `m` space-separated integers.  
- The third line of input contains `n` space-separated integers.  

### Output Format
- The output represents the elements common in both the input arrays in sorted order.

### LeetCode Link
<a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/" target="_blank">LeetCode – Intersection of Two Arrays II (Problem 350)</a>
