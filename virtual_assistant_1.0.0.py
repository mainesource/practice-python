#! /usr/bin/python3
# Virtual Assistant is a python script that keeps track of users preferences ie. name, birthday, shows the weather.
# Can check date/time, show bitcoin price
# Future functions: calendar integration

print('*' * 36)
print('* Welcome to Virtual Assistant 1.0 *')
print('*' * 36)


def greet(user_name):       # Greet user
    return print(f'Hello {user_name}, the future is yours!')


current_user = input("Who's virtual assistant would you like to start: ")       # User enters their name
while True:
    user_database = []
    user_file = open('user.txt', 'r')  # Open user.txt file read names to file object
    user_file_content = user_file.read()  # File Object is converted to string
    user_file.close()
    user_database = user_file_content.split(',')  # split names string with ',' put in a list
    if current_user in user_database:
        greet(current_user)
    else:
        print('You are not in the database.')
        user_database.append(current_user)
        print(f'{current_user} was entered.')
        user_file_content = ','.join(user_database)
        user_file = open('user.txt', 'w')
        user_file.write(user_file_content)
        user_file.close()

    stop_assistant = input('Do you want to continue Assistant? Y/N: ')
    if stop_assistant.lower() == 'n':
        break
    # TODO check if user has a birthday in Dictionary
    birthday = []
    birthday_month = input('What month is your Birthday?(1-12): ')
    birthday_day = input(f'What day in {birthday_month}?(1-31): ')
    birthday_year = input('What year?(19XX): ')
    birthday.append(birthday_month + '/' + birthday_day + '/' + birthday_year)
    user_info = {}
    user_info = {current_user: birthday[0]}
    print(user_info)
    with open('user_info.txt', 'w+') as user_info_file:
        user_info_file.write(f'{user_info.keys()}-->{user_info[current_user]}')







