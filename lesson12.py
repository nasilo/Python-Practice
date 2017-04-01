n = [1, 3, 5]
print n[1]

n[1] = n[1] * 5
print n

# Append the number 4 here
n.append(4)
print n

# Remove the first item in the list here
n.pop(0)
print n

m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y
print add_function(m, n)

n = "Hello"
# Your function here!
def string_function(s):
    return s + "world"
print string_function(n)

def list_function(x):
    return x[1]
n = [3, 5, 7]
print list_function(n)

def list_function(x):
    x[1] = x[1] + 3
    return x
n = [3, 5, 7]
print list_function(n)

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst
print list_extender(n)

n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print x[i]
print_list(n)

n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print double_list(n)

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print my_function(range(3))

n = [3, 5, 7]
def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for word in words:
        result += word
    return result
print join_strings(n)

m = [1, 2, 3]
n = [4, 5, 6]
# Add your code here!
def join_lists(x,y):
    return x + y
print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results
print flatten(n)
