import os

from telephone_operator import Operator
# phone = '4673212345'

import os

map1 = {
  '1': 0.9,
  '268': 5.1,
  '46': 0.17,
  '4620': 0.0,
  '468': 0.15,
  '4631': 0.15,
  '4673': 0.9,
  '467320': 1.1
}

map2 = {
  '1': 0.92,
  '44': 0.5,
  '46': 0.2,
  '467': 1.0,
  '48': 1.2
}

operators = Operator()
operators.add_operator(map1)
operators.add_operator(map2)

# phone = '4673212345'
# phone = '87097978'
phone = '4683212345'

print(operators.low_cost(phone))

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
 
def colorize(string, color):
  if not color in colors: return string
  return colors[color] + string + '\033[0m'
 
def show_operators():
  print("List of avaliable operators")
  operators.show_operators()
  input("Press [Enter] to continue...")
 
def search():
  print("Search lowest cost by number: ")
  phone = input("Please, write a phone number: ")
  low_cost = operators.low_cost(phone)
  if low_cost == -1:
    print('Prefix number does not exist registered')
  else:
    print('The lowest cost is {}'.format(low_cost))

  input("Press [Enter] to continue...")
 
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
      print(colorize(item, 'blue'), menuItems[item][1])
    choice = input(">> ")
    try:
      if int(choice) < 0 : raise ValueError
      # Call the matching function
      menuItems[choice][0]()
    except (ValueError, IndexError):
      pass
 
if __name__ == "__main__":
  main()

