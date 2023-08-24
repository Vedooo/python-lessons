import random as rd

attemps_list = []

def show_score():
    if not attemps_list:
        print('There is currently no high score,'
              ' it\'s yours for the taking!')
    else:
        print(f'The current high score is'
              f' {min(attemps_list)} attempts')
        
def start_game():
    attemps = 0
    number = rd.randint(1,100)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play =input(
        f'Hi,{player_name}, would you like to play '
        f'the guessing game? (Enter:Yes/No) '
    )
    if wanna_play.lower() != 'yes':
        print("That's cool!\n Thanks!")
    else:
        show_score()
        
    while wanna_play == 'yes':
        try:
            guess = int(input("Guess the number, pick between 1 and 100: "))
            if guess < 1 or guess > 100:
                raise ValueError(
                    "Please guess a number between 1 and 100"
                )
            attemps += 1
            attemps_list.append(attemps)
            if guess == number:
                print("You got it!")
                f'It took you {attemps} attemps'
                wanna_play =input(
                    f'So,{player_name}, wanna play again? (Enter:Yes/No)'
                )
                if wanna_play.lower() != 'yes':
                    print("That\ 's cool!\n Thanks!")
                    show_score()
                    break
                else:
                    attemps = 0
                    number = rd.randint(1,100)
                    show_score()
                    continue
            else:
                if guess > number:
                    print('It\'s lower')
                else:
                    print('It\'s higher')   
        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            return err

if __name__ == '__main__':
    start_game()