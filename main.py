import requests
import json
import sqlite3

def aggiorna_campionati():
    # 1. Configurazione
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c" 
    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        # Connessione al database locale di SQLite del repository
        conn = sqlite3.connect('database.db') # O il nome del tuo file db se diverso
        cursor = conn.cursor()
        
        # Crea la tabella se non esiste
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leagues (
                league_id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                type TEXT
            )
        ''')

        print("Richiesta dati all'API...")
        resp = requests.get(url, headers=headers)
        
        if resp.status_code != 200:
            print(f"Errore API: Stato {resp.status_code}")
            return

        data = resp.json()
        
        if not data or "response" not in data:
            print("Errore: Risposta API vuota o non valida.")
            return

        count = 0
        for item in data["response"]:
            c_name = str(item["country"]["name"])
            
            if c_name in target_countries:
                for season in item["seasons"]:
                    if season["current"]:
                        l_id = int(item["league"]["id"])
                        l_name = str(item["league"]["name"])
                        l_type = str(item["league"]["type"])

                        # Qui la query è sicura usando i parametri standard (?) di Python
                        query = "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)"
                        cursor.execute(query, (l_id, l_name, c_name, l_type))
                        
                        count += 1

        conn.commit()
        conn.close()
        print(f"Lopislab Online! Salvati {count} campionati nel database.")

    except Exception as e:
        print(f"Errore tecnico durante l'esecuzione: {str(e)}")

if __name__ == "__main__":
    aggiorna_campionati()
