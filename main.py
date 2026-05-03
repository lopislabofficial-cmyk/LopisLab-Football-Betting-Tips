from js import Response

def on_fetch(request):
    # Qui puoi inserire i tuoi pronostici del giorno
    tips = [
        {"match": "Inter vs Milan", "tip": "1X + Over 1.5", "odds": "1.65"},
        {"match": "Real Madrid vs Barcellona", "tip": "Goal", "odds": "1.55"},
        {"match": "Man City vs Arsenal", "tip": "1", "odds": "1.80"},
    ]

    # Costruiamo la tabella HTML
    rows = "".join([
        f"<tr><td>{t['match']}</td><td><strong>{t['tip']}</strong></td><td>{t['odds']}</td></tr>" 
        for t in tips
    ])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LopisLab Football Tips</title>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 20px; }}
            table {{ margin: 20px auto; border-collapse: collapse; width: 90%; max-width: 600px; background: #1e1e1e; }}
            th, td {{ padding: 12px; border: 1px solid #333; }}
            th {{ background: #00b894; color: black; }}
            h1 {{ color: #00b894; }}
            .footer {{ margin-top: 30px; font-size: 0.8em; color: #888; }}
        </style>
    </head>
    <body>
        <h1>⚽ LopisLab Football Tips</h1>
        <p>I migliori pronostici selezionati dall'IA</p>
        <table>
            <thead>
                <tr><th>Partita</th><th>Pronostico</th><th>Quota</th></tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        <div class="footer">Aggiornato automaticamente via GitHub Actions</div>
    </body>
    </html>
    """
    
    return Response.new(html_content, headers={{"content-type": "text/html;charset=UTF-8"}})
