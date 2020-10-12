#! /usr/bin/python3
# Virtual Assistant is a python script that keeps track of users preferences ie. name, birthday, shows the weather.
# Can check date/time, show bitcoin price
# Future functions: calendar integration

import shelve, sys, requests, json


def greet_user(current_user):
    print(f'Hello {current_user}!')


def get_menu():
    print('''1. List Users\n2. Get weather\n3. Delete user\n4. Quit\n''')
    menu_choice = int(input('What would you like to do: '))
    return menu_choice

def get_weather():
    my_city = input('Enter the city for the area you would like to lookup: ')
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q='
    API_KEY = ''
    units = 'imperial'
    # updating URL
    URL = BASE_URL + my_city + '&units=' + units + '&appid=' + API_KEY
    # HTTP request
    response = requests.get(URL)
    response.raise_for_status()
    if response.status_code == 200:
        data = response.json()
        main = data['main']

        temperature = main['temp']
        report = data['weather']
        print(f'{my_city:-^30}')
        print(f'Temperature: {temperature}')
        print(f'Weather Report: {report[0]["description"]}')


print('*' * 36)
print('* Welcome to Virtual Assistant 2.0 *')
print('*' * 36)

current_user = input('Enter which user: ')
user_database = shelve.open('user_data')

if current_user not in user_database:
    birthday_month = input('What month is your Birthday?(1-12): ')
    birthday_day = input(f'What day in {birthday_month}?(1-31): ')
    birthday_year = input('What year?(19XX): ')
    birthday = birthday_month + '/' + birthday_day + '/' + birthday_year
    user_database[current_user] = birthday

greet_user(current_user)
choice = get_menu()

if choice == 1:
    for name in user_database.keys():
        print(name, end=' ')
    user_database.close()
elif choice == 2:
    get_weather()
elif choice == 3:
    if current_user in user_database:
        user_database.pop(current_user)
    print('Choice 3')
elif choice == 4:
    print('Choice 4')



