import random
from random import randint
from time import sleep

class Room:
    def __init__(self, room_num):
        self.room_num = room_num


class Hero:
    def __init__(self, current_room, health, atk):
        self.current_room = current_room
        self.health = health
        self.atk = atk

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

    def attack(self):
        self.atk = randint(1, 5)
        print(f"You deal {self.atk} damage.")
        return self.atk


class Orc:
    def __init__(self, atk, health, location):
        self.atk = atk
        self.health = health
        self.location = location

    def attack(self):
        self.atk = randint(1, 3)
        print(f"The orc deals {self.atk} damage.")
        return self.atk


room_one = Room(1)
room_two = Room(2)
room_three = Room(3)
room_four = Room(4)
room_five = Room(5)
room_six = Room(6)
room_seven = Room(7)
room_eight = Room(8)
room_nine = Room(9)

hero_one = Hero(5, 10, 5)
direction = ''
in_room = hero_one.currently_in_room()
hero_health = hero_one.health
new_health = hero_health

orc_location = randint(1, 9)
orc_one = Orc(3, 10, orc_location)
orc_one_health = orc_one.health
new_orc_health = orc_one_health

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
        new_health = new_health - orc_one.attack()
        print(f"Your current health is {new_health}.")

    if in_room == orc_one.location:
        print("You attack the orc.")
        new_orc_health = new_orc_health - hero_one.attack()
        print(f"The orc's health is {new_orc_health}")

    if new_health <= 0:
        print("You died.")
        break

    if new_orc_health <= 0:
        print("The orc is dead.")
        print("You won!")
        break
print("Goodbye!")
sleep(5)
