import turtle


def draw_square(square):
	for i in range(0,2):
		square.forward(100)
		square.right(30)
		square.forward(100)
		square.right(150)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("blue")

	pen = turtle.Turtle()
	pen.shape("triangle")
	pen.color("yellow")

	for i in range(0,36):
		draw_square(pen)
		pen.right(10)

	pen.speed(100)
	pen.right(90)
	pen.forward(300)
	pen.right(90)
	

	window.exitonclick()

draw_flower()
