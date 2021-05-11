import turtle
import time

window = turtle.Turtle()
window.shape("turtle")
window.color("black")

while True:
    window.shape("turtle")
    time.sleep(0.5)
    window.shape("circle")
    time.sleep(0.5)

turtle.mainloop()
