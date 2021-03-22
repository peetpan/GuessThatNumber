import random

num = random.randint(1, 100)

print('''
 _______         _______  _______ _______   _________        ________________   _               _______ ______  _______ _______ 
(  ____ \\     /(  ____ \(  ____ (  ____ \  \__   __/\     /(  ___  )__   __/  ( (    /|\     /(       |  ___ \(  ____ (  ____ )
| (    \/ )   ( | (    \/| (    \/ (    \/     ) (  | )   ( | (   ) |  ) (     |  \  ( | )   ( | () () | (   ) ) (    \/ (    )|
| |     | |   | | (__    | (_____| (_____      | |  | (___) | (___) |  | |     |   \ | | |   | | || || | (__/ /| (__   | (____)|
| | ____| |   | |  __)   (_____  |_____  )     | |  |  ___  |  ___  |  | |     | (\ \) | |   | | |(_)| |  __ ( |  __)  |     __)
| | \_  ) |   | | (            ) |     ) |     | |  | (   ) | (   ) |  | |     | | \   | |   | | |   | | (  \ \| (     | (\ (   
| (___) | (___) | (____/\/\____) /\____) |     | |  | )   ( | )   ( |  | |     | )  \  | (___) | )   ( | )___) ) (____/\ ) \ \__
(_______|_______|_______/\_______)_______)     )_(  |/     \|/     \|  )_(     |/    )_|_______)/     \|/ \___/(_______//   \__/
''')


def game_mech(attem):
    while attem != 0:
        print(f'You have {attem} attempts to guess the number')
        guess = int(input("Make a Guess: "))
        if guess > num:
            print("Too high")
            attem -= 1
        elif guess < num:
            print("Too low")
            attem -= 1
        else:
            print('You Guessed it right. Congrats')
            return
    print('You lost!')


flag = 'y'
while flag == 'y':
    print("\nWelcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
    diff = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
    if diff == 'easy':
        game_mech(10)
    elif diff == 'hard':
        game_mech(5)
    else:
        print("Invalid Text")
    flag = input('Do you want to try again? \'y\' or \'n\': ')
