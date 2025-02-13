import random
from turtle import *
import requests

inventory = []
current_area = 'you are outside a old run down bar'
def area():
    print(current_area)

def bar_drink():
    response = requests.get(
        'https://en.wikipedia.org/w/api.php', 
        params={
            'action': 'query',
            'format': 'json',
            'titles': 'Beer_cocktail',
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
        }
    ).json()

    page = next(iter(response['query']['pages'].values()))


    print(page['extract'])

def look():
    print("You are in a small, dimly lit room. There are old wooden shelves on the walls you could pick up, and a door leads to the north.")
    
def show_inventory():
    if len(inventory) == 0: 
        print('Inventory is empty')
    else:
        print('Inventory:', inventory)

def examine(item):
    if item == "key":
        print("The brass key looks old but well-maintained. It most open the bar room door.")
       
        circle(50)
        left(270)
        forward(100)
        left(90)
        forward(50)
        left(180)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
    elif item == "shelf":
        print('the shelf is old but simple and well-maintained')
    else:
        print(f"You don't see a {item} here.")

def get(item):
    if item == "key" and item not in inventory:
            inventory.append(item)
            print("You pick up the brass key.")
    elif item == "shelf" and item not in inventory:
            inventory.append(item)
            print("You pick up the shelf.")
    elif item == "key" and item in inventory:
            inventory.append(item)
            print("You already have the shelf.")
    elif item == 'key' and item in inventory:
            print("You already have the brass key.")
    else:
        print(f"There is no {item} to pick up here.")

def use(item):
    if item in inventory and item == 'key':
        print("You use the key to open the door. It creaks open, revealing a dark hallway.")
        inventory.remove(item)
    elif item in inventory and item != 'key':
        print(f"You use the {item}. But nothing special happens.") 
    else:
        print(f"You don't have a {item} in your inventory.")

def dice_game():
    print("Welcome to the Over or Under dice game!")
    
    die_roll = random.randint(1, 6)
    
    chosen_number = int(input("Choose a number between 1 and 6: "))
    
    if chosen_number < 1 or chosen_number > 6:
        print("Please choose a valid number between 1 and 6.")
        return 
    
    guess = input(f"Do you think the die roll will be 'over' or 'under' {chosen_number}? ").strip().lower()
    
    if guess not in ['over', 'under']:
        print("Please type 'over' or 'under'.")
        return 

    if (guess == 'over' and die_roll >= chosen_number) or (guess == 'under' and die_roll < chosen_number):
        print(f"Congratulations! You guessed correctly. The die rolled a {die_roll}.")
        print(f'since you won he gives you a bar key now all you need is a key to the drink instructions')
    else:
        print(f"Sorry, you guessed wrong. The die rolled a {die_roll}. You lost the game")
        exit()
        
def coin_flip():
    return random.choice(['heads', 'tails'])

def play_game():
    print("Welcome to the Heads or Tails game!")
   
    guess = input("Guess the coin flip result ('heads' or 'tails'): ").strip().lower()
   
    if guess not in ['heads', 'tails']:
        print("Invalid input. Please type 'heads' or 'tails'.")
        return  
    
    result = coin_flip()
    print(f"The coin landed on: {result}")
   
    if guess == result:
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, you guessed wrong.")
        exit()
        
def bar_room():
    print('you enter the bar and finally make your self a beer cocktail')
    
def back_room():
    print('you enter the back room and find the key on the desk')
    
def game_loop():
    while True:
        user_input = input("Enter a command (look, examine item, get item, inventory, current area, quit): ").strip().lower()

        if user_input == "quit":
            print("Exiting the command loop.")
            break

        if user_input == "look":
            look()
        elif user_input == "inventory":
            show_inventory()
        elif user_input == 'current area':
            area()
        elif user_input.startswith("examine "):
            item = user_input[len("examine "):].strip()
            examine(item)
        elif user_input.startswith("get "):
            item = user_input[len("get "):].strip()
            get(item)
        else:
            print("Unknown command. Please try again.")  

def game_loop2():
    while True:
        user_input = input("Enter a command (look, examine item, use item, inventory, current area, quit): ").strip().lower()

        if user_input == "quit":
            print("Exiting the command loop.")
            break

        if user_input == "look":
            look()
        elif user_input == "inventory":
            show_inventory()
        elif user_input == 'current area':
            area()
        elif user_input.startswith("examine "):
            item = user_input[len("examine "):].strip()
            examine(item)
            get(item)
        elif user_input.startswith("use "):
            item = user_input[len("use "):].strip()
            use(item)
        else:
            print("Unknown command. Please try again.")
            

introduction = input('welcome to the game, win games to find the key to the bar to get a beer cocktail, do you wish to continue: yes or no: ')
bar_drink()
if introduction == 'yes':
    outside_bar = input('you stand outside a old dingy bar, do you wish to enter: yes or no: ')
if outside_bar == 'yes':
    print('you enter a empty bar and find a man in the corner who offers to play a game of over or under in exhange for a hint')
    dice_game()
print('after beating the man at a game he tells you the key to the bar is kept in the back room, so you go on to the back room')
current_area = 'back rooms'
back_room()
game_loop()
print('you go back to the bar room and find a man standing in front of the door who will only move if you beat him at game of heads or tails')
play_game()
print('now you only have to use the key to open the door')
current_area = 'you are outside bar room the door looks surprisingly well kept'
game_loop2()
bar_room()