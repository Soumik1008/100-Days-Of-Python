from art import logo, vs
from game_data import data
import random

print(logo)
score = 0
game_should_continue = True
account_B = random.choice(data)


def clear():
    return '\n * 50'


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_desc} from {account_country}"


def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'


while game_should_continue:
    account_A = account_B
    account_B = random.choice(data)

    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    
    if is_correct:
        score = score + 1
        print(f"You are correct. Current Score: {score}")
    else:
        game_should_continue = False
        print(f"You're wrong. Final Score: {score}")