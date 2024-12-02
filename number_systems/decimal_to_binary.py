import number_utils

def integer_digits_to_binary(decimal_number):
    binary_digits = []
    
    while not number_utils.is_zero(decimal_number):
        decimal_number, remainder = number_utils.divide_by_two(decimal_number)
        binary_digits.insert(0, remainder)
        
    if len(binary_digits) == 0:
        binary_digits = [0]
        
    return binary_digits

def fraction_digits_to_binary(decimal_digits, max_length = 10):
    binary_digits = []
    for i in range(max_length):
        decimal_digits, carry = number_utils.multiply_by_two(decimal_digits)
        binary_digits.append(carry)
        
        if number_utils.is_zero(decimal_digits):
            break
        
    return binary_digits    
    
def main():
    decimal_number = input("Enter a decimal real number:\n")
    
    if decimal_number[0] == "-":
        sign = "-"
        decimal_number = decimal_number[1:]
    
    else:
        sign = ""
        
    
    if "." in decimal_number:
        int_part, frac_part = decimal_number.split(".")
    
    else:
        int_part = decimal_number
        frac_part = "0"
        
    
    int_digits = []
    for char in int_part:
        int_digits.append(int(char))
        
        
    binary_int_digits = integer_digits_to_binary(int_digits)
    
        
    frac_digits = []
    for char in frac_part:
        frac_digits.append(int(char))
        
    binary_frac_digits = fraction_digits_to_binary(frac_digits)
    
    
    int_binary_str = ""
    for bit in binary_int_digits:
        int_binary_str += str(bit)
        
    frac_binary_str = ""
    for bit in binary_frac_digits:
        frac_binary_str += str(bit)
        
    if len(frac_binary_str) > 0 and int(frac_binary_str) != 0:
        binary_number = sign + int_binary_str + "." + frac_binary_str
        
    else:
        binary_number = sign + int_binary_str
        
    
    print("The binary equivalent is:")
    print(binary_number)
    
    
if __name__ == "__main__":
    main()
