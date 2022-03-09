import turtle
import time
import random

def iscollision(obj1, obj2, w1, w2, h1, h2):
	if obj1.xcor() + w1 > obj2.xcor() - w2 and obj1.xcor() - w1 < obj2.xcor() + w2:
		if obj1.ycor() + h1 > obj2.ycor() - h2 and obj1.ycor() - h1 < obj2.ycor() + h2:
			return True
	return False

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

GROUND = -400
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

platforms = []
y = GROUND
for i in range(12):
	platform = turtle.Turtle()
	platform.speed(0)
	platform.color('orange')
	platform.shape('square')
	platform.shapesize(1,8)
	platform.penup()
	platform.width = 60
	platform.height = 20
	platform.dy = 0
	platform.dx = 0
	platform.goto(random.randint(-300, 300), y)
	y += random.randint(70, 100)
	platforms.append(platform)

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
	for platform in platforms:
		if iscollision(hero, 
						platform, 
						hero.width, 
						platform.width, 
						hero.height, 
						platform.height):
			GRAVITY = 0
			hero.dy = 0
			hero.state = 'ready'


	if hero.ycor() <= GROUND:
		GRAVITY = 0
		hero.dy = 0
		hero.state = 'ready'
	else:
		GRAVITY = -0.9

	if hero.ycor() >= 400:
		for platform in platforms:
			if platform.ycor() <= GROUND:
				platform.goto(random.randint(-300, 300), y)
				y += random.randint(70, 100)
			platform.sety(platform.ycor() - 5)

	time.sleep(0.01)
	window.update()