# First Word in Dictionary Order

**Difficulty:** Easy  
**Time Complexity:** O(N × M)  
**Space Complexity:** O(N)  

---

You are given a sentence `S` containing space-separated words.  
Your task is to find and print the word that comes **first in dictionary order**.

### Note
- Uppercase and lowercase letters should be treated as **the same**.
- Dictionary order refers to **alphabetical order**.

### Example 1
Input:  
S = "He is bit slow"

Output:  
bit

**Explanation:**  
Words: He, is, bit, slow  
Dictionary order: bit, He, is, slow  
The first word is **bit**.

### Example 2
Input:  
S = "We Are of One Mind"

Output:  
Are

**Explanation:**  
After comparing words case-insensitively, **Are** comes first.

### Your Task
Read a sentence `S` and print the word that comes first in dictionary order.

### Constraints
- The sentence contains at least one word
- Words contain only English letters
- Words are separated by single spaces

### Input Format
- A single line containing the string `S`

### Output Format
- A single word that comes first in dictionary order
