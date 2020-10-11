#!/usr/bin/python3
import os


def get_name():
    player_name = input('Hello, what is your name: ')
    return player_name


def get_age():
    player_age = input('How old are you? ')
    return int(player_age)


def check_in_dict():
    name_database = {}
    name = get_name()
    age = get_age()
    if name not in name_database:
        name_database.setdefault(name, age)
        print('Name Entered')
        enter_another = input('Do you want to enter another name?(y/n) ')
        if enter_another == 'y':
            check_in_dict()
        else:
            return False, len(name_database)
    else:
        print('Your name is in the system!')
        return True


answer, enteries = check_in_dict()
print(enteries)
