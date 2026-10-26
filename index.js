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
            <!-- Sevilla FC vs CA Osasuna -->
            <a href="/?match_id=sevilla_fc_ca_osasuna" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sevilla FC</span> vs <span>CA Osasuna</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">40.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">58.1%</span></div>
                </div>
            </a>

            <!-- US Sassuolo Calcio vs SS Lazio -->
            <a href="/?match_id=us_sassuolo_calcio_ss_lazio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>US Sassuolo Calcio</span> vs <span>SS Lazio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">51.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.8%</span></div>
                </div>
            </a>

            <!-- AS Roma vs Cagliari Calcio -->
            <a href="/?match_id=as_roma_cagliari_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AS Roma</span> vs <span>Cagliari Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">57.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">53.1%</span></div>
                </div>
            </a>

            <!-- Torino FC vs Como 1907 -->
            <a href="/?match_id=torino_fc_como_1907" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Torino FC</span> vs <span>Como 1907</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">38.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">72.2%</span></div>
                </div>
            </a>

            <!-- Parma Calcio 1913 vs Udinese Calcio -->
            <a href="/?match_id=parma_calcio_1913_udinese_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Parma Calcio 1913</span> vs <span>Udinese Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 0.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">52.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.6%</span></div>
                </div>
            </a>

            <!-- Venezia FC vs FC Internazionale Milano -->
            <a href="/?match_id=venezia_fc_fc_internazionale_milano" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Venezia FC</span> vs <span>FC Internazionale Milano</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">40.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">40.2%</span></div>
                </div>
            </a>

            <!-- AC Milan vs Bologna FC 1909 -->
            <a href="/?match_id=ac_milan_bologna_fc_1909" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AC Milan</span> vs <span>Bologna FC 1909</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">34.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.9%</span></div>
                </div>
            </a>

            <!-- AC Monza vs SSC Napoli -->
            <a href="/?match_id=ac_monza_ssc_napoli" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AC Monza</span> vs <span>SSC Napoli</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.8 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">57.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">53.2%</span></div>
                </div>
            </a>

            <!-- Genoa CFC vs Juventus FC -->
            <a href="/?match_id=genoa_cfc_juventus_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Genoa CFC</span> vs <span>Juventus FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.9 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">42.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">46.7%</span></div>
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
