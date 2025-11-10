# Union of Two Sorted Arrays

**Difficulty:** Medium  
**Time Complexity:** O(m + n)  
**Space Complexity:** O(m + n)  
**Companies:** Amazon  

---

You are given two sorted arrays `a` and `b` of integers of length `m` and `n` respectively.  
Your task is to find the union of the arrays.

### Note
The union of two arrays is defined as the set containing all distinct elements from both arrays.

### Example 1
Input:  
m = 5, n = 4  
a = [3, 5, 5, 6, 6]  
b = [1, 2, 3, 5]  

Output:  
1 2 3 5 6  

**Explanation:**  
1, 2, 3, 5 and 6 are the elements included in the union set of both arrays.

### Example 2
Input:  
m = 6, n = 6  
a = [1, 3, 3, 7, 9, 11]  
b = [2, 4, 6, 6, 10, 12]  

Output:  
1 2 3 4 6 7 9 10 11 12  

**Explanation:**  
1, 2, 3, 4, 6, 7, 9, 10, 11 and 12 are the elements included in the union set of both arrays.

### Your Task
Complete the provided `unionOfTwoSortedArrays` function that takes two arrays of integers `a` and `b` as arguments and returns the array containing the union of these arrays.

### Constraints
- 1 ≤ m, n ≤ 10⁵  
- 0 ≤ a[i], b[i] ≤ 10⁵  

### Input Format
- The first line of input contains two integers `m` and `n`.  
- The second line of input contains `m` space-separated integers.  
- The third line of input contains `n` space-separated integers.  

### Output Format
- The output represents the set of union of input arrays.
