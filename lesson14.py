count = 0
if count < 10:
    print "Hello, I am an if statement and count is", count
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

choice = raw_input('Enjoying the course? (y/n)')
while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

count = 0
while count < 10: # Add a colon
    print count
    count += 1  # Increment count

count = 0
while True:
    print count
    count += 1
    if count >= 10:
        break

import random
print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
# Start your game!
while guesses_left > 0:
    print "guesses left: %i" % guesses_left
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose."

thing = "spam!"
for c in thing:
    print c
word = "eggs!"
# Your code here!
for c in word:
    print c

phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
    if char.upper() == "A":
        print "X",
    else:
        print char,
#Don't delete this print statement!
print

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    # Your code here!
    print "%s %s" % (key, d[key])

choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item
