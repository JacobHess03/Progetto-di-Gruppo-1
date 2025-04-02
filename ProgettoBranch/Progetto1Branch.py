concerti=[]
sala=[]
utenti=[]
accounts=[]

def login(nome,password,account,persona):
    
    i=0
    j=0
    
    while(i<(len(account)) ):
        while(j<len(persona)):
            
            if(nome==persona[j]):
                print("ciao,benvenuto")
            
            else:
                print("mi dispaice nome non disponibile")
            
        

def controllo(parola):
    
    controller=True
    while(controller):
        if(parola=="GHIBLI"):
            controller=False
            
            
            

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
                     concerti.append([sala])
                     return False
         #aggiungo il concerto alla lista concerti
    
        
    return True
     
     
     # for per prenotare massimo 3 concerti

 
 
 #3 metodo per creare un concerto
def crea_concerto(concerti, sala):
    password=input("inserisci password segreta")
    controllo(password)
    
    
    
    if sala in concerti:
            print("Concerto già esistente")
            return False
    else:
            print("Concerto creato con successo")
            #aggiungo il concerto alla lista concerti
            concerti.append(sala)
            return True
        
 
 
 
 
 #programma vero
scelta=int(input("Ciao, inserisci la scelta\n1.REGISTRATI\n2Login,Prenotazione\n3 Crea Concerto"))   

match scelta:
    
    case 1:
        
       nome=input("inserire nome")
       password=input("inserire password")
       crea_utente(utenti, nome, password)
       
    case 2:
        
        login(nome,password,accounts,utenti)
        i=0
        
        for i in range(2):
            
              prenota_concerto(accounts, concerti, sala, utenti, nome)
       
            
      
            
    
    case 3:
        
        crea_concerto(concerti, sala)
    
    case _:
        print("Uscita dal sistema")
        
        
       
    
        
    
    