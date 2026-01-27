🚀 Mastering Sliding Window & Two Pointers (Python)Efficiently solving array and string problems by reducing time complexity from $O(n^2)$ to $O(n)$.🪟 1. Sliding Window (Fixed Size)Concept: Instead of re-calculating the sum/result for every possible subarray, we "slide" a window of size k across the list.The Secret: To move the window, add the new element entering from the right and subtract the old element leaving from the left.💡 Example: Max Sum Subarray (Size K)Array: [2, 1, 5, 1, 3, 2], K: 3Initial Window: [2, 1, 5] → Sum = 8Slide Right: Add 1, Remove 2 → (8 + 1 - 2) = 7Slide Right: Add 3, Remove 1 → (7 + 3 - 1) = 9 (New Max!)Slide Right: Add 2, Remove 5 → (9 + 2 - 5) = 6🛠️ Python ImplementationPythondef max_sum_subarray(arr, k):
    # 1. Calculate sum of the first window
    window_sum = sum(arr[:k])
    max_val = window_sum

    # 2. Slide the window from index k to the end
    for i in range(k, len(arr)):
        # Add the next element, subtract the element that fell out
        window_sum += arr[i] - arr[i - k]
        max_val = max(max_val, window_sum)
        
    return max_val
📏 2. Two Pointers (Variable Window)Concept: Use two markers (start and end) to create a window that grows or shrinks dynamically based on a condition (like a target sum).The Strategy: * Use end to expand the window until the condition is met.Use start to shrink the window to find the smallest possible valid size.💡 Example: Smallest Subarray with Sum ≥ TargetArray: [2, 3, 1, 2, 4], Target: 7Expand: end moves until sum is 8 (Window: [2, 3, 1, 2]).Shrink: start moves forward to see if [3, 1, 2] or [1, 2, 4] works.Result: [1, 2, 4] has a length of 3.🛠️ Python ImplementationPythondef min_subarray_len(arr, target):
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
📊 Summary TableFeatureSliding Window (Fixed)Two Pointers (Variable)Window SizeConstant ($k$)Changes dynamicallyComplexity$O(n)$$O(n)$Space$O(1)$$O(1)$VisualA sliding frame of fixed widthAn accordion (stretching/squeezing)🔑 Key TakeawayWhenever you see words like "subarray", "substring", or "consecutive", stop yourself from writing a nested loop! Use these techniques to process each element only once.
