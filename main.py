import requests
import os
import time

def get_combined_data():
    api_key = os.environ.get('FOOTBALL_API_KEY')
    # I nostri 5 campionati: Italia, Inghilterra, Germania, Francia, Spagna
    leagues = ['SA', 'PL', 'BL1', 'FL1', 'PD']
    all_matches = []
    
    headers = {'X-Auth-Token': api_key}
    
    for league in leagues:
        # Cerchiamo solo i match programmati (SCHEDULED)
        url = f"https://api.football-data.org/v4/competitions/{league}/matches?status=SCHEDULED"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                matches = data.get('matches', [])
                # Prendiamo i primi 6 match per ogni lega per non appesantire
                all_matches.extend(matches[:6])
            
            # Pausa tecnica per rispettare i limiti del piano Free (10 chiamate/min)
            time.sleep(0.5) 
        except:
            continue
            
    return all_matches

def generate_bolletta(target_quota):
    title = ""
    color = ""
    if target_quota == 10: 
        title = "🎯 La Prudente (Q10)"
        color = "#4ade80"
    elif target_quota == 30: 
        title = "🏎️ La Bilanciata (Q30)"
        color = "#fbbf24"
    else: 
        title = "🚀 La Follia (Q100)"
        color = "#f87171"
    
    return f"""
    <div class="bolletta-card" style="border-top: 4px solid {color};">
        <h3 style="margin:0; font-size:16px;">{title}</h3>
        <p style="font-size:11px; color:#94a3b8; margin:5px 0;">Algoritmo LopisLab</p>
        <div class="stats-row"><span>Rischio:</span><span class="val" style="color:{color};">{"★" * (1 if target_quota==10 else 3 if target_quota==30 else 5)}</span></div>
        <button class="btn-copy">Vedi Selezione</button>
    </div>
    """

def get_html_content():
    matches = get_combined_data()
    if not matches:
        return "<p style='text-align:center; padding:40px; color:#94a3b8;'>Nessun match trovato per i campionati selezionati. Controlla se ci sono pause nazionali.</p>"
    
    bollette_html = f"""
    <div class="section-title">Bollette Suggerite</div>
    <div class="bolletta-grid">
        {generate_bolletta(10)}
        {generate_bolletta(30)}
        {generate_bolletta(100)}
    </div>
    """
    
    match_html = "<div class='section-title'>Analisi Big Five (SA, PL, BL1, FL1, PD)</div><div class='card-grid'>"
    
    flags = {{'SA': '🇮🇹', 'PL': '🏴󠁧󠁢󠁥󠁮󠁧󠁿', 'BL1': '🇩🇪', 'FL1': '🇫🇷', 'PD': '🇪🇸'}}
    
    for m in matches:
        home = m['homeTeam']['shortName'] or m['homeTeam']['name']
        away = m['awayTeam']['shortName'] or m['awayTeam']['name']
        l_code = m['competition']['code']
        flag = flags.get(l_code, '⚽')
        
        match_html += f"""
        <div class="match-card">
            <div style="font-size:11px; color:#38bdf8; margin-bottom:8px; font-weight:bold;">{flag} {m['competition']['name']}</div>
            <div class="teams">
                <span style="flex:1;">{home}</span>
                <span style="color:#64748b; margin:0 5px;">-</span>
                <span style="flex:1; text-align:right;">{away}</span>
            </div>
            <div class="stats-row"><span>Inizio:</span><span class="val">{m['utcDate'][8:10]}/{m['utcDate'][5:7]} {m['utcDate'][11:16]} UTC</span></div>
            <div class="stats-row"><span>Predizione:</span><span class="val" style="color:#4ade80;">Calcolo in corso...</span></div>
        </div>
        """
    match_html += "</div>"
    
    return bollette_html + match_html

def generate_full_page():
    content = get_html_content()
    return f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LopisLab Hybrid v5.1</title>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #0b0e14; color: #e2e8f0; padding: 15px; margin: 0; }}
            .container {{ max-width: 1100px; margin: 0 auto; }}
            .header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 25px; border-radius: 15px; border-left: 5px solid #38bdf8; margin-bottom: 25px; text-align: center; }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }}
            .section-title {{ font-weight: bold; margin: 30px 0 15px; font-size: 18px; border-bottom: 2px solid #334155; padding-bottom: 8px; color: #38bdf8; }}
            .bolletta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-bottom: 30px; }}
            .bolletta-card {{ background: #1e293b; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
            .btn-copy {{ width: 100%; margin-top: 15px; background: #38bdf8; border: none; padding: 10px; border-radius: 6px; font-weight: bold; color: #0f172a; cursor: pointer; }}
            .card-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }}
            .match-card {{ background: #1e293b; padding: 18px; border-radius: 12px; border: 1px solid #334155; transition: transform 0.2s; }}
            .match-card:hover {{ transform: translateY(-3px); border-color: #38bdf8; }}
            .teams {{ font-size: 16px; font-weight: bold; display: flex; justify-content: space-between; margin-bottom: 12px; }}
            .stats-row {{ display: flex; justify-content: space-between; font-size: 13px; margin-top: 6px; color: #94a3b8; }}
            .val {{ font-weight: bold; color: #f8fafc; }}
            @media (max-width: 480px) {{ .bolletta-grid {{ grid-template-columns: 1fr; }} .header {{ padding: 15px; }} h1 {{ font-size: 20px; }} }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>LopisLab Predictive Engine</h1>
                <p style="color:#94a3b8; font-size:13px; margin-top:5px;">Big Five European Leagues Live Analytics</p>
            </div>
            {content}
        </div>
    </body>
    </html>
    """

def handle_request(request):
    return generate_full_page()
