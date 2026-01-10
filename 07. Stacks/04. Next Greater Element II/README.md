# Next Greater Element II

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Apple, Amazon, Microsoft, Google  

---

You are given a **circular integer array** `arr` of size `n`  
(i.e., the next element of `arr[n-1]` is `arr[0]`).

Your task is to find the **Next Greater Element (NGE)** for each element.

The **Next Greater Element** of `arr[i]` is the first element greater than `arr[i]`
encountered while traversing the array **circularly**.

If no such element exists, return `-1` for that position.

### Example 1
Input:  
arr = [1, 5, 0, 8, 4, -9, 2]

Output:  
[5, 8, 8, -1, 5, 2, 5]

**Explanation:**  
- NGE of 1 → 5  
- NGE of 5 → 8  
- NGE of 0 → 8  
- NGE of 8 → -1  
- NGE of 4 → 5  
- NGE of -9 → 2  
- NGE of 2 → 5  

### Example 2
Input:  
arr = [10]

Output:  
[-1]

### Your Task
Complete the function `nextGreaterElementII()` that returns the next greater element
for each index in a circular array.

### Constraints
- 1 ≤ arr.length ≤ 10³  
- −10⁷ ≤ arr[i] ≤ 10⁷  

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

### Output Format
- A single line containing `n` space-separated integers

### LeetCode Link
<a href="https://leetcode.com/problems/next-greater-element-ii/" target="_blank">
LeetCode – Next Greater Element II (Problem 503)
</a>
