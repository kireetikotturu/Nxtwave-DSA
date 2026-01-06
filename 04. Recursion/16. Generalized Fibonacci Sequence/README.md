# Generalized Fibonacci Sequence

**Difficulty:** Medium  
**Time Complexity:** O(n · k)  
**Space Complexity:** O(n)  

---

You're given:
- an integer `k`,
- an array `start` of size `k` containing the first `k` numbers,
- an integer `n` representing the total length of the sequence.

Your task is to generate a **generalized Fibonacci sequence** where **each number is the sum of the previous `k` numbers**, using **recursion**.  
The resulting sequence must contain **exactly `n` numbers**.

### Example 1
Input:  
k = 3, n = 6  
start = [0, 1, 2]  

Output:  
[0, 1, 2, 3, 6, 11]

**Explanation:**  
- 3 = 0 + 1 + 2  
- 6 = 1 + 2 + 3  
- 11 = 2 + 3 + 6  

### Example 2
Input:  
k = 4, n = 8  
start = [1, 1, 2, 3]  

Output:  
[1, 1, 2, 3, 7, 13, 25, 48]

**Explanation:**  
- 7 = 1 + 1 + 2 + 3  
- 13 = 1 + 2 + 3 + 7  
- 25 = 2 + 3 + 7 + 13  
- 48 = 3 + 7 + 13 + 25  

### Your Task
Complete the function `generateGeneralizedFibonacci()` that takes:
- `k`: number of previous terms to sum,
- `start`: list of the first `k` numbers,
- `n`: total length of the sequence,

and returns a list containing exactly `n` numbers of the generalized Fibonacci sequence.

### Constraints
- 1 ≤ k ≤ 30  
- 1 ≤ n ≤ 30  
- 0 ≤ start[i] ≤ 30  
- Length of `start` is exactly `k`

### Input Format
- First line: two integers `k` and `n`
- Second line: `k` space-separated integers (`start` array)

### Output Format
- A single line containing the generated generalized Fibonacci sequence.
