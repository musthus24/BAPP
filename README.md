# BAPP: Basketball Analytics Performance Platform

**Status:** scaffold created; building features step-by-step for learning and clarity.

## What this is
A cloud-hosted platform that ingests NBA data, stores it in SQL, computes core basketball metrics, serves them via a tiny API, and visualizes them in a single-page web UI. It demonstrates end-to-end data + software engineering aligned with an NBA Basketball Operations SWE internship.

## Why it matters (for Basketball Ops)
- **Faster decisions:** quick view of a player’s form and lineup performance.
- **Reliable pipeline:** ingestion → storage → metrics → API → UI, with CI.
- **Extensible:** clean schema + FastAPI make adding new metrics straightforward   

---

## MVP Scope
- **Data:** one recent season of games, players, and box scores.
- **Storage:** SQLite (MVP) with clean tables and a couple of views for reads.
- **Metrics:** TS%, Usage%, rolling eFG% (last 10), team/lineup Off/Def/Net Rating (simple pace estimate OK).
- **API:**
  - `GET /players/search?q=`
  - `GET /players/{id}/summary` (season averages + last-10 trend)
  - `GET /teams/{id}/lineups/top` (top 5 by net rating)
- **UI:** static HTML/JS page with Plotly charts + sortable lineup table.
- **Deploy:** Azure App Service (HTTPS, env vars, basic logging).
- **CI:** GitHub Actions runs tests on push.

**Non-goals (MVP):** authentication/roles, full play-by-play fidelity, advanced models.
