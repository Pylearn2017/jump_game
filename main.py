# Эта самая новая версия

import turtle
import time

def jump():
	if hero.state == 'ready':
		hero.dy = 15
		hero.state = 'jumping'

def left():
	hero.dx = -15

def right():
	hero.dx = 15

window = turtle.Screen()
window.title('Jump-Game')
window.setup(height=320, width=800)
window.tracer(0)

GROUND = -100
GRAVITY = -0.3
INERT = 0.5

hero = turtle.Turtle()
hero.speed(0)
hero.shapesize(3)
hero.shape('square')
hero.penup()
hero.width = 20
hero.height = 20
hero.dy = 0
hero.dx = 0
hero.state = 'ready'
hero.goto(-200, GROUND + hero.height / 2)
window.listen()
window.onkeypress(jump, 'space')
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
while True:
	if hero.dx > 0:
		hero.dx -= INERT
	elif hero.dx < 0: 
		hero.dx += INERT
	x = hero.xcor()
	x += hero.dx
	hero.setx(x)

	hero.dy += GRAVITY
	y = hero.ycor()
	y += hero.dy
	hero.sety(y)

	if hero.ycor() <= GROUND:
		GRAVITY = 0
		hero.dy = 0
		hero.state = 'ready'
	else:
		GRAVITY = -0.9
	time.sleep(0.01)
	window.update()