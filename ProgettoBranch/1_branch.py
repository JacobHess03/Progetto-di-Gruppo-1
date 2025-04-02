
nome = input("Inserisci il tuo nome: ")
password = input("Inserisci la tua password: ")

#1 metodo per creare un utente
def crea_utente(utenti, nome, password):
    if nome in utenti:
        print("Utente già esistente")
        return False
    else:
        print("Utente creato con successo")
        #aggiungo l'utente alla lista utenti
        utenti.append(nome)
        utenti.append(password)
        return True


#2 metodo per prenpotare un concerto
def prenota_concerto(accounts, concerti, sala, utenti, nome):
    if sala in concerti:
        print("Concerto già prenotato")
        return False
    else:
        print("Concerto prenotato con successo")
        for i in range(len(accounts)):
            for j in range(len(utenti)):
                if nome == utenti[j]:
                    print("Utente già esistente")
                    sala.append(accounts[utenti[j]])
                    return False
        #aggiungo il concerto alla lista concerti
        concerti.append(sala.append(accounts).append(utenti).append(nome, password))
        return True
    
    
    # for per prenotare massimo 3 concerti
for i in range(3):
    sala = input("Inserisci il nome del concerto: ")
   # prenota_concerto(concerti_1, sala_1)


#3 metodo per creare un concerto
def crea_concerto(concerti, sala):
    if sala in concerti:
        print("Concerto già esistente")
        return False
    else:
        print("Concerto creato con successo")
        #aggiungo il concerto alla lista concerti
        concerti.append(sala)
        return True
    

utenti_1 = []
sala_1 = [] 
concerti_1 = [sala_1]
accounts_1 = [utenti_1]

