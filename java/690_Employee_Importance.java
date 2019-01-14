/*
https://leetcode.com/problems/employee-importance/
You are given a data structure of employee information, which includes the employee's unique id, his importance value
and his direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance
value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has
[2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1,
the relationship is not direct.
Now given the employee information of a company, and an employee id, you need to return the total importance value
of this employee and all his subordinates.

Create a map from if to Employee class instances. Then depth-first search from the input employee to add his/her
importance (which is the base case) then recursively the importances of all employees.
Time - O(n)
Space - O(n)
*/

class Solution {

    Map<Integer, Employee> idToEmployee = new HashMap<>();          // map from id to Employee

    public int getImportance(List<Employee> employees, int id) {

        for (Employee employee : employees)
            idToEmployee.put(employee.id, employee);

        return sumImportances(id);
    }

    private int sumImportances(int id) {

        int total = idToEmployee.get(id).importance;

        for (int subordinateId : idToEmployee.get(id).subordinates)
            total += sumImportances(subordinateId);
        return total;
    }
}
