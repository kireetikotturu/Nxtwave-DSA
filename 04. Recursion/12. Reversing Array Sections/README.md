# Reversing Array Sections

**Difficulty:** Easy  
**Time Complexity:** O(right − left + 1)  
**Space Complexity:** O(right − left + 1)  

---

You're given an array `arr` of size `n` and two indices `left` and `right`.  
Your task is to **recursively reverse the elements between indices `left` and `right` (inclusive)** while keeping the rest of the array unchanged.

### Example 1
Input:  
n = 7  
left = 2, right = 5  
arr = [1, 2, 3, 4, 5, 6, 7]

Output:  
[1, 2, 6, 5, 4, 3, 7]

**Explanation:**  
The subarray `[3, 4, 5, 6]` is reversed to `[6, 5, 4, 3]`.  
All other elements remain unchanged.

### Example 2
Input:  
n = 8  
left = 2, right = 6  
arr = [10, 20, 30, 40, 50, 60, 70, 80]

Output:  
[10, 20, 70, 60, 50, 40, 30, 80]

**Explanation:**  
The subarray `[30, 40, 50, 60, 70]` is reversed to `[70, 60, 50, 40, 30]`.

### Your Task
Complete the function `reverseArraySection()` that takes:
- an array `arr`,
- its size `n`,
- two indices `left` and `right`,  

and **recursively reverses** the subarray between `left` and `right`.

### Constraints
- 1 ≤ n ≤ 1000  
- 0 ≤ arr[i] ≤ 10⁵  
- 0 ≤ left ≤ right < n  

### Input Format
- First line: integer `n`  
- Second line: integers `left` and `right`  
- Third line: `n` space-separated integers (array elements)

### Output Format
- Output the modified array after reversing the specified section.
