'''
Summer 2022 Game Project

Tank-Game-2.0

Author: Camellia Guan
Start Date: July 29, 2022
End Date: N/A

'''

import math
import time
from consts import *
import turtle


''' GLOBAL VARIABLES '''

# SCREEN
gameScreen = turtle.Screen()

# TURTLES
projectile = turtle.Turtle(visible=False)
wordTurtle = turtle.Turtle(visible=False)
labelTurtle = turtle.Turtle(visible=False)

turtles = (projectile, wordTurtle, labelTurtle)

tank1 = turtle.Turtle(visible=False)
tank2 = turtle.Turtle(visible=False)

tanks = (tank1, tank2)

# GAME
game_end = False
winner = None


def setup_screen_turt(sc, turts):
    '''
    Setup the game screen and turtles.

    Returns None.
    '''
    sc.title('Tank Game 2.0')
    sc.setup(width=GAME_WIDTH,height=GAME_HEIGHT)

    for turt in turts:
        turt.speed(10)
        turt.color('#CDCDFF')

    # PROJECTILE
    turts[0].shape('circle')
    turts[0].turtlesize(0.2)
    turts[0].pendown()

def start_game(sc, turt):
    '''
    Starts the game by creating the welcome screen and dismissing it.

    Returns None.
    '''
    print('Welcome Screen Loaded...')

    setup_welcome(sc, turt)

    dismiss_welcome(sc)
    
    # REGISTERING SHAPES
    turtle.register_shape('images/tank1.gif')
    turtle.register_shape('images/tank2.gif')

def setup_welcome(sc, turt):
    '''
    Sets up the welcome screen with background and words.

    Returns None.
    '''
    change_background(sc, 'images/background1-resized.gif')

    turt.penup()
    turt.goto(0, -GAME_HEIGHT/10)
    turt.write('tanks', move=False, align='center', font=('Vonique64', LARGE_FONT, 'normal'))
    turt.goto(0, -GAME_HEIGHT/6)
    turt.write('press s to start...', move=False, align='center', font=('Vonique64', MEDIUM_FONT, 'normal'))

def dismiss_welcome(sc):
    '''
    Dismisses the welcome screen by listening for the 's' key to be clicked. 
    When 's' is clicked, the game is played.

    Returns None.
    '''
    sc.onkey(play_game, 's')
    sc.listen()

def setup_game(sc, pturt, label):
    '''
    Sets up the game by changing background and moving turtles.

    Returns None.    
    '''
    change_background(sc, 'images/background2-edited-resized-modified.gif')
    
    setup_tanks(tank1, True)
    setup_tanks(tank2, False)

    move_projectile(pturt, True)

    # DRAW LABELS FOR NAME AND AIM
    label.goto(-GAME_WIDTH/2 + GRID_SIZE * 0.5, GAME_HEIGHT/2 - GRID_SIZE * 1.5)
    label.write('power: ', move=False, align='left', font=('Raleway Light', SMALL_FONT, 'normal'))
    label.goto(-GAME_WIDTH/2 + GRID_SIZE * 0.5, GAME_HEIGHT/2 - GRID_SIZE * 2.5)
    label.write('angle: ', move=False, align='left', font=('Raleway Light', SMALL_FONT, 'normal'))

    label.goto(-GAME_WIDTH/3, -GAME_HEIGHT/4 + GRID_SIZE/2)
    label.write('tank 1', move=False, align='center', font=('Raleway Light', MINI_FONT, 'normal'))
    label.goto(GAME_WIDTH/3, -GAME_HEIGHT/4 + GRID_SIZE/2)
    label.write('tank 2', move=False, align='center', font=('Raleway Light', MINI_FONT, 'normal'))

def play_game():
    '''
    Plays the game.

    Returns None.
    '''
    print('Playing Game...')

    # REMOVING THE BIND TO 's'
    gameScreen.onkey(None , 's')

    # CLEAR SCREEN FOR GAME
    gameScreen.clear()

    setup_game(gameScreen, projectile, labelTurtle)
    tanks_health = [100] * len(tanks)

    currPlayer = 0

    global game_end
    global winner

    while not game_end:

        nextPlayer = (currPlayer + 1) % 2

        wordTurtle.goto(-GAME_WIDTH/3, -GAME_HEIGHT/2 + GRID_SIZE * 2.25)
        wordTurtle.write(str(tanks_health[0]), move=False, align='center', font=('Raleway Light', MINI_FONT, 'normal'))
        wordTurtle.goto(GAME_WIDTH/3, -GAME_HEIGHT/2 + GRID_SIZE * 2.25)
        wordTurtle.write(str(tanks_health[1]), move=False, align='center', font=('Raleway Light', MINI_FONT, 'normal'))

        # CHECKS CURRENT PLAYER AND MOVES ARROW
        if currPlayer == 0:
            facing_right = True
            wordTurtle.goto(-GAME_WIDTH/3, -GAME_HEIGHT/4 + GRID_SIZE * 1.5)
        else: 
            facing_right = False
            wordTurtle.goto(GAME_WIDTH/3, -GAME_HEIGHT/4 + GRID_SIZE * 1.5)

        wordTurtle.write('⇩', move=False, align='center', font=('Raleway Light', SMALL_FONT, 'normal'))

        time.sleep(3)
        projectile.clear()

        move_projectile(projectile, facing_right)

        hit, power, angle = shoot_projectile(projectile, tanks[currPlayer], tanks[nextPlayer], facing_right)

        wordTurtle.goto(-GAME_WIDTH/2 + GRID_SIZE * 3.5, GAME_HEIGHT/2 - GRID_SIZE * 1.5)
        wordTurtle.write(power, move=False, align='left', font=('Raleway Light', SMALL_FONT, 'normal'))
        wordTurtle.goto(-GAME_WIDTH/2 + GRID_SIZE * 3.5, GAME_HEIGHT/2 - GRID_SIZE * 2.5)
        wordTurtle.write(angle, move=False, align='left', font=('Raleway Light', SMALL_FONT, 'normal'))

        # TARGEt HIT, LOWER HEALTH
        if hit:
            pass
        else:
            pass

        if min(tanks_health) <= 0:
            game_end = True
            winner = currPlayer + 1

        currPlayer = (currPlayer + 1) % 2

        time.sleep(3)
        wordTurtle.clear()


''' HELPER FUNCTIONS '''

def change_background(sc, background):
    '''
    Changes the background picture of the given screen.

    Returns None.
    '''
    sc.bgpic(background)

def setup_tanks(tank, facing_right = True):
    '''
    Sets up the position of the given tank.

    Returns None.
    '''
    tank.hideturtle()
    tank.penup()

    if facing_right:
        tank.goto(-GAME_WIDTH/3, -GAME_HEIGHT/4)
        tank.shape('images/tank1.gif')
    else:
        tank.goto(GAME_WIDTH/3, -GAME_HEIGHT/4)
        tank.shape('images/tank2.gif')

    tank.showturtle()    

def move_projectile(turt, facing_right = True):
    '''
    Sets up the position of the projectile.

    Returns None.
    '''
    turt.hideturtle()
    turt.penup()

    if facing_right:
        turt.goto(-GAME_WIDTH/3, -GAME_HEIGHT/4)
        turt.setheading(180)
    else:
        turt.goto(GAME_WIDTH/3, -GAME_HEIGHT/4)
        turt.setheading(0)
    
    turt.pendown()
    
def hit_tank():
    '''
    Determines if the target is hit by the projectile.

    Returns True if the target has been hit, False otherwise. [boolean].
    '''
    pass

def get_aim():
    '''
    Asks the user for aim.

    Returns the power and angle [tuple].
    '''

    power = input('Enter Power (0 - 100): ')
    angle = input('Enter Angle (in degrees): ')
    print('')

    while not angle.isnumeric() and not power.isnumeric():
        print('Please enter integers!\n')
        power = input('Enter Power (0 - 100): ')
        angle = input('Enter Angle (in degrees): ')
        print('')
    
    return (power, angle)

def shoot_projectile(turt, tank, target, facing_right = True):
    '''
    Shoots a projectile in a parabolic shape based on power and angle.

    Returns whether target is hit, power, and angle [tuple].
    '''
    power, angle = get_aim()
    
    prev_x = 0
    prev_y = 0

    angle = int(angle)
    power = int(power)

    for t in range(1, 30):

        # PROJECTILE DIRECTION (BASED ON KINEMATICS)
        if facing_right:
            x = power * math.cos(math.radians(angle)) * t + tank.xcor()
            y = power * math.sin(math.radians(angle)) * t - (((t ** 2) * 9.81) / 2) + tank.ycor()
        
        else:
            x = (power * math.cos(math.radians(angle)) * t) * -1 + tank.xcor()
            y = power * math.sin(math.radians(angle)) * t - (((t ** 2) * 9.81) / 2) + tank.ycor()
        
        turt.goto(x, y)
        turt.stamp()

        prev_x = x
        prev_y = y

        # STOP PROJECTILE WHEN TARGET IS REACHED
        if y <= target.ycor() + GRID_SIZE/2:
            break
    
    hit = hit_tank()

    return (hit, power, angle)


if __name__ == '__main__':
    setup_screen_turt(gameScreen, turtles)
    start_game(gameScreen, wordTurtle)

    gameScreen.mainloop()