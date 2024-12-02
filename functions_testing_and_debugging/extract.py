
def location(block):
    # Your code here
    start = block.find("END") - 2
    end = block.find("S") + 1
    location = ""
    
    for letter in range(start, end, -1):
        location = location + block[letter]
        
    
    return location.title()    


def temperature(block):
    # Your code here
    length = 0
    
    for letter in block:
        if letter == "_":
            break
        else:
            length += 1
            
    end = length
    start = block.find("BEGIN") + len("BEGIN ")
    
    temperature = block[start:end]
    #print(temperature)
    temp = float(temperature)
    
    return temp
    
def x_coordinate(block):
    # Your code here
    start = block.find(":") + 1
    end = block.find(",")
    
    x_coordinate = block[start:end]
    return x_coordinate


def y_coordinate(block):
    # Your code here
    start = block.find(",") + 1
    
    end = block.find(" ", start)
    
    y_coordinate = block[start:end]
    return y_coordinate    


def pressure(block):
    # Your code here
    start = block.find("_") + 1
    end = block.find(":")
    
    pressure = block[start:end]
    
    
    return float(pressure)
            


def get_block(data):
    # Your code here
    start = data.find("BEGIN ")
        
    end = data.find("END") + len("END")
    
    raw_data = data[start : end]
    #print(raw_data)
    return raw_data
    

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
