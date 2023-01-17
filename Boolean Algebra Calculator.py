import csv
from datetime import datetime

class Algebra():
    def __init__(self):
        self.function=""
        self.newfunction=""
        self.implication_state=False
        self.clean=""
        self.variables={}
        today = str(datetime.now())
        today=today.replace(" ","_")
        today=today.replace(":","-")
        today=today[0:19]
        self.logname="Your_Path/Universal-boolean-algebra-table/logs/log_"+str(today)+".csv"
        
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

    def implication(self,function_imp):
        self.function_imp=function_imp
        find_ind=self.function_imp.find("->")
        a=eval(self.function_imp[0:find_ind-1])
        b=eval(self.function_imp[find_ind+3:])
        ges=0
        if a == 0:
            ges=1
        elif a ==1:
            if b==0:
                ges=0
            elif b==1:
                ges=1
        return ges

    def calculate(self,function):
        self.function=function
        self.variables={}
        self.function=self.function.replace("(", " ( ")
        self.function=self.function.replace(")", " ) ")
        self.function=self.function.replace("->", " -> ")
        self.function=self.function.replace("xor", " ^ ")
        self.clean=self.function.strip().split(" ",-1)
        for i in range(len(self.clean)):
            if "and" in self.clean:
                self.clean.remove("and") 
            if "or" in self.clean:
                self.clean.remove("or")
            if "not" in self.clean:
                self.clean.remove("not")
            if "(" in self.clean:
                self.clean.remove("(")
            if ")" in self.clean:
                self.clean.remove(")")
            if "xor" in self.clean:
                self.clean.remove("xor")
            if "^" in self.clean:
                self.clean.remove("^")
            if "->" in self.clean:
                self.clean.remove("->")
                self.implication_state=True
        for i in range(len(self.clean)):
            if len(self.clean[i])==0:
                self.clean[i]=self.clean[i].replace(self.clean[i], "placeholder")
        for i in range(len(self.clean)):
            if "placeholder" in self.clean:
                self.clean.remove("placeholder")
        for i in range(len(self.clean)):
            self.clean[i]=" "+self.clean[i]+" "
            self.variables[self.clean[i]]=0
        self.newfunction=" "+self.function+" " 
        for i in range(len(self.variables)):
            self.newfunction=self.newfunction.replace(str(list(self.variables.keys())[i])," int(list(self.variables.values())["+str(i)+"]) ")  
        
        with open(self.logname, 'a', newline='') as f:
            writer = csv.writer(f, delimiter=";")
            line=[]
            writer.writerow(line)
            for i in list(self.variables.keys()):
                line.append(i)
            line.append("Result")
            line.append("Function")
            writer.writerow(line)
        
        if "^" in self.function:  
            self.function=self.function.replace("^", "xor")
        print("Function: "+self.function)
        try:
            if self.implication_state==False:
                for i in range(len(Algebra.booleanlist(len(self.variables)))):
                    for j in range(len(self.variables)):
                        self.variables[[x for x in self.variables][j]]=int(Algebra.booleanlist(len(self.variables))[i][j])
                    result=int(eval(self.newfunction))
                    with open(self.logname, 'a', newline='') as f:
                        writer = csv.writer(f, delimiter=";")
                        line=[]
                        for i in range(len(self.variables.values())):
                            variable=list(self.variables.values())[i]
                            line.append(variable)
                        line.append(result)
                        line.append(self.function)
                        writer.writerow(line)
                    print(self.variables,"Result:",result)
            elif self.implication_state==True:
                for i in range(len(Algebra.booleanlist(len(self.variables)))):
                    for j in range(len(self.variables)):
                        self.variables[[x for x in self.variables][j]]=int(Algebra.booleanlist(len(self.variables))[i][j])
                    result=Algebra.implication(self,function_imp=self.newfunction)
                    with open(self.logname, 'a', newline='') as f:
                        writer = csv.writer(f, delimiter=";")
                        line=[]
                        for i in range(len(self.variables.values())):
                            variable=list(self.variables.values())[i]
                            line.append(variable)
                        line.append(result)
                        line.append(self.function)
                        writer.writerow(line)
                    print(self.variables,"Result:",result)
        except SyntaxError:
            print("Syntax Error (Wrong input) - Calculation aborted")
        
a=Algebra()       
while True:
    f=input("Enter the function: ")
    if f == "break":
        print("program ended")
        break
    a.calculate(f)