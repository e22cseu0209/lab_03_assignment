class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, condition, target_salary):
        if condition == '==':
            result = [emp for emp in self.employees if emp.salary == target_salary]
        elif condition == '>':
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif condition == '<':
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif condition == '>=':
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif condition == '<=':
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []
        return result

def main():
    employees_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    employee_table = EmployeeTable(employees_data)

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = input("Enter your choice: ")

    if choice == '1':
        target_age = int(input("Enter the age to search: "))
        result = employee_table.search_by_age(target_age)
    elif choice == '2':
        target_name = input("Enter the name to search: ")
        result = employee_table.search_by_name(target_name)
    elif choice == '3':
        condition = input("Enter the condition (>, <, <=, >=): ")
        target_salary = int(input("Enter the salary to search: "))
        result = employee_table.search_by_salary(condition, target_salary)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching records found")
    else:
        print("Matching records:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
