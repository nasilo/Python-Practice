def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

"""
     Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True


not is evaluated first;
and is evaluated next;
or is evaluated last.
"""

def using_control_once():
    if 10**2 == 100:
        return "Success #1"

def using_control_again():
    if not False:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False       # Make sure this returns False

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if "Brian" == "Messiah":
        naughty_boy = "Now listen here! He's not the Messiah. He's a very naughty boy!"
        print naughty_boy
    elif "Woman" <= "Duck" and "Duck" == "Wood":
        print "She's a witch!"
    else:
        return True
