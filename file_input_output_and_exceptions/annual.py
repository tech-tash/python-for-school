
    
def main():
    while True:
        print("1. Enter rainfall.\n2. Read rainfall.\n3. Quit.")
        
        try:
            option = input("Select an option:\n")
            opt = int(option)
            
            while opt not in [1,2,3]:
                print("Sorry, that's not a valid value.")
                option = input("Select an option:\n")        
           
        except ValueError:
            while option not in ["1","2","3"]:
                print("Sorry, that's not a valid value.")
                option = input("Select an option:\n")
            
            opt = int(option)
        
        if opt == 3:
            print("Okay, bye.")
            break            
         
        city = input("Enter the city name:\n")
            
        while city.isdigit():
            print("Sorry, that's not a valid value.")
            city = input("Enter the city name:\n").strip('?!.,;:)([]{}\'" \n')
            
        year = input("Enter the year:\n")
            
        while not year.isdigit() or len(year) != 4:
            print("Sorry, that's not a valid value.")
            year = input("Enter the year:\n")
            
        if opt == 1: 
            city = city.replace(" ","").lower()
            file = city + "_" + year + ".dat"
            
            f = open(file, "w")
            
            for temp in range(1, 13):
                value = input("Enter a value for month number {}:\n".format(temp))
                
                while value.isalpha():
                    print("Sorry, that's not a valid value.")
                    value = input("Enter a value for month number {}:\n".format(temp))
                    
                while "," in value:
                    print("Sorry, that's not a valid value.")
                    value = input("Enter a value for month number {}:\n".format(temp))                    
            
                f.write(value + "\n")
                
            print("Wrote '{}'.".format(file))
            f.close()
            
        elif opt == 2:
            city = city.replace(" ","").lower()
            file = city + "_" + year + ".dat"
            print("Reading '{}'...".format(file))
            
            try:
                f = open(file, "r")
            
            except IOError:
                print("Sorry, file not found.")
                continue
            
            invalid = 0
            valid = 0
            sum_valid = 0
            average = 0
            temp = 0
            
            for line in f:
                
                line = line.strip()                 
                
                try:
                    num = float(line)
                    valid += 1
                    sum_valid += num                    
                    
                except ValueError:
                    invalid += 1
                    print("Data for month {} is invalid: '{}'. ".format(temp, line.strip()))
                    
                temp += 1
            
            print("Invalid values: {}.".format(invalid))
            print("Valid values: {}.".format(valid))
            
            if valid > 0: 
                average = sum_valid / valid
                print("Average of valid values: {:.2f}.".format(average))
            
            f.close()
                
if __name__ == "__main__":
    main()