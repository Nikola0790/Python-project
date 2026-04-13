class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User: {self.name}"

class User_2:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

u = User('Nikola')
print(u)

u_2 = User_2('Nikola')
print(repr(u_2))

#Exercise 1 - Calculator
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result
    
    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result
    
    def print_operations(self):
        for item in self.history:
            print(item)

calc1 = Calculator()
calc1.add(5, 10)
calc1.multiply(5, 11)
calc1.print_operations()

#Exercise 2 - Shape
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        return f"Color: {self.color}"

    def distance(self, other):
        dx = other.x - self.x 
        dy = other.y - self.y
        return f"Distance: {(dx**2 + dy**2)**0.5}"

    def __str__(self):
        return f"Figure of the {self.color} color with center at point ({self.x}, {self.y})"
    
shape1 = Shape(5, 5, "blue")
shape2 = Shape(2, 3, "green")
shape3 = Shape(10, 15, 'yellow')

print(shape1.describe())
print(shape1.distance(shape2))
print(shape1)

print(shape2.describe())
print(shape2.distance(shape3))
print(shape2)

#Exercise Bank Account
class BankAccount:
    def __init__(self, number: int):
        self.number = number
        self.cash: float = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
    
    def withdraw_cash(self, amount):
        if amount <= 0.0:
            return 0.0

        if amount <= self.cash:
            self.cash -= amount
            return amount
        else:
            withdrawn = self.cash
            self.cash = 0.0
            return withdrawn
        
    def print_info(self):
        return f"Account number {self.number} - Status: {self.cash}"
    
account1 = BankAccount(1)
account2 = BankAccount(2)

account1.deposit_cash(1000)
print(account1.print_info())
print("Withdrawn:", account1.withdraw_cash(420))
print(account1.print_info())

account2.deposit_cash(1000)
print(account2.print_info())
print("Withdrawn:", account2.withdraw_cash(1200))
print(account2.print_info())
account2.deposit_cash(200)
print(account2.print_info())

#Exercise 4 - Employee

class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0.0:
                self._salary = salary

    def print_info(self):
        return f"{self.first_name} {self.last_name}, ID: {self.id} has salary {self._salary} per hour."
    
employee_1 = Employee(10, "Petar", "Petrovic")
employee_2 = Employee(11, "John", "Rambo")
employee_3 = Employee(12, "Klark", "Kent")

employee_1.set_salary(50.00)
employee_2.set_salary(510.75)
employee_3.set_salary(325.555)

print(employee_1.print_info())
print(employee_2.print_info())
print(employee_3.print_info())