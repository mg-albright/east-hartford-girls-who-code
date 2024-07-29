import time

def explore_room(room):
    print("\nYou are now in the", room["name"])
    print(room["description"])
    time.sleep(1)
    if "item" in room:
        print("You found a", room["item"])
        inventory.append(room["item"])
        del room["item"]
    time.sleep(1)

def main_game_loop():
    current_room = rooms["entrance"]
    while True:
        explore_room(current_room)
        if current_room == rooms["treasure"]:
            print("Congratulations! You found the treasure and won the game!")
            break
        next_room = input("Where do you want to go next? (north/south/east/west): ").lower()
        if next_room in current_room:
            current_room = rooms[current_room[next_room]]
        else:
            print("You can't go that way. Try another direction.")

# Define the rooms and their connections
rooms = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "You are standing in the dusty entrance hall of a haunted house.",
        "north": "kitchen",
        "east": "living room"
    },
    "kitchen": {
        "name": "Kitchen",
        "description": "You enter a dimly lit kitchen with cobwebs covering the ceiling.",
        "south": "entrance"
    },
    "living room": {
        "name": "Living Room",
        "description": "You step into a spooky living room with old furniture covered in sheets.",
        "west": "entrance",
        "north": "treasure"
    },
    "treasure": {
        "name": "Treasure Room",
        "description": "You find yourself in a room filled with glittering treasure!"
    }
}

inventory = []

print("Welcome to the Haunted House Adventure Game!")
print("Your goal is to find the treasure hidden in the house.")

main_game_loop()
