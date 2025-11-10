# Check if an Array is Sorted

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Google, Bloomberg  

---

You are given an array of integers `arr` with size `n`.  
Your task is to check whether the given array is sorted in non-decreasing order or not.  

If it is sorted in non-decreasing order, return `true`; otherwise, return `false`.

### Example 1
Input:  
n = 5  
arr = [1, 2, 3, 4, 5]  

Output:  
true  

**Explanation:**  
The given array is sorted in non-decreasing order.

### Example 2
Input:  
n = 4  
arr = [7, 3, 6, 2]  

Output:  
false  

**Explanation:**  
The given array is not sorted in non-decreasing order.

### Your Task
Complete the provided `isSorted` function that takes an array of integers `arr` and an integer `n` as arguments and returns `true` if the array is sorted; otherwise, returns `false`.

### Constraints
- 1 ≤ n ≤ 10⁶  
- -10⁹ ≤ arr[i] ≤ 10⁹  

### Input Format
- The first line of input contains an integer `n`.  
- The second line of input contains `n` space-separated integers.

### Output Format
- The output represents `true` if the input array is sorted in non-decreasing order; otherwise `false`.
