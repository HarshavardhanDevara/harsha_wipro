# Task:
# create class staf with name  role , salary as instance variables. [ Role can be programmer, Developer etc ]
# def netSalry() based on salary and rules are given below
# hra=50% of basic
# cca = 25 % of basic
# totsalary = basic+hra+cca and create displayInfo() .
# The output is like this
# Name          :  ***************8
# Role          :  *********
# Salary        :  **********
# Hra           :  **********
# Cca           :  *********
# TotalSalary   :  *******
class Staf:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def netSalary(self):
        hra = 0.50 * self.salary
        cca = 0.25 * self.salary
        total_salary = self.salary + hra + cca
        return hra, cca, total_salary

    def displayInfo(self):
        hra, cca, total_salary = self.netSalary()
        print(f"Name          :  {self.name}")
        print(f"Role          :  {self.role}")
        print(f"Salary        :  {self.salary}")
        print(f"Hra           :  {hra}")
        print(f"Cca           :  {cca}")
        print(f"TotalSalary   :  {total_salary}")
staff_member = Staf("harsha vardhan", "Developer", 50000)
staff_member.displayInfo()
