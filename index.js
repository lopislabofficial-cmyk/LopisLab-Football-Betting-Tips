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
            <!-- LASK Linz vs Liverpool FC -->
            <a href="/?match_id=lask_linz_liverpool_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>LASK Linz</span> vs <span>Liverpool FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.0 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.2%</span></div>
                </div>
            </a>

            <!-- Feyenoord Rotterdam vs Como 1907 -->
            <a href="/?match_id=feyenoord_rotterdam_como_1907" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Feyenoord Rotterdam</span> vs <span>Como 1907</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.9 - 0.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.1%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.3%</span></div>
                </div>
            </a>

            <!-- FK Bodø/Glimt vs Borussia Dortmund -->
            <a href="/?match_id=fk_bod__glimt_borussia_dortmund" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FK Bodø/Glimt</span> vs <span>Borussia Dortmund</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">41.4%</span></div>
                </div>
            </a>

            <!-- Real Betis Balompié vs FC Porto -->
            <a href="/?match_id=real_betis_balompi__fc_porto" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Real Betis Balompié</span> vs <span>FC Porto</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">38.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.4%</span></div>
                </div>
            </a>

            <!-- AS Roma vs Real Madrid CF -->
            <a href="/?match_id=as_roma_real_madrid_cf" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AS Roma</span> vs <span>Real Madrid CF</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.9 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">57.8%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">52.8%</span></div>
                </div>
            </a>

            <!-- ŠK Slovan Bratislava vs VfB Stuttgart -->
            <a href="/?match_id=_k_slovan_bratislava_vfb_stuttgart" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>ŠK Slovan Bratislava</span> vs <span>VfB Stuttgart</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.1</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">58.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">57.1%</span></div>
                </div>
            </a>

            <!-- Aston Villa FC vs Fenerbahçe SK -->
            <a href="/?match_id=aston_villa_fc_fenerbah_e_sk" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Aston Villa FC</span> vs <span>Fenerbahçe SK</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.3 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">33.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">65.4%</span></div>
                </div>
            </a>

            <!-- FK Shakhtar Donetsk vs PAE AEK -->
            <a href="/?match_id=fk_shakhtar_donetsk_pae_aek" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FK Shakhtar Donetsk</span> vs <span>PAE AEK</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.2 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">61.6%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">55.5%</span></div>
                </div>
            </a>

            <!-- Manchester City FC vs Paris Saint-Germain FC -->
            <a href="/?match_id=manchester_city_fc_paris_saint_germain_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Manchester City FC</span> vs <span>Paris Saint-Germain FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.0 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">45.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.4%</span></div>
                </div>
            </a>

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
        </div>
    </div>
</body>
</html>`;

    return new Response(html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
  }
};
