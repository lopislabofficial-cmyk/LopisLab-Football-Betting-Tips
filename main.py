import requests
import os

# API Setup
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def get_data(endpoint):
    url = f"https://api.football-data.org/v4/competitions/SA/{endpoint}"
    return requests.get(url, headers=headers).json()

def main():
    try:
        # 1. Recuperiamo sia le partite che la classifica
        matches_data = get_data("matches?status=SCHEDULED")
        standings_data = get_data("standings")
        
        # Creiamo un "dizionario" della classifica per accesso rapido
        standings = {}
        for table in standings_data.get('standings', [{}])[0].get('table', []):
            standings[table['team']['name']] = {
                'position': table['position'],
                'points': table['points'],
                'goalDiff': table['goalDifference']
            }

        matches = matches_data.get('matches', [])[:10]

        # 2. Inizio HTML (Manteniamo il tuo bellissimo design)
        html = """
        <html><head><title>LopisLab AI Insights</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f4f7f6; padding: 40px; color: #333; }
            .container { max-width: 900px; margin: 0 auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }
            h1 { color: #1a2a6c; border-bottom: 3px solid #1a2a6c; display: inline-block; margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th { background: #1a2a6c; color: white; padding: 15px; text-align: left; font-size: 13px; }
            td { padding: 15px; border-bottom: 1px solid #eee; font-size: 14px; }
            .badge { padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 12px; }
            .high { background: #d4edda; color: #155724; }
            .med { background: #fff3cd; color: #856404; }
        </style></head><body>
        <div class="container">
            <h1>LopisLab AI Prediction Engine</h1>
            <p>Data-driven insights for upcoming Serie A matches.</p>
            <table>
                <tr><th>Date</th><th>Match</th><th>AI Prediction</th><th>Confidence</th></tr>
        """

        for m in matches:
            home = m['homeTeam']['name']
            away = m['awayTeam']['name']
            date = m['utcDate'][:10]
            
            # Recuperiamo i dati delle due squadre dalla classifica
            h_stats = standings.get(home, {'points': 0, 'goalDiff': 0})
            a_stats = standings.get(away, {'points': 0, 'goalDiff': 0})

            # LOGICA DI PRONOSTICO (VERSIONE 1.0)
            # Calcoliamo il gap di potenza basato su punti e differenza reti
            power_gap = (h_stats['points'] + h_stats['goalDiff']) - (a_stats['points'] + a_stats['goalDiff'])

            if power_gap > 10:
                pred, conf = "Home Win (1)", "High"
            elif power_gap > 0:
                pred, conf = "1X Double Chance", "Medium"
            elif power_gap > -10:
                pred, conf = "X2 Double Chance", "Medium"
            else:
                pred, conf = "Away Win (2)", "High"

            badge_class = "high" if conf == "High" else "med"

            html += f"""
                <tr>
                    <td>{date}</td>
                    <td><b>{home}</b> vs {away}</td>
                    <td>{pred}</td>
                    <td><span class="badge {badge_class}">{conf}</span></td>
                </tr>
            """

        html += f"</table><div style='margin-top:20px; font-size:11px; color:#999;'>Algorithm v1.1 | Last Update: {date}</div></div></body></html>"

        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html)
        print("Success: Data-driven predictions generated!")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
