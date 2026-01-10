# Nearest Smaller Element

**Difficulty:** Medium  
**Time Complexity:** O(N)  
**Space Complexity:** O(N)  

---

You are given an array `arr` of integers with length `n`.  
Your task is to find the **nearest smaller element on the left** for each element.

If no smaller element exists on the left side, return `-1` for that position.

### Example 1
Input:  
arr = [2, 4, 6, 5, 3]

Output:  
[-1, 2, 4, 4, 2]

**Explanation:**  
- No smaller element before 2 → -1  
- Nearest smaller before 4 → 2  
- Nearest smaller before 6 → 4  
- Nearest smaller before 5 → 4  
- Nearest smaller before 3 → 2  

### Example 2
Input:  
arr = [3, 4, 2, 5, 9, 7, 8, 5]

Output:  
[-1, 3, -1, 2, 5, 5, 7, 2]

### Your Task
Complete the function `nearestSmallerElement()` that returns the nearest smaller element on the left for each array element.

### Constraints
- 1 ≤ n ≤ 10⁵  
- 1 ≤ arr[i] ≤ 10⁵  

### Input Format
- First line: integer `n`
- Second line: `n` space-separated integers

### Output Format
- `n` space-separated integers representing nearest smaller elements
