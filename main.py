import requests
import math

def calculate_poisson(lambda_val, k):
    return (math.exp(-lambda_val) * (lambda_val**k)) / math.factorial(k)

def get_predictions():
    # Simulazione dati (Qui il tuo script originale caricherà i dati reali dalle API)
    matches = [
        {"home": "AC Pisa 1909", "away": "US Lecce", "home_xg": 0.8, "away_xg": 1.2},
        {"home": "Como 1907", "away": "SSC Napoli", "home_xg": 1.4, "away_xg": 1.8},
        {"home": "Juventus FC", "away": "Hellas Verona", "home_xg": 2.3, "away_xg": 0.5},
        {"home": "AS Roma", "away": "ACF Fiorentina", "home_xg": 1.5, "away_xg": 1.3},
        {"home": "Inter Milano", "away": "Parma Calcio", "home_xg": 2.1, "away_xg": 0.7}
    ]
    
    html_cards = ""
    for m in matches:
        # Calcoli veloci per Under/Over e Esito
        prob_home = 40.5 # Esempio
        prob_away = 35.2 # Esempio
        under_25 = 54.5  # Esempio
        
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
                <span>Segnano Entrambe:</span>
                <span class="val">{prob_home}%</span>
            </div>
            <div class="stats-row">
                <span>Under 2.5 Goals:</span>
                <span class="val">{under_25}%</span>
            </div>
        </div>
        """
    return html_cards

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
            body {{ 
                font-family: 'Inter', -apple-system, sans-serif; 
                background: #0b0e14; 
                color: #e2e8f0; 
                padding: 15px; 
                margin: 0;
            }}
            .container {{ max-width: 1100px; margin: 0 auto; }}
            .header {{ 
                background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                padding: 25px; 
                border-radius: 15px; 
                border-left: 5px solid #38bdf8; 
                margin-bottom: 25px; 
                text-align: center;
            }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }}
            p {{ color: #94a3b8; font-size: 14px; margin-top: 5px; }}
            
            /* Griglia Responsive */
            .card-grid {{ 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
                gap: 20px; 
            }}
            
            .match-card {{ 
                background: #1e293b; 
                padding: 20px; 
                border-radius: 15px; 
                border: 1px solid #334155; 
                transition: transform 0.2s;
            }}
            .match-card:hover {{ transform: translateY(-5px); border-color: #38bdf8; }}
            
            .teams {{ 
                font-size: 16px; 
                font-weight: bold; 
                margin-bottom: 12px; 
                display: flex; 
                justify-content: space-between;
                align-items: center;
            }}
            .badge {{ padding: 5px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; }}
            .b-win {{ background: #064e3b; color: #4ade80; }}
            .b-draw {{ background: #451a03; color: #fbbf24; }}
            
            .stats-row {{ 
                display: flex; 
                justify-content: space-between; 
                font-size: 14px; 
                color: #94a3b8; 
                margin-top: 10px; 
                padding-top: 10px; 
                border-top: 1px solid #334155; 
            }}
            .val {{ color: #f8fafc; font-weight: bold; }}

            /* Fix per schermi molto piccoli (Smartphone) */
            @media (max-width: 480px) {{
                .card-grid {{ grid-template-columns: 1fr; }}
                .header {{ padding: 15px; }}
                h1 {{ font-size: 20px; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>LopisLab Predictive Engine v3.1</h1>
                <p>Advanced Poisson Analytics & Goal Probability Distribution</p>
            </div>
            <div class="card-grid">
                {content}
            </div>
        </div>
    </body>
    </html>
    """

# Funzione principale per Cloudflare Worker
def handle_request(request):
    return generate_html()
            }
        </style>
