# Asteroid Collision

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  
**Companies:** Flipkart, Oracle, Uber, Amazon, Google, Microsoft, Zoho  

---

You are given an array `arr` of integers representing asteroids moving in a straight line.

- **Positive value** → asteroid moving to the right  
- **Negative value** → asteroid moving to the left  
- Absolute value represents the **size** of the asteroid  

All asteroids move at the same speed.

---

### Collision Rules
- Only asteroids moving **towards each other** can collide  
- The **smaller asteroid explodes**
- If both have the **same size**, both explode
- Asteroids moving in the same direction **never collide**

---

### Example 1
Input:  
n = 6  
arr = [4, 8, -3, 9, 7, -8]

Output:  
[4, 8, 9]

**Explanation:**  
- 8 and -3 collide → -3 explodes  
- 7 and -8 collide → 7 explodes  
- 9 and -8 collide → -8 explodes  
Final state: [4, 8, 9]

---

### Example 2
Input:  
n = 5  
arr = [20, 5, 10, -10, -20]

Output:  
[]

**Explanation:**  
- 10 and -10 collide → both explode  
- 5 and -20 collide → 5 explodes  
- 20 and -20 collide → both explode  
Final state: []

---

### Your Task
Complete the function `asteroidCollision()` that returns the final state of asteroids after all collisions.

---

### Constraints
- 2 ≤ n ≤ 10³  
- -900 ≤ arr[i] ≤ 900  
- arr[i] ≠ 0  

---

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

---

### Output Format
- Space-separated integers representing the final asteroid state  
- If no asteroids remain, output an empty line

---

### LeetCode Link
<a href="https://leetcode.com/problems/asteroid-collision/" target="_blank">
LeetCode – Asteroid Collision (Problem 735)
</a>
