# Number of Employees Unable to Eat Snacks

**Difficulty:** Medium  
**Time Complexity:** O(N²)  
**Space Complexity:** O(N)  
**Companies:** Amazon, Google, Microsoft  

---

A group of employees is waiting in a queue to receive snacks.

You are given two arrays:

- `employees`: where  
  - `0` → prefers chips  
  - `1` → prefers cookies  

- `snacks`: representing a stack of snacks  
  - `0` → chips  
  - `1` → cookies  

---

### Rules
1. The employee at the **front** of the queue checks the **top snack**.
2. If the snack matches their preference, both the employee and snack are removed.
3. Otherwise, the employee moves to the **back of the queue**.
4. The process stops when:
   - All snacks are taken, or
   - No employee wants the top snack.

---

### Example 1
Input:  
employees = [1, 0]  
snacks = [0, 1]

Output:  
0

---

### Example 2
Input:  
employees = [1, 1, 1, 0, 0, 1]  
snacks = [1, 0, 0, 0, 1, 1]

Output:  
3

**Explanation:**  
At some point, no employee prefers the snack on top, so the process stops.

---

### Your Task
Complete the function `unableToEatSnacks()` that returns the number of employees
who are unable to get their preferred snack.

---

### Constraints
- 1 ≤ employees.length ≤ 100  
- employees.length == snacks.length  
- employees[i], snacks[j] ∈ {0, 1}

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers (employees)
- Third line: `n` space-separated integers (snacks)

---

### Output Format
- Single integer representing employees unable to eat

---

### LeetCode Link
<a href="https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/" target="_blank">
LeetCode – Number of Students Unable to Eat Lunch (Problem 1700)
</a>
