import random

def get_guess():
    return list(input("What is your guess: "))

def generate_code():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome Code Breaker!")

secret_code = generate_code()

clue_reporter = []

while clue_reporter != "CODE CRACKED!":
    guess = get_guess()

    clue_reporter = generate_clues(guess, secret_code)
    print("here is the result of your guess: ")
    for clue in clue_reporter:
        print(clue)