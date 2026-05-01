<style>
            body { 
                font-family: 'Inter', -apple-system, sans-serif; 
                background: #0b0e14; 
                color: #e2e8f0; 
                padding: 15px; /* Ridotto per mobile */
                line-height: 1.6; 
            }
            .container { max-width: 1100px; margin: 0 auto; }
            .header { 
                background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                padding: 20px; 
                border-radius: 15px; 
                border-left: 5px solid #38bdf8; 
                margin-bottom: 25px; 
            }
            h1 { color: #38bdf8; margin: 0; font-size: 22px; } /* Leggermente più piccolo */
            
            /* LA MAGIA: Grid che si adatta */
            .card-grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 15px; 
            }
            
            .match-card { 
                background: #1e293b; 
                padding: 20px; 
                border-radius: 15px; 
                border: 1px solid #334155; 
            }
            .teams { 
                font-size: 16px; /* Ottimo per mobile */
                font-weight: bold; 
                margin-bottom: 12px; 
                display: flex; 
                justify-content: space-between;
                flex-wrap: wrap; /* Evita che i nomi lunghi escano fuori */
            }
            .badge { padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: bold; text-transform: uppercase; }
            .b-win { background: #064e3b; color: #4ade80; }
            .b-draw { background: #451a03; color: #fbbf24; }
            .stats-row { 
                display: flex; 
                justify-content: space-between; 
                font-size: 13px; 
                color: #94a3b8; 
                margin-top: 8px; 
                padding-top: 8px; 
                border-top: 1px solid #334155; 
            }
            .val { color: #f8fafc; font-weight: bold; }

            /* Ottimizzazione specifica per schermi molto piccoli */
            @media (max-width: 480px) {
                .teams span { width: 100%; margin-bottom: 5px; }
                h1 { font-size: 18px; }
            }
        </style>
