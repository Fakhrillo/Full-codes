###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
def generate_code():
    digits = list(range(10))
    random.shuffle(digits)
    print(digits[:3])
    return (digits[:3])

def TakeNumbers():
    # number = list(input("Enter your guess ?"))
    number=[int(n) for n in input("Enter Number:").split(",")]
    return number

def comp(gen_code,usr_inp):

    if (gen_code==usr_inp):
        return "Code CRACKED!!"
    # code for comaparison of user input and generated code
    for count, elem in enumerate(gen_code):
        if elem==usr_inp[count]:
            return "Match"
        elif elem==usr_inp:
            return "Close"
        else:
            return "Nope"

# Run Game
print (" Welcome Code Breaker, Let's see if you can guess my 3 digit number!\n Code has been generated, please guess a 3 digit number")
# declaring return_code
return_code=""
#ask the user until he gives correct code
while (return_code != "Code CRACKED!!"):
    # take user guess
    usr_inp=TakeNumbers()
    # generate the numbers
    gen_code = generate_code()
    # comaparison
    return_code=comp(gen_code,usr_inp)
    # print result
    print(return_code)


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!