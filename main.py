from js import Response, Headers

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    css = (
        "<style>"
        "body { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; margin: 0; padding: 10px; display: flex; justify-content: center; }"
        ".card { width: 100%; max-width: 450px; background: #1e293b; border-radius: 20px; padding: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); border: 1px solid #334155; margin-top: 40px; }"
        "h1 { color: #38bdf8; font-size: 1.5rem; margin-bottom: 5px; text-align: center; }"
        ".badge { background: #064e3b; color: #34d399; font-size: 0.7rem; padding: 4px 10px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px; }"
        ".match-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #334155; }"
        ".match-row: last-child { border: none; }"
        ".teams { flex: 1; font-weight: 500; font-size: 0.95rem; }"
        ".prediction { background: #334155; padding: 6px 12px; border-radius: 8px; color: #fbbf24; font-weight: bold; font-size: 0.85rem; min-width: 60px; text-align: center; }"
        "footer { text-align: center; margin-top: 20px; font-size: 0.75rem; color: #94a3b8; }"
        "</style>"
    )

    # Content in English with realistic matches
    content = (
        "<div class='card'>"
        "<h1>LopisLab Football</h1>"
        "<div style='text-align:center;'><span class='badge'>● AI SYSTEM LIVE</span></div>"
        
        "<div class='match-row'>"
        "<div class='teams'>Liverpool vs Tottenham</div>"
        "<div class='prediction'>Home Win</div>"
        "</div>"
        
        "<div class='match-row'>"
        "<div class='teams'>Bayer Leverkusen vs Roma</div>"
        "<div class='prediction'>Over 2.5</div>"
        "</div>"
        
        "<div class='match-row'>"
        "<div class='teams'>Real Madrid vs Bayern</div>"
        "<div class='prediction'>BTTS - Yes</div>"
        "</div>"
        
        "<footer>v1.2 - Powered by LopisLab Intelligence</footer>"
        "</div>"
    )

    html = f"<!DOCTYPE html><html lang='en'><head><title>LopisLab Tips</title>{css}</head><body>{content}</body></html>"
    
    return Response.new(html, headers=hdrs)
