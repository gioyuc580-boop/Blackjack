import random
dealer=random.randint(1,10)
carte=random.randint(1,10)
pesca=True

#Chiedo la quantità di fiches disponibili e la confronto con la scommessa
while True:
    try:
        f=int(input("Quante fiches hai a disposizione?  "))


        chips=int(input("Quanto scommetti?"))
        if chips>f:
            print("Errore, sfiori il budget!")
        else:
            break
    except ValueError:
        print("Errore inserisci un valore valido")
        continue
        
    
        


print("La tua carta è: ",carte)
print("Daler: ",dealer)

#chiedo se vuoi pescare
while True:
    
    try:
        if pesca == True:
           
            
            carta=input("Vuoi pescare una carta? (si/no): ").lower()
    
        
        if carta == "si":
            c=random.randint(1,10)
            carte+=c
            
            print("Mio Mazzo: ",carte)
            #se la carta è >21 e le fiches sono <=0 vai in banca rotta e hai 0 fiches totali
            if carte>21:
                fichesT=f-chips
                if fichesT<=0:
                    print("Bancarotta!")
                    fichesT=0
                    f=0
                    print("Fiches disponibili: {}".format(f+fichesT))   
                    break
                #altrimenti perdi e ti vengono sottratte le fiches
                else:
                    fichesT=f-chips
                    print("Hai perso!")
                    print("Fiches disponibili: {}".format(fichesT))  
                    break
                
            
             
                
            #se le carte sono uguali a 21 hai fatto blackjack!
            elif carte == 21:
                
                print("BlackJack!")
                fichesT=chips*2
                print("Fiches disponibili: {}".format(f+fichesT))
                break
        #Passa il turno al dealer
        if carta == "no":
            pesca = False
            print("Hai passato. Il dealer sta giocando...")

            # Il dealer pesca finché ha meno di 17
            while dealer < 17:
                d = random.randint(1,10)
                dealer += d
                print("Dealer pesca: {}, mazzo dealer: {}".format(d, dealer))
                #se ha + di 21 perde e tu vinci il doppio!
                if dealer > 21:
                    print("Il banco ha sballato, Hai vinto!")
                    fichesT=chips*2
                    print("Fiches disponibili: {}".format(f+fichesT))
                    break

            # Se il while non ha fatto break per sballo, confrontiamo i punteggi
            else:
                #se ha il dealer 21 ha fatto blackjack e tu perdi
                if dealer == 21:
                    print("BlackJack per il dealer!")
                    fichesT=f-chips
                    if fichesT<=0:
                        print("Bancarotta!")
                        fichesT=0
                        f=0
                        print("Fiches disponibili: {}".format(f+fichesT))   
                        break
                    else:
                        fichesT=f-chips
                        print("Fiches disponibili: {}".format(fichesT))
                        break
                
                
                print("Il dealer ha : {}".format(dealer))
                if dealer > carte:                      #Se il dealer ha un numero maggiore al tuo vince lui
                    print("Ha vinto il banco!")
                    fichesT=f-chips
                    if fichesT<=0:
                        print("Bancarotta!")
                        fichesT=0
                        f=0
                        print("Fiches disponibili: {}".format(f+fichesT))   
                        break
                    else:
                        fichesT=f-chips
                        print("Fiches disponibili: {}".format(fichesT))
                        break
                #se il numero è uguale è parità
                elif dealer == carte:
                    
                    print("Pareggio")
                    fichesT=chips
                    print("Fiches disponibili: {}".format(fichesT))
                    break
                #altrimenti hai vinto!
                else:
                    print("Hai vinto!")
                    fichesT=chips*2
                    print("Fiches disponibili: {}".format(f+fichesT))
                    break
                
            
                
    except:
        print("ERRORE")
