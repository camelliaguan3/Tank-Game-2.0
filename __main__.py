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


if __name__ == '__main__':
    setup_screen_turt(gameScreen, turtles)

    gameScreen.mainloop()