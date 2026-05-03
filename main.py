from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # --- METTI LA TUA CHIAVE QUI ---
    API_KEY = "311c7fcfaef748e7a3579601f576ad4d"
    
    # Puntiamo alla Serie A (SA) per vedere Roma vs Fiorentina
    URL = "https://api.football-data.org/v4/competitions/SA/matches?status=SCHEDULED"
    
    api_headers = Headers.new()
    api_headers.set("X-Auth-Token", API_KEY)
    api_headers.set("User-Agent", "LopisLab/1.1")
    
    matches_html = ""
    
    try:
        response = await fetch(URL, headers=api_headers)
        if response.status == 200:
            raw_text = await response.text()
            data = json.loads(raw_text)
            matches = data.get("matches", [])[:5] # Vediamo i prossimi 5
            
            if not matches:
                matches_html = "<div class='match-row'>No upcoming Serie A matches.</div>"
            
            for m in matches:
                home = m['homeTeam']['name']
                away = m['awayTeam']['name']
                # Simuliamo il pronostico IA
                matches_html += f"""
                <div class='match-row'>
                    <div class='teams'>{home} vs {away}</div>
                    <div class='prediction'>AI TIP: GOAL</div>
                </div>"""
        else:
            matches_html = f"<div class='match-row'>API Syncing... (Status {response.status})</div>"
    except Exception:
        matches_html = "<div class='match-row'>Updating real-time data...</div>"

    css = "<style>body{background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;padding:10px;}.card{width:100%;max-width:400px;background:#1e293b;border-radius:20px;padding:20px;border:1px solid #334155;}h1{color:#38bdf8;text-align:center;font-size:1.4rem;}.badge{background:#064e3b;color:#34d399;font-size:0.7rem;padding:4px 10px;border-radius:20px;display:block;width:fit-content;margin:0 auto 20px;}.match-row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #334155;}.teams{font-size:0.9rem;}.prediction{color:#fbbf24;font-weight:bold;font-size:0.8rem;}</style>"
    content = f"<div class='card'><h1>LopisLab Live</h1><span class='badge'>SERIE A REAL-TIME</span>{matches_html}</div>"
    
    return Response.new(f"<!DOCTYPE html><html><head>{css}</head><body>{content}</body></html>", headers=hdrs)
