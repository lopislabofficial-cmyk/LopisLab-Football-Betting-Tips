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
            <!-- Hull City AFC vs Everton FC -->
            <a href="/?match_id=hull_city_afc_everton_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Hull City AFC</span> vs <span>Everton FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 0.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">54.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.6%</span></div>
                </div>
            </a>

            <!-- US Lecce vs Bologna FC 1909 -->
            <a href="/?match_id=us_lecce_bologna_fc_1909" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>US Lecce</span> vs <span>Bologna FC 1909</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">60.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">72.0%</span></div>
                </div>
            </a>

            <!-- SS Lazio vs AC Monza -->
            <a href="/?match_id=ss_lazio_ac_monza" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SS Lazio</span> vs <span>AC Monza</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 0.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">53.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.0%</span></div>
                </div>
            </a>

            <!-- Crystal Palace FC vs Nottingham Forest FC -->
            <a href="/?match_id=crystal_palace_fc_nottingham_forest_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Crystal Palace FC</span> vs <span>Nottingham Forest FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">51.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">64.9%</span></div>
                </div>
            </a>

            <!-- 1. FC Köln vs Borussia Mönchengladbach -->
            <a href="/?match_id=1__fc_k_ln_borussia_m_nchengladbach" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>1. FC Köln</span> vs <span>Borussia Mönchengladbach</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.4 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">45.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">69.2%</span></div>
                </div>
            </a>

            <!-- Real Sociedad de Fútbol vs RC Deportivo La Coruña -->
            <a href="/?match_id=real_sociedad_de_f_tbol_rc_deportivo_la_coru_a" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Sociedad de Fútbol</span> vs <span>RC Deportivo La Coruña</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.2 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">35.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">64.0%</span></div>
                </div>
            </a>

            <!-- SC Freiburg vs FC Schalke 04 -->
            <a href="/?match_id=sc_freiburg_fc_schalke_04" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SC Freiburg</span> vs <span>FC Schalke 04</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">40.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">53.0%</span></div>
                </div>
            </a>

            <!-- Liverpool FC vs Manchester City FC -->
            <a href="/?match_id=liverpool_fc_manchester_city_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Liverpool FC</span> vs <span>Manchester City FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">53.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">53.8%</span></div>
                </div>
            </a>

            <!-- US Sassuolo Calcio vs AC Milan -->
            <a href="/?match_id=us_sassuolo_calcio_ac_milan" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>US Sassuolo Calcio</span> vs <span>AC Milan</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">47.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">62.1%</span></div>
                </div>
            </a>

            <!-- Real Betis Balompié vs CA Osasuna -->
            <a href="/?match_id=real_betis_balompi__ca_osasuna" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Betis Balompié</span> vs <span>CA Osasuna</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">56.4%</span></div>
                </div>
            </a>

            <!-- Cagliari Calcio vs Juventus FC -->
            <a href="/?match_id=cagliari_calcio_juventus_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Cagliari Calcio</span> vs <span>Juventus FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">34.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">58.9%</span></div>
                </div>
            </a>

            <!-- Real Racing Club de Santander vs Valencia CF -->
            <a href="/?match_id=real_racing_club_de_santander_valencia_cf" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Racing Club de Santander</span> vs <span>Valencia CF</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 0.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">65.1%</span></div>
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
