import random
dealer=random.randint(1,10)
carte=random.randint(1,10)
pesca=True

print("La tua carta è: ",carte)
print("Daler: ",dealer)

while True:
    
    try:
        if pesca == True:
            carta=input("Vuoi pescare una carta? (si/no): ").lower()
    
        
        if carta == "si":
            c=random.randint(1,10)
            carte+=c
            
            print("Mio Mazzo: ",carte)
            
            if carte>21:
                
                print("Hai perso!")
                break
            elif carte == 21:
                
                print("BlackJack!")
                break
        if carta == "no":
            pesca = False
            print("Hai passato. Il dealer sta giocando...")

            # Il dealer pesca finché ha meno di 17
            while dealer < 17:
                d = random.randint(1,10)
                dealer += d
                print("Dealer pesca: {}, mazzo dealer: {}".format(d, dealer))
                if dealer > 21:
                    print("Il banco ha sballato, Hai vinto!")
                    break

            # Se il while non ha fatto break per sballo, confrontiamo i punteggi
            else:
                if dealer == 21:
                    print("BlackJack per il dealer!")
                    break

                print("Il dealer ha : {}".format(dealer))
                if dealer > carte:
                    print("Ha vinto il banco!")
                    break
                elif dealer == carte:
                    print("Pareggio")
                    break
                else:
                    print("Hai vinto!")
                    break
                    
            
                
    except:
        print("ERRORE")