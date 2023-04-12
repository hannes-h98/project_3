# **The Battleship** #
The Battleship is a version of the classic battleship game made in python 

The game runs in the python terminal and your mission is to sink the computers ships before it sinks yours

## **How to play** ##
 * You take turns on trying to sink each others ships 
 * both the player and the computer have 3 ships each
 * The players ships are marked with a 1 and the computers ships are invisible

## **Features** ##
 ## Existing features ##
   * The ships are randomly generated onto the board
   * The player can not see the computers board
   * it accepts user input aswell as input validation for entering wrong numbers or letters
   * you can not enter the same coordinates twice


  ## Features to implement
  * Make the sunken ships on the computers board show as another number
  * Have an "enter your name" input

  ## Testing
  * passed through PEP8 with no problem
  * Tried to enter same numbers more then once, tried entering a string value, integers that are out of range from the grid
   it all works as intended

  ## Unfixed Bugs
  * For some reason the application works in the vs code terminal and local terminal, 
  but it does not work in the heroku mock terminal (wich is the whole point).
  Sadly i noticed that too late and i did not have the time to fix it.

  ## Deployment
  * The site was deployed using code institutes mock terminal for Heroku.
  * Fork or clone this repository
  * Create a new heroku app
  * set the buildbacks to python and Nodejs in that order
  * Link the Heroku app to the repository
  * click on deploy

  ## Credits
  * How to raise an exception from stackoverflow: [https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python]