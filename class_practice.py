#! /usr/bin/python3
# class_practice.py - I'm just practicing making a class
import random

class Robot:

    def randomize_name(self):
        first_name = ''
        last_name = ''
        for i in range(2):
            first_name += random.choice('RX')
        for i in range(3):
            last_name += random.choice('013456789')
        full_name = first_name + last_name
        return full_name

    def get_name(self):
        return self.name

    def say_hello(self):
        print(f'Hello, my name is {self.name}.')

    def __init__(self):
        self.name = self.randomize_name()

R = Robot()
R.say_hello()

