import random
print "Hey you, what is your name?" 
name = raw_input("Type your name: "), 
print "Lets play a game." 
print " %s, I am thinking of a number between 1 and 100. Try to guess my number" % name
attempts = 0
generated_integer = random.randint(1,100)

#guessing loop
while True:

    your_guess = raw_input("Your Guess: ")
    attempts = attempts + 1
    if attempts > 9:
        print "You have exceeded the limit of 9 attempts."
        break


    elif not your_guess.isdigit():
        print "Try again. Enter a number between 1 and 100."

    elif int(your_guess) < 1 or int(your_guess) > 100:
        print "Try again. Enter a number between 1 and 100."

    elif int(your_guess) < generated_integer:
        print "You've guessed too low, guess again:"

    elif int(your_guess) > generated_integer:
        print "You've guessed too high, guess again:"

    else:
        print "You win with %d attempts!"  % attempts
        break
