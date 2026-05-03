from js import Response, Headers, fetch
import json

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # Usiamo ScoreBat API (Gratuita e non blocca Cloudflare)
    URL = "https://www.scorebat.com/video-api/v3/"
    
    matches_html = ""
    
    try:
        response = await fetch(URL)
        if response.status == 200:
            data = await response.json()
            # Prendiamo i primi 8 match recenti o live
            matches = data.get("response", [])[:8]
            
            for m in matches:
                title = m.get("title", "Match")
                competition = m.get("competition", "")
                # Puliamo il titolo (spesso è 'Squadra A - Squadra B')
                teams = title.replace(" - ", " vs ")
                
                matches_html += f"""
                <div class='match-row'>
                    <div class='teams'>
                        {teams}<br>
                        <small style='color:#64748b; font-size:0.7rem;'>{competition}</small>
                    </div>
                    <div class='prediction'>LIVE</div>
                </div>
                """
        else:
            matches_html = f"<div class='match-row'>Server busy ({response.status})</div>"
    except Exception as e:
        matches_html = "<div class='match-row'>Loading matches... Please refresh.</div>"

    css = "<style>body{background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;padding:10px;}.card{width:100%;max-width:400px;background:#1e293b;border-radius:20px;padding:20px;border:1px solid #334155;}h1{color:#38bdf8;text-align:center;font-size:1.4rem;}.badge{background:#064e3b;color:#34d399;font-size:0.7rem;padding:4px 10px;border-radius:20px;display:block;width:fit-content;margin:0 auto 20px;}.match-row{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid #334155;}.teams{font-size:0.85rem;line-height:1.2;}.prediction{color:#fbbf24;font-weight:bold;font-size:0.75rem;border:1px solid #fbbf24;padding:2px 6px;border-radius:4px;}</style>"
    
    content = f"<div class='card'><h1>LopisLab Live</h1><span class='badge'>GLOBAL FOOTBALL</span>{matches_html}</div>"
    
    return Response.new(f"<!DOCTYPE html><html><head><title>LopisLab</title>{css}</head><body>{content}</body></html>", headers=hdrs)
