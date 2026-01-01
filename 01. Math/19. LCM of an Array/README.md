# LCM of an Array

**Difficulty:** Easy  
**Time Complexity:** O(n · log(max(arr[i])))  
**Space Complexity:** O(1)  

---

You are given an array of integers `arr` of size `n`.  
Your task is to find the **Least Common Multiple (LCM)** of all the elements of the array, modulo **(10⁹ + 7)**.

### Example 1
Input:  
arr = [1, 2, 4, 6]  

Output:  
12  

**Explanation:**  
LCM of 1, 2, 4, and 6 is `12`.

### Example 2
Input:  
arr = [2, 3, 9, 4, 7]  

Output:  
252  

**Explanation:**  
LCM of 2, 3, 9, 4, and 7 is `252`.

### Your Task
Complete the function `lcmArray()` that takes an array of integers `arr` as an argument and returns the LCM of the array elements modulo **(10⁹ + 7)**.

### Constraints
- 1 ≤ n ≤ 10⁴  
- 1 ≤ arr[i] ≤ 10⁴  

### Input Format
- The first line contains an integer `n`, representing the size of the array.  
- The second line contains `n` space-separated integers representing the elements of `arr`.

### Output Format
- Output a single integer representing the LCM of the array elements modulo **(10⁹ + 7)**.
