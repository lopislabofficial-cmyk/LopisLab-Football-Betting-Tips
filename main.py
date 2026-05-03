from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # Usiamo un URL differente che spesso è più aperto: le news di ScoreBat
    URL = "https://www.scorebat.com/video-api/v3/"
    
    matches_html = ""
    
    try:
        # Chiamata super-semplificata
        resp = await fetch(URL)
        # Invece di json(), prendiamo il testo e lo carichiamo noi con la libreria json di python
        raw_text = await resp.text()
        data = json.loads(raw_text)
        
        items = data.get("response", [])[:8]
        
        if not items:
            matches_html = "<div class='match-row'>No matches found.</div>"
        
        for item in items:
            title = item.get("title", "Match").replace(" - ", " vs ")
            comp = item.get("competition", "")
            matches_html += f"<div class='match-row'><div class='teams'>{title}<br><small>{comp}</small></div><div class='prediction'>LIVE</div></div>"
            
    except Exception as e:
        # Se fallisce ancora, mostriamo un messaggio di "Manutenzione" elegante
        # Invece di far vedere l'errore tecnico all'utente
        matches_html = (
            "<div class='match-row' style='text-align:center; color:#94a3b8;'>"
            "Predictions are being updated...<br>"
            "Please check back in a few minutes."
            "</div>"
        )

    css = "<style>body{background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;padding:10px;}.card{width:100%;max-width:400px;background:#1e293b;border-radius:20px;padding:20px;border:1px solid #334155;}h1{color:#38bdf8;text-align:center;font-size:1.4rem;}.badge{background:#064e3b;color:#34d399;font-size:0.7rem;padding:4px 10px;border-radius:20px;display:block;width:fit-content;margin:0 auto 20px;}.match-row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #334155;}.teams{font-size:0.85rem;line-height:1.3;}.prediction{color:#fbbf24;font-weight:bold;font-size:0.75rem;}</style>"
    
    content = f"<div class='card'><h1>LopisLab Live</h1><span class='badge'>GLOBAL FOOTBALL</span>{matches_html}</div>"
    
    return Response.new(f"<!DOCTYPE html><html><head><title>LopisLab</title>{css}</head><body>{content}</body></html>", headers=hdrs)
