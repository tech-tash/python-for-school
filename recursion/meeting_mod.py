# Program calculating the number of handshakes an attendee would have to shake with people
# Name: Natasha Mazibuko
# Date: 31 August 2024

def handshakes(n):
    if n <= 1:
        return 0
    
    else:
        return handshakes(n-1) + n-1
    