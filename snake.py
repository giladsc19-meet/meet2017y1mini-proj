import turtle
import random #we'll need this later in the lab.

turtle.tracer(1,0) #this helps the turtle move more smoothlty.

size_x=800
size_y=500

turtle.setup(size_x,size_y) #curious? it,s the turtle window. size.

turtle.penup()

square_size=22
start_length=5

#intialize lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

#set up positions (x,y) of boxes that make up the snake.
snake=turtle.clone()
snake.shape("square")

#hide thee turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#draw a snake at the start of the game with a for loop.
#for loop should use range() and count up to the number of pieces.
#in the snake (i.e. start_length).
for snake_draw in range(start_length):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    #add square_size to x_pos. where does x_pos point  to now?
    #you're right
    x_pos+=square_size

    my_pos=(x_pos,y_pos) #store position variables in a tuple
    snake.goto(x_pos,y_pos) #move snake to new (x,y)

    #append the new position tuple to pos_list
    pos_list.append(my_pos)
    #save the stamp id! you'll need to erase it later. than append it to stamp_list.
    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)
##############################################################################
#make sure you pay attention to upper and lower case.
UP_ARROW="UP"
LEFT_ARROW="LEFT"
DOWN_ARROW="DOWN"
RIGHT_ARROW="RIGHT"
TIME_STEP=100 #update snake position after this many milliseconds

SPACEBAR="space" #careful,it's not supposed to be capitalized

UP=0
LEFT=1
DOWN=2
RIGHT=3

SPACEBAR="Space"

direction=UP

def up():
    global direction
    direction= UP
    move_snake()
    print("you pressed the up key!")

def left():
    global direction
    direction= LEFT
    move_snake()
    print("you pressed the left key!")

def down():
    global direction
    direction= DOWN
    move_snake()
    print("you pressed the down key!")

def right():
    global direction
    direction= RIGHT
    move_snake()
    print("you pressed the right key!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos=snake.pos()        

