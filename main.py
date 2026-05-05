from js import Response, fetch
import json

async def on_fetch(request, env):
    # 1. Configurazione (Metti la tua API KEY qui)
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c"
    
    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    # Paesi target per la tua "miniera d'oro"
    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        resp = await fetch(url, headers=headers)
        data = await resp.json()
        
        # Se l'API restituisce errori o dati vuoti
        if not data.get('response'):
            return Response.new("L'API non ha restituito dati. Controlla la tua API Key.")

        count = 0
        for item in data['response']:
            country_name = str(item['country']['name'])
            
            if country_name in target_countries:
                for season in item['seasons']:
                    if season['current'] is True:
                        league = item['league']
                        
                        # TRUCCO TECNICO: Convertiamo tutto in tipi semplici (int, str) 
                        # per evitare l'errore 'Sequence'
                        l_id = int(league['id'])
                        l_name = str(league['name'])
                        l_type = str(league['type'])

                        # Usiamo bind() passando i valori uno per uno
                        await env.DB.prepare(
                            "INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES (?, ?, ?, ?)"
                        ).bind(l_id, l_name, country_name, l_type).run()
                        
                        count += 1

        return Response.new(f"Successo! Ho trovato e salvato {count} campionati nel database di Lopislab.")

    except Exception as e:
        # Questo ti aiuterà a vedere meglio l'errore se dovesse ricapitare
        return Response.new(f"Errore tecnico dettagliato: {str(e)}", status=500)
