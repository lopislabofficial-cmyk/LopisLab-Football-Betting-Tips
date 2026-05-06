from js import Response, fetch

async def on_fetch(request, env):
    # 1. Configurazione
    API_KEY = "04bbd211c6fd8dde4d54633de6775a3c" 
    
    url = "https://v3.football.api-sports.io/leagues"
    headers = {
        "x-apisports-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    target_countries = ["Sweden", "Norway", "Brazil", "USA", "Japan", "Colombia", "Nigeria"]

    try:
        resp = await fetch(url, headers=headers)
        data = await resp.json()
        
        if not data or not data.response:
            return Response.new("Errore: Risposta API vuota.")

        count = 0
        for item in data.response:
            c_name = str(item.country.name)
            
            if c_name in target_countries:
                for season in item.seasons:
                    if season.current:
                        # Estraiamo i dati in variabili semplici
                        l_id = int(item.league.id)
                        l_name = str(item.league.name)
                        l_type = str(item.league.type)

                        # SOLUZIONE: Usiamo la query diretta con i valori inseriti 
                        # Questo evita il problema del 'Sequence' nel bind
                        query = f"INSERT OR REPLACE INTO leagues (league_id, name, country, type) VALUES ({l_id}, '{l_name.replace("'", "''")}', '{c_name}', '{l_type}')"
                        
                        await env.DB.prepare(query).run()
                        
                        count += 1

        return Response.new(f"Lopislab Online! Salvati {count} campionati.")

    except Exception as e:
        return Response.new(f"Errore tecnico: {str(e)}", status=500)
                      
