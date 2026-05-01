import math

def calculate_poisson(lambda_val, k):
    return (math.exp(-lambda_val) * (lambda_val**k)) / math.factorial(k)

def get_predictions():
    # Dati di esempio (Il tuo script caricherà i dati reali)
    matches = [
        {"home": "AC Pisa 1909", "away": "US Lecce", "home_xg": 0.8, "away_xg": 1.2},
        {"home": "Como 1907", "away": "SSC Napoli", "home_xg": 1.4, "away_xg": 1.0},
        {"home": "Juventus FC", "away": "Hellas Verona", "home_xg": 2.3, "away_xg": 0.5},
        {"home": "Inter Milano", "away": "Parma Calcio", "home_xg": 2.1, "away_xg": 0.7}
    ]
    
    html_cards = ""
    for m in matches:
        res = "1X" if m['home_xg'] >= m['away_xg'] else "X2"
        res_class = "b-win" if res == "1X" else "b-draw"

        html_cards += f"""
        <div class="match-card">
            <div class="teams">
                <span>{m['home']}</span>
                <span style="color: #64748b; font-size: 12px;">vs</span>
                <span>{m['away']}</span>
            </div>
            <div style="display: flex; gap: 10px; margin-bottom: 15px;">
                <span class="badge {res_class}">{res}</span>
                <span class="badge" style="background: #451a03; color: #fbbf24;">xG: {m['home_xg']} - {m['away_xg']}</span>
            </div>
            <div class="stats-row">
                <span>Probabilità Goal:</span>
                <span class="val">48.5%</span>
            </div>
            <div class="stats-row">
                <span>Under 2.5:</span>
                <span class="val">56.2%</span>
            </div>
        </div>
        """
    return html_cards

def generate_html():
    content = get_predictions()
    # NOTA: Le doppie graffe {{ }} servono a Python per non andare in errore nel CSS
    return f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LopisLab Predictive Engine</title>
        <style>
            body {{ 
                font-family: 'Inter', sans-serif; 
                background: #0b0e14; 
                color: #e2e8f0; 
                padding: 15px; 
                margin: 0;
            }}
            .container {{ max-width: 1100px; margin: 0 auto; }}
            .header {{ 
                background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                padding: 20px; 
                border-radius: 15px; 
                border-left: 5px solid #38bdf8; 
                margin-bottom: 25px; 
                text-align: center;
            }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 22px; }}
            
            .card-grid {{ 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 15px; 
            }}
            
            .match-card {{ 
                background: #1e293b; 
                padding: 20px; 
                border-radius: 15px; 
                border: 1px solid #334155; 
            }}
            
            .teams {{ 
                font-size: 16px; 
                font-weight: bold; 
                margin-bottom: 12px; 
                display: flex; 
                justify-content: space-between;
                align-items: center;
            }}
            
            .badge {{ padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: bold; }}
            .b-win {{ background: #064e3b; color: #4ade80; }}
            .b-draw {{ background: #451a03; color: #fbbf24; }}
            
            .stats-row {{ 
                display: flex; 
                justify-content: space-between; 
                font-size: 13px; 
                color: #94a3b8; 
                margin-top: 8px; 
                padding-top: 8px; 
                border-top: 1px solid #334155; 
            }}
            .val {{ color: #f8fafc; font-weight: bold; }}

            @media (max-width: 480px) {{
                .card-grid {{ grid-template-columns: 1fr; }}
                h1 {{ font-size: 18px; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>LopisLab Predictive Engine v3.1</h1>
                <p style="color: #94a3b8; font-size: 12px;">Poisson Analytics</p>
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
