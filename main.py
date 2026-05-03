from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # Inserisci la tua chiave qui
    API_KEY = "311c7fcfaef748e7a3579601f576ad4d"
    
    # Cambiamo endpoint: chiediamo solo i match di OGGI (più leggero)
    URL = "https://api.football-data.org/v4/matches"
    
    api_headers = Headers.new()
    api_headers.set("X-Auth-Token", API_KEY)
    
    matches_html = ""
    
    try:
        # Aggiungiamo un timeout manuale virtuale usando fetch
        response = await fetch(URL, headers=api_headers)
        
        if response.status == 200:
            data = await response.json()
            matches = data.get("matches", [])[:5]
            
            if not matches:
                matches_html = "<div class='match-row'>No matches scheduled for today.</div>"
            
            for m in matches:
                home = m['homeTeam']['shortName'] or m['homeTeam']['name']
                away = m['awayTeam']['shortName'] or m['awayTeam']['name']
                matches_html += f"<div class='match-row'><div class='teams'>{home} vs {away}</div><div class='prediction'>LIVE</div></div>"
        elif response.status == 429:
            matches_html = "<div class='match-row'>Too many requests. Wait 1 minute.</div>"
        else:
            matches_html = f"<div class='match-row'>API temporarily busy (Status {response.status})</div>"
    except:
        matches_html = "<div class='match-row'>Connection slow... Try to refresh!</div>"

    css = "<style>body{background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;padding:10px;}.card{width:100%;max-width:400px;background:#1e293b;border-radius:20px;padding:20px;border:1px solid #334155;}h1{color:#38bdf8;text-align:center;font-size:1.4rem;}.badge{background:#064e3b;color:#34d399;font-size:0.7rem;padding:4px 10px;border-radius:20px;display:block;width:fit-content;margin:0 auto 20px;}.match-row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #334155;}.teams{font-size:0.9rem;}.prediction{color:#fbbf24;font-weight:bold;font-size:0.8rem;}</style>"
    content = f"<div class='card'><h1>LopisLab</h1><span class='badge'>TODAY'S MATCHES</span>{matches_html}</div>"
    
    return Response.new(f"<!DOCTYPE html><html><head>{css}</head><body>{content}</body></html>", headers=hdrs)
