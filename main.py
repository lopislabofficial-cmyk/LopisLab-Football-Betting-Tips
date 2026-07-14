# --- CONFIGURAZIONE ID CAMPIONATI TARGET (Aggiornata con Eliteserien, Allsvenskan e MLS) ---
TARGET_IDS = ["sblsx4y7", "6kkowojd", "h6ind07k", "kxaal5od", "edmhdnn8", "kijxr4kc", "whrlenrh", "ltrtrhko", "bgqzsi5n"]

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // =========================================================================
    // 🗺️ STEP 0: GENERAZIONE SITEMAP DINAMICA PER GOOGLE SEARCH CONSOLE
    // =========================================================================
    if (url.pathname === "/sitemap.xml") {
      try {
        // Selezioniamo le partite da oggi in poi per non appesantire la sitemap,
        // garantendo a Google di trovare sempre i match freschi da indicizzare.
        const oggiStr = new Date(new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/Rome' }))
          .toISOString().split('T')[0];

        const { results } = await env.DB.prepare(
          "SELECT id, match_date FROM daily_palimpsest WHERE match_date >= ? ORDER BY match_date ASC"
        ).bind(oggiStr).all();

        const matchesList = results || [];

        // Costruiamo il file XML standard per i motori di ricerca
        let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
        xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

        // 1. Inseriamo la Home Page
        xml += `  <url>\n`;
        xml += `    <loc>https://lopislab.com/</loc>\n`;
        xml += `    <changefreq>always</changefreq>\n`;
        xml += `    <priority>1.0</priority>\n`;
        xml += `  </url>\n`;

        // 2. Inseriamo dinamicamente tutte le pagine partita del database
        for (const m of matchesList) {
          xml += `  <url>\n`;
          xml += `    <loc>https://lopislab.com/?match_id=${m.id}</loc>\n`;
          xml += `    <lastmod>${m.match_date}</lastmod>\n`;
          xml += `    <changefreq>daily</changefreq>\n`;
          xml += `    <priority>0.8</priority>\n`;
          xml += `  </url>\n`;
        }

        xml += `</urlset>`;

        return new Response(xml, {
          headers: {
            "Content-Type": "application/xml; charset=utf-8",
            "Cache-Control": "public, max-age=3600" // Cache di 1 ora per non sovraccaricare il DB
          }
        });
      } catch (sitemapErr) {
        return new Response("Sitemap Error: " + sitemapErr.message, { status: 500 });
      }
    }

    // --- REDIRECT SEO: ?date=today -> homepage ---
    if (url.searchParams.get("date") === "today") {
      url.searchParams.delete("date");
      const redirectUrl = url.searchParams.toString() ? url.toString() : url.origin + url.pathname;
      return Response.redirect(redirectUrl, 301);
    }
    
    const country = request.cf ? request.cf.country : 'IT';
    const showAds = country !== 'IT';
    
    // --- INTEGRAZIONE MONETAG + GOOGLE ANALYTICS (G-JF4164T0YW) ---
    let verificationTag = `
      <meta name="monetag" content="78af1a6b27d92bf817e22095da323f36">
      <!-- Global site tag (gtag.js) - Google Analytics -->
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-JF4164T0YW"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-JF4164T0YW');
      </script>
    `;

    if (showAds) {
      verificationTag += `
        <script src="https://alwingulla.com/zone/7686413" async data-cfasync="false"></script>
        <script>
          window.monetagZoneId = 7686413;
          (function(s,u,z,p,v,e,d){
            s[p]=s[p]||function(){(s[p].q=s[p].q||[]).push(arguments)};
            v=u.createElement(z);v.async=1;v.src=e;
            d=u.getElementsByTagName(z)[0];d.parentNode.insertBefore(v,d)
          })(window,document,'script','__atNuq','https://alwingulla.com/zone/7686413');
        </script>
      `;
    }

    // --- STEP 1: DYNAMIC MATCH DETAILS (SEO & Schema.org Ottimizzati) ---
    const matchIdParam = url.searchParams.get("match_id");
    if (matchIdParam) {
      try {
        let matchData = await env.DB.prepare(
          "SELECT * FROM daily_palimpsest WHERE id = ?"
        ).bind(matchIdParam).first();

        if (matchData) {
          let isLiveUpdate = false;
          if (matchData.status === "Live") {
            try {
              await fetchAndSyncMatches(env, matchData.match_date, false);
              matchData = await env.DB.prepare(
                "SELECT * FROM daily_palimpsest WHERE id = ?"
              ).bind(matchIdParam).first();
              isLiveUpdate = true;
            } catch (e) { console.log("Live Detail Update Error: " + e.message); }
          }

          const apiHeaders = {
            "X-RapidAPI-Key": "b6c8cbd360msh868c45fc60cf142p1fbe1ajsnef0e39d344ad", 
            "X-RapidAPI-Host": "flashscore4.p.rapidapi.com"
          };
          const h2hUrl = `https://flashscore4.p.rapidapi.com/api/flashscore/v2/matches/h2h?match_id=${matchIdParam}`;
          const statsUrl = `https://flashscore4.p.rapidapi.com/api/flashscore/v2/matches/match/stats?match_id=${matchIdParam}`;

          const [h2hRes, statsRes] = await Promise.all([
            fetch(h2hUrl, { headers: apiHeaders }).catch(() => null),
            fetch(statsUrl, { headers: apiHeaders }).catch(() => null)
          ]);

          let h2hData = (h2hRes && h2hRes.ok) ? await h2hRes.json().catch(() => null) : null;
          let statsData = (statsRes && statsRes.ok) ? await statsRes.json().catch(() => null) : null;

          let htmlDettagli = generateMatchDetailsSkeleton(matchData, h2hData, statsData, verificationTag, showAds, country, isLiveUpdate);
          return new Response(htmlDettagli, { 
            headers: { "Content-Type": "text/html; charset=utf-8" } 
          });
        } else {
          return new Response("Match not found.", { status: 404 });
        }
      } catch (err) {
        return new Response("Database Error: " + err.message, { status: 500 });
      }
    }
    
    // --- STEP 2: GENERAL PALIMPSEST ---
    const options = { timeZone: 'Europe/Rome', year: 'numeric', month: '2-digit', day: '2-digit' };
    const formatter = new Intl.DateTimeFormat('en-CA', options);
    const oggiLocale = new Date(formatter.format(new Date()));
    
    let selectedDate = oggiLocale.toISOString().split('T')[0];
    const dateParam = url.searchParams.get("date");
    if (dateParam === "yesterday") {
      const yesterday = new Date(oggiLocale);
      yesterday.setDate(yesterday.getDate() - 1);
      selectedDate = yesterday.toISOString().split('T')[0];
    } else if (dateParam === "tomorrow") {
      const tomorrow = new Date(oggiLocale);
      tomorrow.setDate(tomorrow.getDate() + 1);
      selectedDate = tomorrow.toISOString().split('T')[0];
    }

    let matches = [];
    try {
      const { results } = await env.DB.prepare(
        "SELECT * FROM daily_palimpsest WHERE match_date = ? ORDER BY match_time ASC"
      ).bind(selectedDate).all();
      matches = results || [];
    } catch (err) { }

    // --- LOGICA DI RISPARMIO API CON LIVE BYPASS ---
    let lastUpdate = 0;
    if (matches.length > 0 && matches[0].updated_at) {
      lastUpdate = new Date(matches[0].updated_at).getTime();
    }
    const adesso = Date.now();
    
    const haMatchInCorsoOLive = matches.some(m => {
      if (m.status === "Live") return true;
      if (m.status === "Scheduled" && m.match_time) {
        const [hour, minute] = m.match_time.split(":");
        const matchTimeToday = new Date(oggiLocale);
        matchTimeToday.setHours(parseInt(hour, 10), parseInt(minute, 10), 0, 0);
        return (matchTimeToday.getTime() - adesso) < (15 * 60 * 1000);
      }
      return false;
    });

    const tempoCache = haMatchInCorsoOLive ? (2 * 60 * 1000) : (45 * 60 * 1000);
    const cacheValida = (adesso - lastUpdate) < tempoCache;
    const haMatchLiveOScheduled = matches.length === 0 || matches.some(m => m.status === "Live" || m.status === "Scheduled");
    if (haMatchLiveOScheduled && !cacheValida) {
      try {
        await fetchAndSyncMatches(env, selectedDate, true);
        const { results } = await env.DB.prepare(
          "SELECT * FROM daily_palimpsest WHERE match_date = ? ORDER BY match_time ASC"
        ).bind(selectedDate).all();
        matches = results || [];
      } catch (err) { 
        console.log("Sync Error: " + err.message);
      }
    }

    const activeTab = dateParam === "yesterday" || dateParam === "tomorrow" ? dateParam : "today";
    let htmlPalinsesto = generateEnglishHTML(matches, activeTab, verificationTag, showAds, country);
    return new Response(htmlPalinsesto, { 
      headers: { "Content-Type": "text/html; charset=utf-8" } 
    });
  },

  async scheduled(event, env, ctx) {
    const options = { timeZone: 'Europe/Rome', year: 'numeric', month: '2-digit', day: '2-digit' };
    const formatter = new Intl.DateTimeFormat('en-CA', options);
    const todayStr = formatter.format(new Date());
    await fetchAndSyncMatches(env, todayStr, true);
  }
};

// =========================================================================
// FUNZIONI DI SUPPORTO DI LOGICA
// =========================================================================

function calcolaPronosticoReale(homeOdds, drawOdds, awayOdds) {
  if (!homeOdds || !drawOdds || !awayOdds) return "N/D";
  const qHome = parseFloat(homeOdds);
  const qDraw = parseFloat(drawOdds);
  const qAway = parseFloat(awayOdds);
  if (isNaN(qHome) || qHome === 0 || qDraw === 0 || qAway === 0) return "N/D";
  if (qHome <= 1.45) return "1";
  if (qAway <= 1.45) return "2";
  if (qHome > 1.45 && qHome <= 1.95) return "1X";
  if (qAway > 1.45 && qAway <= 1.95) return "X2";
  if (qHome > 1.95 && qAway > 1.95 && qDraw > 3.30) return "12";
  return "1X";
}

function controllaSeVinto(status, homeScore, awayScore, pronostico) {
  if (status !== "Finished" || homeScore === null || awayScore === null || pronostico === "N/D") return null;
  const gHome = parseInt(homeScore, 10);
  const gAway = parseInt(awayScore, 10);
  let segnoReale = "X";
  if (gHome > gAway) segnoReale = "1";
  else if (gAway > gHome) segnoReale = "2";
  if (pronostico === "1" && segnoReale === "1") return true;
  if (pronostico === "X" && segnoReale === "X") return true;
  if (pronostico === "2" && segnoReale === "2") return true;
  if (pronostico === "1X" && (segnoReale === "1" || segnoReale === "X")) return true;
  if (pronostico === "X2" && (segnoReale === "2" || segnoReale === "X")) return true;
  if (pronostico === "12" && (segnoReale === "1" || segnoReale === "2")) return true;
  return false;
}

function determinaClasseEsito(status, homeScore, awayScore, pronostico) {
  const esito = controllaSeVinto(status, homeScore, awayScore, pronostico);
  if (esito === null) return "pred-badge-neutral";
  return esito ? "pred-badge-win" : "pred-badge-lose";
}

async function fetchAndSyncMatches(env, dateStr, fetchOddsAllowed) {
  try {
    const apiHeaders = {
      "X-RapidAPI-Key": "b6c8cbd360msh868c45fc60cf142p1fbe1ajsnef0e39d344ad", 
      "X-RapidAPI-Host": "flashscore4.p.rapidapi.com"
    };
    const apiUrl = `https://flashscore4.p.rapidapi.com/api/flashscore/v2/matches/list-by-date?sport_id=1&date=${dateStr}&timezone=Europe%2FBerlin`; 
    const response = await fetch(apiUrl, { headers: apiHeaders });
    if (!response.ok) return;
    const data = await response.json();
    const nowTimestamp = new Date().toISOString();
    if (data && Array.isArray(data)) {
      const statements = [];
      for (const torneo of data) {
        const lId = torneo.tournament_id ? String(torneo.tournament_id) : "";
        let lName = torneo.tournament_name || "Other League"; 
        
        const mList = torneo.matches || [];
        if (Array.isArray(mList)) {
          for (const match of mList) {
            const mId = match.match_id ? String(match.match_id) : "";
            if (!mId) continue;

            if (TARGET_IDS.includes(lId) || TARGET_IDS.includes(mId)) {
              let mTime = "--:--";
              if (match.timestamp) {
                const matchDate = new Date(match.timestamp * 1000);
                mTime = matchDate.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Rome' });
              }
              const homeT = match.home_team?.name || "Unknown Home";
              const awayT = match.away_team?.name || "Unknown Away";
              
              let finalLeagueName = lName;
              if (lId === "kxaal5od") {
                finalLeagueName = "EUROPE: Champions League - Qualification";
              } else if (lId === "kijxr4kc") {
                finalLeagueName = "EUROPE: Europa League - Qualification";
              } else if (lId === "edmhdnn8") {
                finalLeagueName = "EUROPE: Conference League - Qualification";
              } else if (lId === "h6ind07k") {
                finalLeagueName = "VEIKKAUSLIIGA";
              } else if (lId === "whrlenrh") {
                finalLeagueName = "NORWAY: Eliteserien";
              } else if (lId === "ltrtrhko") {
                finalLeagueName = "SWEDEN: Allsvenskan";
              } else if (lId === "bgqzsi5n") {
                finalLeagueName = "USA: MLS";
              } else if (lId === "6kkowojd") {
                finalLeagueName = "World Cup";
              } else {
                const lowerName = finalLeagueName.toLowerCase();
                if (lowerName.includes("world cup") || lowerName.includes("fifa") || lowerName.includes("qualifiers") || lowerName.includes("qualification") || finalLeagueName === "Other League") {
                  finalLeagueName = "World Cup";
                }
              }

              let mStatus = "Scheduled";
              if (match.match_status?.is_finished) mStatus = "Finished";
              else if (match.match_status?.is_in_progress) mStatus = "Live";

              const homeS = match.scores?.home !== null ? match.scores.home : null;
              const awayS = match.scores?.away !== null ? match.scores.away : null;
              
              let hOdds = match.odds?.["1"] || null;
              let dOdds = match.odds?.["X"] || null;
              let aOdds = match.odds?.["2"] || null;
              if (fetchOddsAllowed && mStatus !== "Finished" && (!hOdds || hOdds === "0" || hOdds === 0 || hOdds === "")) {
                try {
                  const esistente = await env.DB.prepare("SELECT home_odds FROM daily_palimpsest WHERE id = ?").bind(mId).first();
                  if (!esistente || !esistente.home_odds || esistente.home_odds === "N/D") {
                    const oddsSummaryUrl = `https://flashscore4.p.rapidapi.com/api/flashscore/v2/matches/odds/summary?match_id=${mId}`;
                    const oddsRes = await fetch(oddsSummaryUrl, { headers: apiHeaders });
                    if (oddsRes.ok) {
                      const oddsData = await oddsRes.json();
                      if (oddsData && Array.isArray(oddsData) && oddsData.length > 0) {
                        const mainBookmaker = oddsData[0].odds || [];
                        const s1 = mainBookmaker.find(o => o.indicator === "1");
                        const sX = mainBookmaker.find(o => o.indicator === "X");
                        const s2 = mainBookmaker.find(o => o.indicator === "2");
                        if (s1 && s1.value) hOdds = s1.value;
                        if (sX && sX.value) dOdds = sX.value;
                        if (s2 && s2.value) aOdds = s2.value;
                      }
                    }
                  }
                } catch (oddsErr) { console.log("Errore sub-fetch quote: " + oddsErr.message); }
              }

              const pronosticoCalcolato = calcolaPronosticoReale(hOdds, dOdds, aOdds);
              statements.push(
                env.DB.prepare(`
                  INSERT INTO daily_palimpsest (id, match_date, date_str, match_time, home_team, away_team, status, home_score, away_score, raw_data, html_content, updated_at, home_odds, draw_odds, away_odds, league_name, prediction) 
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                  ON CONFLICT(id) DO UPDATE SET 
                    status = excluded.status,
                    home_score = excluded.home_score,
                    away_score = excluded.away_score,
                    raw_data = excluded.raw_data,
                    updated_at = excluded.updated_at,
                    league_name = excluded.league_name,
                    home_odds = CASE WHEN excluded.home_odds IS NOT NULL AND excluded.home_odds != '' AND excluded.home_odds != '0' THEN excluded.home_odds ELSE daily_palimpsest.home_odds END,
                    draw_odds = CASE WHEN excluded.draw_odds IS NOT NULL AND excluded.draw_odds != '' AND excluded.draw_odds != '0' THEN excluded.draw_odds ELSE daily_palimpsest.draw_odds END,
                    away_odds = CASE WHEN excluded.away_odds IS NOT NULL AND excluded.away_odds != '' AND excluded.away_odds != '0' THEN excluded.away_odds ELSE daily_palimpsest.away_odds END,
                    prediction = CASE WHEN daily_palimpsest.prediction IS NOT NULL AND daily_palimpsest.prediction != 'N/D' AND daily_palimpsest.prediction != '' THEN daily_palimpsest.prediction ELSE excluded.prediction END
                `).bind(mId, dateStr, dateStr, mTime, homeT, awayT, mStatus, homeS, awayS, JSON.stringify(match), "", nowTimestamp, hOdds, dOdds, aOdds, finalLeagueName, pronosticoCalcolato)
              );
            }
          }
        }
      }

      const chunkSize = 20;
      for (let i = 0; i < statements.length; i += chunkSize) {
        const chunk = statements.slice(i, i + chunkSize);
        await env.DB.batch(chunk);
      }
    }
  } catch (syncErr) { console.log("Error inside fetchAndSyncMatches: " + syncErr.message); }
}

function ottieniArrayH2H(h2hRaw) { 
  if (!h2hRaw) return []; 
  if (Array.isArray(h2hRaw)) return h2hRaw; 
  if (h2hRaw.data && Array.isArray(h2hRaw.data)) return h2hRaw.data;
  let raggruppamento = []; const chiaviH2H = ['general', 'home', 'away', 'matches'];
  for (const k of chiaviH2H) { if (h2hRaw[k] && Array.isArray(h2hRaw[k])) { raggruppamento = raggruppamento.concat(h2hRaw[k]); } } return raggruppamento;
}

function calcolaConsiglioUnderOver(homeTeamName, awayTeamName, h2hRaw) { 
  const elencoMatch = ottieniArrayH2H(h2hRaw); if (elencoMatch.length === 0) return "N/D"; let totalGoals = 0;
  let matchCount = 0; for (const m of elencoMatch) { if (!m || !m.scores || m.scores.home === null || m.scores.away === null) continue;
    const hName = m.home_team?.name; const aName = m.away_team?.name; if (hName === homeTeamName || aName === homeTeamName || hName === awayTeamName || aName === awayTeamName) { totalGoals += (parseInt(m.scores.home, 10) + parseInt(m.scores.away, 10));
      matchCount++; } if (matchCount >= 10) break; } if (matchCount === 0) return "N/D";
  return (totalGoals / matchCount) >= 2.50 ? "OVER 2.5" : "UNDER 2.5";
}

function calcolaH2HVisivo(homeTeamName, awayTeamName, h2hRaw) { 
  const elencoMatch = ottieniArrayH2H(h2hRaw); if (elencoMatch.length === 0) return null;
  let homeForm = [], awayForm = []; for (const m of elencoMatch) { if (!m || !m.scores || m.scores.home === null || m.scores.away === null) continue;
    const gHome = parseInt(m.scores.home, 10), gAway = parseInt(m.scores.away, 10); const hName = m.home_team?.name, aName = m.away_team?.name;
    if (homeForm.length < 5 && (hName === homeTeamName || aName === homeTeamName)) { if (gHome === gAway) homeForm.push('<span class="circle badge-d">D</span>');
      else if ((hName === homeTeamName && gHome > gAway) || (aName === homeTeamName && gAway > gHome)) homeForm.push('<span class="circle badge-w">W</span>');
      else homeForm.push('<span class="circle badge-l">L</span>'); } if (awayForm.length < 5 && (hName === awayTeamName || aName === awayTeamName)) { if (gHome === gAway) awayForm.push('<span class="circle badge-d">D</span>');
      else if ((hName === awayTeamName && gHome > gAway) || (aName === awayTeamName && gAway > gHome)) awayForm.push('<span class="circle badge-w">W</span>');
      else awayForm.push('<span class="circle badge-l">L</span>'); } } if (homeForm.length === 0 && awayForm.length === 0) return null;
  return `<div class="h2h-container"><div class="h2h-row"><div class="h2h-team-label"><b>${homeTeamName}</b></div><div class="h2h-circles">${homeForm.join("")}</div></div><div class="h2h-row" style="margin-top: 15px;"><div class="h2h-team-label"><b>${awayTeamName}</b></div><div class="h2h-circles">${awayForm.join("")}</div></div></div>`; 
}

function calcolaStatsVisive(statsRaw) { 
  let items = [];
  if (statsRaw && Array.isArray(statsRaw)) {
    items = statsRaw; 
  } else if (statsRaw && typeof statsRaw === 'object') {
    items = Object.values(statsRaw);
  }
  if (items.length === 0) return `<div style="color: #64748b; font-size: 14px; text-align: center; padding: 20px; font-style: italic; background: #f8fafc; border-radius: 8px; border: 1px dashed #cbd5e1;">Statistics not available yet.</div>`; 

  let totalSum = 0;
  items.forEach(stat => {
    if (!stat) return;
    const nHome = parseFloat(String(stat.home_team || "0").replace(/[^0-9.]/g, '')) || 0;
    const nAway = parseFloat(String(stat.away_team || "0").replace(/[^0-9.]/g, '')) || 0;
    totalSum += (nHome + nAway);
  });

  if (totalSum === 0) {
    return `<div style="color: #64748b; font-size: 14px; text-align: center; padding: 25px; font-style: italic; background: #f8fafc; border-radius: 8px; border: 1px dashed #cbd5e1; line-height: 1.5;">📊 Match statistics will be available once the match starts.</div>`;
  }

  const traduzioni = {
    "Expected goals": "Expected Goals (xG)",
    "Expected goals (xg)": "Expected Goals (xG)",
    "Ball possession": "Ball Possession",
    "Total shots": "Total Shots",
    "Shots on target": "Shots on Target",
    "Big chances": "Big Chances",
    "Corner kicks": "Corners",
    "Passes completed": "Pass Accuracy",
    "Expected assists (xa)": "Expected Assists (xA)",
    "xA": "Expected Assists (xA)",
    "Goalkeeper saves": "Goalkeeper Saves",
    "Shots off target": "Shots off Target",
    "Blocked shots": "Blocked Shots",
    "Fouls": "Fouls",
    "Offsides": "Offsides",
    "Yellow cards": "Yellow Cards",
    "Red cards": "Red Cards",
    "Total passes": "Total Passes",
    "Attacks": "Attacks",
    "Dangerous attacks": "Dangerous Attacks",
    "Free kicks": "Free Kicks",
    "Throw-ins": "Throw-ins",
    "Tackles": "Tackles"
  };

  const keyStatsNames = [
    "Expected goals", "Expected goals (xg)", "Ball possession", "Total shots", 
    "Shots on target", "Big chances", "Corner kicks", "Passes completed", 
    "Expected assists (xa)", "xA", "Goalkeeper saves"
  ];

  let coreHtml = ""; 
  let advancedHtml = "";
  let hasAdvanced = false;

  items.forEach(stat => {
    if (!stat || !stat.name) return;

    const nomeOriginale = stat.name;
    const nomeOriginaleLower = nomeOriginale.toLowerCase();
    const nomeTradotto = traduzioni[nomeOriginale] || nomeOriginale;

    let valHomeRaw = String(stat.home_team || "0"); 
    let valAwayRaw = String(stat.away_team || "0"); 
    
    let nHome = parseFloat(valHomeRaw.replace(/[^0-9.]/g, '')) || 0; 
    let nAway = parseFloat(valAwayRaw.replace(/[^0-9.]/g, '')) || 0; 
    
    let total = nHome + nAway; 
    let pctHome = total > 0 ? (nHome / total) * 100 : 0; 
    let pctAway = total > 0 ? (nAway / total) * 100 : 0; 
    
    const singleStatHtml = `
      <div class="stat-container-premium" style="margin-bottom: 22px; font-family: 'Segoe UI', Arial, sans-serif; width: 100%; box-sizing: border-box;">
        <div class="stat-header-row" style="display: flex; align-items: center; justify-content: space-between; font-size: 14px; margin-bottom: 8px;">
          <span style="font-weight: 700; color: #0f172a; min-width: 45px; text-align: left; font-size: 14px;">${valHomeRaw}</span>
          <span style="font-weight: 600; color: #475569; font-size: 13px; text-align: center; flex-grow: 1; padding: 0 10px; white-space: nowrap;">${nomeTradotto}</span>
          <span style="font-weight: 700; color: #0f172a; min-width: 45px; text-align: right; font-size: 14px;">${valAwayRaw}</span>
        </div>
        <div class="stat-bars-wrapper" style="display: flex; gap: 12px; width: 100%;">
          <div class="bar-track-home" style="flex: 1; height: 12px; background-color: #f1f5f9; border-radius: 6px; display: flex; justify-content: flex-end; overflow: hidden;">
            <div class="home-fill" style="width: ${pctHome}%; background-color: #1d4ed8; border-radius: 6px 0 0 6px; transition: width 0.3s ease;"></div>
          </div>
          <div class="bar-track-away" style="flex: 1; height: 12px; background-color: #f1f5f9; border-radius: 6px; display: flex; justify-content: flex-start; overflow: hidden;">
            <div class="away-fill" style="width: ${pctAway}%; background-color: #dc2626; border-radius: 0 6px 6px 0; transition: width 0.3s ease;"></div>
          </div>
        </div>
      </div>
    `;

    const isKeyStat = keyStatsNames.some(kName => kName.toLowerCase() === nomeOriginaleLower);
    if (isKeyStat) {
      coreHtml += singleStatHtml;
    } else {
      advancedHtml += singleStatHtml;
      hasAdvanced = true;
    }
  });

  let totalOutputHtml = coreHtml;

  if (hasAdvanced) {
    totalOutputHtml += `
      <div id="advanced-stats-container" style="display: none; width: 100%; overflow: hidden;">
        ${advancedHtml}
      </div>
      <div style="text-align: center; margin-top: 15px; margin-bottom: 10px;">
        <button id="toggle-advanced-btn" onclick="toggleAdvancedStats()" style="background-color: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 10px 20px; border-radius: 6px; font-weight: 600; font-size: 13px; cursor: pointer; transition: background-color 0.2s;">
          Show advanced statistics ▾
        </button>
      </div>
      <script>
        function toggleAdvancedStats() {
          var container = document.getElementById('advanced-stats-container');
          var btn = document.getElementById('toggle-advanced-btn');
          if (container.style.display === 'none') {
            container.style.display = 'block';
            btn.innerHTML = 'Hide advanced statistics ▴';
            btn.style.backgroundColor = '#e2e8f0';
          } else {
            container.style.display = 'none';
            btn.innerHTML = 'Show advanced statistics ▾';
            btn.style.backgroundColor = '#f1f5f9';
          }
        }
      </script>
    `;
  }

  return totalOutputHtml; 
}

// =========================================================================
// RENDER HTML TEMPLATES
// =========================================================================

function generateEnglishHTML(matches, currentTab, verificationTag, showAds, country) { 
  let rows = "";
  let finishedCount = 0; let wonCount = 0; 
  if (matches.length === 0) { 
    rows = `<tr><td colspan="5" style="text-align:center; padding: 40px; color: #888;">No matches available for this date.</td></tr>`;
  } else { 
    matches.forEach(m => { 
      const scoreText = (m.home_score !== null && m.away_score !== null) ? `${m.home_score} - ${m.away_score}` : 'vs'; 
      const statusBadge = m.status === "Live" ? `<span class="status-badge live-pulse">LIVE</span>` : `<span class="status-badge">${m.status || 'Scheduled'}</span>`; 
      
      let pronostico = m.prediction || calcolaPronosticoReale(m.home_odds, m.draw_odds, m.away_odds); 
      if (m.home_team && m.home_team.includes("Belgium") && m.away_team && m.away_team.includes("Senegal")) {
        pronostico = "12";
      }
      
      const classeEsito = determinaClasseEsito(m.status, m.home_score, m.away_score, pronostico); 
      const esitoVinto = controllaSeVinto(m.status, m.home_score, m.away_score, pronostico); 
      if (esitoVinto !== null) { finishedCount++; if (esitoVinto === true) wonCount++; } 
      const nomeCampionato = m.league_name || ""; 
      const leagueBadge = nomeCampionato ? `<div class="league-title">${nomeCampionato}</div>` : '';
      
      // OPTIMIZATION (SEO): Abbiamo trasformato le righe della tabella in veri link semantici HTML <a> 
      // per consentire a Googlebot di scoprire tutte le sotto-pagine in modo naturale durante lo scraping.
      rows += `
        <tr class="clickable-row">
          <td><a href="?match_id=${m.id}">${m.match_time || '--:--'}</a></td>
          <td style="text-align: left;">
            <a href="?match_id=${m.id}">
              ${leagueBadge}
              <b>${m.home_team}</b><br>${m.away_team}
            </a>
          </td>
          <td><a href="?match_id=${m.id}"><b>${scoreText}</b></a></td>
          <td><a href="?match_id=${m.id}"><span class="pred-badge ${classeEsito}">${pronostico}</span></a></td>
          <td><a href="?match_id=${m.id}">${statusBadge}</a></td>
        </tr>
      `;
    }); 
  } 
  let winRateHtml = ""; 
  if (finishedCount > 0) { 
    const percentage = Math.round((wonCount / finishedCount) * 100);
    winRateHtml = ` <div class="winrate-widget"> <div class="winrate-info"> <span>🎯 <b>Daily Win Rate:</b> ${percentage}%</span> <span class="winrate-stats">(${wonCount} of ${finishedCount} won)</span> </div> <div class="winrate-bar-bg"> <div class="winrate-bar-fill" style="width: ${percentage}%;"></div> </div> </div> `;
  } 
  
  let adsWidgetHtml = ""; 
  if (showAds) { 
    adsWidgetHtml = ` <div class="ads-widget"> <div class="ads-content"> 🚀 <b>Premium Predictions Active for ${country}!</b> Click below to unlock special statistical insights and external server sheets.
    </div> <a href="https://omg10.com/4/11162345" target="_blank" class="ads-button">Unlock Advanced Stats</a> </div> `; 
  } 
  
  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">${verificationTag}<title>Lopislab - Data-Driven Football Statistics & Picks</title><style>body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; color: #333; } header { background-color: #1e293b; padding: 0px 20px; text-align: center; cursor: pointer; display: flex; justify-content: center; align-items: center; box-sizing: border-box; overflow: hidden; height: 130px; } .logo-img { height: 320px; max-height: 40vh; width: auto; object-fit: contain; mix-blend-mode: screen; filter: brightness(1.15) contrast(1.15); margin: -95px 0; display: block; } .date-nav { display: flex; justify-content: center; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); } .date-nav a { padding: 15px 25px; text-decoration: none; color: #64748b; font-weight: 600; font-size: 15px; } .date-nav a.active { color: #2563eb; border-bottom: 3px solid #2563eb; background-color: #f8fafc; } .container { max-width: 900px; margin: 25px auto; padding: 0 15px; } .winrate-widget { background: white; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 4px solid #10b981; } .winrate-info { display: flex; justify-content: space-between; align-items: center; font-size: 15px; margin-bottom: 8px; color: #1e293b; } .winrate-stats { font-size: 13px; color: #64748b; font-weight: 500; } .winrate-bar-bg { height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; } .winrate-bar-fill { height: 100%; background: linear-gradient(90deg, #10b981, #059669); border-radius: 4px; transition: width 0.5s ease-in-out; } .ads-widget { background: linear-gradient(135deg, #1e293b, #0f172a); border-radius: 8px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.15); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; border-left: 4px solid #e11d48; color: white; } .ads-content { font-size: 14px; max-width: 600px; line-height: 1.4; } .ads-button { background-color: #e11d48; color: white; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; font-size: 14px; transition: transform 0.2s, background-color 0.2s; } .ads-button:hover { background-color: #be123c; transform: scale(1.03); } table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); } th { background-color: #334155; color: white; padding: 14px; text-align: center; font-size: 14px; text-transform: uppercase; } td { padding: 0; text-align: center; border-bottom: 1px solid #e2e8f0; font-size: 14px; } .clickable-row:hover { background-color: #f8fafc; } .clickable-row td a { display: block; padding: 14px; text-decoration: none; color: inherit; width: 100%; height: 100%; box-sizing: border-box; } .league-title { font-size: 11px; color: #94a3b8; font-weight: 600; text-transform: uppercase; margin-bottom: 3px; letter-spacing: 0.5px; } .pred-badge { color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; display: inline-block; min-width: 32px; } .pred-badge-neutral { background-color: #22c55e; } .pred-badge-win { background-color: #10b981; border: 1px solid #047857; } .pred-badge-lose { background-color: #ef4444; border: 1px solid #b91c1c; } .status-badge { background-color: #cbd5e1; color: #334155; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; } .status-badge.live-pulse { background-color: #ef4444; color: white; animation: pulse 1.5s infinite; } @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }</style></head><body><header onclick="window.location.href='/'"><img src="https://www.lifesmartworld.net/wp-content/uploads/2026/06/WhatsApp-Image-2026-06-19-at-12.51.20-1.jpeg" alt="Lopislab Logo" class="logo-img"></header><div class="date-nav"><a href="?date=yesterday" class="${currentTab === 'yesterday' ? 'active' : ''}">Yesterday</a><a href="/" class="${currentTab === 'today' ? 'active' : ''}">Today</a><a href="?date=tomorrow" class="${currentTab === 'tomorrow' ? 'active' : ''}">Tomorrow</a></div><div class="container">${adsWidgetHtml}${winRateHtml}<table><thead><tr><th style="width: 15%;">Time</th><th style="width: 45%; text-align: left;">Match</th><th style="width: 15%;">Score</th><th style="width: 12%;">Pick</th><th style="width: 13%;">Status</th></tr></thead><tbody>${rows}</tbody></table><footer style="margin-top: 40px; padding: 25px 20px; text-align: center; color: #64748b; font-size: 13px; line-height: 1.6; border-top: 1px solid #e2e8f0;"><p style="margin: 0 0 8px 0; font-size: 14px; color: #1e293b;">📊 <b>Lopislab Sports Analytics Lab</b></p><p style="margin: 0 0 12px 0;">Our proprietary analytics engine processes historical data and betting odds to generate <b>real-time football algorithm picks</b> for major global leagues. We provide premium, <b>data-driven 1X2 football stats</b> to help analysts and enthusiasts track global sports trends. Monitor our <b>daily football win rate tracker</b> to check the live accuracy of our laboratory system.</p><p style="margin: 0; font-size: 11px; color: #94a3b8;">© 2026 Lopislab. All rights reserved. Play responsibly (18+).</p></footer></div></body></html>`; 
}

function generateMatchDetailsSkeleton(m, h2hData, statsData, verificationTag, showAds, country, isLiveUpdate) { 
  const scoreText = (m.home_score !== null && m.away_score !== null) ? `${m.home_score} - ${m.away_score}` : 'vs'; 
  
  let finalPick = m.prediction || calcolaPronosticoReale(m.home_odds, m.draw_odds, m.away_odds); 
  if (m.home_team && m.home_team.includes("Belgium") && m.away_team && m.away_team.includes("Senegal")) {
    finalPick = "12";
  }
  
  const goalsPick = calcolaConsiglioUnderOver(m.home_team, m.away_team, h2hData); 
  const h2hHtmlVisivo = calcolaH2HVisivo(m.home_team, m.away_team, h2hData); 
  const statsHtmlVisivo = calcolaStatsVisive(statsData?.match || statsData); 
  
  const classeEsitoDettaglio = determinaClasseEsito(m.status, m.home_score, m.away_score, finalPick); 
  const h2hBlock = h2hHtmlVisivo ? `<div class="stat-section"><div class="section-title">Team Form & Head to Head (H2H)</div>${h2hHtmlVisivo}</div>` : `<div class="stat-section"><div class="section-title">Team Form & Head to Head (H2H)</div><div style="color: #64748b; font-size: 14px; text-align: left; font-style: italic;">Historical H2H data not available for this match.</div></div>`; 
  const statsBlock = `<div class="stat-section"><div class="section-title">Match Statistics</div>${statsHtmlVisivo}</div>`; 
  const nomeCampionatoDettaglio = m.league_name || ""; const dettagliCampionato = nomeCampionatoDettaglio ? ` • <b>${nomeCampionatoDettaglio}</b>` : ''; 
  
  let homeLogoHtml = "";
  let awayLogoHtml = "";
  try {
    const rawJSON = m.raw_data ? JSON.parse(m.raw_data) : null;
    if (rawJSON) {
      const homeId = rawJSON.home_team?.id;
      const awayId = rawJSON.away_team?.id;
      if (homeId) {
        homeLogoHtml = `<img src="https://www.flashscore.com/res/image/data/t_g_${homeId}_1.png" class="team-logo" style="width: 28px; height: 28px; margin-right: 10px; object-fit: contain; vertical-align: middle;" onerror="this.style.display='none';" />`;
      }
      if (awayId) {
        awayLogoHtml = `<img src="https://www.flashscore.com/res/image/data/t_g_${awayId}_1.png" class="team-logo" style="width: 28px; height: 28px; margin-left: 10px; object-fit: contain; vertical-align: middle;" onerror="this.style.display='none';" />`;
      }
    }
  } catch (e) { console.log("Logo generation error: " + e.message); }

  let dataBadgeHtml = "";
  if (m.status === "Live" || isLiveUpdate) {
    dataBadgeHtml = `<span class="data-badge live" style="background-color: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px;"><span class="pulse-dot"></span>🟢 Live data</span>`;
  } else {
    dataBadgeHtml = `<span class="data-badge cached" style="background-color: #fef9c3; color: #a16207; border: 1px solid #fef08a; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px;">🟡 Cached data</span>`;
  }

  const canonicalUrl = `https://lopislab.com/?match_id=${m.id}`;
  const seoTitle = `${m.home_team} vs ${m.away_team} Prediction, H2H & Live Stats | Lopislab`;
  const seoDescription = `Get the best algorithmic football pick, head-to-head records, form guide, and live statistics for ${m.home_team} vs ${m.away_team}${nomeCampionatoDettaglio ? ' in ' + nomeCampionatoDettaglio : ''}. Data-driven sports trends by Lopislab.`;

  let schemaStatus = "https://schema.org/EventScheduled";
  if (m.status === "Live") schemaStatus = "https://schema.org/EventLive";
  else if (m.status === "Finished") schemaStatus = "https://schema.org/EventPostponed"; 

  const schemaJson = {
    "@context": "https://schema.org",
    "@type": "SportsEvent",
    "name": `${m.home_team} vs ${m.away_team}`,
    "description": seoDescription,
    "startDate": `${m.match_date}T${m.match_time || '00:00'}:00+02:00`,
    "eventStatus": schemaStatus,
    "homeTeam": { "@type": "SportsTeam", "name": m.home_team },
    "awayTeam": { "@type": "SportsTeam", "name": m.away_team },
    "sport": "https://en.wikipedia.org/wiki/Association_football"
  };
  if (nomeCampionatoDettaglio) {
    schemaJson.competitor = [
      { "@type": "SportsTeam", "name": m.home_team },
      { "@type": "SportsTeam", "name": m.away_team }
    ];
  }

  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">${verificationTag}<title>${seoTitle}</title><meta name="description" content="${seoDescription}"><link rel="canonical" href="${canonicalUrl}"><script type="application/ld+json">${JSON.stringify(schemaJson)}</script><style>body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; color: #333; } header { background-color: #1e293b; padding: 0px 20px; text-align: center; cursor: pointer; display: flex; justify-content: center; align-items: center; box-sizing: border-box; overflow: hidden; height: 130px; } .logo-img { height: 320px; max-height: 40vh; width: auto; object-fit: contain; mix-blend-mode: screen; filter: brightness(1.15) contrast(1.15); margin: -95px 0; display: block; } .back-btn { display: inline-block; margin: 15px 0; color: #2563eb; text-decoration: none; font-weight: 600; font-size: 15px; } .container { max-width: 800px; margin: 10px auto; padding: 0 15px; } .match-board { background: white; border-radius: 12px; padding: 30px 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.06); margin-bottom: 25px; } .match-info { color: #64748b; font-size: 14px; margin-bottom: 15px; display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 5px; } .teams-row { display: flex; justify-content: space-between; align-items: center; max-width: 600px; margin: 0 auto; gap: 10px; } .team-box { flex: 1; font-size: 17px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: center; } .score-box { font-size: 28px; font-weight: 800; color: #2563eb; padding: 0 10px; white-space: nowrap; display: inline-block; } .prediction-container { display: flex; justify-content: center; gap: 20px; margin-top: 25px; flex-wrap: wrap; } .prediction-box { background: #f8fafc; border-radius: 8px; padding: 12px 20px; border: 1px solid #e2e8f0; min-width: 160px; } .pred-title { font-size: 11px; color: #64748b; text-transform: uppercase; margin-bottom: 5px; font-weight: bold; } .pred-value { color: white; display: inline-block; padding: 4px 18px; border-radius: 6px; font-size: 20px; font-weight: 800; } .pred-badge-neutral { background-color: #22c55e; } .pred-badge-win { background-color: #10b981; border: 1px solid #047857; } .pred-badge-lose { background-color: #ef4444; border: 1px solid #b91c1c; } .pred-value.goals { background: #3b82f6; } .stat-section { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.06); margin-bottom: 25px; } .section-title { font-size: 15px; font-weight: bold; text-transform: uppercase; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 20px; text-align: left; } .h2h-row { display: flex; justify-content: space-between; align-items: center; } .h2h-circles { display: flex; gap: 8px; } .circle { display: inline-flex; width: 26px; height: 26px; border-radius: 50%; color: white; font-weight: bold; justify-content: center; align-items: center; font-size: 12px; } .badge-w { background-color: #22c55e; } .badge-d { background-color: #eab308; } .badge-l { background-color: #ef4444; } .pulse-dot { width: 6px; height: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; animation: pulse-anim 1.5s infinite; } @keyframes pulse-anim { 0% { transform: scale(0.9); opacity: 1; } 50% { transform: scale(1.4); opacity: 0.5; } 100% { transform: scale(0.9); opacity: 1; } }</style></head><body><header onclick="window.location.href='/'"><img src="https://www.lifesmartworld.net/wp-content/uploads/2026/06/WhatsApp-Image-2026-06-19-at-12.51.20-1.jpeg" alt="Lopislab Logo" class="logo-img"></header><div class="container"><a href="/" class="back-btn">← Back to Palimpsest</a><div class="match-board"><div class="match-info">📅 ${m.match_date} ${dettagliCampionato} ${dataBadgeHtml}</div><div class="teams-row"><div class="team-box" style="justify-content: flex-end;">${homeLogoHtml}${m.home_team}</div><div class="score-box">${scoreText}</div><div class="team-box" style="justify-content: flex-start;">${m.away_team}${awayLogoHtml}</div></div><div class="prediction-container"><div class="prediction-box"><div class="pred-title">1X2 Pick</div><div class="pred-value ${classeEsitoDettaglio}">${finalPick}</div></div><div class="prediction-box"><div class="pred-title">Goals Pick</div><div class="pred-value goals">${goalsPick}</div></div></div></div>${h2hBlock}${statsBlock}</div></body></html>`;
}
