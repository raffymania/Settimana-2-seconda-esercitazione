"""Esercizio 2: Una persona brilla è all'interno di una griglia di strade (al centro di un incrocio),
e in modo del tutto casuale prende una delle 4 direzioni (nord è +, sud è -, est è +, ovest è -)
e si muoverà di un numero casuale di passi (da 1 a 10) che lo porterà al centro di un nuovo incrocio.
Rappresenta la posizione della persona con la coppia di interi (x, y).
Immagina che la persona sia all'interno di un piano cartesiano (x asse delle ordinate, y asse delle ascisse),
implementa il cammino della persona brilla per 100 intersezioni a partire dalla posizione (0, 0),
visualizza la posizione finale. Esempio, alla prima iterazione se la persona si sposta verso sud di
7 passi la sua nuova posizione sarà (0, -7), se alla successiva si muove verso nord i 3 passi la sua nuova posizione sarà (0, -4)
 """

#importo pacchetto random
import random
i=0
while (i<100):
    #creo valore x random tra -10 e 10
    x = random.randint(-10, 10)
    #creo valore y random tra -10 e 10
    y = random.randint(-10, 10)
    #stampo per ogni ciclo la posizione che ho creato random
    print("(",x,",",y,")")
    i+=1
