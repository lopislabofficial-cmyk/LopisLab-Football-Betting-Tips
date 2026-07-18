import os
import requests

def main():
    # 1. Recupera la chiave API dai segreti di GitHub Actions
    API_KEY = os.getenv("FOOTBALL_DATA_API_KEY") or os.getenv("API_SPORTS_KEY")
    
    if not API_KEY:
        print("❌ Errore: Chiave API non trovata nei segreti di GitHub.")
        return

    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        print("⚽ Connessione a API-Sports in corso...")
        resp = requests.get(url, headers=headers)
        data = resp.json()
        
        if not data or not data.get("response"):
            print("❌ Errore: Risposta API vuota o non valida.")
            return

        # Generiamo le righe per la tabella HTML
        html_rows = ""
        count = 0
        
        for item in data["response"]:
            c_name = str(item["country"]["name"])
            
            if c_name in target_countries:
                for season in item["seasons"]:
                    if season.get("current"):
                        l_id = item["league"]["id"]
                        l_name = item["league"]["name"]
                        l_type = item["league"]["type"]
                        
                        html_rows += f"""
            <tr>
                <td>{l_id}</td>
                <td>{l_name}</td>
                <td>{c_name}</td>
                <td>{l_type}</td>
            </tr>"""
                        count += 1

        # 2. Scrittura o Aggiornamento del file index.html
        html_content = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LopisLab - Campionati Attivi</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #121212; color: #fff; padding: 20px; }}
        h1 {{ color: #00ff88; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #333; padding: 10px; text-align: left; }}
        th {{ background-color: #1a1a1a; color: #00ff88; }}
        tr:nth-child(even) {{ background-color: #1f1f1f; }}
    </style>
</head>
<body>
    <h1>Lopislab Online!</h1>
    <p>Ultimo aggiornamento automatico. Campionati attivi monitorati: <strong>{count}</strong></p>
    <table>
        <thead>
            <tr>
                <th>ID Campionato</th>
                <th>Nome</th>
                <th>Nazione</th>
                <th>Tipo</th>
            </tr>
        </thead>
        <tbody>{html_rows}
        </tbody>
    </table>
</body>
</html>"""

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Ottimo! File index.html generato con successo. Salvati {count} campionati.")

    except Exception as e:
        print(f"❌ Errore tecnico durante l'esecuzione: {str(e)}")

if __name__ == "__main__":
    main()
