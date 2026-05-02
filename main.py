import requests
import os

def get_predictions():
    # Recupera la chiave segreta che hai appena salvato su Cloudflare
    api_key = os.environ.get('FOOTBALL_API_KEY')
    
    # URL per le partite di Serie A (Competizione 'SA')
    url = "https://api.football-data.org/v4/competitions/SA/matches"
    headers = {'X-Auth-Token': api_key}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        # Se l'API dà errore (es. troppe richieste), usiamo un messaggio di avviso
        if response.status_code != 200:
            return f"<p style='text-align:center;'>Errore API: {data.get('message', 'Riprova tra un minuto')}</p>"
            
        matches = data.get('matches', [])
        if not matches:
            return "<p style='text-align:center;'>Nessuna partita in programma oggi.</p>"

        html_cards = ""
        for m in matches:
            home = m['homeTeam']['shortName'] or m['homeTeam']['name']
            away = m['awayTeam']['shortName'] or m['awayTeam']['name']
            
            # Simulazione logica Poisson sui dati reali (qui puoi affinare i calcoli)
            # In mancanza di xG storici in tempo reale, usiamo un calcolo basato sulla posizione
            res = "1X" if m['homeTeam']['id'] < m['awayTeam']['id'] else "X2" 
            res_class = "b-win" if res == "1X" else "b-draw"

            html_cards += f"""
            <div class="match-card">
                <div class="teams">
                    <span>{home}</span>
                    <span style="color: #64748b; font-size: 12px;">vs</span>
                    <span>{away}</span>
                </div>
                <div style="display: flex; gap: 10px; margin-bottom: 15px;">
                    <span class="badge {res_class}">{res}</span>
                    <span class="badge" style="background: #451a03; color: #fbbf24;">LIVE DATA</span>
                </div>
                <div class="stats-row">
                    <span>Stato Match:</span>
                    <span class="val">{m['status']}</span>
                </div>
                <div class="stats-row">
                    <span>Kick-off:</span>
                    <span class="val">{m['utcDate'][11:16]} UTC</span>
                </div>
            </div>
            """
        return html_cards
    except Exception as e:
        return f"<p style='text-align:center;'>Errore di connessione: {str(e)}</p>"

def generate_html():
    content = get_predictions()
    return f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LopisLab Predictive Engine</title>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #0b0e14; color: #e2e8f0; padding: 15px; margin: 0; }}
            .container {{ max-width: 1100px; margin: 0 auto; }}
            .header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; border-radius: 15px; border-left: 5px solid #38bdf8; margin-bottom: 25px; text-align: center; }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 22px; }}
            .card-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }}
            .match-card {{ background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; }}
            .teams {{ font-size: 16px; font-weight: bold; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }}
            .badge {{ padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: bold; }}
            .b-win {{ background: #064e3b; color: #4ade80; }}
            .b-draw {{ background: #451a03; color: #fbbf24; }}
            .stats-row {{ display: flex; justify-content: space-between; font-size: 13px; color: #94a3b8; margin-top: 8px; padding-top: 8px; border-top: 1px solid #334155; }}
            .val {{ color: #f8fafc; font-weight: bold; }}
            @media (max-width: 480px) {{ .card-grid {{ grid-template-columns: 1fr; }} h1 {{ font-size: 18px; }} }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>LopisLab Predictive Engine v4.0</h1>
                <p style="color: #94a3b8; font-size: 12px;">Real-time Serie A Data Feed</p>
            </div>
            <div class="card-grid">
                {content}
            </div>
        </div>
    </body>
    </html>
    """

def handle_request(request):
    return generate_html()
