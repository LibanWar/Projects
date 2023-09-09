import turtle as t
playerAscore=0
playerBscore=0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


#creates Left Paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creates Right Paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creates Ball
ball=t.Turtle()
ball.speed(10000000000000000000000000000000)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2


#creates the ScoreBoard
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))

#Moves Left Paddle Up
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

#Moves Left Paddle Down
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#Moves Right Paddle Up
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
    
#Moves Right Paddle Down
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

#assigns keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    #Moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #Making the border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore += playerAscore + 1
        pen.clear()
        pen.write("player A:{}   player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerBscore += playerBscore + 1
        pen.clear()
        pen.write("player A:{}   player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    #Handiling the Colisions
    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection *= -1

    if(ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection *-1
        
        
      










    











