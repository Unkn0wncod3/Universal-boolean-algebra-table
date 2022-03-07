def binärliste(wert):
    liste=[]
    endzahl=2**wert
    zeichenanzahl=len(bin(endzahl-1))-2
    for i in range(endzahl):
        binärzahl=bin(i)        
        binärzahl_sauber=binärzahl[2:]
        fehlende_nullen=zeichenanzahl-len(binärzahl_sauber)
        binärzahl_sauber=fehlende_nullen*"0"+binärzahl_sauber
        liste.append(binärzahl_sauber)
    return liste

def create(funktion):
    variabeln={}
    funktion=funktion.replace("(", " ( ")
    funktion=funktion.replace(")", " ) ")
    clean=funktion.strip().split(" ",-1)
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
        variabeln[clean[i]]=0
    newfunktion=" "+funktion+" " 
    for i in range(len(variabeln)):
        newfunktion=newfunktion.replace(str(list(variabeln.keys())[i])," int(list(variabeln.values())["+str(i)+"]) ")  
    print("Funktion: "+funktion)
    print("Neue Funktion:"+newfunktion)
    try:
        for i in range(len(binärliste(len(variabeln)))):
            for j in range(len(variabeln)):
                variabeln[clean[j]]=int(binärliste(len(variabeln))[i][j])
            ergebnis=int(eval(newfunktion))
            print(variabeln,"Ergebnis:",ergebnis)
    except SyntaxError:
        print("Syntax Error (Falsche Eingabe) - Berechnung abgebrochen")

while True:
    f=input("Eingabe der Funktion: ")
    if f == "break":
        print("Programm beendet")
        break
    create(f)