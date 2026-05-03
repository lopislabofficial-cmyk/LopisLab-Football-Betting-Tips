from js import Response, Headers

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # QUI INSERISCI I TUOI PRONOSTICI REALI
    # Puoi cambiare questi nomi e suggerimenti quando vuoi
    tips = [
        {"match": "Fiorentina vs Roma", "tip": "X2 + Goal", "odds": "2.10"},
        {"match": "Inter vs Empoli", "tip": "1 + Over 2.5", "odds": "1.65"},
        {"match": "Juventus vs Udinese", "tip": "1", "odds": "1.45"},
        {"match": "Milan vs Lecce", "tip": "Home Over 1.5", "odds": "1.55"}
    ]
    
    rows = ""
    for t in tips:
        rows += f"""
        <div class='match-row'>
            <div class='teams'>{t['match']}</div>
            <div class='prediction'>{t['tip']} <span style='color:#64748b; font-size:0.7rem;'>@{t['odds']}</span></div>
        </div>
        """

    css = (
        "<style>"
        "body { background:#0f172a; color:#f8fafc; font-family:sans-serif; display:flex; justify-content:center; padding:20px; }"
        ".card { width:100%; max-width:400px; background:#1e293b; border-radius:20px; padding:25px; border:1px solid #334155; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }"
        "h1 { color:#38bdf8; text-align:center; margin:0; font-size:1.8rem; letter-spacing:-1px; }"
        ".badge { background:#064e3b; color:#34d399; font-size:0.7rem; padding:5px 12px; border-radius:20px; display:block; width:fit-content; margin:15px auto; font-weight:bold; border: 1px solid #059669; }"
        ".match-row { display:flex; justify-content:space-between; align-items:center; padding:15px 0; border-bottom:1px solid #334155; }"
        ".match-row:last-of-type { border:none; }"
        ".teams { font-size:0.95rem; font-weight:500; }"
        ".prediction { background:#0f172a; color:#fbbf24; font-weight:bold; font-size:0.8rem; padding:8px 12px; border-radius:10px; border:1px solid #fbbf2433; text-align:right; }"
        "footer { text-align:center; margin-top:20px; font-size:0.7rem; color:#64748b; }"
        "</style>"
    )
    
    content = f"""
    <div class='card'>
        <h1>LopisLab</h1>
        <div class='badge'>● AI ANALYST LIVE</div>
        {rows}
        <footer>Aggiornato: Oggi, 4 Maggio</footer>
    </div>
    """
    
    return Response.new(f"<!DOCTYPE html><html><head><title>LopisLab</title>{css}</head><body>{content}</body></html>", headers=hdrs)
