import random

i=0
ar=[]

iAnzahl=int(input("Wie viele Lottozahlen wollen Sie generieren?"))
      
while i < iAnzahl:
    ia=round(random.random()*44+1)
    x=0
    leng = len(ar)
    if len(ar)==0:
        ar= ar + [ia]
    else:
        while x <= len(ar)-1:
            if ar[x] == ia:
                ia=0
            x +=1  
        if ia != 0:
            ar = ar + [ia]
              
    i +=1
print(ar)

