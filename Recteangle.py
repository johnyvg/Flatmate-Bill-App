from random import randint
import turtle
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle): # all atributes form Rectangle

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90) #Turn for 90 degree
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=10, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
            Point(randint(0, 100), randint(0, 100)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
    rectangle.point1.x, ",",
    rectangle.point1.y, "and",
    rectangle.point2.x, ",",
    rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

mytrutle = turtle.Turtle()
rectangle.draw(canvas=mytrutle)
user_point.draw (canvas = mytrutle)

# The Canvas is a rectangular area intended for drawing pictures or other complex layouts.
# You can place graphics, text, widgets or frames on a Canvas

turtle.done()  # libery.command causes the program to pause until the user closes the Python Turtle Graphics window.
# The purpose of this is to give the user time to view the graphics.
# Without this line, the graphics window would be closed right after the program is finished.