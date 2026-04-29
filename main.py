import requests
import os
import math

# API Setup
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def get_data(endpoint):
    url = f"https://api.football-data.org/v4/competitions/SA/{endpoint}"
    return requests.get(url, headers=headers).json()

def poisson_prob(k, lamb):
    """Calcola la probabilità di segnare esattamente k gol con una media lamb."""
    return (math.pow(lamb, k) * math.exp(-lamb)) / math.factorial(k)

def main():
    try:
        # 1. Recupero dati
        standings_data = get_data("standings")
        matches_data = get_data("matches?status=SCHEDULED")
        
        table = standings_data['standings'][0]['table']
        played = table[0]['playedGames']
        total_g = sum(t['goalsFor'] + t['goalsAgainst'] for t in table) / 2
        l_avg = total_g / (len(table) * played)

        teams = {t['team']['name']: {
            'att': (t['goalsFor'] / played) / l_avg,
            'def': (t['goalsAgainst'] / played) / l_avg
        } for t in table}

        matches = matches_data.get('matches', [])[:12]

        # 2. HTML Design (Professional Dark Mode)
        html = """
        <html><head><title>LopisLab Pro Insights</title>
        <style>
            body { font-family: 'Inter', -apple-system, sans-serif; background: #0b0e14; color: #e2e8f0; padding: 30px; line-height: 1.6; }
            .container { max-width: 1100px; margin: 0 auto; }
            .header { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 30px; border-radius: 20px; border-left: 5px solid #38bdf8; margin-bottom: 30px; }
            h1 { color: #38bdf8; margin: 0; font-size: 28px; }
            .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
            .match-card { background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; transition: transform 0.2s; }
            .match-card:hover { transform: translateY(-5px); border-color: #38bdf8; }
            .teams { font-size: 18px; font-weight: bold; margin-bottom: 15px; display: flex; justify-content: space-between; }
            .badge { padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; text-transform: uppercase; }
            .b-win { background: #064e3b; color: #4ade80; }
            .b-draw { background: #451a03; color: #fbbf24; }
            .stats-row { display: flex; justify-content: space-between; font-size: 13px; color: #94a3b8; margin-top: 10px; padding-top: 10px; border-top: 1px solid #334155; }
            .val { color: #f8fafc; font-weight: bold; }
        </style></head><body>
        <div class="container">
            <div class="header">
                <h1>LopisLab Predictive Engine v3.0</h1>
                <p>Advanced Poisson Analytics & Goal Probability Distribution</p>
            </div>
            <div class="card-grid">
        """

        for m in matches:
            h, a = m['homeTeam']['name'], m['awayTeam']['name']
            h_s, a_s = teams.get(h, {'att':1,'def':1}), teams.get(a, {'att':1,'def':1})
            
            # xG (Expected Goals)
            h_xg, a_xg = h_s['att'] * a_s['def'] * l_avg, a_s['att'] * h_s['def'] * l_avg
            
            # Probabilità Under 2.5 (Somma di 0-0, 1-0, 0-1, 1-1, 2-0, 0-2)
            p_under = 0
            for i in range(3):
                for j in range(3):
                    if i + j < 2.5:
                        p_under += poisson_prob(i, h_xg) * poisson_prob(j, a_xg)
            
            # Probabilità BTTS (Both Teams To Score)
            p_btts = (1 - poisson_prob(0, h_xg)) * (1 - poisson_prob(0, a_xg))
            
            tip = "1X" if h_xg > a_xg else "X2"
            if abs(h_xg - a_xg) < 0.3: tip = "DRAW / X"

            html += f"""
                <div class="match-card">
                    <div class="teams"><span>{h}</span> vs <span>{a}</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">{tip}</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: {h_xg:.1f} - {a_xg:.1f}</span>
                    </div>
                    <div class="stats-row">
                        <span>Both Teams to Score:</span> <span class="val">{p_btts*100:.1f}%</span>
                    </div>
                    <div class="stats-row">
                        <span>Under 2.5 Goals:</span> <span class="val">{p_under*100:.1f}%</span>
                    </div>
                </div>
            """

        html += "</div></div></body></html>"

        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html)
        print("V3.0 Deploy Success!")

    except Exception as e:
        print(f"Error: {e}"); exit(1)

if __name__ == "__main__":
    main()
