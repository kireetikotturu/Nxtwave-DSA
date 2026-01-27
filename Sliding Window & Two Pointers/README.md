# 🚀 Sliding Window & Two Pointers

Efficiently solving array and string problems by reducing time complexity from   $O(n^2)$ to $O(n)$.

---

## 🪟 1. Sliding Window (Fixed Size)

**Concept:** Instead of re-calculating the sum/result for every possible subarray, we "slide" a window of size `k` across the list.

* **The Secret:** To move the window, **add** the new element entering from the right and **subtract** the old element leaving from the left.

### 💡 Example: Max Sum Subarray (Size K)

**Array:** `[2, 1, 5, 1, 3, 2]`, **K:** `3`

1. **Initial Window:** `[2, 1, 5]` → Sum = **8**
2. **Slide Right:** Add `1`, Remove `2` → `(8 + 1 - 2)` = **7**
3. **Slide Right:** Add `3`, Remove `1` → `(7 + 3 - 1)` = **9** (New Max!)
4. **Slide Right:** Add `2`, Remove `5` → `(9 + 2 - 5)` = **6**

### 🛠️ Python Implementation

```python
def max_sum_subarray(arr, k):
    # 1. Calculate sum of the first window
    window_sum = sum(arr[:k])
    max_val = window_sum

    # 2. Slide the window from index k to the end
    for i in range(k, len(arr)):
        # Add the next element, subtract the element that fell out
        window_sum += arr[i] - arr[i - k]
        max_val = max(max_val, window_sum)
        
    return max_val

```

---

## 📏 2. Two Pointers (Variable Window)

**Concept:** Use two markers (`start` and `end`) to create a window that grows or shrinks dynamically based on a condition (like a target sum).

* **The Strategy:** * Use `end` to **expand** the window until the condition is met.
* Use `start` to **shrink** the window to find the smallest possible valid size.



### 💡 Example: Smallest Subarray with Sum ≥ Target

**Array:** `[2, 3, 1, 2, 4]`, **Target:** `7`

* **Expand:** `end` moves until sum is 8 (Window: `[2, 3, 1, 2]`).
* **Shrink:** `start` moves forward to see if `[3, 1, 2]` or `[1, 2, 4]` works.
* **Result:** `[1, 2, 4]` has a length of 3.

### 🛠️ Python Implementation

```python
def min_subarray_len(arr, target):
    start = 0
    current_sum = 0
    min_len = float('inf')

    for end in range(len(arr)):
        current_sum += arr[end]  # Expand the window
        
        # While the condition is met, try to shrink it
        while current_sum >= target:
            min_len = min(min_len, end - start + 1)
            current_sum -= arr[start]
            start += 1
            
    return min_len if min_len != float('inf') else 0

```

---

## 📊 Summary Table

| Feature | Sliding Window (Fixed) | Two Pointers (Variable) |
| --- | --- | --- |
| **Window Size** | Constant (k) | Changes dynamically |
| **Complexity** | $O(n)$ | $O(n)$ |
| **Space** | $O(1)$ | $O(1)$ |
| **Visual** | A sliding frame of fixed width | An accordion (stretching/squeezing) |

### 🔑 Key Takeaway

Whenever you see words like **"subarray"**, **"substring"**, or **"consecutive"**, stop yourself from writing a nested loop! Use these techniques to process each element only once.

---

# 🚀 Mastering Arrays: Subarrays vs. Subsequences

To solve array problems like a pro, you first need to know what you are looking for. The technique you choose depends entirely on the "type" of group you are analyzing.

---

## 🔍 The Big Three: What's the Difference?

| Type | Order Matters? | Must be Contiguous? | Example: `[1, 2, 3]` |
| --- | --- | --- | --- |
| **Subarray** | ✅ Yes | ✅ Yes (Connected) | `[1, 2]`, `[2, 3]` |
| **Subsequence** | ✅ Yes | ❌ No (Can skip) | `[1, 3]` |
| **Subset** | ❌ No | ❌ No (Any combo) | `[3, 1]`, `[2]` |

### 1. Subarray (Use: Sliding Window)

A **Subarray** is a contiguous (connected) part of an array.

* **Problem Hint:** "Find the longest **consecutive**..." or "Find a **continuous** sum..."
* **Best Tool:** **Sliding Window.** Since the elements are connected, you can just slide a "frame" over them.

### 2. Subsequence (Use: Two Pointers)

A **Subsequence** maintains the relative order but can skip elements.

* **Problem Hint:** "Is String A a subsequence of String B?" or "Find the longest increasing subsequence..."
* **Best Tool:** **Two Pointers.** You usually keep one pointer on the first array and another on the second to check for matches in order.

---

## 🪟 1. Sliding Window (For Subarrays)

**Goal:** Process a "window" of elements without recalculating everything from scratch.

### 💡 Example: Max Sum of Subarray (Size K)

```python
def max_sum(arr, k):
    # Initial window sum
    window_sum = sum(arr[:k])
    max_val = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        # Add entering element, subtract exiting element
        window_sum += arr[i] - arr[i-k]
        max_val = max(max_val, window_sum)
    return max_val

```

---

## 📏 2. Two Pointers (For Subsequences/Variable Ranges)

**Goal:** Use two indices to "hunt" for a specific condition. This is often used to compare two different arrays or check if one is a subsequence of another.

### 💡 Example: Is 's' a Subsequence of 't'?

```python
def is_subsequence(s, t):
    p1, p2 = 0, 0  # Two pointers
    
    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1  # Move p1 only if we find a match
        p2 += 1      # Always move p2 (the main string)
        
    return p1 == len(s)

```

---

## 🎯 Summary Cheat Sheet

* **Subarray + Fixed Size**  **Fixed Sliding Window** (e.g., Max sum of size K).
* **Subarray + Flexible Size**  **Variable Sliding Window** (e.g., Smallest subarray with sum > X).
* **Subsequence + Comparison**  **Two Pointers** (e.g., Comparing two strings or finding pairs).
* **Subset**  **Recursion / Backtracking** (Since elements can be picked from anywhere).

---
