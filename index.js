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

            <!-- Ipswich Town FC vs Nottingham Forest FC -->
            <a href="/?match_id=ipswich_town_fc_nottingham_forest_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Ipswich Town FC</span> vs <span>Nottingham Forest FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">62.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.7%</span></div>
                </div>
            </a>

            <!-- Deportivo Alavés vs Málaga CF -->
            <a href="/?match_id=deportivo_alav_s_m_laga_cf" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Deportivo Alavés</span> vs <span>Málaga CF</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">44.9%</span></div>
                </div>
            </a>

            <!-- Aston Villa FC vs Manchester City FC -->
            <a href="/?match_id=aston_villa_fc_manchester_city_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Aston Villa FC</span> vs <span>Manchester City FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">60.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">62.7%</span></div>
                </div>
            </a>

            <!-- Rayo Vallecano de Madrid vs Elche CF -->
            <a href="/?match_id=rayo_vallecano_de_madrid_elche_cf" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Rayo Vallecano de Madrid</span> vs <span>Elche CF</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">51.7%</span></div>
                </div>
            </a>

            <!-- Como 1907 vs US Sassuolo Calcio -->
            <a href="/?match_id=como_1907_us_sassuolo_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Como 1907</span> vs <span>US Sassuolo Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.4 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">64.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">57.3%</span></div>
                </div>
            </a>

            <!-- Cagliari Calcio vs Bologna FC 1909 -->
            <a href="/?match_id=cagliari_calcio_bologna_fc_1909" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Cagliari Calcio</span> vs <span>Bologna FC 1909</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">56.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">66.9%</span></div>
                </div>
            </a>

            <!-- 1. FC Köln vs FC Schalke 04 -->
            <a href="/?match_id=1__fc_k_ln_fc_schalke_04" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>1. FC Köln</span> vs <span>FC Schalke 04</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">58.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">71.4%</span></div>
                </div>
            </a>

            <!-- FC Augsburg vs 1. FC Union Berlin -->
            <a href="/?match_id=fc_augsburg_1__fc_union_berlin" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Augsburg</span> vs <span>1. FC Union Berlin</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">66.9%</span></div>
                </div>
            </a>

            <!-- RB Leipzig vs SV 07 Elversberg -->
            <a href="/?match_id=rb_leipzig_sv_07_elversberg" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RB Leipzig</span> vs <span>SV 07 Elversberg</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">36.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.4%</span></div>
                </div>
            </a>

            <!-- SC Paderborn 07 vs Hamburger SV -->
            <a href="/?match_id=sc_paderborn_07_hamburger_sv" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SC Paderborn 07</span> vs <span>Hamburger SV</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">64.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.7%</span></div>
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
