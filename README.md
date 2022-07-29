# Tank-Game-2.0

## Summer 2022 Project


__Purpose of Project__

I wanted to put my coding skills in practice over the summer and create my very first game from scratch. By implementing a game such as this, I will be able to learn more about the process of game development and creating interfaces. I will be able to design a game, implement it, and test the game throughout my process, and to make the process streamlined, the creation of the game will be separated into ten milestones to be completed throughout the summer. If I am unable to meet a milestone, I will adjust accordingly. New tasks will be added to milestones when appropriate. After all milestones have been completed, changes and fixes will periodically be added to the game.

I originally created Tank-Game (https://github.com/camelliaguan3/Tank-Game), but I realized that my expectations for the game might have been too much for the Kivy module to handle. I wanted projectiles to fly across the screen in specific arcs depending on the aim of the tank gun. I instead decided to opt for the Turtle module, which can draw parabolas for projectiles. However, a downside is that the game will not be updating regularly, so listening for key or mouse inputs is more complicated, and drawing is also not done regularly with an update function. I aim to complete the game by the same deadline as the original Tank-Game.

<hr />

## How to Run the Game

1. Install introcs.

2. Run `python ..\Tank-Game-2.0` within the Tank-Game-2.0 folder.

<hr />

## Milestones

The *Milestones* section outlines each milestone and their due dates.

**Milestone 1**

*Due: July 29, 2022*

> &check; Create `main` function & `start_game()` function

> &check; Create welcome interface for the game

> &check; Create some functions to dismiss welcome interface and load in game

> &check; Create mid-game interface

> &cross; Make progress on tank projectile movement

**Milestone 2**

*Due: August 05, 2022*

> &cross; Clean up code

> &cross; Complete any code that is not finished

**Milestone 3**

*Due: August 12, 2022*

> &cross; Test game and fix/refine any smaller issues

> &cross; Add extra features if possible (i.e. animation, wind)

**Milestone 4**

*Due: August 19, 2022*

> &cross; Complete game :D

<hr />

## Design Choices

The *Design Choices* section explains any choices that I may have made in changing certain parts of the project or any parts of the project that required outside sources.

**Milestone 1**: I decided to have the turtles and screen as global variables to avoid situations where the screen and turtles cannot be accessed by functions. This was used with the dismissal of the welcome screen, as the `onkey()` method only calls a function that does not have parameters. Therefore, the `play_game()` function is unable to be called with the screen and turtle arguments and is required to reference the global variables. I will attempt to find a way that allows `play_game()` to have parameters.

<hr />

## Citations

The *Citations* section cites any outside sources that I may have used throughout the project and also describes the part of the project the source was used for. All images were drawn myself (via Piskel).

| Project Section | Description of Section | Source |
| - | - | - |
| | | |