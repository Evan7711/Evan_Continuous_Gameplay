#------------------------------------------------------------------------------
# Created By: Evan_Smart
# Created On: 09/03/23
# Version = '1.0'
# Class: CS 30
# Assignment: Continuous Game Play
#-----------------------------------------------------------------------------

"""
This Code runs a Continuous gameplay where you can Explore, Fight, or Hide
"""

# Code for the repeating phases
Start = "Would you like to Explore, Fight, Hide, or Quit: "
Travel = "Which Direction Would you like to go: North, South, East, West: "
Error = "You can't do that"
Attack = "Do you want to Punch, Kick, or Slap: "

while True:
  Choice = input(Start).lower()
  if Choice == "explore":
    # Code for the Explore Option
    while True:
      Direction = (input(Travel).lower())
      if Direction == "north" or "south" or "east" or "west":
        print(f"You travelled {Direction}")
        break
      else:
        print(Error)
  elif Choice == "fight":
    # Code for the Fight option
    while True:
      Fight = (input(Attack).lower())
      if Fight == "punch" or "slap" or "kick":
        print(f"You {Fight}ed him and won!")
        break
      else:
        print(Error)
  elif Choice == "hide":
    # Code for the Hide option
    print("You are in hiding")
  elif Choice == "quit":
    # Code for the Quit option
    print("Thank you for playing")
    break
  else:
    print(Error)