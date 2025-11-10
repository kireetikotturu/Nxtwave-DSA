# Find the Element K in the Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** PayTM  

---

You are given an array of integers `arr` of size `n` and a number `k`.  
Your task is to determine if the array contains the element `k`.

If the array contains the element, return the index (0-based indexing) of `k`; otherwise, return `-1`.

### Note
If the same element is present more than once in the array, return the index of the first occurrence of that element.

### Example 1
Input:  
n = 5, k = 3  
arr = [4, 3, 2, 1, 5]  

Output:  
1  

**Explanation:**  
In the input array, element `3` is present at index `1`.

### Example 2
Input:  
n = 8, k = 9  
arr = [2, 4, 6, 1, 0, 3, 5, 8]  

Output:  
-1  

**Explanation:**  
In the input array, element `9` is not present.  
So, the output is `-1`.

### Your Task
Complete the provided `search` function that takes an array of integers `arr` and two integers `n` and `k` as arguments and returns the index of `k` if it is present in the array; otherwise, return `-1`.

### Constraints
- 1 ≤ n ≤ 10⁵  
- 1 ≤ k ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵  

### Input Format
- The first line of input contains two integers `n` and `k`.  
- The second line of input contains `n` space-separated integers.  

### Output Format
- The output represents the index of `k` in the array.
