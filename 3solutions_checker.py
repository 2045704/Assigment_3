with open(r'C:\Users\newma\OneDrive\Desktop\PCS_II\Assignment3\3my_output.txt','r') as file:

    A = file.readlines()

with open(r'C:\Users\newma\OneDrive\Desktop\PCS_II\Assignment3\3sample_output.txt','r') as file:

    B = file.readlines()

def output_checker(A,B):

    if A==B:
        print("YAY")
    else:
        print("nope,try again you can do it!!!!")
        
output_checker(A,B)
    
def find_errors(A, B):
    errors = []

    for el in A:
        if el not in B:
            errors.append(el)

    for el in B:
        if el not in A:
            errors.append(el)
    
    if errors == []:
        print("No errors :-) !!")
    else:
        for error in errors:
            #print(" ")
            print(error)
    

find_errors(A,B)

with open("Assignment_list.txt","r") as file:
    counter = 0
    lines = file.readlines()
    for line in lines:
        if "(DONE)" not in line:
            counter += 1
    if counter == 1:
        print("ONLY ONE LEFT!!!")
    elif counter == 0:
        print("ALL DONE, YOU ROCKSTAR")
        
    else:
        print(f"you have {counter} exercises left")