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
            <!-- Eintracht Frankfurt vs 1. FC Köln -->
            <a href="/?match_id=eintracht_frankfurt_1__fc_k_ln" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Eintracht Frankfurt</span> vs <span>1. FC Köln</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 2.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">50.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">48.4%</span></div>
                </div>
            </a>

            <!-- Frosinone Calcio vs US Sassuolo Calcio -->
            <a href="/?match_id=frosinone_calcio_us_sassuolo_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Frosinone Calcio</span> vs <span>US Sassuolo Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">59.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">62.1%</span></div>
                </div>
            </a>

            <!-- RC Deportivo La Coruña vs Levante UD -->
            <a href="/?match_id=rc_deportivo_la_coru_a_levante_ud" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RC Deportivo La Coruña</span> vs <span>Levante UD</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">60.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">47.1%</span></div>
                </div>
            </a>

            <!-- Everton FC vs Chelsea FC -->
            <a href="/?match_id=everton_fc_chelsea_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Everton FC</span> vs <span>Chelsea FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">74.4%</span></div>
                </div>
            </a>

            <!-- RCD Espanyol de Barcelona vs Club Atlético de Madrid -->
            <a href="/?match_id=rcd_espanyol_de_barcelona_club_atl_tico_de_madrid" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RCD Espanyol de Barcelona</span> vs <span>Club Atlético de Madrid</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">57.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.1%</span></div>
                </div>
            </a>

            <!-- Venezia FC vs SSC Napoli -->
            <a href="/?match_id=venezia_fc_ssc_napoli" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Venezia FC</span> vs <span>SSC Napoli</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">50.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.9%</span></div>
                </div>
            </a>

            <!-- FC Schalke 04 vs 1. FSV Mainz 05 -->
            <a href="/?match_id=fc_schalke_04_1__fsv_mainz_05" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Schalke 04</span> vs <span>1. FSV Mainz 05</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">41.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">45.3%</span></div>
                </div>
            </a>

            <!-- SV Werder Bremen vs SC Paderborn 07 -->
            <a href="/?match_id=sv_werder_bremen_sc_paderborn_07" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SV Werder Bremen</span> vs <span>SC Paderborn 07</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">43.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.5%</span></div>
                </div>
            </a>

            <!-- 1. FC Union Berlin vs Borussia Dortmund -->
            <a href="/?match_id=1__fc_union_berlin_borussia_dortmund" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>1. FC Union Berlin</span> vs <span>Borussia Dortmund</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.4 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">45.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">73.3%</span></div>
                </div>
            </a>

            <!-- Hamburger SV vs VfB Stuttgart -->
            <a href="/?match_id=hamburger_sv_vfb_stuttgart" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Hamburger SV</span> vs <span>VfB Stuttgart</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">54.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.6%</span></div>
                </div>
            </a>

            <!-- SV 07 Elversberg vs FC Augsburg -->
            <a href="/?match_id=sv_07_elversberg_fc_augsburg" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SV 07 Elversberg</span> vs <span>FC Augsburg</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">46.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">43.7%</span></div>
                </div>
            </a>

            <!-- Brentford FC vs Liverpool FC -->
            <a href="/?match_id=brentford_fc_liverpool_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Brentford FC</span> vs <span>Liverpool FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">59.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.5%</span></div>
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
