'''
Summer 2022 Game Project

Tank-Game-2.0

Author: Camellia Guan
Start Date: July 29, 2022
End Date: N/A

'''

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
    



if __name__ == '__main__':
    setup_screen_turt(gameScreen, turtles)
    start_game(gameScreen, wordTurtle)

    gameScreen.mainloop()