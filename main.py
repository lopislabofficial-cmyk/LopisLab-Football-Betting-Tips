# Creiamo una pagina web semplice (HTML) in inglese
    html = "<html><head><title>LopisLab Football Insights</title></head><body style='font-family:sans-serif;'>"
    html += "<h1>LopisLab - Football Betting Tips</h1>"
    html += "<h2>Upcoming Serie A Matches</h2><table border='1' cellpadding='10' style='border-collapse: collapse; width: 100%;'>"
    html += "<tr style='background-color: #f2f2f2;'><th>Date</th><th>Match</th><th>Prediction</th></tr>"

    for match in matches:
        home = match['homeTeam']['name']
        away = match['awayTeam']['name']
        date = match['utcDate'][:10]
        # 'In Analisi...' diventa 'Analyzing...'
        html += f"<tr><td>{date}</td><td>{home} vs {away}</td><td>Analyzing...</td></tr>"

    html += "</table></body></html>"
