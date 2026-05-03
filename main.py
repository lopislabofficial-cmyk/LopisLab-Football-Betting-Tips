from js import Response

def on_fetch(request):
    # Costruiamo l'HTML riga per riga per evitare errori di formattazione
    h = "<h1>⚽ LopisLab Football Tips</h1>"
    h += "<p>Il sistema e online.</p>"
    h += "<ul>"
    h += "<li>Inter - Milan: 1X</li>"
    h += "<li>Real - Barca: Goal</li>"
    h += "</ul>"
    h += "<p>Aggiornato via GitHub.</p>"
    
    return Response.new(h, headers={"content-type": "text/html;charset=UTF-8"})
