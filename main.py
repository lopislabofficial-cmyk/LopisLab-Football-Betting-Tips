from js import Response

def on_fetch(request):
    html = """
    <h1>⚽ LopisLab Football Tips</h1>
    <p>Il sistema e online e pronto per i pronostici.</p>
    <hr>
    <ul>
        <li><b>Inter - Milan:</b> 1X + Over 1.5</li>
        <li><b>Real Madrid - Barcellona:</b> Goal</li>
        <li><b>Man City - Arsenal:</b> 1</li>
    </ul>
    <p><small>Aggiornato automaticamente via GitHub</small></p>
    """
    return Response.new(html, headers={"content-type": "text/html;charset=UTF-8"})
