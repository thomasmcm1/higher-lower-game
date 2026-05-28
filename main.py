import random
from game_data import data
from art import logo
from art import vs


def clear():
    print("\033[H\033[J",end="")

def assign():                   
    return random.choice(data)

def compare(p1, p2, user_input):
    sum1 = p1['net_worth']
    sum2 = p2["net_worth"]
    if sum1 > sum2:
        correct_person = p1
    else:
        correct_person = p2
    #valid answers
    first_name = correct_person["fname"].lower().strip()
    last_name = correct_person["Lname"].lower().strip()
    full_name = f"{first_name} {last_name}"
    
    guessed_answer = user_input.lower().strip()
    
    if guessed_answer in [first_name, last_name, full_name]:
        return True


def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        
        person1 = assign()
        person2 = assign()
        
        while person2 == person1:
            person2 = assign()
            
        
        while still_guessing:
            clear()
            print(logo)
            
            print(f"Name: {person1["fname"]} {person1["Lname"]}, Desc: {person1["description"]}")
            print(vs)
            print(f"Name: {person2["fname"]} {person2["Lname"]}, Desc: {person2["description"]}")
            
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            
            guess = input("Enter name of person with Higher Net Worth: ")
           
            if compare(person1, person2, guess):
                score = score + 1
                person1 = person2
                person2 = assign()
                
                while person2 == person1:
                    person2 = assign()
            else:
                still_guessing = False
        
        print("INCORRECT!")
        print("GAME OVER!")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        
        if play_again == "y":
            continue
        elif play_again == "n":
            playing_game = False
            clear()
            print("GAME OVER")
        else:
            playing_game = False
            print("INVALID")
            
            
want_to_play = input("Do you want to play? (y/n)\n").lower()
if want_to_play == "y":
    clear()
    play_higher_lower()
elif want_to_play == "n":
    print("Exit program")
else:
    print("Invalid, Exit program")