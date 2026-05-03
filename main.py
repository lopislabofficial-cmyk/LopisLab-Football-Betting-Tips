from js import Response

async def on_fetch(request, env):
    # Costruiamo l'HTML in una variabile singola senza ritorni a capo strani
    h = "<html><body style='background:#121212;color:#00b894;text-align:center;font-family:sans-serif;'>"
    h += "<h1>LopisLab Football Tips</h1>"
    h += "<p style='color:white;'>Sito Online - In attesa dei pronostici</p>"
    h += "</body></html>"
    
    # Restituiamo la risposta con l'header formattato in modo ultra-semplice
    return Response.new(h, headers={"Content-Type": "text/html"})
