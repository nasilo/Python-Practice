my_dict = {
    "caffinated": "overly",
    "tired": True,
    "age": 30,
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()
for key in my_dict:
    print key, my_dict[key]

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,12) if (x**2) % 2 == 0]
print even_squares

cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
print cubes_by_four

my_list = range(1, 11) # List of numbers 1 - 10
# Add your code below!
print my_list[::2]

my_list = range(1, 11)
# Add your code below!
backwards = my_list[::-1]

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

squares = [x**2 for x in range(1,11)]
print filter(lambda x: 30 <= x and x <= 70, squares)

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
