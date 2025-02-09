#!/usr/bin/env python3


"""- Define a Worker class with a name, a salary, and number of years worked.
	- Provide a method called pension that returns an amount equal to the years worked times 10% of the salary.
	- Implement a name() method in the Worker class and have this be a default method for all derived classes.
- Derive Manager from Worker.
	- A manager's pension is defined by the number of years worked times 20% of the salary.
- Derive Executive from Manager.
	- An executive's pension is defined by the number of years worked times 30% of the salary."""

class Employee:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
        
    def getname(self):
        return self.name
    
    def pension(self):
        return self.years * self.salary * 0.1

class Manager(Employee):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)
        
    def pension(self):
        return self.years * self.salary * 0.2

class Executive(Manager):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)
        
    def pension(self):
        return self.years * self.salary * 0.3
    
def main():
    workers = [
        Manager("Chris", 100000, 10),
        Executive("Susan", 100000, 10),
        Employee("Michael", 100000, 10),
    ]

    for idx, worker in enumerate(workers):
        print("{:3} {:15.2f} {}".format(idx, worker.pension(),worker.getname()))
        # {} used for field characters
        # :3 in firs position moves it 3 characters spaces wide
        # :15.2f  floating-point number with a width of 15 characters and two decimal places
        # {} placeholder that is used to display the third value, which is the name of the worker
        # worker.getname() method is used to retrieve and display the name.
if __name__ == "__main__":
    main()