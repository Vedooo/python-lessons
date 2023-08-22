from art import logo, vs
from game_data import data
from replit import clear
import random as rd


def get_random_data():
    return rd.choice(data)

def generate_case(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return print(f"{name}, {description} from {country}")
    
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    game_should_continue = True
    
    account_a = get_random_data()
    account_b = get_random_data()
    
    while game_should_continue:
        account_a = account_b
        account_b = get_random_data()
        
        while account_a == account_b:
            account_b = get_random_data()
        
        print(f"Compare A: {generate_case(account_a)}")
        print(vs)
        print(f"Compare B: {generate_case(account_b)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess,a_follower_count, b_follower_count)
        
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            
game()