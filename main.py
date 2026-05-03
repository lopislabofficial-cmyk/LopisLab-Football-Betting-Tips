from js import Response

def on_fetch(request):
    return Response.new("Benvenuti su LopisLab. Il server e attivo. Presto arriveranno i pronostici.")
