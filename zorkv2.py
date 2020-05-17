import random
from random import randint

class Room:
    def __init__(self, room_num, can_go_north, can_go_east, can_go_south, can_go_west):
        self.room_num = room_num
        self.can_go_north = can_go_north
        self.can_go_east = can_go_east
        self.can_go_south = can_go_south
        self.can_go_west = can_go_west


class Hero:
    def __init__(self, current_room, health):
        self.current_room = current_room
        self.health = health

    def move_north(self):
        self.current_room = self.current_room - 3

    def move_south(self):
        self.current_room = self.current_room + 3

    def move_east(self):
        self.current_room = self.current_room + 1

    def move_west(self):
        self.current_room = self.current_room - 1

    def currently_in_room(self):
        return self.current_room


class Orc:
    def __init__(self, atk, health, location):
        self.atk = atk
        self.health = health
        self.location = location

    def attack(self):
        self.atk = randint(1, 3)


room_one = Room(1, False, True, True, False)
room_two = Room(2, False, True, True, True)
room_three = Room(3, False, False, True, True)
room_four = Room(4, True, True, True, False)
room_five = Room(5, True, True, True, True)
room_six = Room(6, True, False, True, True)
room_seven = Room(7, True, True, False, False)
room_eight = Room(8, True, True, False, True)
room_nine = Room(9, True, False, False, True)

hero_one = Hero(5, 10)
direction = ''
in_room = hero_one.currently_in_room()

orc_one = Orc(3, 10, 1)

while direction != 'q':
    direction = input("Where would you like to go? Type q to quit. ")
    if direction == 'north':
        if hero_one.currently_in_room() == room_one.room_num:
            print("You cannot go north")
        elif hero_one.currently_in_room() == room_two.room_num:
            print("You cannot go north")
        elif hero_one.currently_in_room() == room_three.room_num:
            print("You cannot go north")
        else:
            hero_one.move_north()
            hero_one.currently_in_room()
            in_room = hero_one.currently_in_room()
            print(f"You are now in room {in_room}.")
    if direction == 'south':
        if hero_one.currently_in_room() == room_seven.room_num:
            print("You cannot go south")
        elif hero_one.currently_in_room() == room_eight.room_num:
            print("You cannot go south")
        elif hero_one.currently_in_room() == room_nine.room_num:
            print("You cannot go south")
        else:
            hero_one.move_south()
            hero_one.currently_in_room()
            in_room = hero_one.currently_in_room()
            print(f"You are now in room {in_room}.")
    if direction == 'west':
        if hero_one.currently_in_room() == room_one.room_num:
            print("You cannot go west")
        elif hero_one.currently_in_room() == room_four.room_num:
            print("You cannot go west")
        elif hero_one.currently_in_room() == room_seven.room_num:
            print("You cannot go west")
        else:
            hero_one.move_west()
            hero_one.currently_in_room()
            in_room = hero_one.currently_in_room()
            print(f"You are now in room {in_room}.")
    if direction == 'east':
        if hero_one.currently_in_room() == room_three.room_num:
            print("You cannot go east")
        elif hero_one.currently_in_room() == room_six.room_num:
            print("You cannot go east")
        elif hero_one.currently_in_room() == room_nine.room_num:
            print("You cannot go west")
        else:
            hero_one.move_east()
            hero_one.currently_in_room()
            in_room = hero_one.currently_in_room()
            print(f"You are now in room {in_room}.")

    if in_room == orc_one.location:
        print("An orc attacks you!")
