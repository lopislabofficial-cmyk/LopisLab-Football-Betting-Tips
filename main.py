import requests
import json
import sqlite3
from datetime import datetime

def aggiorna_lopislab():
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c" 
    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]
    oggi = datetime.now().strftime('%Y-%m-%d')

    try:
        # Connessione al database di Cloudflare (tramite l'ambiente locale del repository)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        print(f"Esecuzione aggiornamento per la data: {oggi}")

        # 1. SCARICA E SALVA I CAMPIONATI
        url_leagues = "https://v3.football.api-sports.io/leagues"
        headers = {"x-apisports-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}
        
        resp_l = requests.get(url_leagues, headers=headers)
        if resp_l.status_code == 200:
            data_l = resp_l.json()
            for item in data_l.get("response", []):
                c_name = str(item["country"]["name"])
                if c_name in target_countries:
                    for season in item["seasons"]:
                        if season["current"]:
                            l_id = int(item["league"]["id"])
                            l_name = str(item["league"]["name"])
                            l_type = str(item["league"]["type"])
                            
                            cursor.execute(
                                "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)",
                                (l_id, l_name, c_name, l_type)
                            )

        # 2. SCARICA E SALVA LE PARTITE DI OGGI
        url_fixtures = f"https://v3.football.api-sports.io/fixtures?date={oggi}"
        resp_f = requests.get(url_fixtures, headers=headers)
        
        match_count = 0
        if resp_f.status_code == 200:
            data_f = resp_f.json()
            for item in data_f.get("response", []):
                c_name = str(item["league"]["country"])
                
                # Prendiamo solo i match delle nazioni che ti interessano
                if c_name in target_countries:
                    f_id = str(item["fixture"]["id"])
                    m_date = str(item["fixture"]["date"]).split('T')[0]
                    m_time = str(item["fixture"]["date"]).split('T')[1][:5]
                    l_name = str(item["league"]["name"])
                    h_team = str(item["teams"]["home"]["name"])
                    a_team = str(item["teams"]["away"]["name"])
                    
                    h_score = item["goals"]["home"]
                    a_score = item["goals"]["away"]
                    status = str(item["fixture"]["status"]["short"])
                    
                    # Generiamo un pronostico automatico basato sulle quote o di default (es: 1X)
                    prediction = "1X" 
                    
                    # Inseriamo i dati nella tabella matches che hai creato su Cloudflare
                    cursor.execute("""
                        INSERT OR REPLACE INTO matches 
                        (id, match_date, match_time, league_name, home_team, away_team, home_score, away_score, prediction, status, home_odds, draw_odds, away_odds) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (f_id, m_date, m_time, l_name, h_team, a_team, h_score, a_score, prediction, status, 2.0, 3.2, 3.0))
                    
                    match_count += 1

        conn.commit()
        conn.close()
        print(f"Configurazione completata! Salvate {match_count} partite nella tabella matches.")

    except Exception as e:
        print(f"Errore tecnico: {str(e)}")

if __name__ == "__main__":
    aggiorna_lopislab()
