# import os
import time


def setup_game():

  # os.system('clear')

  print('''
Welcome to the Haunted House Adventure Game!

                              .     .
                               !!!!!!!
                       .       [[[|]]]    .
                       !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\\-_--\\
               |=|    /-_---__/__-__-_\\__-_\\
           . . |=| ._/-__-__\\===========/-__\\_
           !!!!!!!!!\\========[ /]]|[[\\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\\ ||== =|
        /-_-/^|^\\-_--| /^|^\\=|| | | | ||^\\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\\===========/-----/
   ^^^\\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\\ ]
       ||== =|/ _____ \\|== = ||=/^|^\\=||^\\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
      _||_ = =||o---.|| = ==_||_= == =||==_||_
      \\__/= = ||:   :||= == \\__/[][][][][]\\__/
      [||]= ==||:___:|| = = [||]\\\\//\\\\//\\\\[||]
      }  {---'"'-----'"'- --}  {//\\\\//\\\\//}  {
    __[==]__________________[==]\\\\//\\\\//\\\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
   |^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \\|//\\/^|/==============\\|/^\\\\^/^.\\^///\\//|///
 \\\\///\\\\//===============\\\\//\\\\///\\\\////\\\\/////
 ""'""'""".'..'. ' '. ''..'.""'""'""'""''"''"''""

You find yourself in a dark and eerie haunted house.
Your goal is to find the hidden treasure, but first 
you will need to find the key to open the treasure chest. 
At any point, you can type "help" to see a list of commands,
"inventory" to see a list of your items, or "quit" to exit 
the game.
=============================================================
''')
  
  time.sleep(1)

  while True:
    player = input('''
Hello traveler, it has been a long while since we have seen a visitor such as yourself. 
Please enlighten us, what is your identity? 

Are you a:
Ghost?
Witch?
Vampire?
Werewolf? 

''').lower()
    if player not in ['ghost', 'witch', 'vampire', 'werewolf']:
      print('\nHmmm I do not recognize your kind. Please try again.')
    else:
      break
  
  inventory = []

  
  while True:
    if player == "ghost":
      inventory.append(input('''
Ah, a fellow ghost. Welcome home friend. There will be many here who welcome your 
return, but other venegeful spirits will be waiting for you. To protect yourself, I can 
grant you one item. Please choose carefully:

Spectral Lantern: Emits a dim light that reveals hidden clues or secrets in 
  the environment.

Haunting Howl: A spectral ability that can frighten or distract enemies for a 
  short duration.
  
''').lower())

      if inventory[-1] not in ['spectral lantern', 'haunting howl']:
        print('\nHmmm I do not recognize that item. Please try again.')
      else: 
        break

    elif player == "witch":
      inventory.append(input('''
Hmmm, a witch. I can offer you one item to help you on your journey. Please choose carefully:

Grimoire of Shadows: A forbidden tome containing dark and powerful spells. While risky 
  to use, these spells could offer unparalleled destructive capabilities or control over
  supernatural forces.

Wand: A magical instrument that can be used for casting spells.

''').lower())

      if inventory[-1] not in ['grimoire of shadows', 'wand']:
        print('\nHmmm I do not recognize that item. Please try again.')
      else: 
        break

    elif player == "vampire":
      inventory.append(input('''
Hmmm, a vampire. I can offer you one item to help you on your journey. Please choose carefully:

Vial of Blood: Serves as a source of sustenance for the vampire character. Drinking 
blood replenishes health and possibly unlocks special abilities.

Crimson Cloak: Grants the vampire enhanced stealth abilities, allowing them to blend 
into the shadows and avoid detection.

''').lower())

      if inventory[-1] not in ['vial of blood', 'crimson cloak']:
        print('\nHmmm I do not recognize that item. Please try again.')
      else: 
        break

    elif player == "werewolf":
      inventory.append(input('''
Hmmm, a werewolf. I can offer you one item to help you on your journey. Please choose carefully:

Claw Gauntlets: Powerful melee weapons that amplify the werewolf's natural strength.

Scent Tracker: Allows the werewolf to detect hidden paths, track prey, and uncover hidden 
  items by following scent trails.

''').lower())

      if inventory[-1] not in ['claw gauntlets', 'scent tracker']:
        print('\nHmmm I do not recognize that item. Please try again.')
      else: 
        break

  
  # Define the rooms and their connections
  rooms = {
    "entrance": {
      "name": "Entrance Hall",
      "description": '''You are standing in the spacious entrance hall with a grand 
staircase leading to the upper floors. Chandeliers hang ominously overhead, 
casting eerie shadows. Tattered tapestries line the walls, depicting scenes 
from the mansion's dark history.''',
      "north": "library",
      "east": "parlor",
      "up": "ballroom"
    },
    "library": {
      "name": "Library",
      "description": '''You enter a dimly lit library filled with dusty books. 
Floor-to-ceiling bookshelves line the walls, filled with ancient tomes 
and dusty volumes. A faint whispering can be heard echoing through the 
stacks, as if the books themselves hold secrets.''',
      "south": "entrance",
      "east": "dining room",
       "encounter": "\nBooks fly off shelves and attack you! You must dodge or find a way to calm the restless spirits within the books."
    },
    "dining room": {
      "name": "Dining Room",
      "description": '''You enter a dining room with A long, ornate table set 
with dusty silverware and tarnished candlesticks. The room is filled with 
the lingering scent of decay, despite there being no food in sight. A portrait 
of the mansion's former owner presides over the room, their stern gaze 
unsettling to behold.''',
      "south": "parlor",
      "west": "library",
      "north": "kitchen",
      "item": "knife"
    },
    "kitchen": {
      "name": "Kitchen",
      "description": '''You enter a cavernous space filled with rusted pots and pans, 
cobweb-covered countertops, and an ancient stove. The air is thick with the 
scent of rotting food, despite the kitchen appearing abandoned for years. 
Mysterious noises emanate from the pantry, suggesting something sinister 
lurks within.''',
      "south": "dining room",
      "item": "key"
    },
    "parlor": {
      "name": "Parlor",
      "description": '''You step into a large room furnished with antique furniture, 
including plush sofas and armchairs. A fireplace crackles with ghostly flames, 
casting flickering shadows across the room. Portraits of long-deceased ancestors 
gaze down from the walls, their eyes seemingly following visitors as they move.''',
      "west": "entrance",
      "north": "dining room"
    },
    "ballroom": {
      "name": "Ballroom",
      "description": '''You find yourself in a grand ballroom with a worn wooden floor 
and tattered drapes adorning the walls. Faint music can be heard playing in the 
distance, echoing through the empty halls. The room is filled with the ghostly 
echoes of a long-forgotten celebration, frozen in time.''',
      "down": "entrance",
      "east": "child's bedroom",
      "north": "study",
      "encounter": "\nYou are pulled into a ghostly dance with an unseen partner! Match the rhythm of the dance to escape or risk being trapped forever in the ballroom."
    },
    "study": {
      "name": "Study",
      "description": '''You enter a cluttered room filled with dusty scrolls, arcane 
symbols, and half-finished experiments. The desk is covered with yellowed papers 
and quill pens, as if the owner vanished mid-task. Strange artifacts line the 
shelves, each radiating a sense of malevolent energy.''',
      "south": "ballroom",
      "east": "master bedroom",
      "encounter": "\nThere appears to be a thick wall of spider webbs blocking your path."
    },
    "master bedroom": {
      "name": "Master Bedroom",
      "description": '''You enter a grand master bedroom with a large, ornate bed 
and a dresser filled with ancient artifacts. The room is adorned with 
intricate carvings and ornate statues, each depicting a former owner's 
deeds and legacy. A faint whispering can be heard echoing through the 
room, as if the bedroom itself holds secrets.''',
      "west": "study",
      "south": "child's bedroom",
      "north": "attic",
      "encounter": "\nThe malevolent former master of the house appears as a ghost. It lashes out with spectral tendrils of energy, attempting to assert dominance over you, an intruder in the house!"
    },
    "child's bedroom": {
      "name": "Child's Bedroom",
      "description": '''You enter a small child's bedroom where a lone rocking horse 
sways eerily in the moonlight, its creaking filling the air with a haunting 
melody. Tattered teddy bears lie scattered on the floor, their button eyes 
seemingly following your every move with silent scrutiny. A faded mural on the 
wall depicts scenes of innocence and joy, now twisted into nightmarish visions 
of despair and longing.''',
      "west": "ballroom",
      "north": "master bedroom"
    },
    "attic": {
      "name": "Attic",
      "description": '''You ascend into a dark and damp attic filled with forgotten 
treasures, old furniture, and cobweb-covered trunks. Strange shadows dance along 
the walls, seemingly moving of their own accord. The attic holds the darkest 
secrets of the mansion, waiting to be uncovered by brave adventurers.''',
      "south": "master bedroom"
    }
  }

  # later -- add encounters to rooms dictionary based on character type
  num_rooms = 1
  return rooms, player, inventory, num_rooms

def explore_room(room):
  print("\nYou are now in the", room["name"])
  time.sleep(1)
  print('\n' + room["description"])
  time.sleep(1)
  if "item" in room:
    print("\nYou found a", room["item"])
    inventory.append(room["item"])
    del room["item"]
  time.sleep(1)


def encounter_room(room, inventory):
  if "encounter" in room:
    print(room["encounter"])
    time.sleep(1)

    # Encounter for master bedroom -- need an item from original game setup
    if room["name"] == "Master Bedroom":
      if "haunting howl" in inventory:
        print("\nYou use the haunting howl to distract the malevolent master, allowing you to sneak past him.")
        inventory.remove("haunting howl")
        time.sleep(1)
      elif "grimoire of shadows" in inventory:
        print("\nYou use the grimoire of shadows to control the malevolent master, allowing you to continue on through the house.")  # when implementing health, have this be a function that controls the master but decreases the player's health
        inventory.remove("grimoire of shadows")
        time.sleep(1)
      elif "crimson cloak" in inventory:
        print("\nYou use the crimson cloak to blend into the shadows, allowing you to sneak past the malevolent master.")
        inventory.remove("crimson cloak")
        time.sleep(1)
      elif "claw gauntlets" in inventory:
        print("\nYou use the claw gauntlets to amplify the werewolf's strength, allowing you to defeat the malevolent master and continue on through the house.")
        inventory.remove("claw gauntlets")
        time.sleep(1)
      else:
        print("\nYou do not have any items in your inventory that can help you defeat the malevolent master. You are defeated. Game over.")
        return False

    # Encounter for Study -- need knife from the dining room
    elif room['name'] == 'Study':
      if 'knife' in inventory:
        print('\nYou used your knife to cut through the webs, so you were able to move to the next room!')
        inventory.remove('knife')
        time.sleep(1)
      elif player == 'ghost':
        print('\nYou are a ghost, so you glide through the walls, avoiding the spider webs.')
        time.sleep(1)
      else:
        print('\nThe webs captured you, and you became dinner for the giant spider hiding in the corner of the room. Game over.')
        time.sleep(1)
        return False # instead of ending game here, can always stop you from entering room instead

    elif room['name'] == 'Library':
      if player == "vampire":
        print("\nThe books seem indifferent to your presence. You feel frustrated but continue on.")
        time.sleep(1)
      elif player == 'ghost':
        print('\nYou feel a sense of peace and understanding among the flying books. They lead you to a hidden passage.')
        time.sleep(1)
        print('\nThe hidden passage takes you through the house to the attic.')
        time.sleep(1)
        del room["encounter"]
        return "attic"
      elif player == 'witch':
        if "wand" in inventory:
          print('\nYou use your wand to cast a calming spell, and the books settle down, revealing a secret tunnel.')
          time.sleep(1)
          print('\nThere must have been lots of hungry scholars who lived here in a previous life because he hidden tunnel takes you to the kitchen.')
          time.sleep(1)
          inventory.remove('wand')
          del room["encounter"]
          return 'kitchen'
        else:
          print('\nYou do not have any skills or items to calm the books, and they chase you out of the house.')
          time.sleep(1)
          return False
      elif player == 'werewolf':
        print("\nThe flying books attack you, but you easily overpower them with your werewolf strength!")
        time.sleep(1)

    # elif room['name'] == 'Ballroom':
      

    del room["encounter"]
    
  return True


def check_inventory(inventory):
  print(f'\nYou have {len(inventory)} item(s) in your inventory, including:')
  for item in inventory:
    print('\n', item)


def help():
  print('\nType "north", "south", "east", or "west" to move to the next room. Type "inventory" to see a list of your items. Type "quit" to exit the game. Type "help" to see this list again.')


def move_to_next_room():
  return input(
    "\nWhere do you want to go next? (north/south/east/west/up/down): "
  ).lower()


def end_game(inventory, num_rooms):
  print(f'\nYou entered {num_rooms} rooms.')
  print(f"\nYou finished the game with {len(inventory)} items in your inventory, including:")
  for item in inventory:
    print('\n', item)


# def game_options(user_input):
  
  
  
def main_game_loop(rooms, player, inventory, num_rooms):
  current_room = rooms["entrance"]
  while True:
      explore_room(current_room)
      do_continue = encounter_room(current_room, inventory)
      if do_continue is False:
        end_game(inventory, num_rooms)
        break 
      elif do_continue is not True:
        current_room = rooms[do_continue]
        explore_room(current_room)
    
      if current_room == rooms["attic"]:
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
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

             ''')
        open = input(
          '\nThere appears to be a chest hidden under a dusty sheet. \
          Try to open it? (yes/no) '
        ).lower()
        if open == "yes":
          if "key" in inventory:
            print(
              "\nCongratulations! You found the key and unlocked the treasure chest!"
            )
            time.sleep(1)
            end_game(inventory, num_rooms)
            # print(f"\nYou won the game with {len(inventory)} items in your inventory.")
            # later -- add a line that tells you how many moved you beat the game in
            break
          else:
            print("\nThe chest was locked tight. Seems like you need a key to open it.")
        else:
          print("\nYou decided not to open the chest.")
      
      next_room = move_to_next_room()

      if next_room in ['quit', 'help', 'inventory']:
        if next_room == 'quit':
          print('\nThank you for playing!')
          end_game(inventory, num_rooms)
          break
        if next_room == 'help':
          help()
          next_room = move_to_next_room()
        if next_room == 'inventory':
          check_inventory(inventory)
          next_room = move_to_next_room()

      if next_room in current_room:
        current_room = rooms[current_room[next_room]]
        num_rooms += 1
        
      else:
        print("\nUh oh, there's no door in that direction, so you can't go that way.\n \
        Try another direction.")

      

rooms, player, inventory, num_rooms = setup_game()

main_game_loop(rooms, player, inventory, num_rooms)
