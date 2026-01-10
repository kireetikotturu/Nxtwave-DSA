# Next Greater Element

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  

---

You are given an array `arr` of size `n`.  
Your task is to find the **Next Greater Element (NGE)** for every element in the array.

The **Next Greater Element** for an element is the **closest element to its right that is greater than it**.

If no such element exists, return `-1` for that position.  
The last element always has `-1` as its NGE.

### Example 1
Input:  
arr = [3, 8, 4, 1, 2]

Output:  
[8, -1, -1, 2, -1]

**Explanation:**  
- Next greater of 3 → 8  
- Next greater of 8 → -1  
- Next greater of 4 → -1  
- Next greater of 1 → 2  
- Next greater of 2 → -1  

### Example 2
Input:  
arr = [5, 3, 9, 4, 7]

Output:  
[9, 9, -1, 7, -1]

### Your Task
Complete the function `nextGreaterElement()` that returns the next greater element for each index.

### Constraints
- 1 ≤ n ≤ 10³  
- 0 ≤ arr[i] ≤ 10⁴  

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

### Output Format
- A single line of `n` space-separated integers representing NGE values

### LeetCode Link
<a href="https://leetcode.com/problems/next-greater-element-i/" target="_blank">
LeetCode – Next Greater Element I (Problem 496)
</a>
