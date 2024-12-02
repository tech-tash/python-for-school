
import math

def vector_sum(A, B):
    A = str(A)
    B = str(B)
    
    len_A = len(A)
    list_A = []
    
    
    for num in range(len_A):
        if A[num] == "-":
            num2 = int(A[num] + A[num+1])
            list_A.append(num2)
        elif A[num].isdigit() and A[num-1] != "-":
            num2 = int(A[num])
            list_A.append(num2)
    
    len_B = len(B)
    list_B = []
    
    for num in range(len_B):
        if B[num] == "-":
            num2 = int(B[num] + B[num+1])
            list_B.append(num2)
        elif B[num].isdigit() and B[num-1] != "-":
            num2 = int(B[num])
            list_B.append(num2)    
    
    
    sum_x = list_A[0] + list_B[0]
    sum_y = list_A[1] + list_B[1]
    sum_z = list_A[2] + list_B[2]
    
    sum = [sum_x, sum_y, sum_z]
    
    return sum

def vector_product(A, B):
    A = str(A)
    B = str(B)
    
    len_A = len(A)
    list_A = []
    
    
    for num in range(len_A):
        if A[num] == "-":
            num2 = int(A[num] + A[num+1])
            list_A.append(num2)
        elif A[num].isdigit() and A[num-1] != "-":
            num2 = int(A[num])
            list_A.append(num2)
    
    len_B = len(B)
    list_B = []
    
    for num in range(len_B):
        if B[num] == "-":
            num2 = int(B[num] + B[num+1])
            list_B.append(num2)
        elif B[num].isdigit() and B[num-1] != "-":
            num2 = int(B[num])
            list_B.append(num2)      
    
    vector_x = list_A[0] * list_B[0]
    vector_y = list_A[1] * list_B[1]
    vector_z = list_A[2] * list_B[2]
    
    vector = vector_x + vector_y + vector_z 
    
    return vector

def vector_norm(A):
    A = str(A)
    
    len_A = len(A)
    list_A = []
    
    for num in range(len_A):
        if A[num] == "-":
            num2 = int(A[num] + A[num+1])
            list_A.append(num2)
        elif A[num].isdigit() and A[num-1] != "-":
            num2 = int(A[num])
            list_A.append(num2)    
    
    norm_x = list_A[0] ** 2
    norm_y = list_A[1] ** 2
    norm_z = list_A[2] ** 2
    
    norm = math.sqrt(norm_x + norm_y + norm_z)    
    
    return norm