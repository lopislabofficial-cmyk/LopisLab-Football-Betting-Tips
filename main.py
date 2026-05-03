from js import Response

def on_fetch(request):
    return Response.new("Ciao! Il Worker Python e attivo e funzionante!")
