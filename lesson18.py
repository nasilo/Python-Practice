print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)

shift_right = 0b1100
shift_left = 0b1
# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2
print bin(shift_right)
print bin(shift_left)

print bin(0b1110 & 0b101) # and operator = 0100
print bin(0b1110 | 0b101) # or operator = 1111
print bin(0b1110 ^ 0b101) # xor operator = 1011

print ~1 # -2
print ~2 # -3
print ~3 # -4
print ~42 # -43
print ~123 # -124

def check_bit4(input):
    bit4 = 0b1000
    if input & bit4 > 0:
        return "on"
    else:
        return "off"

a = 0b10111011
print bin(a | 0b100)

a = 0b11101110
mask = 0b11111111
print bin(a ^ mask)

def flip_bit(number, n):
    mask = 0b1 << n - 1
    result = number ^ mask
    return bin(result)
