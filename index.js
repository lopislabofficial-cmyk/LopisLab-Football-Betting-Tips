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
            <!-- Atalanta BC vs Venezia FC -->
            <a href="/?match_id=atalanta_bc_venezia_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Atalanta BC</span> vs <span>Venezia FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">53.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.8%</span></div>
                </div>
            </a>

            <!-- Torino FC vs Udinese Calcio -->
            <a href="/?match_id=torino_fc_udinese_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Torino FC</span> vs <span>Udinese Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">62.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.1%</span></div>
                </div>
            </a>

            <!-- Levante UD vs Sevilla FC -->
            <a href="/?match_id=levante_ud_sevilla_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Levante UD</span> vs <span>Sevilla FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.7 - 0.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">63.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.3%</span></div>
                </div>
            </a>

            <!-- Coventry City FC vs Newcastle United FC -->
            <a href="/?match_id=coventry_city_fc_newcastle_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Coventry City FC</span> vs <span>Newcastle United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">61.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">40.1%</span></div>
                </div>
            </a>

            <!-- Racing Club de Lens vs Sporting Clube de Portugal -->
            <a href="/?match_id=racing_club_de_lens_sporting_clube_de_portugal" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Racing Club de Lens</span> vs <span>Sporting Clube de Portugal</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.3%</span></div>
                </div>
            </a>

            <!-- Sabah FK vs SK Slavia Praha -->
            <a href="/?match_id=sabah_fk_sk_slavia_praha" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sabah FK</span> vs <span>SK Slavia Praha</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">67.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">74.1%</span></div>
                </div>
            </a>

            <!-- Viking FK vs FC Bayern München -->
            <a href="/?match_id=viking_fk_fc_bayern_m_nchen" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Viking FK</span> vs <span>FC Bayern München</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">58.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">72.8%</span></div>
                </div>
            </a>

            <!-- FC Internazionale Milano vs Club Brugge KV -->
            <a href="/?match_id=fc_internazionale_milano_club_brugge_kv" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Internazionale Milano</span> vs <span>Club Brugge KV</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.4 - 1.3</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.3%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">68.3%</span></div>
                </div>
            </a>

            <!-- Villarreal CF vs SSC Napoli -->
            <a href="/?match_id=villarreal_cf_ssc_napoli" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Villarreal CF</span> vs <span>SSC Napoli</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.4 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">54.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">44.2%</span></div>
                </div>
            </a>

            <!-- Club Atlético de Madrid vs Manchester United FC -->
            <a href="/?match_id=club_atl_tico_de_madrid_manchester_united_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Club Atlético de Madrid</span> vs <span>Manchester United FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.4 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">49.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.3%</span></div>
                </div>
            </a>

            <!-- RB Leipzig vs PSV -->
            <a href="/?match_id=rb_leipzig_psv" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>RB Leipzig</span> vs <span>PSV</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">63.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">69.7%</span></div>
                </div>
            </a>

            <!-- Galatasaray SK vs FC Barcelona -->
            <a href="/?match_id=galatasaray_sk_fc_barcelona" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Galatasaray SK</span> vs <span>FC Barcelona</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">48.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">49.6%</span></div>
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
