# Move Zeros to the Front of an Array

**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Companies:** Apple, Amazon, Google, Microsoft, Bloomberg  

---

You are given an array of integers `arr` of size `n`.  
Your task is to move all the zeros in the array to the front while preserving the relative order of the non-zero elements.

### Example 1
Input:  
n = 7  
arr = [0, 1, 0, 3, 0, 12, 0]  

Output:  
0 0 0 0 1 3 12  

**Explanation:**  
After moving all of the zeros to the front of the array, the array becomes `[0, 0, 0, 0, 1, 3, 12]`.

### Example 2
Input:  
n = 5  
arr = [0, 0, 0, 0, 0]  

Output:  
0 0 0 0 0  

**Explanation:**  
After moving all of the zeros to the front of the array, the array becomes `[0, 0, 0, 0, 0]`.

### Your Task
Complete the provided `moveZerosToFront` function that takes an array of integers `arr` and an integer `n` as arguments and moves all the zeros in the array to the front while preserving the relative order of the non-zero elements.

### Constraints
- 1 ≤ n ≤ 10⁴  
- -10⁶ ≤ arr[i] ≤ 10⁶  

### Input Format
- The first line of input contains an integer `n`.  
- The second line of input contains `n` space-separated integers.  

### Output Format
- The output represents the modified array after moving all the zeros in the array to the front.
