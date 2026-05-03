from js import Response, Headers

async def on_fetch(request, env):
    # Creiamo gli headers in modo esplicito
    hdrs = Headers.new()
    hdrs.set("Content-Type", "text/html; charset=utf-8")
    
    # HTML super pulito
    html = (
        "<html>"
        "<body style='background:#121212;color:#00b894;text-align:center;padding-top:50px;font-family:sans-serif;'>"
        "<h1>LopisLab Football Tips</h1>"
        "<p style='color:white;'>Sito Online - Test di connessione IA riuscito</p>"
        "</body>"
        "</html>"
    )
    
    # Restituiamo la risposta usando l'oggetto Headers creato sopra
    return Response.new(html, headers=hdrs)
