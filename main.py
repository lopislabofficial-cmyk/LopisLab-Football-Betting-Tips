from js import Response, fetch
import json

async def on_fetch(request, env):
    # 1. Configurazione
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c" # <--- Metti la tua chiave qui
    
    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        resp = await fetch(url, headers=headers)
        data = await resp.json()
        
        if not data.get('response'):
            return Response.new("Dati API non disponibili. Verifica la tua API Key.")

        count = 0
        for item in data['response']:
            country_name = str(item['country']['name'])
            
            if country_name in target_countries:
                for season in item.get('seasons', []):
                    if season.get('current') is True:
                        league = item.get('league', {})
                        
                        # CREIAMO LA SEQUENZA (LISTA) RICHIESTA
                        # Questo risolve l'errore "not of type Sequence"
                        params = [
                            int(league.get('id')), 
                            str(league.get('name')), 
                            str(country_name), 
                            str(league.get('type'))
                        ]

                        # Passiamo la lista intera al bind
                        await env.DB.prepare(
                            "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)"
                        ).bind(*params).run()
                        
                        count += 1

        return Response.new(f"Successo totale! Database popolato con {count} campionati mondiali.")

    except Exception as e:
        return Response.new(f"Tentativo finale - Errore: {str(e)}", status=500)
                      
