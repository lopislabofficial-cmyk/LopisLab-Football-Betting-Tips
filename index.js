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
            <!-- CA Osasuna vs Real Racing Club de Santander -->
            <a href="/?match_id=ca_osasuna_real_racing_club_de_santander" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>CA Osasuna</span> vs <span>Real Racing Club de Santander</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.2 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">46.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">73.6%</span></div>
                </div>
            </a>

            <!-- ACF Fiorentina vs Como 1907 -->
            <a href="/?match_id=acf_fiorentina_como_1907" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>ACF Fiorentina</span> vs <span>Como 1907</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.2%</span></div>
                </div>
            </a>

            <!-- Leeds United FC vs Manchester United FC -->
            <a href="/?match_id=leeds_united_fc_manchester_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Leeds United FC</span> vs <span>Manchester United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">48.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.0%</span></div>
                </div>
            </a>

            <!-- Brighton & Hove Albion FC vs Crystal Palace FC -->
            <a href="/?match_id=brighton___hove_albion_fc_crystal_palace_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Brighton & Hove Albion FC</span> vs <span>Crystal Palace FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 0.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">44.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.4%</span></div>
                </div>
            </a>

            <!-- AFC Bournemouth vs Sunderland AFC -->
            <a href="/?match_id=afc_bournemouth_sunderland_afc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AFC Bournemouth</span> vs <span>Sunderland AFC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">49.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">65.6%</span></div>
                </div>
            </a>

            <!-- Bayer 04 Leverkusen vs SC Freiburg -->
            <a href="/?match_id=bayer_04_leverkusen_sc_freiburg" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Bayer 04 Leverkusen</span> vs <span>SC Freiburg</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">34.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.0%</span></div>
                </div>
            </a>

            <!-- RC Celta de Vigo vs Deportivo Alavés -->
            <a href="/?match_id=rc_celta_de_vigo_deportivo_alav_s" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RC Celta de Vigo</span> vs <span>Deportivo Alavés</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">38.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">58.8%</span></div>
                </div>
            </a>

            <!-- Nottingham Forest FC vs Arsenal FC -->
            <a href="/?match_id=nottingham_forest_fc_arsenal_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Nottingham Forest FC</span> vs <span>Arsenal FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">45.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.6%</span></div>
                </div>
            </a>

            <!-- Borussia Mönchengladbach vs TSG 1899 Hoffenheim -->
            <a href="/?match_id=borussia_m_nchengladbach_tsg_1899_hoffenheim" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Borussia Mönchengladbach</span> vs <span>TSG 1899 Hoffenheim</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">49.4%</span></div>
                </div>
            </a>

            <!-- AC Milan vs Atalanta BC -->
            <a href="/?match_id=ac_milan_atalanta_bc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AC Milan</span> vs <span>Atalanta BC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">62.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">46.2%</span></div>
                </div>
            </a>

            <!-- Málaga CF vs Real Sociedad de Fútbol -->
            <a href="/?match_id=m_laga_cf_real_sociedad_de_f_tbol" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Málaga CF</span> vs <span>Real Sociedad de Fútbol</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">40.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">49.1%</span></div>
                </div>
            </a>

            <!-- Juventus FC vs SS Lazio -->
            <a href="/?match_id=juventus_fc_ss_lazio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Juventus FC</span> vs <span>SS Lazio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">39.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">71.9%</span></div>
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
