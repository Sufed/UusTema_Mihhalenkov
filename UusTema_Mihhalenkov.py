from OmaMoodul import *
laused=[]

while True:
    print("")
    v=int(input("1-Loeme failist\n2-Salvestame failisse\n3-Tekstist kõne\n"))
    if v==1:
        laused=Loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt",laused)
