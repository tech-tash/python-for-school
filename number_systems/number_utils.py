"""
Module version 1.1

This module contains simple functions for positive decimal integers represented by lists of digits.

Given a list, L, of N digits, the digit, df, at L[0] is the most significant, and the digit, dl at
L[-1] is the least significant. The digit, df, has the value df*10^(N-1) i.e. df times ten to the
power of N-1. The digit, dl, has the value dl*10^(0) i.e. dl times ten to the power of zer0.

For example, the integer 365 may be represented as the list [3, 6, 5], the integer 0 by [0], and the
integer 1024 by [1, 0, 2, 4].

The functions provided enable:
* an integer to be divided by two
* an integer to be multiplied by two
* a string such as "365" to be translated to a list of digits [3, 6, 5]
* a list of digits, such as [3, 6, 5] to be translated to a string "365"
* a list of digits to be tested to see if it is zero.

The division function returns the integer part and the remainder e.g. 21 divided by 2 is 10 remainder 1.
Representing 21 as a list fo digits, [2, 1] divided by 2 is [1, 0] remainder 1.

Given an integer N digits long, the multiplication function returns a result that is N digits long plus
a carry digit. For example, 93 multiplied by 2 is (1)86 where the result is 86 and the carry digit is 1.
i.e the carry digit is what is carried in to the 10^N (ten to the power of N) column.

"""

def divide_by_two(decimal_number):
    """
    Divides the decimal_number by two, returning the result plus any remainder.
    e,g. 13/2 is divide_by_two([1, 3]) and the result is ([6], 1).
    :param decimal_number: list of digits representing a decimal integer
    :return:  a list of digits representing the integer result along with the remainder.
    """
    result = []
    carry = 0
    for digit in decimal_number:
        value = carry*10+digit
        carry = value % 2
        value = value // 2
        if not (value == 0 and result == []):
            result.append(value)
    if not result:
        result = [0]
    return result, carry


def multiply_by_two(decimal_number):
    """
    Multiplies the number by 2 returning the result in two parts: the lower len(decimal_number)
     digits and the carry from the left-most column.
    :param decimal_number: sequence of digits representing a decimal number.
    :return:  a sequence of digits and a carry digit.
    """
    result = []
    carry = 0
    for digit in decimal_number[::-1]:
        value = carry+digit*2
        carry = value // 10
        value = value % 10
        if not (value == 0 and result == []):
            result.append(value)
    if not result:
        result = [0]
    else:
        result = result[::-1]
    return result, carry


def is_zero(decimal_number):
    """
    Returns True if decimal_number is zero, otherwise False.
    :param decimal_number: a list of digits.
    """
    for digit in decimal_number:
        if not digit == 0:
            return False
    return True

def to_digits(string):
    """
    Translates a string of digits into a
    :param string:
    :return:
    """
    result = []
    for char in string:
        result.append(int(char))
    return result

def to_string(digits):
    result = ''
    for digit in digits:
        result=result+str(digit)
    return result


