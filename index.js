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
            <!-- AC Monza vs Cagliari Calcio -->
            <a href="/?match_id=ac_monza_cagliari_calcio" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AC Monza</span> vs <span>Cagliari Calcio</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.7 - 0.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">67.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">61.9%</span></div>
                </div>
            </a>

            <!-- Parma Calcio 1913 vs Torino FC -->
            <a href="/?match_id=parma_calcio_1913_torino_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Parma Calcio 1913</span> vs <span>Torino FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.6 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">55.2%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">71.8%</span></div>
                </div>
            </a>

            <!-- Getafe CF vs Rayo Vallecano de Madrid -->
            <a href="/?match_id=getafe_cf_rayo_vallecano_de_madrid" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Getafe CF</span> vs <span>Rayo Vallecano de Madrid</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.4</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">41.4%</span></div>
                </div>
            </a>

            <!-- Tottenham Hotspur FC vs Coventry City FC -->
            <a href="/?match_id=tottenham_hotspur_fc_coventry_city_fc" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Tottenham Hotspur FC</span> vs <span>Coventry City FC</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 1.7</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">49.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">58.6%</span></div>
                </div>
            </a>

            <!-- Fenerbahçe SK vs SK Slavia Praha -->
            <a href="/?match_id=fenerbah_e_sk_sk_slavia_praha" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Fenerbahçe SK</span> vs <span>SK Slavia Praha</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.7 - 0.9</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">63.9%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">51.5%</span></div>
                </div>
            </a>

            <!-- Sabah FK vs Borussia Dortmund -->
            <a href="/?match_id=sabah_fk_borussia_dortmund" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Sabah FK</span> vs <span>Borussia Dortmund</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.4 - 2.0</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">42.7%</span></div>
                </div>
            </a>

            <!-- SSC Napoli vs FK Bodø/Glimt -->
            <a href="/?match_id=ssc_napoli_fk_bod__glimt" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>SSC Napoli</span> vs <span>FK Bodø/Glimt</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.5 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">57.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">50.7%</span></div>
                </div>
            </a>

            <!-- VfB Stuttgart vs Club Atlético de Madrid -->
            <a href="/?match_id=vfb_stuttgart_club_atl_tico_de_madrid" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>VfB Stuttgart</span> vs <span>Club Atlético de Madrid</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-draw">DRAW / X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.8 - 1.5</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">65.4%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">64.3%</span></div>
                </div>
            </a>

            <!-- AS Roma vs ŠK Slovan Bratislava -->
            <a href="/?match_id=as_roma__k_slovan_bratislava" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>AS Roma</span> vs <span>ŠK Slovan Bratislava</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 0.7 - 1.2</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">37.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">63.0%</span></div>
                </div>
            </a>

            <!-- FC Porto vs PSV -->
            <a href="/?match_id=fc_porto_psv" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>FC Porto</span> vs <span>PSV</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.1 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">60.5%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">54.3%</span></div>
                </div>
            </a>

            <!-- Manchester City FC vs PAE AEK -->
            <a href="/?match_id=manchester_city_fc_pae_aek" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Manchester City FC</span> vs <span>PAE AEK</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">1X</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 2.1 - 1.6</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">40.0%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">49.7%</span></div>
                </div>
            </a>

            <!-- Paris Saint-Germain FC vs FC Barcelona -->
            <a href="/?match_id=paris_saint_germain_fc_fc_barcelona" class="match-link">
                <div class="match-card">
                    <div class="teams"><span>Paris Saint-Germain FC</span> vs <span>FC Barcelona</span></div>
                    <div style="margin-bottom:15px;">
                        <span class="badge b-win">X2</span>
                        <span class="badge b-draw" style="margin-left:5px;">xG: 1.3 - 1.8</span>
                    </div>
                    <div class="stats-row"><span>Both Teams to Score:</span> <span class="val">58.7%</span></div>
                    <div class="stats-row"><span>Under 2.5 Goals:</span> <span class="val">60.5%</span></div>
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
