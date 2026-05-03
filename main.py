from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # --- CONFIGURAZIONE API ---
    API_KEY = "311c7fcfaef748e7a3579601f576ad4d" # <--- METTI QUI LA TUA CHIAVE
    URL = "https://api.football-data.org/v4/matches"
    
    # Prepariamo la chiamata all'API
    api_headers = Headers.new()
    api_headers.set("X-Auth-Token", API_KEY)
    
    matches_html = ""
    
    try:
        # Chiamata asincrona all'API
        response = await fetch(URL, headers=api_headers)
        data = await response.json()
        
        # Prendiamo solo i primi 5 match per non sovraccaricare la pagina
        matches = data.matches[:5]
        
        for m in matches:
            home = m.homeTeam.name
            away = m.awayTeam.name
            # Football-Data non dà "pronostici", ma noi simuliamo un'analisi IA
            # basata sulle quote o semplicemente mostriamo il match
            matches_html += f"""
            <div class='match-row'>
                <div class='teams'>{home} vs {away}</div>
                <div class='prediction'>TBD</div>
            </div>
            """
    except Exception as e:
        matches_html = f"<div class='match-row'>Error loading matches: {str(e)}</div>"

    css = (
        "<style>"
        "body { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; margin: 0; padding: 10px; display: flex; justify-content: center; }"
        ".card { width: 100%; max-width: 450px; background: #1e293b; border-radius: 20px; padding: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); border: 1px solid #334155; margin-top: 40px; }"
        "h1 { color: #38bdf8; font-size: 1.5rem; margin-bottom: 5px; text-align: center; }"
        ".badge { background: #064e3b; color: #34d399; font-size: 0.7rem; padding: 4px 10px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px; }"
        ".match-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #334155; }"
        ".teams { flex: 1; font-weight: 500; font-size: 0.95rem; text-align: left; }"
        ".prediction { background: #334155; padding: 6px 12px; border-radius: 8px; color: #fbbf24; font-weight: bold; font-size: 0.85rem; min-width: 60px; text-align: center; }"
        "footer { text-align: center; margin-top: 20px; font-size: 0.75rem; color: #94a3b8; }"
        "</style>"
    )

    content = (
        f"<div class='card'>"
        f"<h1>LopisLab Football</h1>"
        f"<div style='text-align:center;'><span class='badge'>● LIVE DATA ACTIVE</span></div>"
        f"{matches_html}"
        f"<footer>Real-time data from Football-Data.org</footer>"
        f"</div>"
    )

    html = f"<!DOCTYPE html><html lang='en'><head><title>LopisLab Live</title>{css}</head><body>{content}</body></html>"
    
    return Response.new(html, headers=hdrs)
