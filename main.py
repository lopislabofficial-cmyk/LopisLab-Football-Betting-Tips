import requests
import os

# Recuperiamo la tua chiave segreta
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
headers = {'X-Auth-Token': API_KEY}

def main():
    try:
        # 1. Recupero dati dalla Serie A
        url = "https://api.football-data.org/v4/competitions/SA/matches?status=SCHEDULED"
        response = requests.get(url, headers=headers)
        data = response.json()

        # Prendiamo le prime 10 partite
        matches = data.get('matches', [])[:10] 

        # 2. Costruzione della pagina HTML con un design professionale
        html = """
        <html>
        <head>
            <title>LopisLab Football Insights</title>
            <style>
                body {
                    font-family: 'Segoe UI', Arial, sans-serif; 
                    background-color: #f4f7f6; 
                    margin: 0; 
                    padding: 40px;
                    color: #333;
                }
                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    background: white;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
                }
                h1 {
                    color: #1a2a6c;
                    border-bottom: 2px solid #1a2a6c;
                    padding-bottom: 10px;
                    margin-bottom: 5px;
                }
                h2 {
                    color: #555;
                    font-weight: 400;
                    margin-bottom: 30px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th {
                    background-color: #1a2a6c;
                    color: white;
                    text-transform: uppercase;
                    font-size: 12px;
                    letter-spacing: 1px;
                    padding: 15px;
                    text-align: left;
                }
                td {
                    padding: 15px;
                    border-bottom: 1px solid #eee;
                }
                tr:hover {
                    background-color: #f9f9f9;
                }
                .prediction {
                    font-weight: bold;
                    color: #27ae60;
                }
                .footer {
                    margin-top: 20px;
                    font-size: 12px;
                    color: #999;
                    text-align: right;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>LopisLab - Football Betting Tips</h1>
                <h2>Upcoming Serie A Matches</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Match</th>
                            <th>Prediction</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        if not matches:
            html += "<tr><td colspan='3' style='text-align:center;'>No matches scheduled at the moment.</td></tr>"

        # 3. Ciclo per ogni partita
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            date = match['utcDate'][:10]
            
            # Qui applicheremo la formula di Poisson. 
            # Per ora usiamo un'indicazione basata sull'ID squadra (temporaneo)
            if (match['homeTeam']['id'] % 2 == 0):
                prediction = "1X (High Prob.)"
            else:
                prediction = "X2 (Medium Prob.)"
            
            html += f"""
                <tr>
                    <td>{date}</td>
                    <td>{home_team} vs {away_team}</td>
                    <td class="prediction">{prediction}</td>
                </tr>
            """

        # 4. Chiusura HTML
        html += f"""
                    </tbody>
                </table>
                <div class="footer">
                    Last Update: {date if matches else 'N/A'} | Powered by LopisLab Algorithm
                </div>
            </div>
        </body>
        </html>
        """

        # Scrittura del file index.html
        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html)
        print("Success: Professional index.html generated!")

    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    main()
