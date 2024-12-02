import vectormaths

def main():
    vector_A = input("Enter vector A:\n")
    vector_B = input("Enter vector B:\n")
    
    calc = input("Select a calculation to perform. Enter '+', '.' or '|':\n")
    
    if calc == "+":
        addition = vectormaths.vector_sum(vector_A, vector_B)
        print("A+B = [{}, {}, {}]".format(addition[0], addition[1], addition[2]))
        
    elif calc == ".":
        multiplication = vectormaths.vector_product(vector_A, vector_B)
        print("A.B =", multiplication)
        
    elif calc == "|":
        magnitude_A = vectormaths.vector_norm(vector_A)
        magnitude_B = vectormaths.vector_norm(vector_B)
        
        print("|A| = {:.2f}".format(magnitude_A))
        print("|B| = {:.2f}".format(magnitude_B))
        
    else:
        print("Selection not recognised.")


if __name__=='__main__': 
    main()     