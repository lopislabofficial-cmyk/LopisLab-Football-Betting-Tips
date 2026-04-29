import requests
import os
import math

# Configurazione API
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def get_data(endpoint):
    url = f"https://api.football-data.org/v4/competitions/SA/{endpoint}"
    return requests.get(url, headers=headers).json()

def poisson(actual, mean):
    """Calcola la probabilità statistica di un evento."""
    return (math.pow(mean, actual) * math.exp(-mean)) / math.factorial(actual)

def main():
    try:
        # 1. Recupero dati Classifica e Partite
        standings_data = get_data("standings")
        matches_data = get_data("matches?status=SCHEDULED")
        
        table = standings_data['standings'][0]['table']
        played_games = table[0]['playedGames']
        
        # Calcoliamo la media gol del campionato (League Average)
        total_goals = sum(t['goalsFor'] + t['goalsAgainst'] for t in table) / 2
        league_avg_goals = total_goals / (len(table) * played_games)

        # Creiamo il database delle squadre
        teams = {}
        for t in table:
            teams[t['team']['name']] = {
                'att': (t['goalsFor'] / played_games) / league_avg_goals,
                'def': (t['goalsAgainst'] / played_games) / league_avg_goals
            }

        matches = matches_data.get('matches', [])[:10]

        # 2. Design della Pagina (Ancora più professionale)
        html = """
        <html><head><title>LopisLab Quant Engine</title>
        <style>
            body { font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }
            .container { max-width: 950px; margin: 0 auto; background: #1e293b; padding: 30px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); }
            h1 { color: #38bdf8; font-size: 28px; margin-bottom: 5px; }
            p { color: #94a3b8; margin-bottom: 30px; }
            table { width: 100%; border-collapse: collapse; }
            th { text-align: left; padding: 15px; color: #38bdf8; border-bottom: 2px solid #334155; font-size: 12px; text-transform: uppercase; }
            td { padding: 18px 15px; border-bottom: 1px solid #334155; font-size: 14px; }
            .score-tag { background: #38bdf8; color: #0f172a; padding: 4px 8px; border-radius: 4px; font-weight: bold; margin-right: 10px; }
            .prob-high { color: #4ade80; font-weight: bold; }
            .prob-med { color: #fbbf24; }
        </style></head><body>
        <div class="container">
            <h1>LopisLab Quant Engine v2.0</h1>
            <p>Predictive analytics based on Poisson Distribution and League Scoring Averages.</p>
            <table>
                <tr><th>Match</th><th>Predicted Score</th><th>Betting Tip</th><th>AI Confidence</th></tr>
        """

        for m in matches:
            h_name = m['homeTeam']['name']
            a_name = m['awayTeam']['name']
            
            # Calcolo Forza Attacco vs Difesa
            h_stats = teams.get(h_name, {'att': 1, 'def': 1})
            a_stats = teams.get(a_name, {'att': 1, 'def': 1})

            # Gol Attesi (xG)
            h_xg = h_stats['att'] * a_stats['def'] * league_avg_goals
            a_xg = a_stats['att'] * h_stats['def'] * league_avg_goals

            # Risultato più probabile (arrotondato)
            pred_score = f"{round(h_xg)} - {round(a_xg)}"
            
            # Tipologia di giocata
            if h_xg > a_xg + 0.5: tip, conf = "1", "High"
            elif a_xg > h_xg + 0.5: tip, conf = "2", "High"
            else: tip, conf = "X / GG", "Medium"

            conf_class = "prob-high" if conf == "High" else "prob-med"

            html += f"""
                <tr>
                    <td><b>{h_name}</b> vs {a_name}</td>
                    <td><span class='score-tag'>{pred_score}</span></td>
                    <td>{tip}</td>
                    <td class='{conf_class}'>{conf}</td>
                </tr>
            """

        html += f"</table><div style='margin-top:30px; font-size:11px; color:#64748b;'>Last Deep Analysis: {m['utcDate'][:10]}</div></div></body></html>"

        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html)
        print("Success: Quant Analysis Complete!")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
