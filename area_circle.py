class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        ar = (22/7) * (self.radius ** 2)  # Use radius to calculate area
        print(f"\nThe area of the circle is: {ar}")
        return ar

# Input from user
num = int(input("Enter the radius: "))
c = Circle(num)
c.area()  # Call the area method