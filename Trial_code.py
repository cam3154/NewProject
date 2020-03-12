import turtle

wn = turtle.Screen()
wn.bgcolor("black")

leo = turtle.Turtle()
leo.color("red")
leo.speed(0)
def draw_picture():
    for i in range(10):
        for i in range(10):
            leo.circle(150/(i+1),360)
            leo.right(i*2)


draw_picture()


wn.exitonclick()
