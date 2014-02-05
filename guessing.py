import random
print "Hey You, What is your name?" 
name = raw_input("Type your name: "), 
print "Lets play a game." 
print " %s, I am thinking of a number between 1 and 100. Try to guess my number" % name

generated_integer = random.randint(1,100)
your_guess = ""

while generated_integer != your_guess:

    your_guess = int(raw_input("Your Guess:"))

    if your_guess == generated_integer:
        print "You Win!"

    if your_guess < generated_integer:
        print "You've guessed too low, guess again:"

    elif your_guess > generated_integer:
        print "You've guessed too high, guess again:"

    