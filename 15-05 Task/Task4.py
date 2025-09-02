# Create a class hierarchy (Person → Employee → Manager) and display all details from Manager. Use Inheritance
class Person:
    def moral(self):
        print("Every person should be moral.")
class Employee(Person):
    pass
class Manager(Employee):
    pass
try:
   x=Manager()
   x.moral()
except:
    print("An error has occurred.")