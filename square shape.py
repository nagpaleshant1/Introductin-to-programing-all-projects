import turtle
def square():
    window=turtle.Screen()
    window.bgcolor("black")
    ferry=turtle.Turtle()
    ferry.color("white")
    
    for i in range(4):
        ferry.forward(50)
        ferry.right(90)
square()      


def circle():
    ferry=turtle.Turtle()
    ferry.color("Yellow")
    ferry.circle(100)

    
circle()

def triangle():
    ferry=turtle.Turtle()
    ferry.color("Red")
    ferry.speed(100)
    for i in range(1):
        ferry.forward(100)
        ferry.left(175)
        ferry.forward(100)
        ferry.left(90)
        ferry.forward(10)
        ferry.left(90)
        ferry.right(2)

    window.exitonclick()
triangle()

        
