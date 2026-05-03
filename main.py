from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # URL di ScoreBat
    URL = "https://www.scorebat.com/video-api/v3/"
    
    matches_html = ""
    error_info = ""
    
    try:
        # Specifichiamo il metodo e la modalità
        response = await fetch(URL, method="GET", redirect="follow")
        
        if response.status == 200:
            data = await response.json()
            matches = data.get("response", [])[:8]
            
            if not matches:
                matches_html = "<div class='match-row'>No live matches right now.</div>"
            
            for m in matches:
                teams = m.get("title", "Match").replace(" - ", " vs ")
                comp = m.get("competition", "")
                matches_html += f"<div class='match-row'><div class='teams'>{teams}<br><small>{comp}</small></div><div class='prediction'>LIVE</div></div>"
        else:
            matches_html = f"<div class='match-row'>Error: Status {response.status}</div>"
    except Exception as e:
        # Questo ci dirà l'errore reale sulla pagina
        error_info = f"<div style='font-size:0.6rem; color:red;'>Debug: {str(e)}</div>"
        matches_html = "<div class='match-row'>Connection blocked by API.</div>"

    css = "<style>body{background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;padding:10px;}.card{width:100%;max-width:400px;background:#1e293b;border-radius:20px;padding:20px;border:1px solid #334155;}h1{color:#38bdf8;text-align:center;font-size:1.4rem;}.badge{background:#064e3b;color:#34d399;font-size:0.7rem;padding:4px 10px;border-radius:20px;display:block;width:fit-content;margin:0 auto 20px;}.match-row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #334155;}.teams{font-size:0.85rem;}.prediction{color:#fbbf24;font-weight:bold;font-size:0.75rem;}</style>"
    
    content = f"<div class='card'><h1>LopisLab Live</h1><span class='badge'>GLOBAL FOOTBALL</span>{matches_html}{error_info}</div>"
    
    return Response.new(f"<!DOCTYPE html><html><head>{css}</head><body>{content}</body></html>", headers=hdrs)
