import os
import time
clear=lambda: os.system('cls')

def MapaPlanszy(plansza):
    print("\n",end='')
    for i in range(9):
        if i==0 or i==3 or i==6:
            print("    ",end='')
        if plansza[i]==5:
            print("   ",end='')
        elif plansza[i]==0:
            print(" O ",end='')
        elif plansza[i]==1:
            print(" X ",end='')
        if i==0 or i==1 or i==3 or i==4 or i==6 or i==7:
            print("|",end='')
        if i==2 or i==5:
            print("\n    -----------\n",end='')
        if i==8:
            print("\n",end='')

def RuchGracza(plansza,kogo_kolej):
    numer_pola=9
    while(numer_pola>8):
        clear()
        print("    Podaj numer pola jakie chcesz zagrac\n")
        MapaPlanszy(plansza)
        numer_pola=int(input())
        numer_pola-=1
        if numer_pola > 8:
            print("    Nieprawidlowy numer pola!")
            time.sleep(2)
            numer_pola=9
        elif plansza[numer_pola]!=5:
            print("    To pole jest juz zajete!")
            time.sleep(2)
            numer_pola=9
    if kogo_kolej==1:
        plansza[numer_pola]=1
    elif kogo_kolej==0:
        plansza[numer_pola]=0
    MapaPlanszy(plansza)

def SprawdzZwyciezce(plansza):
    remis=0
    for i in range(7):
        if (plansza[i]!=5 and plansza[i+1]!=5) and plansza[i+2]!=5:
            remis+=1
        if (i==0 or i==6) and (plansza[i]==plansza[i+1] and plansza[i] == plansza[i+2]):
            if plansza[i]==0:
                return 10
            elif plansza[i]==1:
                return -10
            else:
                continue
        elif (i== 0 or i==2) and (plansza[i] == plansza[i+3] and plansza[i] == plansza[i+6]):
            if plansza[i]==0:
                return 10
            elif plansza[i]==1:
                return -10
            else:
                continue
        elif i!=4 and (plansza[i] == plansza[4]) and (plansza[i]==plansza[8-i]):
            if plansza[i]==0:
                return 10
            elif plansza[i]==1:
                return -10
            else:
                continue
        elif remis==7: 
            return 0
    return -100

plansza = [5 for x in range(9)]
kogo_kolej=0
while (True):
    x = SprawdzZwyciezce(plansza)
    if x==0:
        print("      Remis")
        time.sleep(2)
        break
    elif x==10:
        print("      Wygrywa kolko (Gracz 1)!")
        time.sleep(2)
        break
    elif x==-10:
        print("      Wygrywa krzyzyk (Gracz 2)!")
        time.sleep(2)
        break
    RuchGracza(plansza,kogo_kolej)
    kogo_kolej= not kogo_kolej