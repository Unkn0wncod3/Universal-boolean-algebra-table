def booleanlist(value):
    list=[]
    endnumber=2**value
    character_count=len(bin(endnumber-1))-2
    for i in range(endnumber):
        binary_number=bin(i)        
        binary_number_clean=binary_number[2:]
        missing_zeros=character_count-len(binary_number_clean)
        binary_number_clean=missing_zeros*"0"+binary_number_clean
        list.append(binary_number_clean)
    return list

def create(function):
    variables={}
    function=function.replace("(", " ( ")
    function=function.replace(")", " ) ")
    clean=function.strip().split(" ",-1)
    for i in range(len(clean)):
        if "and" in clean:
            clean.remove("and") 
        if "or" in clean:
            clean.remove("or")
        if "not" in clean:
            clean.remove("not")
        if "(" in clean:
            clean.remove("(")
        if ")" in clean:
            clean.remove(")")
    for i in range(len(clean)):
        if len(clean[i])==0:
            clean[i]=clean[i].replace(clean[i], "placeholder")
    for i in range(len(clean)):
        if "placeholder" in clean:
            clean.remove("placeholder")
    for i in range(len(clean)):
        clean[i]=" "+clean[i]+" "
        variables[clean[i]]=0
    newfunction=" "+function+" " 
    for i in range(len(variables)):
        newfunction=newfunction.replace(str(list(variables.keys())[i])," int(list(variables.values())["+str(i)+"]) ")  
    print("Function: "+function)
    print("New function:"+newfunction)
    try:
        for i in range(len(booleanlist(len(variables)))):
            for j in range(len(variables)):
                variables[[x for x in variables][j]]=int(booleanlist(len(variables))[i][j])
            result=int(eval(newfunction))
            print(variables,"Result:",result)
    except SyntaxError:
        print("Syntax Error (Wrong input) - Calculation aborted")

while True:
    f=input("Enter the function: ")
    if f == "break":
        print("program ended")
        break
    create(f)