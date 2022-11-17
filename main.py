print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first = input('You are at a crossroad. Do you want to go "left" or "right?"\n')
first_lower = first.lower()

if first_lower == "left":
  left = input('You reach a lake. In the middle you see a small island. Do you want to "wait" for a boat or try to "swim" to the other side?\n').lower()
  if left == "wait":
    wait = input('You safely reached the island. On a small hill you find a house with three doors. One "red", one "blue" and one "yellow". Which door do you choose?\n').lower()
    if wait == "blue":
      print('You enter the blue door and walk inside. The door behind you closes mysteriously. Suddenly a dog with three heads jumps out of the corner and eats you.\n"Game over"')
    elif wait == "red":
      print('You enter the red door. While walking around the room you hear a clicking sound and immediatly you are inside a blazing hellfire that burns you alive. It seems you stepped on a trap\n"Game over"')
    elif wait == "yellow":
      print('You enter the house through the yellow door. On the other side of the completely dark room you can see a light. You walk over and find a treasure chest full of gold and diamonds.\n"You Win!"')
    else:
      print('You are too indecisive to choose a door. So you leave the island empty handed.\n"Game over"')
  else:
    print('The other side was too far away, so you drowned.\n"Game Over"')
else:
  print('You fell into a hole.\n"Game Over" ')


