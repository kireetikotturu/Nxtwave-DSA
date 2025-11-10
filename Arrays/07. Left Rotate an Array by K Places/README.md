# Left Rotate an Array by K Places

**Difficulty:** Medium  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

You are given an array of integers `arr` of size `n` and a number of positions `k`.  
Your task is to rotate the array to the left by `k` positions.

---

### Example 1
Input:  
n = 5, k = 3  
arr = [1, 2, 3, 4, 5]  

Output:  
4 5 1 2 3  

**Explanation:**  
After rotating the array to the left by 3 positions, the array becomes `[4, 5, 1, 2, 3]`.

---

### Example 2
Input:  
n = 10, k = 100  
arr = [42, 38, 28, 24, 39, 49, 33, 49, 21, 25]  

Output:  
42 38 28 24 39 49 33 49 21 25  

**Explanation:**  
After rotating the array to the left by 100 positions, the array becomes `[42, 38, 28, 24, 39, 49, 33, 49, 21, 25]`.

---

### Your Task
Complete the provided `leftRotate` function that takes an array of integers `arr` and two integers `n` and `k` as arguments and rotates the array to the left by `k` positions.

---

### Constraints
- 1 ≤ n ≤ 10⁵  
- 1 ≤ k ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵  

---

### Input Format
- The first line of input contains two integers `n` and `k`.  
- The second line of input contains `n` space-separated integers.

### Output Format
- The output represents the modified array after rotating it to the left by `k` positions.

---

### LeetCode Link
[LeetCode – Rotate Array](https://leetcode.com/problems/rotate-array/)
