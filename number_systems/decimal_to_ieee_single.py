from decimal_to_binary import fraction_digits_to_binary, integer_digits_to_binary
from number_utils import divide_by_two, multiply_by_two

def normalise(integer_part, fraction_part):
    if integer_part == "0":
        
        index1 = fraction_part.find("1")
        
            
        if index1 == -1:
            normalised_binary = "0"
            exponent = 0
            
        else:
            exponent = -(index1 + 1)
            normalised_binary = fraction_part[index1 + 1:]
            
    else:
        exponent = len(integer_part) - 1
        normalised_binary = integer_part[1:] + fraction_part
        
    return normalised_binary, exponent    


def main():
    num = float(input("Enter a decimal real number:\n"))
    
    
    if round(num,40) == 0.0 and str(num).startswith("-"):
        sign = 1
        ieee_exponent = "00000000"
        ieee_significand = "00000000000000000000000"
        print("The IEEE Single precision equivalent is:")  
        print("[{}][{}][{}]".format(sign, ieee_exponent, ieee_significand))
        return
        
    elif num == 0.0:
        sign = 0
        ieee_exponent = "00000000"
        ieee_significand = "00000000000000000000000"
        print("The IEEE Single precision equivalent is:")  
        print("[{}][{}][{}]".format(sign, ieee_exponent, ieee_significand)) 
        return
    
    else:    
        if num < 0:     #negative
            sign = 1
            num = abs(num)
            
        else:
            sign = 0
            
        #split into interger and fraction parts    
        int_part = int(num)
        frac_part = num - int_part
        
        #convert interger part to binary
        if int_part == 0:
            int_binary = "0"
                
        else:
            int_binary = ""
            while int_part > 0:
                remainder = int_part % 2
                int_binary = str(remainder) + int_binary
                int_part //= 2
        
        #conver fractional part to binary
        
        frac_binary = ""
        temp = frac_part
        count = 0
        
        while temp > 0 and count < 32:
            temp *= 2
            bit = int(temp)
            frac_binary += str(bit)
            temp -= bit
            count += 1
            
        #normalise
        normalised_binary, exponent = normalise(int_binary, frac_binary)
                
        ieee_exponent = exponent + 127
        ieee_binary = ""
        expo_temp = ieee_exponent
        
        #exponent to binary
        while expo_temp > 0:
            remainder = expo_temp % 2
            ieee_binary = str(remainder) + ieee_binary
            expo_temp //= 2
            
        while len(ieee_binary) < 8:
            ieee_binary = "0" + ieee_binary
            
        ieee_significand = ""
        significand_bits = 23
        bit_count = 0
        
        for bit in normalised_binary:
            ieee_significand += bit
            bit_count += 1
            if bit_count == significand_bits:
                break
            
        while len(ieee_significand) < significand_bits:
            ieee_significand += "0"
            
        print("The IEEE Single precision equivalent is:")  
        print("[{}][{}][{}]".format(sign, ieee_binary, ieee_significand))
    
    
if __name__ == '__main__':
    main()