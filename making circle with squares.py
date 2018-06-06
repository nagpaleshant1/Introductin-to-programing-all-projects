import turtle

def draw_square(some_turtle):
    for i in range (1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # Create a turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed(2)
    
    for i in range (36):
        brad.speed(10000)
        draw_square(brad)
        brad.right(10)
    
    brad.forward(200)
    brad.left(100)
    
    window.exitonclick()
    
draw_art()
