"""
Problem: Fruits & Baskets
Approach: Sliding Window + Hash Map
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

class solution:
    def fruitsBaskets(self, tree):
        left = 0
        basket = {}
        max_fruits = 0

        for right in range(len(tree)):
            basket[tree[right]] = basket.get(tree[right], 0) + 1

            while len(basket) > 2:
                basket[tree[left]] -= 1
                if basket[tree[left]] == 0:
                    del basket[tree[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
