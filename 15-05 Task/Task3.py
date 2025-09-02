# Define a class Rectangle with methods to calculate area and perimeter
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"The area of rectangle = {self.length*self.breadth}")
    def perimeter(self):
        add=self.length+self.breadth
        print(f"The perimeter of rectangle = {2*add}")
try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    x=Rectangle(num1,num2)
    x.area()
    x.perimeter()
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("An error has occurred.")
