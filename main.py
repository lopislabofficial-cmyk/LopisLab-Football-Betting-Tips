from js import Response, fetch
import json

async def on_fetch(request, env):
    # 1. Configurazione
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c" # <--- Assicurati che sia corretta!
    
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
            return Response.new("Dati API non disponibili o chiave errata.")

        count = 0
        for item in data['response']:
            # Estraiamo i valori in variabili semplici prima del database
            country_obj = item.get('country', {})
            country_name = country_obj.get('name')
            
            if country_name in target_countries:
                for season in item.get('seasons', []):
                    if season.get('current') is True:
                        league = item.get('league', {})
                        
                        l_id = league.get('id')
                        l_name = league.get('name')
                        l_type = league.get('type')

                        # Eseguiamo l'inserimento senza usare str() come funzione
                        # ma passando direttamente le variabili pulite
                        await env.DB.prepare(
                            "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)"
                        ).bind(l_id, l_name, country_name, l_type).run()
                        
                        count += 1

        return Response.new(f"Successo! Database popolato con {count} campionati.")

    except Exception as e:
        return Response.new(f"Errore tecnico risolto: {str(e)}", status=500)
