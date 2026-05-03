from js import Response

def on_fetch(request):
    # Usiamo solo testo sicuro
    titolo = "LopisLab Football Tips"
    sottotitolo = "Pronostici IA"
    match1 = "Inter vs Milan: 1X"
    match2 = "Real Madrid vs Barcellona: GOAL"
    
    # Uniamo tutto in un formato che Cloudflare digerisce bene
    corpo = f"<h1>{titolo}</h1><p>{sottotitolo}</p><ul><li>{match1}</li><li>{match2}</li></ul>"
    
    return Response.new(corpo, headers={"Content-Type": "text/html"})
