import requests
import os

# Recuperiamo la tua chiave dalla "cassaforte" di GitHub
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def main():
    # Chiediamo i dati della Serie A (ID: SA)
    url = "https://api.football-data.org/v4/competitions/SA/matches?status=SCHEDULED"
    response = requests.get(url, headers=headers)
    data = response.json()

    matches = data.get('matches', [])[:10] # Prendiamo le prime 10 partite in programma

    # Creiamo una pagina web semplice (HTML)
    html = "<html><head><title>LopisLab Pronostici</title></head><body style='font-family:sans-serif;'>"
    html += "<h1>LopisLab - Football Betting Tips</h1>"
    html += "<h2>Prossime Partite Serie A</h2><table border='1' cellpadding='10'>"
    html += "<tr><th>Data</th><th>Incontro</th><th>Pronostico</th></tr>"

    for match in matches:
        home = match['homeTeam']['name']
        away = match['awayTeam']['name']
        date = match['utcDate'][:10]
        html += f"<tr><td>{date}</td><td>{home} vs {away}</td><td>In Analisi...</td></tr>"

    html += "</table></body></html>"

    # Salviamo il file che Cloudflare leggerà
    with open("index.html", "w") as f:
        f.write(html)
    print("Pagina aggiornata con successo!")

if __name__ == "__main__":
    main()
