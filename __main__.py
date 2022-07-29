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

def play_game():
    '''
    Plays the game.

    Returns None.
    '''
    pass


''' HELPER FUNCTIONS '''

def change_background(sc, background):
    '''
    Changes the background picture of the given screen.

    Returns None.
    '''
    sc.bgpic(background)


if __name__ == '__main__':
    setup_screen_turt(gameScreen, turtles)
    start_game(gameScreen, wordTurtle)

    gameScreen.mainloop()