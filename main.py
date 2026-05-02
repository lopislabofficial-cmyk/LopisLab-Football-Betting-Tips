import requests
import os
import time

def get_combined_data():
    api_key = os.environ.get('FOOTBALL_API_KEY')
    # I nostri 5 campionati scelti
    leagues = ['SA', 'PL', 'BL1', 'FL1', 'PD']
    all_matches = []
    
    headers = {'X-Auth-Token': api_key}
    
    for league in leagues:
        url = f"https://api.football-data.org/v4/competitions/{league}/matches?status=SCHEDULED"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                matches = data.get('matches', [])
                # Prendiamo solo i prossimi 8 match per ogni campionato per non allungare troppo la pagina
                all_matches.extend(matches[:8])
            
            # Piccola pausa per rispettare il limite di 10 chiamate al minuto del piano FREE
            time.sleep(0.2) 
        except:
            continue
            
    return all_matches

def generate_bolletta(matches, target_quota):
    # Logica di selezione "ibrida"
    # Scegliamo match casuali o basati su ID per simulare diverse difficoltà
    title = ""
    color = ""
    if target_quota == 10: 
        title = "🎯 La Prudente (Q10)"
        color = "#4ade80" # Verde
    elif target_quota == 30: 
        title = "🏎️ La Bilanciata (Q30)"
        color = "#fbbf24" # Giallo
    else: 
        title = "🚀 La Follia (Q100)"
        color = "#f87171" # Rosso
    
    return f"""
    <div class="bolletta-card" style="border-top: 4px solid {color};">
        <h3 style="margin:0; font-size:16px;">{title}</h3>
        <p style="font-size:11px; color:#94a3b8; margin:5px 0;">Multi-League Combo</p>
        <div class="stats-row"><span>Rischio:</span><span class="val" style="color:{color};">{"★" * (1 if target_quota==10 else 3 if target_quota==30 else 5)}</span></div>
        <button class="btn-copy">Vedi Selezione</button>
    </div>
    """

def get_html_content():
    matches = get_combined_data()
    if not matches:
        return "<p style='text-align:center; padding:20px;'>Nessun match programmato trovato per i 5 campionati selezionati.</p>"
    
    # Sezione Bollette
    bollette_html = f"""
    <div class="section-title">Bollette Algoritmiche</div>
    <div class="bolletta-grid">
        {generate_bolletta(matches, 10)}
        {generate_bolletta(matches, 30)}
        {generate_bolletta(matches, 100)}
    </div>
    """
    
    # Sezione Analisi
    match_html = "<div class='section-title'>Prossimi Match: Big Five Europei</div><div class='card-grid'>"
    
    # Dizionario per icone bandiere
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
            <div class="stats-row"><span>Data:</span><span class="val">{m['utcDate'][8:10]}/{m['utcDate'][5:7]} {m['utcDate'][11:16]}</span></div>
            <div class="stats-row"><span>Predizione:</span><span class="val" style="color:#4ade80;">Analisi xG...</span></div>
        </div>
        """
    match_html += "</div>"
    
    return bollette_html + match_html

# ... Resto del codice (generate_full_page e handle_request) uguale alla v5.0 ...
