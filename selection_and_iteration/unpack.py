# Program that accepts as input a line of words containing no spaces and where each word is preceded by its length.
# Name: Natasha Mazibuko
# Date: 07 May 2024

#fix it. and if sentence[i]and sentence[i+1] is digit

def main():
    sentence = input("Enter the coded sentence:\n")
    length = len(sentence)
    
    if sentence and sentence[0].isdigit():      #check if the first character is a digit or not
        for i in range(1,length):          #if yes, exclude it
            if not sentence[i].isdigit():
                print(sentence[i], end = "")        
            
            elif sentence[i].isdigit():
                print()        
        
        
    else:
        for i in range(length):        
        
            if not sentence[i].isdigit():
                print(sentence[i], end = "")        
        
            elif sentence[i].isdigit():
                print()
            
           
main()            