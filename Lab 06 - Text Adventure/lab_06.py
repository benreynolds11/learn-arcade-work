class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    # Description for room 0
    room = Room("You are in a master bedroom. You see doors going to the east and south.", None, 1, 5, None)
    room_list.append(room)

    # Description for room 1
    room = Room("You are in a bathroom. There is one door which goes back into the bedroom west.", None, None, None, 0)
    room_list.append(room)

    # Description for room 2
    room = Room("You are now in what looks to be a living room. "
        "You can enter different rooms to you east and south.", None, 3, 7, None)
    room_list.append(room)

    # Description for room 3
    room = Room("You see that you are in a theater room. There are doors to your east and south.", None, 4, 8, None)
    room_list.append(room)

    # Description for room 4
    room = Room("You now enter a room with a bar. There are doors to your west and south.", None, None, 9, 3)
    room_list.append(room)

    # Description for room 5
    room = Room("You now enter what looks to be a kids bedroom. "
                "There are doors to your north and east.", 0, 6, None, None)
    room_list.append(room)

    # Description for room 6
    room = Room("You enter a gym with a bunch of weights and lifting machines. "
            "You see doors to your west and east.", None, 7, None, 5)
    room_list.append(room)

    # Description for room 7
    room = Room("You now enter a kitchen. You see doors to your west, north, and east.", 2, 8, None, 6)
    room_list.append(room)

    # Description for room 8
    room = Room("You now enter a super cool man cave. There are doors to your east and west.", None, 9, None, 7)
    room_list.append(room)

    # Description for room 9
    room = Room("You now enter a big room with a full size basketball court. "
            "There are doors to the north and west.", 4, None, None, 8)
    room_list.append(room)

    # Starting room
    current_room = 0


    done = False

    while not done:
        print(room_list[current_room].description)
        print()
        user_input = input("Which direction do you want to go? ")
        room_choice = user_input


        if room_choice.upper() == "North" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "South" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "East" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                    current_room = next_room

        elif room_choice.upper() == "West" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            print()
            if next_room is None:
                print("You can't go that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "Quit" or room_choice.upper() == "Q":
            done = True
            print()
            print("You have quit.")

        else:
            print()
            print("The program does not understand what you typed. Try again.")


main()
