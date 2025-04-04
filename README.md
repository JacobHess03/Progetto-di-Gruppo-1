# 🎵 Sistema di Prenotazione Concerti in Python

Questo progetto è un semplice sistema di gestione per concerti, scritto in **Python**, che permette agli utenti di registrarsi, accedere e prenotare concerti. L’accesso alla creazione di nuovi concerti è protetto da una password segreta.

---

## 🔧 Funzionalità principali

- **Registrazione utenti** con nome e password
- **Login degli utenti**
- **Prenotazione concerti** (max 3 a testa)
- **Gestione delle sale** (max 10 posti per sala)
- **Creazione concerti** protetta da password
- **Visualizzazione dettagli utente**

---

## 🗂️ Struttura del programma

- Liste globali:
  - `utenti`: contiene i dati degli utenti
  - `id_utenti`: ID univoci per ogni utente
  - `concerti`: rappresenta i concerti creati
  - `sala`: contiene gli ID degli utenti prenotati in una sala
  - `id_concerti`: ID univoci per ogni concerto

- Funzioni principali:
  - `crea_utente()`: registra un nuovo utente
  - `login()`: login tramite nome e password
  - `prenota_concerto()`: permette la prenotazione da parte di un utente loggato
  - `crea_concerto()`: consente la creazione di un nuovo concerto (protetta da password)
  - `controllo()`: verifica della password segreta per creare concerti

---

## 🔐 Limiti e regole

- Ogni utente può prenotare **al massimo 3 concerti**
- Ogni sala può contenere **massimo 10 utenti**
- La creazione di un nuovo concerto richiede la **password "GHIBLI"**

---



