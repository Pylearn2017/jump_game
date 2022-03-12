import turtle
import time
import random

def show_score():
	helper.clear()
	helper.write(f'Your score: {hero.score}')

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
window.setup(width = 1.0, height = 1.0)
window.tracer(0)

GROUND = -400
GRAVITY = -0.3
INERT = 0.5

helper = turtle.Turtle()
helper.speed(0)
helper.penup()
helper.hideturtle()
helper.setposition(400, 400)

hero = turtle.Turtle()
hero.speed(0)
hero.shapesize(3)
hero.shape('square')
hero.penup()
hero.width = 20
hero.height = 20
hero.dy = 0
hero.dx = 0
hero.lives = 5
hero.score = 0
hero.state = 'ready'
hero.goto(-200, GROUND + hero.height / 2)

platforms = []
py = GROUND + 50
for i in range(15):
	platform = turtle.Turtle()
	platform.speed(0)
	platform.color('orange')
	platform.shape('square')
	platform.shapesize(1,8)
	platform.penup()  
	platform.width = 70
	platform.height = 20
	platform.dy = 0
	platform.dx = 0
	platform.score = 1
	platform.status = random.choice(['strong', 'broken'])
	if platform.status == 'broken':
		platform.color('brown')
	else:
		platform.dx = random.choice([-1, 1])
	platform.goto(random.randint(-300, 300), py)
	py += random.randint(120, 150)
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

		platform.dy += GRAVITY
		y = platform.ycor()
		y += platform.dy
		platform.sety(y)

		if platform.status == 'strong':
			if abs(platform.xcor()) > 300:
				platform.dx *= -1
			x = platform.xcor()
			x += platform.dx
			platform.setx(x)


	GRAVITY = -.9

	for platform in platforms:
		if iscollision(hero, 
						platform, 
						hero.width, 
						platform.width, 
						hero.height, 
						platform.height):
			hero.dy = 0
			GRAVITY = 0
			hero.score += platform.score
			show_score()
			platform.score = 0
			hero.state = 'ready'
			hero.lives = hero.lives - platform.score
			if platform.status == 'broken':
				platform.score = 1
				platform.goto(random.randint(-300, 300), py)
				py += random.randint(50, 80)

	if hero.ycor() <= GROUND:
		if hero.lives <= 0:
			break  
		GRAVITY = 0
		hero.dy = 0
		hero.state = 'ready'

	for platform in platforms:
		if platform.ycor() <= GROUND:
			platform.score = 1
			platform.goto(random.randint(-300, 300), py)
			py += random.randint(50, 90)
		# platform.sety(platform.ycor() - 1)
		# hero.sety(hero.ycor() - 1)
		platform.dy = -1


	time.sleep(0.01)

	window.update()