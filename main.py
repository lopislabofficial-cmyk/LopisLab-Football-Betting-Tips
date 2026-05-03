from js import Response

def on_fetch(request):
    # Scriviamo l'HTML su una riga sola, senza f-strings o variabili intermedie
    return Response.new(
        "<h1>LopisLab</h1><p>Sistema Online</p><ul><li>Inter-Milan: 1X</li></ul>", 
        headers={"Content-Type": "text/html; charset=utf-8"}
    )
