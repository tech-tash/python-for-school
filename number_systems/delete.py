# decimal_to_ieee_single.py
from number_utils import to_digits, is_zero
from decimal_to_binary import divide_by_two, multiply_by_two

def normalize(int_part, frac_part):
    """
    Normalize the number and return the significand and exponent.
    :param int_part: The integer part of the number.
    :param frac_part: The fractional part of the number.
    :return: Tuple of normalized binary string and exponent.
    """
    # Convert integer and fraction to binary
    int_binary = to_digits(str(int_part))
    frac_binary = []

    # Get the binary representation of the fractional part
    while frac_part > 0 and len(frac_binary) < 23:  # Limit to 23 bits for the significand
        frac_part *= 2
        bit = int(frac_part)
        frac_binary.append(bit)
        frac_part -= bit

    # Normalize the binary representation
    if int_part == 0:
        # Find the first 1 in the fractional part
        for i, bit in enumerate(frac_binary):
            if bit == 1:
                exponent = -(i + 1)
                significand = frac_binary[i + 1:]
                break
        else:
            exponent = 0
            significand = [0] * 23  # If it is zero
    else:
        # Handle integer part normalization
        exponent = len(int_binary) - 1
        significand = int_binary[1:] + frac_binary  # Drop the leading 1 and append fraction
    
    # Ensure significand is 23 bits long
    significand = significand[:23] + [0] * (23 - len(significand))
    
    return ''.join(map(str, significand)), exponent

def main():
    num = float(input("Enter a decimal real number:\n"))

    if num == 0.0:
        sign = 0
        ieee_exponent = "00000000"
        ieee_significand = "00000000000000000000000"
    else:
        if num < 0:
            sign = 1
            num = abs(num)
        else:
            sign = 0
        
        int_part = int(num)
        frac_part = num - int_part
        
        # Normalize the number
        significand, exponent = normalize(int_part, frac_part)
        
        # Calculate biased exponent
        biased_exponent = exponent + 127
        ieee_exponent = format(biased_exponent, '08b')  # Convert to 8-bit binary

    print("The IEEE Single precision equivalent is:")  
    print(f"[{sign}][{ieee_exponent}][{ieee_significand}]")

if __name__ == '__main__':
    main()
