import os

from telephone_operator import OperatorsDirectory

"""
    Filling out operator prefixes and costs
"""
directory1 = {
    '1': 0.9,
    '268': 5.1,
    '46': 0.17,
    '4620': 0.0,
    '468': 0.15,
    '4631': 0.15,
    '4673': 0.9,
    '467320': 1.1
}

directory2 = {
    '1': 0.92,
    '44': 0.5,
    '46': 0.2,
    '467': 1.0,
    '48': 1.2
}

operators = OperatorsDirectory()
operators.add_operator(directory1)
operators.add_operator(directory2)

phone = '4683212345'

print(operators.low_cost(phone))

"""
    Menu resources are initialized and customized.
"""
header = "\
  _____ _____  _____ _____    _____ _           _ _                        \n\
 |_   _/ ____|/ ____/ ____|  / ____| |         | | |                       \n\
   | || |    | (___| (___   | |    | |__   __ _| | | ___ _ __   __ _  ___  \n\
   | || |     \___ \\___ \  | |    | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \ \n\
  _| || |____ ____) |___) | | |____| | | | (_| | | |  __/ | | | (_| |  __/ \n\
 |_____\_____|_____/_____/   \_____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___| \n\
                                                                __/ |      \n\
                                                               |___/       \n"
colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}

"""
    Colorize string for our menu
"""
def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'

"""
    Show operator function which shows prefixies and costs.
"""
def show_operators():
    print("List of avaliable operators")
    operators.show_operators()
    input("Press [Enter] to continue...")

"""
    Call search function, if response is -1 we
    consider phone does not exist. We validate our input too.
"""
def search():
    print("Search lowest cost by number: ")
    phone = input("Please, write a phone number: ")
    try:
        validated_phone = int(phone)
        if validated_phone >= 0:
            low_cost = operators.low_cost(str(validated_phone))
            if low_cost == -1:
                print('Prefix number does not exist registered')
            else:
                print('The lowest cost is {}'.format(low_cost))
        else:
            print('This is a negative number, try again')
    except ValueError:
        print('This is not an int, try again')
    input("Press [Enter] to continue...")

"""
    Menu options and descriptions
"""
menuItems = {
    "1": [show_operators, "Show operators"],
    "2": [search, "Search telephone number"],
    "3": [exit, "Exit"]
}


def main():
    while True:
        os.system('clear')
        print(colorize(header, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        for item in menuItems:
            print(colorize(item, 'blue'), menuItems[item][1])   # Print the color option and its description
        choice = input(">> ")
        try:
            if int(choice) < 0 or int(choice) > 3 : raise ValueError
            # Call the matching function
            menuItems[choice][0]()   
        except (ValueError, IndexError):
            print('This option does not exist, try again')

if __name__ == "__main__":
    main()
