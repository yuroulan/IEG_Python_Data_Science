# i assess
# 1
'''
Area (Polymorphism)
                                                    
Create a base Class Shape and derive the CalAreaSquare, CalAreaRectangle, CalAreaTriangle, CalAreaCircle classes.

Use the following method in base class Shape:
Method Name            Description
area()                          Display the input parmaters

Calculate area of square in all the derived classes:
Method Name            Description
area()                                       Find the area of the Square, Rectangle, Triganle and Circle, in their respective derived classes.

Note: The area of triangle=0.5*base*height
pi value will be considered as 3.14

Sample Input and Output Format 1:
Select an Option
1.Square
2.Rectangle
3.Triangle
4.Circle
4
Enter the radius
2
Radius of Circle : 2
Area of Circle : 12.57
'''
class Shape:
    def area(self):
        pass

class CalAreaSqr(Shape):
    def area(self, side):
        self.side = side
        print(f"Side of Square : {self.side}")
        print(f"Area of Square : {self.side * self.side:.2f}") 

class CalAreaRect(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
        print(f"Area of Rectangle : {self.length * self.width}")

class CalAreaTri(Shape):
    def area(self, base, height):
        self.base = base
        self.height = height
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        print(f"Area of Triangle : {0.5 * self.base * self.height:.2f}")

class CalAreaCircle(Shape):
    def area(self, radius):
        self.radius = radius
        print(f"Radius of Circle : {self.radius}")
        print(f"Area of Circle : {3.14 * self.radius * self.radius:.2f}")

# Main program
print("Select an Option")
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")

option = int(input())

if option == 1:
    side = int(input("Enter the side length"))
    square = CalAreaSqr()
    square.area(side)
elif option == 2:
    length = int(input("Enter the length"))
    width = int(input("Enter the breadth"))
    rectangle = CalAreaRect()
    rectangle.area(length, width)
elif option == 3:
    base = int(input("Enter the base"))
    height = int(input("Enter the height"))
    triangle = CalAreaTri()
    triangle.area(base, height)
elif option == 4:
    radius = int(input("Enter the radius"))
    circle = CalAreaCircle()
    circle.area(radius)
else:
    print("Invalid Option")