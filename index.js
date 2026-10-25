export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Rotta Sitemap per SEO
    if (url.pathname === '/sitemap.xml') {
      const xml = `<?xml version="1.0" encoding="UTF-8"?>
      <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url><loc>https://lopislab.com/</loc><priority>1.0</priority></url>
      </urlset>`;
      return new Response(xml, { headers: { 'Content-Type': 'application/xml' } });
    }

    // Struttura HTML del sito
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LopisLab Pro Insights - Predictive Football Engine</title>
    <meta name="description" content="Advanced Poisson Analytics & Goal Probability Distribution. Get professional mathematical football predictions, xG statistics and data-driven insights.">
    <style>
        body { font-family: 'Inter', -apple-system, sans-serif; background: #0b0e14; color: #e2e8f0; padding: 30px; line-height: 1.6; }
        .container { max-width: 1100px; margin: 0 auto; }
        .header { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 30px; border-radius: 20px; border-left: 5px solid #38bdf8; margin-bottom: 30px; }
        h1 { color: #38bdf8; margin: 0; font-size: 28px; }
        .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
        .match-link { text-decoration: none; color: inherit; display: block; }
        .match-card { background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; transition: transform 0.2s, border-color 0.2s; height: 100%; box-sizing: border-box; }
        .match-link:hover .match-card { transform: translateY(-5px); border-color: #38bdf8; }
        .teams { font-size: 18px; font-weight: bold; margin-bottom: 15px; display: flex; justify-content: space-between; }
        .badge { padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: bold; text-transform: uppercase; }
        .b-win { background: #064e3b; color: #4ade80; }
        .b-draw { background: #451a03; color: #fbbf24; }
        .stats-row { display: flex; justify-content: space-between; font-size: 13px; color: #94a3b8; margin-top: 10px; padding-top: 10px; border-top: 1px solid #334155; }
        .val { color: #f8fafc; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>LopisLab Predictive Engine v3.0</h1>
            <p>Advanced Poisson Analytics & Goal Probability Distribution</p>
        </div>
        <div class="card-grid">
            <!-- FC Internazionale Milano vs ACF Fiorentina -->
            <a href="/?match_id=fc_internazionale_milano_acf_fiorentina" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Internazionale Milano</span> vs <span>ACF Fiorentina</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">36.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.1%</span></div>
                </div>
            </a>

            <!-- Athletic Club vs Getafe CF -->
            <a href="/?match_id=athletic_club_getafe_cf" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Athletic Club</span> vs <span>Getafe CF</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">48.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">44.1%</span></div>
                </div>
            </a>

            <!-- Hull City AFC vs Brentford FC -->
            <a href="/?match_id=hull_city_afc_brentford_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Hull City AFC</span> vs <span>Brentford FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 1.3</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">36.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">64.7%</span></div>
                </div>
            </a>

            <!-- Genoa CFC vs Venezia FC -->
            <a href="/?match_id=genoa_cfc_venezia_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Genoa CFC</span> vs <span>Venezia FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">41.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.0%</span></div>
                </div>
            </a>

            <!-- Crystal Palace FC vs Newcastle United FC -->
            <a href="/?match_id=crystal_palace_fc_newcastle_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Crystal Palace FC</span> vs <span>Newcastle United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">49.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">48.8%</span></div>
                </div>
            </a>

            <!-- Liverpool FC vs Brighton & Hove Albion FC -->
            <a href="/?match_id=liverpool_fc_brighton___hove_albion_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Liverpool FC</span> vs <span>Brighton & Hove Albion FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">46.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.1%</span></div>
                </div>
            </a>

            <!-- Atalanta BC vs Frosinone Calcio -->
            <a href="/?match_id=atalanta_bc_frosinone_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Atalanta BC</span> vs <span>Frosinone Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 0.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">53.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">62.4%</span></div>
                </div>
            </a>

            <!-- Manchester United FC vs AFC Bournemouth -->
            <a href="/?match_id=manchester_united_fc_afc_bournemouth" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Manchester United FC</span> vs <span>AFC Bournemouth</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.4 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">34.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.5%</span></div>
                </div>
            </a>

            <!-- TSG 1899 Hoffenheim vs Bayer 04 Leverkusen -->
            <a href="/?match_id=tsg_1899_hoffenheim_bayer_04_leverkusen" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>TSG 1899 Hoffenheim</span> vs <span>Bayer 04 Leverkusen</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">62.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">62.7%</span></div>
                </div>
            </a>

            <!-- RC Celta de Vigo vs Real Betis Balompié -->
            <a href="/?match_id=rc_celta_de_vigo_real_betis_balompi_" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RC Celta de Vigo</span> vs <span>Real Betis Balompié</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">51.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.7%</span></div>
                </div>
            </a>

            <!-- SC Freiburg vs FC Bayern München -->
            <a href="/?match_id=sc_freiburg_fc_bayern_m_nchen" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SC Freiburg</span> vs <span>FC Bayern München</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.9 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">48.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.2%</span></div>
                </div>
            </a>

            <!-- Sunderland AFC vs Leeds United FC -->
            <a href="/?match_id=sunderland_afc_leeds_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sunderland AFC</span> vs <span>Leeds United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.9 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">44.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">66.3%</span></div>
                </div>
            </a>
        </div>
    </div>
</body>
</html>`;

    return new Response(html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
  }
};
