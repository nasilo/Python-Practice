def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_int(x):
    if type(x) == int or x % int(x) == 0:
        return True
    else:
        return False

def digit_sum(n):
    string = str(n)
    total = 0
    for digit in string:
        total += int(digit)
    return total

def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return 1

def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
                break
        else:
            return True

def reverse(text):
    output = ""
    for i in range(len(text)):
        output += text[len(text) - 1 - i]
    return output

def anti_vowel(text):
    output = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in text:
        is_vowel = False
        for vowel in vowels:
            if char.lower() == vowel:
                is_vowel = True
        if is_vowel == False:
            output += char
    return output

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def scrabble_score(word):
    word_score = 0
    for char in word:
        word_score += score[char.lower()]
    return word_score

def censor(text, word):
    output = ""
    count = 0
    while count < len(text):
        if text[count] != word[0]:
            output += text[count]
            count += 1
        elif len(text) - count + 1 < len(word):
            output += text[count]
            count += 1
        else:
            if text[count:count + len(word)] == word:
                output += "*" * len(word)
                count += len(word)
            else:
                output += text[count]
                count += 1
    return output

def count(sequence, item):
    found = 0
    for index in sequence:
        if index == item:
            found += 1
    return found

def purify(numbers):
    output = []
    for number in numbers:
        if number % 2 == 0:
            output.append(number)
    return output

def product(number_list):
    total = 1
    for number in number_list:
        total *= number
    return total

def remove_duplicates(number_list):
    output = []
    for number in number_list:
        if number not in output:
            output.append(number)
    return output

def median(numbers):
    ordered = sorted(numbers)
    if len(numbers) % 2 == 0:
        a = float(ordered[len(ordered) / 2 - 1])
        b = float(ordered[len(ordered) / 2])
        average = (a + b) / 2
        return average
    else:
        return ordered[len(ordered) / 2]
