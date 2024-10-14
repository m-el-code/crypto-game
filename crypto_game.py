from random import choice

import random
import string
ALPH = string.ascii_uppercase

def select_phrase():
    with open("messages.txt", mode="r") as message:
        message_list = message.readlines()
    return choice(message_list)

MESSAGE = select_phrase()

def rand_alph():
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)

RANDALPH = rand_alph()

def create_crypt():
    cryptDict = {}

    for i in range(len(ALPH)):
        cryptDict[ALPH[i]] = RANDALPH[i]
    return cryptDict

CRYPTDICT = create_crypt()

def encrypt_message():
    newMsg = MESSAGE.upper()
    
    cryptStr = ""
    for c in newMsg:
        if c in CRYPTDICT:
            cryptStr += CRYPTDICT[c]
        else:
            cryptStr += c
    
    return cryptStr

CRYPTMESSAGE = encrypt_message()

def player_input(guesses):
    while True:
        playerInput = input("Guess corresponding letters (i.e A=C): ")
        if valid_input(playerInput, guesses):
            guesses.update({playerInput[0]: playerInput[2]})
            state = check_letter(playerInput, guesses)
            return state
        else:
            print("Invalid input")
        

def valid_input(playerInput, guesses):
    return (
        len(playerInput) == 3 and 
        playerInput not in guesses and
        playerInput[0] in string.ascii_uppercase and
        playerInput[1] == "=" and 
        playerInput[2] in string.ascii_uppercase
    )


def check_letter(playerInput, guesses):
    if playerInput[2] == CRYPTDICT[playerInput[0]]:
        print("Correct Guess!")
        print(updated_message(guesses) + "\n" + CRYPTMESSAGE)
        if check_game(updated_message(guesses)):
            print("Message Solved!")
            return False
        return True

    else:
        print("Incorrect Guess! Try Again:")
        return True
        
#figure out how to display the updated message after ever guess

def display_message():
    newStr = CRYPTMESSAGE.upper()
    for c in newStr:
        if c in string.ascii_uppercase:
            print("_", end='')
        else:
            print(c, end='')
    print("\n" + CRYPTMESSAGE)

def updated_message(guesses):
    updatedMessage = ""
    message = MESSAGE.upper()
    for c in message:
        if c in guesses:
            if guesses[c] == CRYPTDICT[c]:
                updatedMessage += c
            else:
                updatedMessage += "_"
        elif c not in string.ascii_letters:
            updatedMessage += c
        else:
            updatedMessage += "_" 
    return updatedMessage


def check_game(message):
    for c in message:
        if c == "_":
            return False
    return True

if __name__ == "__main__":

    state = True
    guesses = {}
    display_message()

    while state:   
        state = player_input(guesses)
    
    print("Game Over!")