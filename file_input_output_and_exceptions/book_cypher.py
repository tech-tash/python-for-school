
def main():
    file = input("Enter the book filename:\n")
    
    try:
        f = open(file, "r")
        lines_f = f.readlines()
        f.close()
    
    except IOError:
        print("Sorry, file not found.")
        return    
    
    message = input("Enter the message:\n")
    msg = message.split()
    
    output = input("Enter the output filename:\n") 
    
        
    otp = open(output, "w")
    otp.write("BEGIN\n")
    print("BEGIN")
    
    for word in msg:
        clean_w = word.strip('?!.,;:)([]{}\'" \n').lower()
        found = False
        
        for line_num in range(len(lines_f)):
            in_line = lines_f[line_num].strip().split()
            
            for word_n in range(len(in_line)):
                book_word = in_line[word_n].strip('?!.,;:)([]{}\'" \n').lower()
                
                if clean_w == book_word:
                    answer = str(line_num+1) + "-" + str(word_n+1)
                    otp.write(answer + "\n")
                    print(answer)
                    found = True
                    break
                
            if found:
                break
            
        if not found:
            otp.write(clean_w + "\n")
            print(clean_w)
            
    otp.write("END\n")
    print("END")        
    otp.close()    
       
if __name__ == "__main__":
    main()