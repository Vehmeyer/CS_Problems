#Given an integer, write a function that reverses the bits (in binary) and returns the integer result.
#Examples:
#csReverseIntegerBits(417) -> 267
#417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
#csReverseIntegerBits(267) -> 417
#csReverseIntegerBits(0) -> 0

def csReverseIntegerBits(n):
    return int(''.join(reversed(bin(n)[2:])), 2)

#Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.
#Every eight bits in the binary string represents one character on the ASCII table.

def csBinaryToASCII(binary):
    if binary == "":
        return ""
    number = int(binary, 2)
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode()

#Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain 
#potential factors. A factor is a number that evenly divides into another number, leaving no remainder. 
# The simplest way to test if one number is a factor of another is to use the modulo operator.
#Here are the rules for csRaindrop. If the input number:
#has 3 as a factor, add "Pling" to the result.
#has 5 as a factor, add "Plang" to the result.
#has 7 as a factor, add "Plong" to the result.
#does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.

def csRaindrops(number):
    if number % 3 == 0:
        return "Pling"
    elif number % 5 == 0:
        return "Plang"
    elif number % 7 == 0:
        return "Plong"
    elif number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    elif number % 3 == 0 and number % 7 == 0 and number % 5 != 0:
        return "PlingPlong"
    elif number % 3 == 0 and number % 5 == 0 and number % 7 != 0:
        return "PlingPlang"
    elif number % 3 != 0 and number % 5 == 0 and number % 7 == 0:
        return "PlangPlong"
    elif number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)