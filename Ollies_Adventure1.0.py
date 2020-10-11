#!/usr/bin/python3
import sys, random, os


def play_intro():
    print('''Ollie an adventurer trying to free Irene,
from the Evil Grand Marshal. She is locked on top of a pyramid
Ollie must climb 4 levels to get to the top in order to face the Grand Marshal''')


def first_floor(health):
    print('''Ollie Enters the room and sees four doors with strange marks.
Which door do you choose?(1/2/3/4) ''')
    chosen_door = int(input())
    if chosen_door == 1:
        print('You walk in to a booby trap and lose 1 health.')
        health -= 1
        second_floor(health)
    elif chosen_door == 2:
        print('You find some food and gain 1 health')
        health += 1
        second_floor(health)
    elif chosen_door == 3:
        print('You Dead!')
        sys.exit()
    elif chosen_door == 4:
        print('You open the door and there is a staircase to go to a second floor.')
        second_floor(health)


def second_floor(health):
    print('You have made it to the second floor with %s health left' % health)
    print('On this floor there are Three doors, which one do you enter?(1/2/3) ')
    chosen_door = int(input())
    if chosen_door == 1:
        print('You got killed by a fire breathing dragon')
        sys.exit()
    elif chosen_door == 2:
        print('you go up to the third floor')
        third_floor(health)
    elif chosen_door == 3:
        print('You got bit by a spider, OUCH! You lost 1 health')
        health -= 1
        third_floor(health)


def third_floor(health):
    print('you have %s health and you are on the Third Floor' % health)
    print('You see a path with only 2 doors(left/right) which do you choose? ')
    answer = input().lower()
    if answer == 'left':
        print('You go in the door and up the stairs to the final room.')
        forth_floor(health)
    elif answer == 'right':
        health -= 1
        if health == 0:
            print('You ran out of Health')
            sys.exit()
        else:
            print('After fighting a Golem you lost 1 health but made it up the stairs')
            forth_floor(health)


def players_fight(my_health, enemy_health, my_attack, enemy_attack):
    my_health -= enemy_attack
    enemy_health -= my_attack
    print('You hit the enemy for %s attack points' % my_attack)
    print('He has %s HEALTH' % enemy_health)
    print('You have %s HEALTH' % my_health)
    if my_health == enemy_health:
        print('You were gravley wounded')
        print('You escape without Irene')
        sys.exit()
    elif my_health > enemy_health:
        print('You kill the enemy and get Irene')
        sys.exit()
    else:
        print('You die and Irene is taken off with the Grand Marshal!')
        sys.exit()


def forth_floor(health):
    my_health = health
    enemy_health = 3
    my_attack = random.randint(1, 3)
    enemy_attack = random.randint(1, 4)
    players_fight(my_health, enemy_health, my_attack, enemy_attack)


player_health = 3
os.system('clear')
play_intro()
while player_health != 0:
    first_floor(player_health)
