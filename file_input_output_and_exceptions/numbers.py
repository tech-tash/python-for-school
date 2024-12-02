

num_list = []

while True:  
    filename = input('Enter a filename: ')
    
    try:
        file = open(filename, 'r')
        break   #exit the loop if the file has been opened
    except IOError:
        print("Sorry, file not found.")    

line = file.readline()
count = 0    #changed!

while len(line) > 0:          #assuming that the values read from the file are correct
    num = int(line)
    num_list.append(num)
    line = file.readline()
    count += 1    
        
file.close()

print('Read {} value'.format(count), end='')
if count is not 1:
    print('s.')
else:
    print('.')

while True:
    index = input("Enter an index (or '[q]uit' to exit): ")
    if index.lower() == 'q':
        break
    
    try:
        index = int(index)
        if 0 <= index < len(num_list):
            print('Num at position', index, 'is', num_list[index])
        else:
            print("Sorry, that's not a valid value.")
          
    except ValueError:
        print("Sorry, that's not a valid value.")