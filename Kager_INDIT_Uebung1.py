#include <stdio.h>

def add(a,b):
    print("ADD-Funktion mit Werten",a,"und",b,"angestoßen")
    return a+b
def dif (a,b):
    print("DIF-Funktion mit Werten",a,"und",b,"angestoßen")
    return a-b
def mul(a,b):
    print("MUL-Funktion mit Werten",a,"und",b,"angestoßen")
    return a*b
def div (a,b):
    print("DIV-Funktion mit Werten",a,"und",b,"angestoßen")
    return a/b


def AlleWerte(a):
    i=1
    while i < a+1:
        print (i)
        i= i+1
        
    
fa = float(input("Eingabe Zahl 1: "))
fb = float(input("Eingabe Zahl 2: "))

print("Welche Funktion soll ausgeführt werden? (Klartext)")

Case= input("Addieren, Subtrahieren, Multiplizieren, Dividieren")

if Case == "Addieren":
    fc = add(fa,fb)
    print(fc)
elif Case == "Subtrahieren":
    fc = dif(fa,fb)
    print(fc)
elif Case == "Multiplizieren":
    fc = mul(fa,fb)
    print(fc)
elif Case == "Dividieren":
    fc = div(fa,fb)
    print(fc)
else:
    print("Falsche Eingabe")

iAllOut = int(input("Sollen alle Zahlen aufsteigend ausgegeben werden? (1/0)"))

if iAllOut == 1:
    AlleWerte(fc)
else:
    print("Ok")


