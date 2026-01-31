# Convert Array To Linked List

**Difficulty:** Easy  
**Approach:** Iterative Linked List Construction  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Success Rate:** 80%  

---

You are given an array `arr` of size `n`.  
Your task is to **create a singly linked list** from the given array and return the **head** of the linked list.

Each element of the array should be converted into a node of the linked list in the **same order** as they appear in the array.

---

### Example 1
Input:  
n = 5  
arr = [1, 2, 3, 4, 5]

Output:  
1

**Explanation:**  
The linked list created is:  
1 → 2 → 3 → 4 → 5  
The head node contains the value `1`.

---

### Example 2
Input:  
n = 5  
arr = [10, 11, 12, 13, 14]

Output:  
10

**Explanation:**  
The linked list created is:  
10 → 11 → 12 → 13 → 14  
The head node contains the value `10`.

---

### Your Task
Complete the function `arrayToLL()` that takes:
- `n` → size of the array  
- `arr` → array of integers  

and returns the **head node** of the constructed linked list.

---

### Constraints
- 0 ≤ n ≤ 4000  
- 1 ≤ arr[i] ≤ 1000  

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

---

### Output Format
- Print the data value of the **head node** of the linked list
