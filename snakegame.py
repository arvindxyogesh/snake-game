import turtle
import random
import time
screen = turtle.Screen()
turtle.title('Snake Game')
screen.setup(height=700,width=700)
screen.tracer(0)
turtle.bgcolor('grey')


#creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.hideturtle()

#creatingsnake
snake=turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('green')
snake.goto(0,0)
snake.penup()
snake.direction='stop'


#creatingfood
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)


score=0
old_fruit=[]
delay=0.1

#creating score
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color('black')
scoring.penup()
scoring.goto(0,300)
scoring.hideturtle()
scoring.write('score:0',align='center',font=("courier",24,'bold'))

#move
# def up():
#     snake.direction='up'
# def down():
#     snake.direction='down'
# def right():
#     snake.direction='right'
# def left():
#     snake.direction='left
def snake_go_up():
    if snake.direction!='down':
         snake.direction='up'
def snake_go_down():
    if snake.direction!='up':
         snake.direction='down'         
def snake_go_right():
    if snake.direction!='left':
         snake.direction='right'
def snake_go_left():
    if snake.direction!='right':
         snake.direction='left'             

def move():
    if(snake.direction=='up'):
        y=snake.ycor()
        snake.sety(y+20)
    if(snake.direction=='down'):
        y=snake.ycor()
        snake.sety(y-20)
    if(snake.direction=='right'):
        x=snake.xcor()
        snake.setx(x+20)
    if(snake.direction=='left'):
        x=snake.xcor()
        snake.setx(x-20)  
#keybindings
screen.listen()
screen.onkeypress(snake_go_up,'Up')
screen.onkeypress(snake_go_down,'Down')
screen.onkeypress(snake_go_right,'Right')
screen.onkeypress(snake_go_left,'Left')
            


while True:
    screen.update()
    if snake.distance(food)<20:
        score+=1
        scoring.clear()
        scoring.write("Score :",align="center",font=("courier",24,"bold"))
        x= random.randint(-290,270)
        y=random.randint(-240,240)

        food.goto(x,y)
        delay-=0.001

        new_food=turtle.Turtle()
        new_food.color('green')
        new_food.speed(0)
        new_food.shape('circle')
        new_food.penup()
        old_fruit.append(new_food)

    for i in range(len(old_fruit)-1,0,-1):
        x=old_fruit[i-1].xcor()
        y=old_fruit[i-1].ycor()

        old_fruit[i].goto(x,y)
    if len(old_fruit)>0:
        x=snake.xcor()
        y=snake.ycor()

        old_fruit[0].goto(x,y)

    move()

    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear(1)
        screen.turtle.bgcolor('turquoise')
        scoring.goto(0,0)
        scoring.turtle.write(f"GAME OVER \n Your score is {score}",font=("courier",30,"bold"))
    
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.turtle.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write(f"GAME OVER \n Your score is {score}",font=("courier",30,"bold"))



    time.sleep(delay)



