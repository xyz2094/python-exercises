from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class HourlyEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return f"\nHourly Employee Salary: {self.hourly_rate * self.hours_worked}\n"

class MonthlyEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return f"\nMonthly Employee Salary: {self.monthly_salary}\n"
    
hourly_employee = HourlyEmployee(20, 160)
monthly_employee = MonthlyEmployee(3000)

print("-" * 20)
print(hourly_employee.calculate_salary()) 
print("-" * 20)
print(monthly_employee.calculate_salary())
print("-" * 20)