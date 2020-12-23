#1491. Average Salary Excluding the Minimum and Maximum Salary
#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        #print(salary)
        return sum(salary)/len(salary) 