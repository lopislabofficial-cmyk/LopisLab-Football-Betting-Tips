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
            <!-- Genoa CFC vs ACF Fiorentina -->
            <a href="/?match_id=genoa_cfc_acf_fiorentina" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Genoa CFC</span> vs <span>ACF Fiorentina</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.9 - 0.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">72.3%</span></div>
                </div>
            </a>

            <!-- 1. FC Union Berlin vs SV 07 Elversberg -->
            <a href="/?match_id=1__fc_union_berlin_sv_07_elversberg" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>1. FC Union Berlin</span> vs <span>SV 07 Elversberg</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">42.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">66.6%</span></div>
                </div>
            </a>

            <!-- SC Paderborn 07 vs VfB Stuttgart -->
            <a href="/?match_id=sc_paderborn_07_vfb_stuttgart" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SC Paderborn 07</span> vs <span>VfB Stuttgart</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.2%</span></div>
                </div>
            </a>

            <!-- FC Augsburg vs FC Bayern München -->
            <a href="/?match_id=fc_augsburg_fc_bayern_m_nchen" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Augsburg</span> vs <span>FC Bayern München</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">71.0%</span></div>
                </div>
            </a>

            <!-- 1. FSV Mainz 05 vs Bayer 04 Leverkusen -->
            <a href="/?match_id=1__fsv_mainz_05_bayer_04_leverkusen" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>1. FSV Mainz 05</span> vs <span>Bayer 04 Leverkusen</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 0.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">41.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.7%</span></div>
                </div>
            </a>

            <!-- TSG 1899 Hoffenheim vs Hamburger SV -->
            <a href="/?match_id=tsg_1899_hoffenheim_hamburger_sv" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>TSG 1899 Hoffenheim</span> vs <span>Hamburger SV</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">71.0%</span></div>
                </div>
            </a>

            <!-- Sunderland AFC vs Brighton & Hove Albion FC -->
            <a href="/?match_id=sunderland_afc_brighton___hove_albion_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sunderland AFC</span> vs <span>Brighton & Hove Albion FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">49.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.6%</span></div>
                </div>
            </a>

            <!-- Chelsea FC vs AFC Bournemouth -->
            <a href="/?match_id=chelsea_fc_afc_bournemouth" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Chelsea FC</span> vs <span>AFC Bournemouth</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.2 - 0.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.0%</span></div>
                </div>
            </a>

            <!-- Aston Villa FC vs Brentford FC -->
            <a href="/?match_id=aston_villa_fc_brentford_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Aston Villa FC</span> vs <span>Brentford FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">66.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">59.2%</span></div>
                </div>
            </a>

            <!-- Ipswich Town FC vs Fulham FC -->
            <a href="/?match_id=ipswich_town_fc_fulham_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Ipswich Town FC</span> vs <span>Fulham FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">56.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">49.4%</span></div>
                </div>
            </a>

            <!-- Deportivo Alavés vs Club Atlético de Madrid -->
            <a href="/?match_id=deportivo_alav_s_club_atl_tico_de_madrid" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Deportivo Alavés</span> vs <span>Club Atlético de Madrid</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">72.9%</span></div>
                </div>
            </a>

            <!-- FC Internazionale Milano vs Parma Calcio 1913 -->
            <a href="/?match_id=fc_internazionale_milano_parma_calcio_1913" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Internazionale Milano</span> vs <span>Parma Calcio 1913</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">58.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">67.0%</span></div>
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
