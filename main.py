from js import Response, Headers

async def on_fetch(request, env):
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # Definiamo i colori e lo stile CSS
    css = (
        "<style>"
        "body { background-color: #121212; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; text-align: center; }"
        ".container { max-width: 600px; margin: auto; border: 1px solid #333; border-radius: 15px; padding: 20px; background: #1e1e1e; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }"
        "h1 { color: #00b894; margin-bottom: 10px; }"
        ".status { color: #00b894; font-size: 0.9em; margin-bottom: 20px; }"
        "table { width: 100%; border-collapse: collapse; margin-top: 20px; }"
        "th, td { padding: 12px; border-bottom: 1px solid #333; text-align: left; }"
        "th { color: #00b894; font-size: 0.8em; text-transform: uppercase; }"
        ".quota { color: #ffca28; font-weight: bold; }"
        "footer { margin-top: 30px; font-size: 0.8em; color: #777; }"
        "</style>"
    )

    # Definiamo il contenuto della pagina
    content = (
        "<div class='container'>"
        "<h1>⚽ LopisLab Tips</h1>"
        "<div class='status'>● SISTEMA IA ATTIVO</div>"
        "<table>"
        "<thead><tr><th>Partita</th><th>Pronostico</th><th>Quota</th></tr></thead>"
        "<tbody>"
        "<tr><td>Inter - Milan</td><td>1X + Over 1.5</td><td class='quota'>1.45</td></tr>"
        "<tr><td>Real Madrid - Barca</td><td>Goal</td><td class='quota'>1.55</td></tr>"
        "<tr><td>Man. City - Arsenal</td><td>1</td><td class='quota'>1.80</td></tr>"
        "</tbody>"
        "</table>"
        "<footer>Aggiornato automaticamente via GitHub Actions</footer>"
        "</div>"
    )

    html = f"<html><head><title>LopisLab</title>{css}</head><body>{content}</body></html>"
    
    return Response.new(html, headers=hdrs)
