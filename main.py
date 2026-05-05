from js import Response, fetch
import json

async def on_fetch(request, env):
    # 1. Configurazione (Sostituisci con la tua vera API Key)
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c"
    
    # Endpoint per le leghe
    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    # Definiamo i campionati "miniera d'oro" che vogliamo seguire
    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        # 2. Chiamata all'API
        resp = await fetch(url, headers=headers)
        data = await resp.json()
        
        count = 0
        # 3. Ciclo sui dati ricevuti
        for item in data['response']:
            country_name = item['country']['name']
            
            # Se il campionato è in uno dei nostri paesi target e la stagione è quella attuale
            if country_name in target_countries:
                for season in item['seasons']:
                    if season['current'] is True:
                        league = item['league']
                        
                        # Scrittura nel database D1 (il tuo binding 'DB')
                        await env.DB.prepare(
                            "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)"
                        ).bind(league['id'], league['name'], country_name, league['type']).run()
                        
                        count += 1

        return Response.new(f"Successo! Ho trovato e salvato {count} campionati per Lopislab.")

    except Exception as e:
        return Response.new(f"Errore tecnico: {str(e)}", status=500)
