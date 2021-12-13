# This is our Falling Rocks Game
# Made by Riley Collins and Jovan George
# Import turtle & Assign Variables
import turtle as trtl
import random as rand
import time
t = trtl.Turtle()
rock = trtl.Turtle()
t.speed(0)
deathcondition1 = False
deathcondition2 = False
freeze_used = False

# Import Images
assets = ["universe.gif", "spaceship!.gif", "meteor.gif", "white.gif", "gameover.gif"]
wn = trtl.Screen()
wn.bgpic(assets[0])
wn.addshape(assets[1])
t.shape(assets[1])
wn.addshape(assets[2])
rock.shape(assets[2])

# Turtles Setup
t.penup()
t.goto(0, -75)
rock.penup()
rock.hideturtle()

# User Inputs and Difficulty
print("Welcome to the game. Please set your game window to full screen.        Use the left and right arrows for movement, and the spacebar to use a   powerup. ")
print("")
print("Please choose a difficulty level. You can choose Easy, Medium, or Hard.  ")
# This makes it so you answer in the line below.
difficulty = input("")
if difficulty == "Easy":
  fall_speed = 1
  time.sleep(0.5)
elif difficulty == "Medium":
  fall_speed = 2
  time.sleep(0.5)
elif difficulty == "Hard":
  fall_speed = 3
  time.sleep(0.5)
elif difficulty == "Impossible":
  fall_speed = 0
  time.sleep(0.5)
else:
  print("...")
  time.sleep(0.5)
  print("That difficulty cannot be selected. It may because you did not capitalize your answer. Difficulty has been set to Easy by default.")
  fall_speed = 1
print("")
powerup_choice = input("Would you like to use a powerup? Today's powerup is Freeze. You can also        say 'None' for no powerup.    ")

# User Typing Input and Powerup Configuration
def move_right():
  t.forward(30)
def move_left():
  t.backward(30)
def use_freeze():
  if powerup_choice == "Freeze":
    global freeze_used
    if freeze_used == False:
      time.sleep(3)
    if freeze_used == True:
      print("")
      print("You can only use Freeze once per game!")
  freeze_used = True 
wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.onkey(use_freeze, " ")
wn.listen()

# Rock Functions
def rock_fall():
  rock.hideturtle()
  rock.speed(0)
  x_cor = rand.randint(-265,265)
  y_cor = 80
  rock.goto(x_cor,y_cor)
  rock.showturtle()
  rock.speed(fall_speed)
  y_cor = y_cor - 250
  rock.goto(x_cor,y_cor)

# User Interaction with Rocks & Death Event
distance = "22"
while True:
    rock_fall()
    if (abs(rock.xcor() - t.xcor()) < int(distance)):
      deathcondition1 = True
    if (abs(rock.ycor() - t.ycor()) < int(distance)):
      deathcondition2 = True
    if deathcondition1 == True or deathcondition2 == True:
      wn.clear()
      wn.bgpic(assets[3])
      end = trtl.Turtle()
      wn.addshape(assets[4])
      end.shape(assets[4])

wn.mainloop()
# Line 100
