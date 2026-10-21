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
            <!-- Lille OSC vs Galatasaray SK -->
            <a href="/?match_id=lille_osc_galatasaray_sk" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Lille OSC</span> vs <span>Galatasaray SK</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">39.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.0%</span></div>
                </div>
            </a>

            <!-- Como 1907 vs Manchester United FC -->
            <a href="/?match_id=como_1907_manchester_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Como 1907</span> vs <span>Manchester United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">66.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">45.0%</span></div>
                </div>
            </a>

            <!-- Levante UD vs Athletic Club -->
            <a href="/?match_id=levante_ud_athletic_club" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Levante UD</span> vs <span>Athletic Club</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">62.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.1%</span></div>
                </div>
            </a>

            <!-- Club Brugge KV vs Racing Club de Lens -->
            <a href="/?match_id=club_brugge_kv_racing_club_de_lens" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Club Brugge KV</span> vs <span>Racing Club de Lens</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">36.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.7%</span></div>
                </div>
            </a>

            <!-- Sporting Clube de Portugal vs LASK Linz -->
            <a href="/?match_id=sporting_clube_de_portugal_lask_linz" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sporting Clube de Portugal</span> vs <span>LASK Linz</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">50.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.9%</span></div>
                </div>
            </a>

            <!-- FC Internazionale Milano vs FK Shakhtar Donetsk -->
            <a href="/?match_id=fc_internazionale_milano_fk_shakhtar_donetsk" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Internazionale Milano</span> vs <span>FK Shakhtar Donetsk</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.4 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.8%</span></div>
                </div>
            </a>

            <!-- FC Bayern München vs Arsenal FC -->
            <a href="/?match_id=fc_bayern_m_nchen_arsenal_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Bayern München</span> vs <span>Arsenal FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.4 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">40.7%</span></div>
                </div>
            </a>

            <!-- Aston Villa FC vs Viking FK -->
            <a href="/?match_id=aston_villa_fc_viking_fk" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Aston Villa FC</span> vs <span>Viking FK</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">67.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">44.6%</span></div>
                </div>
            </a>

            <!-- Real Madrid CF vs RB Leipzig -->
            <a href="/?match_id=real_madrid_cf_rb_leipzig" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Madrid CF</span> vs <span>RB Leipzig</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">42.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.8%</span></div>
                </div>
            </a>

            <!-- Real Betis Balompié vs Feyenoord Rotterdam -->
            <a href="/?match_id=real_betis_balompi__feyenoord_rotterdam" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Betis Balompié</span> vs <span>Feyenoord Rotterdam</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">41.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">57.7%</span></div>
                </div>
            </a>

            <!-- VfB Stuttgart vs Borussia Mönchengladbach -->
            <a href="/?match_id=vfb_stuttgart_borussia_m_nchengladbach" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>VfB Stuttgart</span> vs <span>Borussia Mönchengladbach</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.2 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.7%</span></div>
                </div>
            </a>

            <!-- Torino FC vs AC Monza -->
            <a href="/?match_id=torino_fc_ac_monza" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Torino FC</span> vs <span>AC Monza</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.8%</span></div>
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
