# Liste globali per tracciare utenti, concerti e ID
concerti = []
sala = []
utenti = []  # Lista di dizionari per rappresentare gli utenti
accounts = []
id_utenti = []  # Lista per tracciare gli ID degli utenti
id_concerti = []  # Lista per tracciare gli ID dei concerti


# Funzione per il login
def login(nome, password, account, utenti):
    for utente in utenti:
        if utente["nome"] == nome and utente["password"] == password:
            print("Ciao, benvenuto!")
            return True
    print("Mi dispiace, nome o password non disponibili.")
    return False


# Funzione di controllo per la password segreta
def controllo(parola):
    controller = True
    while controller:
        if parola == "GHIBLI":
            controller = False
        else:
            parola = input("Password errata. Riprova: ")


# Metodo per creare un utente
def crea_utente(utenti, id_utenti, nome, password):
    # Controllo se l'utente esiste già
    for utente in utenti:
        if utente["nome"] == nome:
            print("Utente già esistente")
            return False

    # Creazione del nuovo utente
    id_utente = len(id_utenti) + 1
    nuovo_utente = {"id": id_utente, "nome": nome, "password": password}
    utenti.append(nuovo_utente)
    id_utenti.append(id_utente)

    print("Utente creato con successo")
    print(f"ID utente assegnato: {id_utente}")
    return True


# Metodo per prenotare un concerto
def prenota_concerto(accounts, concerti, sala, utenti, id_utenti, nome):
    if sala in concerti:
        print("Concerto già prenotato")
        return False

    # Controllo se l'utente esiste
    for utente in utenti:
        if utente["nome"] == nome:
            print("Concerto prenotato con successo")
            sala.append(utente["id"])
            concerti.append(sala.copy())
            id_concerto = len(id_concerti) + 1
            id_concerti.append(id_concerto)
            print(f"ID concerto assegnato: {id_concerto}")
            return True

    print("Utente non trovato")
    return False


# Metodo per creare un concerto
def crea_concerto(concerti, sala, id_concerti):
    password = input("Inserisci password segreta: ")
    controllo(password)

    if sala in concerti:
        print("Concerto già esistente")
        return False
    else:
        print("Concerto creato con successo")
        # Aggiungo il concerto alla lista concerti
        concerti.append(sala)
        # Genero un ID univoco per il concerto
        id_concerto = len(id_concerti) + 1
        id_concerti.append(id_concerto)
        print(f"ID concerto assegnato: {id_concerto}")
        return True


# Programma principale
scelta = int(input("Ciao, inserisci la scelta\n1. Registrati\n2. Login, Prenotazione\n3. Crea Concerto\n"))

match scelta:
    case 1:
        nome = input("Inserire nome: ")
        password = input("Inserire password: ")
        if crea_utente(utenti, id_utenti, nome, password):
            print("Lista utenti aggiornata:")
            print(utenti)  # Stampa di verifica per controllare gli utenti registrati

    case 2:
        nome = input("Inserire nome: ")
        password = input("Inserire password: ")
        if login(nome, password, accounts, utenti):
            while True:
                risposta = input("Vuoi prenotare un concerto? (sì/no): ").lower()
                if risposta == "sì":
                    prenota_concerto(accounts, concerti, sala, utenti, id_utenti, nome)
                elif risposta == "no":
                    break
                else:
                    print("Risposta non valida. Inserisci 'sì' o 'no'.")

    case 3:
        crea_concerto(concerti, sala, id_concerti)

  