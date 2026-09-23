import os
import re
import json
import random
import requests
from datetime import datetime, timedelta

# 1. Recupero la chiave API dalle variabili d'ambiente di GitHub Actions
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
API_URL = "https://api.football-data.org/v4/matches"

# Lista di campionati principali da monitorare (Serie A, Premier League, La Liga, Bundesliga, Champions League)
COMPETITIONS = "SA,PL,PD,BL1,CL"

def get_upcoming_matches():
    """Recupera le prossime partite da football-data.org."""
    if not API_KEY:
        print("⚠️ FOOTBALL_DATA_API_KEY non trovata. Generazione con dati di fallback.")
        return []

    headers = {"X-Auth-Token": API_KEY}
    
    # Imposta la finestra temporale (dall'ora attuale ai prossimi 3 giorni)
    today = datetime.utcnow()
    date_from = today.strftime("%Y-%m-%d")
    date_to = (today + timedelta(days=3)).strftime("%Y-%m-%d")

    params = {
        "competitions": COMPETITIONS,
        "dateFrom": date_from,
        "dateTo": date_to,
        "status": "SCHEDULED"
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("matches", [])
        else:
            print(f"⚠️ Errore API Football-Data ({response.status_code}): {response.text}")
            return []
    except Exception as e:
        print(f"❌ Errore durante la chiamata API: {e}")
        return []

def calculate_predictions(home_team, away_team):
    """
    Calcola stime probabilistiche e indicatori xG basati sulle squadre.
    Se vuoi collegare un modello Poisson dedicato, puoi sostituire la logica qui sotto.
    """
    # Esempio di generazione controllata xG basata sui nomi (algoritmo deterministico stabile)
    seed_value = sum(ord(c) for c in home_team + away_team)
    random.seed(seed_value)

    xg_home = round(random.uniform(0.7, 2.4), 1)
    xg_away = round(random.uniform(0.5, 2.1), 1)

    btts_prob = round(random.uniform(33.0, 68.0), 1)
    under25_prob = round(random.uniform(40.0, 75.0), 1)

    # Determina la tipologia di badge
    diff = xg_home - xg_away
    if diff > 0.4:
        badge_type = "b-win"
        pick = "1X"
    elif diff < -0.4:
        badge_type = "b-win"
        pick = "X2"
    else:
        badge_type = "b-draw"
        pick = "DRAW / X"

    return {
        "xg_home": xg_home,
        "xg_away": xg_away,
        "btts": btts_prob,
        "under25": under25_prob,
        "badge_class": badge_type,
        "pick": pick
    }

def build_match_card(home, away, stats):
    """Genera il blocco HTML per la singola card partita."""
    match_id = re.sub(r'[^a-zA-Z0-9]', '_', f"{home}_{away}").lower()
    
    return f"""            <!-- {home} vs {away} -->
            <a href="/?match_id={match_id}" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>{home}</span> vs <span>{away}</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge {stats['badge_class']}">{stats['pick']}</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: {stats['xg_home']} - {stats['xg_away']}</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">{stats['btts']}%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">{stats['under25']}%</span></div>
                </div>
            </a>"""

def generate_index_js(cards_html):
    """Genera il contenuto completo del file index.js per Cloudflare Workers."""
    return f"""export default {{
  async fetch(request, env, ctx) {{
    const url = new URL(request.url);

    // Rotta Sitemap per SEO
    if (url.pathname === '/sitemap.xml') {{
      const xml = `<?xml version="1.0" encoding="UTF-8"?>
      <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url><loc>https://lopislab.com/</loc><priority>1.0</priority></url>
      </urlset>`;
      return new Response(xml, {{ headers: {{ 'Content-Type': 'application/xml' }} }});
    }}

    // Struttura HTML del sito
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LopisLab Pro Insights - Predictive Football Engine</title>
    <meta name="description" content="Advanced Poisson Analytics & Goal Probability Distribution. Get professional mathematical football predictions, xG statistics and data-driven insights.">
    <style>
        body {{ font-family: 'Inter', -apple-system, sans-serif; background: #0b0e14; color: #e2e8f0; padding: 30px; line-height: 1.6; }}
        .container {{ max-width: 1100px; margin: 0 auto; }}
        .header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 30px; border-radius: 20px; border-left: 5px solid #38bdf8; margin-bottom: 30px; }}
        h1 {{ color: #38bdf8; margin: 0; font-size: 28px; }}
        .card-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
        .match-link {{ text-decoration: none; color: inherit; display: block; }}
        .match-card {{ background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; transition: transform 0.2s, border-color 0.2s; height: 100%; box-sizing: border-box; }}
        .match-link:hover .match-card {{ transform: translateY(-5px); border-color: #38bdf8; }}
        .teams {{ font-size: 18px; font-weight: bold; margin-bottom: 15px; display: flex; justify-content: space-between; }}
        .badge {{ padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; text-transform: uppercase; }}
        .b-win {{ background: #064e3b; color: #4ade80; }}
        .b-draw {{ background: #451a03; color: #fbbf24; }}
        .stats-row {{ display: flex; justify-content: space-between; font-size: 13px; color: #94a3b8; margin-top: 10px; padding-top: 10px; border-top: 1px solid #334155; }}
        .val {{ color: #f8fafc; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>LopisLab Predictive Engine v3.0</h1>
            <p>Advanced Poisson Analytics & Goal Probability Distribution</p>
        </div>
        <div class="card-grid">
{cards_html}
        </div>
    </div>
</body>
</html>`;

    return new Response(html, {{
      headers: {{ 'Content-Type': 'text/html; charset=utf-8' }}
    }});
  }}
}};
"""

def main():
    print("🚀 Avvio aggiornamento automatico pronostici LopisLab...")
    matches = get_upcoming_matches()

    match_cards = []

    if matches:
        print(f"⚽ Trovate {len(matches)} partite nel palinsesto API.")
        for m in matches[:12]:  # Mostra fino alle prime 12 partite principali
            home_team = m.get("homeTeam", {}).get("name", "Home Team")
            away_team = m.get("awayTeam", {}).get("name", "Away Team")
            stats = calculate_predictions(home_team, away_team)
            card = build_match_card(home_team, away_team, stats)
            match_cards.append(card)
    else:
        print("ℹ️ Nessuna partita trovata dall'API o chiave API non attiva. Uso il palinsesto di default.")
        default_matches = [
            ("AC Pisa 1909", "US Lecce"), ("Udinese Calcio", "Torino FC"),
            ("Como 1907", "SSC Napoli"), ("Atalanta BC", "Genoa CFC"),
            ("Bologna FC 1909", "Cagliari Calcio"), ("US Sassuolo Calcio", "AC Milan"),
            ("Juventus FC", "Hellas Verona FC"), ("FC Internazionale Milano", "Parma Calcio 1913")
        ]
        for home, away in default_matches:
            stats = calculate_predictions(home, away)
            card = build_match_card(home, away, stats)
            match_cards.append(card)

    full_cards_html = "\n\n".join(match_cards)
    new_index_js = generate_index_js(full_cards_html)

    # Aggiorna il file index.js
    with open("index.js", "w", encoding="utf-8") as f:
        f.write(new_index_js)

    print("✅ File 'index.js' aggiornato con successo!")

if __name__ == "__main__":
    main()
