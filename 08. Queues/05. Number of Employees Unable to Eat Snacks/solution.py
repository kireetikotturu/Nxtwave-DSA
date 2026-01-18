"""
Problem: Number of Employees Unable to Eat Snacks
Approach: Queue Simulation with Early Termination
Difficulty: Medium
Time Complexity: O(N²)
Space Complexity: O(N)
"""

from collections import deque

class Solution:
    def unableToEatSnacks(self, employees, snacks):
        emp_queue = deque(employees)
        snack_queue = deque(snacks)

        while emp_queue:
            # If no employee wants the top snack, stop
            if snack_queue[0] not in emp_queue:
                return len(emp_queue)

            emp = emp_queue.popleft()
            if emp == snack_queue[0]:
                snack_queue.popleft()
            else:
                emp_queue.append(emp)

        return 0
