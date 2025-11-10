# Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Apple, Amazon, Google, Qualcomm, Microsoft, Bloomberg  

---

Given a sorted integer array `arr` of size `n`, your task is to replace the duplicates **in-place** such that each unique element appears only once, and the relative order of the elements is preserved.  

After replacing the duplicates, return the number of unique elements in the array.

---

### Explanation
Consider the number of unique elements of `arr` to be `k`.  
To be considered a valid solution, you need to do the following:

- Modify the array `arr` such that the first `k` elements of `arr` contain only the **unique elements**, in the same order they appeared initially.  
- The remaining elements in `arr` are irrelevant.  
- Return `k`, which is the number of unique elements in `arr`.

---

### Example 1
Input:  
n = 6  
arr = [5, 5, 7, 7, 9, 9]  

Output:  
3  
5 7 9  

**Explanation:**  
The given array contains three unique values: 5, 7, and 9.  
So, the length of the new array is 3.

---

### Example 2
Input:  
n = 9  
arr = [2, 2, 2, 6, 6, 6, 8, 8, 8]  

Output:  
3  
2 6 8  

**Explanation:**  
The given array contains three unique values: 2, 6, and 8.  
So, the length of the new array is 3.

---

### Your Task
Complete the provided `removeDuplicates` function that takes an array of integers `arr` and an integer `n` as arguments and returns the size of the new array formed by removing duplicate values.

---

### Constraints
- 1 ≤ n ≤ 10⁶  
- -10⁹ ≤ arr[i] ≤ 10⁹  

---

### Input Format
- The first line of input contains an integer `n`.  
- The second line of input contains `n` space-separated integers.

### Output Format
- The output represents an integer value indicating the new length of the modified array after removing all duplicate values.
