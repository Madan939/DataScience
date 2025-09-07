#Write a python class Rectangle with methods to calculate area and perimeter. Create objects and test them
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        add=self.length+self.breadth
        return 2*add
    
try:
    length=float(input("Enter length: "))
    breadth=float(input("Enter breadth: "))
    obj=Rectangle(length,breadth)
    print(f"The area of rectangle is {obj.area()}x")
    print(f"The perimeter of rectangle is {obj.perimeter()}")
except ValueError as e:
    print(e)
except:
    print("An error has occured.")