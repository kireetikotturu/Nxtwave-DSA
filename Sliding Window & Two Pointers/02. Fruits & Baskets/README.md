# Fruits & Baskets

**Difficulty:** Medium  
**Approach:** Sliding Window + Hash Map  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Companies:** Yahoo, Amazon, Google, Adobe, Microsoft  

---

You are visiting a farm where fruit trees are planted in a single row from left to right.  
The type of fruit produced by each tree is represented by an integer array `trees`, where `trees[i]`
denotes the fruit type at position `i`.

You want to collect as many fruits as possible under the following rules:

- You have **two baskets**
- Each basket can hold **only one type of fruit**
- There is **no limit** on the number of fruits in a basket
- You must start from **any tree** and move **only to the right**
- You must pick **exactly one fruit from each tree**
- You must **stop** when a third fruit type appears

Return the **maximum number of fruits** you can collect.

---

### Example 1
Input:  
trees = [3, 1, 3]

Output:  
3

**Explanation:**  
Only two fruit types (3 and 1) are present, so all fruits can be collected.

---

### Example 2
Input:  
trees = [4, 2, 3, 3]

Output:  
3

**Explanation:**  
The longest valid subarray with at most two fruit types is [2, 3, 3].

---

### Your Task
Implement the function `fruitsBaskets()` that returns the maximum number of fruits
that can be collected following the given rules.

---

### Constraints
- 1 ≤ trees.length ≤ 10⁵  
- 0 ≤ trees[i] < trees.length  

---

### Input Format
- First line: integer `n` (number of trees)
- Second line: `n` space-separated integers representing fruit types

---

### Output Format
- A single integer representing the maximum number of fruits collected

---

### LeetCode Link
https://leetcode.com/problems/fruit-into-baskets/
