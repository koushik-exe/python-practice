class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Employee: {self.name} | Salary: ₹{self.salary}"

class Manager(Employee):
    def __init__(self,name,salary, department):
        super().__init__(name,salary)
        self.department = department
    
    def show_details(self):
        return f"Manager: {self.name} | Salary: ₹{self.salary} | Department: {self.department}"

E1 = Employee("Koushik", 50000)
M1 = Manager("Claude", 500000, "IT")

print("Employee Details")
print(E1.show_details() + "\n")

print("Manager Details")
print(M1.show_details() +"\n")