import requests
import os

# Recuperiamo la tua chiave dalla "cassaforte"
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def main():
    try:
        # Chiediamo i dati della Serie A
        url = "https://api.football-data.org/v4/competitions/SA/matches?status=SCHEDULED"
        response = requests.get(url, headers=headers)
        data = response.json()

        matches = data.get('matches', [])[:10] 

        # Inizio HTML
        html = "<html><head><title>LopisLab Football Insights</title>"
        html += "<style>body{font-family:sans-serif; background:#f4f4f4; padding:20px;}"
        html += "table{width:100%; border-collapse:collapse; background:white; shadow: 0 2px 5px rgba(0,0,0,0.1);}"
        html += "th, td{padding:12px; text-align:left; border-bottom:1px solid #ddd;}"
        html += "th{background:#2c3e50; color:white;}</style></head><body>"
        html += "<h1>LopisLab - Football Betting Tips</h1>"
        html += "<h2>Upcoming Serie A Matches</h2><table>"
        html += "<tr><th>Date</th><th>Match</th><th>Prediction</th></tr>"

        if not matches:
            html += "<tr><td colspan='3'>No matches scheduled for the next few days.</td></tr>"

        for match in matches:
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            date = match['utcDate'][:10]
            
            # Qui inseriremo Poisson. Per ora simuliamo un'analisi basata su ID
            # Un piccolo esempio: se la squadra di casa ha ID pari, diamo 1X, altrimenti X2
            prob = "1X (High Prob.)" if (match['homeTeam']['id'] % 2 == 0) else "X2 (Medium Prob.)"
            
            html += f"True<td>{date}</td><td>{home} vs {away}</td><td><b>{prob}</b></td></tr>"

        html += "</table><p><small>Last Update: " + date + "</small></p></body></html>"

        # Salviamo il file
        with open("index.html", "w") as f:
            f.write(html)
        print("Success: index.html generated!")

    except Exception as e:
        print(f"Error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
