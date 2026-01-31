# Search In Linked List

**Difficulty:** Easy  
**Approach:** Linear Search (Iterative Traversal)  
**Time Complexity:** O(N)  
**Space Complexity:** O(1)  
**Success Rate:** 68%  

---

You are given a **singly linked list** and an integer **key `k`**.  
Your task is to **check whether the value `k` is present in the linked list**.

- If the value `k` is found, return **1**
- If the value `k` is not found, return **0**

---

### Example 1
Input:  
Linked List:  
10 → 14 → 20 → 30  
k = 14  

Output:  
1  

**Explanation:**  
The value **14** exists in the linked list, so the output is **1**.

---

### Example 2
Input:  
Linked List:  
10 → 14 → 20 → 30  
k = 13  

Output:  
0  

**Explanation:**  
The value **13** does not exist in the linked list, so the output is **0**.

---

### Your Task
Complete the function `searchInLL()` that takes:
- `head`: pointer to the head of the linked list  
- `k`: the value to search for  

Return:
- **1** if `k` is present  
- **0** otherwise

---

### Constraints
- 0 ≤ n ≤ 4000  
- 1 ≤ data, k ≤ 1000  

---

### Input Format
- First line contains two integers `n` and `k`  
- Second line contains `n` space-separated integers representing node values  

---

### Output Format
- Print `1` if `k` is found in the linked list  
- Print `0` if `k` is not found  

---
