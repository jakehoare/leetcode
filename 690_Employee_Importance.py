_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/employee-importance/
# You are given a data structure of employee information, which includes the employee's unique id, his importance
# value and his direct subordinates' id.
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
# They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]],
# and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
# Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
# Now given the employee information of a company, and an employee id, you need to return the total importance value
# of this employee and all his subordinates.

# Create mapping from employee id to importance and subordinates. Sum importance by recursive depth first search.
# Get importance of root employee and recursively add importance totals of subordinates.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        importance, subordinates = {}, {}

        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates

        def sum_importance(emp_id):         # return emp_id importance plus recursive sum of subordinates

            total = importance[emp_id]

            for sub in subordinates[emp_id]:
                total += sum_importance(sub)

            return total

        return sum_importance(id)