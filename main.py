from js import Response

def on_fetch(request):
    html = """
    <!DOCTYPE html>
    <html lang="it">
    <head><meta charset="UTF-8"></head>
    <body style="background-color: #121212; color: #00b894; font-family: sans-serif; text-align: center;">
        <h1>LopisLab Football Tips</h1>
        <p style="color: white;">Sito Online - Pronostici in arrivo</p>
    </body>
    </html>
    """
    # Nota bene: headers con le doppie virgolette e minuscolo
    return Response.new(html, headers={"content-type": "text/html;charset=UTF-8"})
