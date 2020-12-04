"""
My house
"""


# Create a room class
class Room:
    def __init__(self, description, north, east, south, west, northeast, southeast, southwest, northwest, up, down):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.southeast = southeast
        self.southwest = southwest
        self.northwest = northwest
        self.up = up
        self.down = down


# Create a item class
class Item:
    def __init__(self, room, description, name):
        self.room = room
        self.description = description
        self.name = name


# Create a person class
class Person:
    def __init__(self, room, description, name):
        self.room = room
        self.description = description
        self.name = name


# Create the main function
def main():

    # Create people list
    person_list = []

    # Create the people
    messi = Person(15, "Lionel Messi is standing in front of you. He want's you to shoot with him. "
                       "You can go shoot with him or go to a different room.", "messi")
    person_list.append(messi)

    jordan = Person(9, "Michael Jordan is standing under the basketball hoop. He want's to shoot hoops with him. "
                       "You can go shoot with him or go to a different room.", "jordan")
    person_list.append(jordan)

    bartender = Person(4, "There is a bartender standing behind the bar. "
                          "He says they are only serving water at this time.", "bartender")
    person_list.append(bartender)

    # Create the item list
    item_list = []

    # Create the items
    item = Item(2, "You are bored and want to watch T.V. You see a remote on the table next to you. Pick it up if you "
                   "would like.", "remote")
    item_list.append(item)

    item = Item(7, "You see a delicious apple on the counter. Pick it up and save it for later if you want.", "apple")
    item_list.append(item)

    item = Item(9, "You see a basketball laying on the ground." 
                   "Pick it up if you would like", "basketball")
    item_list.append(item)

    item = Item(15, "There are soccer balls laying around. Go pick one up and keep it if you would like.", "ball")
    item_list.append(item)

    item = Item(4, "You see a glass of water sitting on the bar. Go pick it up and take a drink if you want.", "water")
    item_list.append(item)

    # Create the room list
    room_list = []

    # Description for room 0
    room = Room("You are in a master bedroom. You see doors going to the east and south. You can also go southeast.",
                None, 1, 5, None, None, 6, None, None, None, None)
    room_list.append(room)

    # Description for room 1
    room = Room("You are in a bathroom. There is one door which goes back into the bedroom west.\nYou can also go "
                "southwest.", None, None, None, 0, None, None, 5, None, None, None)
    room_list.append(room)

    # Description for room 2
    room = Room("You are now in what looks to be a living room. "
                "You can enter different rooms to you east and south. You can also go southeast to a man cave.", None,
                3, 7, None, None, 8, None, None, None, None)
    room_list.append(room)

    # Description for room 3
    room = Room("You see that you are in a theater room. There are doors to your east and south. There also is a "
                "entrance to a basketball court southeast.", None, 4, 8, 2, None, 9, None, None, None, None)
    room_list.append(room)

    # Description for room 4
    room = Room("You now enter a room with a bar. There are doors to your west and south. There are also stairs that "
                "go up or down.", None, None, 9, 3, None, None, None, None, 11, 16)
    room_list.append(room)

    # Description for room 5
    room = Room("You now enter what looks to be a kids bedroom. "
                "There are doors to your north and east.", 0, 6, None, None, None, None, None, None, None, None)
    room_list.append(room)

    # Description for room 6
    room = Room("You enter a gym with a bunch of weights and lifting machines. "
                "You see doors to your west and east. You can also go northwest.", None, 7, None, 5, None, None, None,
                0, None, None)
    room_list.append(room)

    # Description for room 7
    room = Room("You now enter a kitchen. You see doors to your west, north, and east. You can also go into the "
                "bathroom northwest or head out to the deck south.", 2, 8, 10, 6, None, None, None, 1, None, None)
    room_list.append(room)

    # Description for room 8
    room = Room("You now enter a super cool man cave. There are doors to your east and west. "
                "You can also go northwest.", None, 9, None, 7, None, None, None, 2, None, None)
    room_list.append(room)

    # Description for room 9
    room = Room("You now enter a big room with a full size basketball court. "
                "There are doors to the north and west. Theres another door that goes northwest.", 4, None, None, 8,
                None, None, None, 3, None, None)
    room_list.append(room)

    # Description for room 10
    room = Room("You are now outside on the deck outlooking the beautiful ocean. You can only go back north where "
                "you came from.", 7, None, None, None, None, None, None, None, None, None)
    room_list.append(room)

    # Description for room 11
    room = Room("You are now upstairs in a hallway. You may go south, southwest, or west. "
                "You can also go back downstairs.", None, None, 13, 12, None, None, 14, None, None, 4)
    room_list.append(room)

    # Description for room 12
    room = Room("You are now in a guest bedroom. You may go east, southeast, south, or west.", None, 11, 14, 15, None,
                13, None, None, None, None)
    room_list.append(room)

    # Description for room 13
    room = Room("You are now in a storage room with nothing but boxes. You may go north back into "
                "the hallway or northwest.", 11, None, None, None, None, None, None, 12, None, None)
    room_list.append(room)

    # Description for room 14
    room = Room("You are in a bathroom. You can go north", 12, None, None, None, None, None, None, None, None, None)
    room_list.append(room)

    # Description for room 15
    room = Room("You are now in a indoor soccer field. You may go east into the bedroom.", None, 12, None, None, None,
                None, None, None, None, None)
    room_list.append(room)

    # Description for room 16
    room = Room("You have now entered the basement which includes a giant pool. "
                "You can only go back upstairs from here.", None, None, None, None, None, None, None, None, None, 4)
    room_list.append(room)

    # Starting room
    current_room = 0

    # Create boolean variable
    done = False
    while not done:
        # Print room description
        print()
        print(room_list[current_room].description)

        # Print items in room
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        # Print the person description
        for person in person_list:
            if person.room == current_room:
                print(person.description)

        # Get command from user
        print()
        user_input = input("What's your command master?")
        command_words = user_input.split(" ")

        # North command
        if command_words[0].upper() == "NORTH" or command_words[0].upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # South command
        elif command_words[0].upper() == "SOUTH" or command_words[0].upper() == "S":
            next_room = room_list[current_room].south
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # East Command
        elif command_words[0].upper() == "EAST" or command_words[0].upper() == "E":
            next_room = room_list[current_room].east
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # West command
        elif command_words[0].upper() == "WEST" or command_words[0].upper() == "W":
            next_room = room_list[current_room].west
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Northeast command
        elif command_words[0].upper() == "NORTHEAST" or command_words[0].upper() == "NE":
            next_room = room_list[current_room].northeast
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Southeast command
        elif command_words[0].upper() == "SOUTHEAST" or command_words[0].upper() == "SE":
            next_room = room_list[current_room].southeast
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Southwest command
        elif command_words[0].upper() == "SOUTHWEST" or command_words[0].upper() == "SW":
            next_room = room_list[current_room].southwest
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Northwest command
        elif command_words[0].upper() == "NORTHWEST" or command_words[0].upper() == "NW":
            next_room = room_list[current_room].northwest
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Up command
        elif command_words[0].upper() == "UP" or command_words[0].upper() == "U":
            next_room = room_list[current_room].up
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Down command
        elif command_words[0].upper() == "DOWN" or command_words[0].upper() == "D":
            next_room = room_list[current_room].down
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        # Allow user to quit
        elif command_words[0].upper() == "QUIT" or command_words[0].upper() == "Q":
            done = True
            print("You have quit.")

        # Be able to pick up objects
        elif command_words[0].upper() == "GET" or command_words[0].upper() == "G":
            get_item = False
            for item in item_list:
                if item.room == current_room and item.name == command_words[1].lower():
                    print()
                    print("You have obtained", item.name)
                    get_item = True
                    item.room = -1
            if not get_item:
                print()
                print("The item your requesting isn't here.")

        # Be able to release objects
        elif command_words[0].upper() == "RELEASE" or command_words[0].upper() == "R":
            get_item = False
            for item in item_list:
                if item.room == -1 and item.name == command_words[1].lower():
                    print()
                    print(f"You have released {item.name}.")
                    get_item = True
                    item.room = current_room
            if not get_item:
                print()
                print("You currently don't have this item.")

        # Allow user to check inventory
        elif command_words[0].upper() == "INVENTORY" or command_words[0].upper() == "I":
            for item in item_list:
                if item.room == -1:
                    print(item.name)

        # Allow user to shoot
        elif command_words[0].upper() == "SHOOT" or command_words[0].upper() == "SH":
            item_use = False
            for item in item_list:
                if item.room == -1 and command_words[1].lower() == "basketball" and item.name == "basketball" \
                        or item.name == "ball":
                    print()
                    print("You shoot the ball.")
                    item_use = True
                    # Allow user to shoot with person
                    for person in person_list:
                        if person.room == current_room:
                            print()
                            print("You have successfully just shot with one of the greatest players of all time. "
                                  "He will now disappear.")
                            person.room = -1
            if not item_use:
                print()
                print("You don't have a ball in your hand.")

        # Allow user to drink
        elif command_words[0].upper() == "DRINK" or command_words[0].upper() == "D":
            item_use = False
            for item in item_list:
                if item.room == -1 and item.name == "water":
                    print()
                    print("You drink the water.")
                    item_use = True
                    for person in person_list:
                        if person.room == current_room:
                            print()
                            print("You just drank some of the best water this bartender has ever had to offer. "
                                  "He now has to leave and go resupply with water.")
                            person.room = -1
            if not item_use:
                print()
                print("You don't have a glass of water in your hand.")

        # Allow user to use an object
        elif command_words[0].upper() == "USE" or command_words[0].upper() == "U":
            item_use = False
            for item in item_list:
                if item.room == -1 and item.name == "remote":
                    print()
                    print("You use the remote.")
                    item_use = True
            if not item_use:
                print()
                print("You don't have the remote in your hand.")

        else:
            print()
            print("The program does not understand what you typed. Try again.")


main()
