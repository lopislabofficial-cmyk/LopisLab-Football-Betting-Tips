from js import Response

def on_fetch(request):
    html_content = """
    <h1>LopisLab Football Tips</h1>
    <p>Sito in fase di aggiornamento...</p>
    <ul>
        <li>Inter - Milan: 1X</li>
        <li>Real - Barca: Goal</li>
    </ul>
    """
    return Response.new(html_content, headers={"content-type": "text/html;charset=UTF-8"})
