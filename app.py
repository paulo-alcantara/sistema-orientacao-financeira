import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sistema de Orientação Financeira",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def img_to_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

base_dir = Path(__file__).parent
hero_path = base_dir / "hero_background.png"
quiz_path = base_dir / "tela2_xp_style_bg.png"

if not hero_path.exists():
    st.error("Arquivo hero_background.png não encontrado na pasta do projeto.")
    st.stop()

if not quiz_path.exists():
    st.error("Arquivo tela2_xp_style_bg.png não encontrado na pasta do projeto.")
    st.stop()

hero_bg = img_to_base64(hero_path)
quiz_bg = img_to_base64(quiz_path)

st.markdown("""
<style>
html, body, [class*="css"] {
    margin: 0 !important;
    padding: 0 !important;
}

.stApp {
    background: #040816;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100vw !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

#MainMenu, footer {
    visibility: hidden !important;
}

div[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
    position: fixed !important;
}

div[data-testid="stAppViewContainer"],
div[data-testid="stMain"],
div[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100vw !important;
}

iframe {
    border: none !important;
    width: 100vw !important;
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
* {
    box-sizing: border-box;
    font-family: Inter, Arial, sans-serif;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}

/* =========================
   BASE
========================= */

.screen {
    position: relative;
    width: 100vw;
    height: 100vh;
    min-height: 860px;
    overflow: hidden;
    display: none;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
}

select option {
    background: #0b1024;
    color: #FFFFFF;
}

.screen.active {
    display: flex;
}

/* =========================
   TELA 1
========================= */

.hero {
    min-height: 700px;
    background:
        linear-gradient(rgba(5, 8, 22, 0.30), rgba(5, 8, 22, 0.45)),
        url("__HERO_BG__");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
}

.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at center, rgba(125, 95, 255, 0.14), transparent 38%);
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 2;
    width: min(980px, 90vw);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transform: translateY(-12px);
}

.hero-title {
    margin: 0 0 24px 0;
    max-width: 1000px;
    font-size: clamp(2.7rem, 5vw, 4.8rem);
    line-height: 1.04;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #FFFFFF;
    text-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.hero-subtitle {
    margin: 0 0 34px 0;
    max-width: 920px;
    font-size: clamp(1.05rem, 1.65vw, 1.42rem);
    line-height: 1.65;
    color: rgba(237, 239, 255, 0.90);
    text-shadow: 0 6px 20px rgba(0, 0, 0, 0.30);
}

.cta {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    min-width: 320px;
    height: 68px;
    padding: 0 34px;
    border: 0;
    border-radius: 20px;
    font-size: 1.22rem;
    font-weight: 700;
    color: #FFFFFF;
    background: linear-gradient(90deg, #5B49FF 0%, #8577FF 100%);
    box-shadow: 0 14px 35px rgba(98, 80, 255, 0.35);
    transition: transform 0.22s ease, box-shadow 0.22s ease, filter 0.22s ease, background 0.22s ease;
    cursor: pointer;
}

.cta:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 18px 42px rgba(122, 105, 255, 0.48);
    filter: brightness(1.08);
    background: linear-gradient(90deg, #7364FF 0%, #A092FF 100%);
}

/* =========================
   QUESTIONÁRIO
========================= */

.quiz {
    background:
        linear-gradient(rgba(4, 8, 22, 0.74), rgba(4, 8, 22, 0.82)),
        url("__QUIZ_BG__");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
}

.quiz::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at center, rgba(105, 87, 255, 0.10), transparent 40%);
    pointer-events: none;
}

.quiz-wrap {
    position: relative;
    z-index: 2;
    width: min(1180px, 90vw);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.progress-wrap {
    width: min(1220px, 92vw);
    margin-bottom: 34px;
}

.progress-track {
    width: 100%;
    height: 8px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.10);
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #2B8EFF 0%, #5B7BFF 100%);
    box-shadow: 0 0 18px rgba(67, 125, 255, 0.35);
    transition: width 0.25s ease;
}

.quiz-title {
    margin: 0 0 20px 0;
    max-width: 980px;
    font-size: clamp(2.5rem, 5vw, 4.6rem);
    line-height: 1.06;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #FFFFFF;
    text-shadow: 0 8px 30px rgba(0,0,0,0.35);
}

.quiz-subtitle {
    margin: 0 0 34px 0;
    max-width: 1080px;
    font-size: clamp(1.02rem, 1.5vw, 1.45rem);
    line-height: 1.65;
    color: rgba(234, 238, 255, 0.92);
    text-shadow: 0 6px 18px rgba(0,0,0,0.34);
}

.question {
    margin: 0 0 22px 0;
    font-size: clamp(1.15rem, 1.8vw, 1.7rem);
    font-weight: 700;
    color: #FFFFFF;
}

.options {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px 28px;
    margin-bottom: 28px;
}

.option {
    width: 100%;
    min-height: 96px;
    padding: 18px 28px;
    text-align: left;
    border: none;
    border-left: 4px solid #2B8EFF;
    background: rgba(249, 249, 250, 0.95);
    color: #0F172A;
    font-size: 0.98rem;
    line-height: 1.45;
    font-weight: 500;
    cursor: pointer;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.18);
    transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease, border-left-color 0.18s ease;
}

.option:hover {
    transform: translateY(-2px);
    background: #FFFFFF;
    box-shadow: 0 16px 38px rgba(0, 0, 0, 0.24);
}

.option.selected {
    background: linear-gradient(90deg, rgba(97, 78, 255, 0.96), rgba(132, 118, 255, 0.96));
    color: #FFFFFF;
    border-left-color: #FFFFFF;
    box-shadow: 0 18px 42px rgba(99, 80, 255, 0.32);
}

.nav {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 22px;
    margin-top: 10px;
}

.btn {
    min-width: 150px;
    height: 58px;
    padding: 0 24px;
    border-radius: 0;
    font-size: 1.03rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-back {
    border: 1px solid rgba(255,255,255,0.78);
    background: rgba(0, 0, 0, 0.18);
    color: #FFFFFF;
}

.btn-back:hover {
    transform: translateY(-2px);
    background: rgba(16, 20, 44, 0.72);
}

.btn-next {
    border: none;
    background: rgba(255,255,255,0.75);
    color: rgba(33, 37, 48, 0.62);
    cursor: not-allowed;
    pointer-events: none;
}

.btn-next.enabled {
    background: linear-gradient(90deg, #5B49FF 0%, #8577FF 100%);
    color: #FFFFFF;
    box-shadow: 0 12px 30px rgba(103, 80, 255, 0.30);
    cursor: pointer;
    pointer-events: auto;
}

.btn-next.enabled:hover {
    transform: translateY(-2px);
    background: linear-gradient(90deg, #7263FF 0%, #9B8EFF 100%);
    box-shadow: 0 16px 38px rgba(103, 80, 255, 0.42);
}

.helper {
    margin-top: 12px;
    min-height: 22px;
    font-size: 0.95rem;
    color: rgba(236, 239, 255, 0.74);
}

/* =========================
   TELA 6 - RESULTADO DO PERFIL
========================= */

.result {
    align-items: flex-start;
    justify-content: center;
    background:
        radial-gradient(circle at top left, rgba(91, 73, 255, 0.24), transparent 34%),
        radial-gradient(circle at bottom right, rgba(43, 142, 255, 0.18), transparent 32%),
        linear-gradient(180deg, #050816 0%, #090D1F 100%);
    overflow-y: auto;
    padding: 42px 0 54px;
}

.result-shell { width: min(1180px, 92vw); }

.result-header {
    background: rgba(15,19,40,0.86);
    border: 1px solid rgba(126,114,255,0.22);
    border-radius: 30px;
    padding: 34px;
    box-shadow: 0 18px 60px rgba(0,0,0,0.35);
    margin-bottom: 26px;
}
.result-kicker {
    margin: 0 0 12px;
    color: rgba(234, 238, 255, 0.72);
    font-size: 0.95rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}
.result-title {
    margin: 0;
    font-size: clamp(2.2rem, 4.8vw, 4.6rem);
    line-height: 1.02;
    letter-spacing: -0.045em;
}
.result-title span { color: var(--profile-color); }
.result-desc {
    max-width: 880px;
    margin: 18px 0 0;
    font-size: 1.12rem;
    line-height: 1.68;
    color: rgba(236,239,255,0.88);
}
.recommend-title { margin: 4px 0 12px; font-size: clamp(1.8rem, 3vw, 2.5rem); letter-spacing: -0.03em; }
.recommend-subtitle { max-width: 850px; margin: 0 0 28px; color: rgba(236,239,255,0.78); line-height: 1.55; }
.result-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 18px; }
.asset-card {
    min-height: 355px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 22px;
    padding: 20px;
    box-shadow: 0 16px 38px rgba(0,0,0,0.22);
    backdrop-filter: blur(8px);
}
.asset-card h3 { margin: 0 0 10px; font-size: 1.1rem; color: #FFFFFF; }
.asset-card p { margin: 0 0 14px; color: rgba(236,239,255,0.78); line-height: 1.48; font-size: 0.92rem; }
.asset-tags { display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }
.asset-tag {
    display: inline-flex;
    padding: 6px 10px;
    border-radius: 999px;
    color: #FFFFFF;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.10);
    font-size: 0.78rem;
}
.asset-details { margin-top: 12px; }
.asset-details summary { cursor: pointer; color: var(--profile-color); font-weight: 800; font-size: 0.9rem; }
.asset-details ul { padding-left: 18px; margin: 12px 0 0; color: rgba(236,239,255,0.78); line-height: 1.55; font-size: 0.86rem; }
.glossary { margin-top: 26px; background: rgba(255,255,255,0.055); border: 1px solid rgba(255,255,255,0.10); border-radius: 24px; padding: 24px; }
.glossary h2 { margin: 0 0 14px; }
.glossary-row { display: flex; flex-wrap: wrap; gap: 10px; }
.term { position: relative; padding: 9px 13px; border-radius: 999px; background: rgba(255,255,255,0.09); border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.9); font-size: 0.9rem; }
.term:hover::after {
    content: attr(data-tip);
    position: absolute;
    left: 0;
    bottom: 125%;
    width: 280px;
    padding: 12px;
    border-radius: 14px;
    background: #111827;
    color: #FFFFFF;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 16px 32px rgba(0,0,0,0.36);
    z-index: 10;
    line-height: 1.4;
}
.result-actions {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    width: 100%;
    margin-top: 28px;
}
.result-actions .btn-soft {
    justify-self: start;
    min-width: 160px;
    height: 48px;
    opacity: 0.78;
    background: rgba(255,255,255,0.055);
}
.result-actions .btn-soft:hover { opacity: 1; }
.result-actions .cta {
    justify-self: center;
    grid-column: 2;
}


/* =========================
   TELA 7 - MONTAGEM DA CARTEIRA
========================= */

.portfolio {
    align-items: flex-start;
    justify-content: center;
    background:
        radial-gradient(circle at top left, rgba(91, 73, 255, 0.24), transparent 34%),
        radial-gradient(circle at bottom right, rgba(43, 142, 255, 0.18), transparent 32%),
        linear-gradient(180deg, #050816 0%, #090D1F 100%);
    overflow-y: auto;
    padding: 42px 0 60px;
}
.portfolio-shell { width: min(1180px, 92vw); }
.portfolio-header { background: rgba(15,19,40,0.86); border: 1px solid rgba(126,114,255,0.22); border-radius: 30px; padding: 34px; box-shadow: 0 18px 60px rgba(0,0,0,0.35); margin-bottom: 26px; }
.portfolio-kicker { margin: 0 0 12px; color: rgba(234, 238, 255, 0.72); font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; }
.portfolio-title { margin: 0; font-size: clamp(2.2rem, 4.5vw, 4.2rem); line-height: 1.02; letter-spacing: -0.045em; }
.portfolio-title span { color: var(--profile-color); }
.portfolio-desc { max-width: 900px; margin: 18px 0 0; font-size: 1.08rem; line-height: 1.68; color: rgba(236,239,255,0.86); }
.portfolio-layout { display: grid; grid-template-columns: 1.55fr 0.9fr; gap: 22px; align-items: start; }
.allocation-panel, .summary-panel, .diversification-callout { background: rgba(255,255,255,0.065); border: 1px solid rgba(255,255,255,0.12); border-radius: 24px; padding: 24px; box-shadow: 0 16px 38px rgba(0,0,0,0.22); backdrop-filter: blur(8px); }
.allocation-panel h2, .summary-panel h2 { margin: 0 0 8px; font-size: 1.45rem; }
.allocation-subtitle, .summary-subtitle { margin: 0 0 20px; color: rgba(236,239,255,0.72); line-height: 1.55; }
.slider-card { background: rgba(255,255,255,0.055); border: 1px solid rgba(255,255,255,0.10); border-radius: 18px; padding: 16px; margin-bottom: 14px; }
.slider-top { display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-bottom: 10px; }
.slider-name { font-weight: 800; color: #FFFFFF; }
.slider-value { font-weight: 900; color: var(--profile-color); font-size: 1.12rem; min-width: 54px; text-align: right; }
.slider-card input[type="range"] { width: 100%; accent-color: var(--profile-color); cursor: pointer; }
.slider-hint { margin-top: 7px; color: rgba(236,239,255,0.60); font-size: 0.82rem; line-height: 1.35; }
.total-number { font-size: clamp(2.2rem, 5vw, 4rem); line-height: 1; font-weight: 900; color: var(--profile-color); margin: 10px 0 10px; letter-spacing: -0.04em; }
.total-bar { width: 100%; height: 12px; border-radius: 999px; background: rgba(255,255,255,0.10); overflow: hidden; margin: 12px 0 18px; }
.total-fill { height: 100%; width: 0%; border-radius: 999px; background: linear-gradient(90deg, var(--profile-color), #8577FF); transition: width 0.22s ease; }
.status-box { border-radius: 18px; padding: 16px; background: rgba(0,0,0,0.18); border: 1px solid rgba(255,255,255,0.10); color: rgba(236,239,255,0.84); line-height: 1.5; margin-bottom: 18px; }
.portfolio-warning { color: #fbbf24; font-weight: 750; margin-top: 10px; }
.portfolio-actions { display: flex; justify-content: center; align-items: center; margin-top: 22px; }
.portfolio-bottom-actions { display: flex; justify-content: flex-start; margin-top: 24px; }
.btn-soft { min-width: 160px; height: 54px; padding: 0 20px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.18); background: rgba(255,255,255,0.08); color: #FFFFFF; font-weight: 800; cursor: pointer; transition: all 0.2s ease; }
.btn-soft:hover { transform: translateY(-2px); background: rgba(255,255,255,0.12); }
.btn-continue-portfolio { min-width: 320px; height: 64px; padding: 0 28px; border-radius: 18px; border: none; font-size: 1.05rem; font-weight: 900; color: rgba(255,255,255,0.56); background: rgba(255,255,255,0.16); cursor: not-allowed; }
.btn-continue-portfolio.enabled { color: #FFFFFF; background: linear-gradient(90deg, #5B49FF 0%, #8577FF 100%); cursor: pointer; box-shadow: 0 12px 30px rgba(103, 80, 255, 0.30); }
.btn-continue-portfolio.enabled:hover { transform: translateY(-2px); }
.pill-list { display: grid; gap: 10px; margin-top: 12px; }
.pill-row { display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 10px 12px; border-radius: 14px; background: rgba(255,255,255,0.06); color: rgba(236,239,255,0.82); font-size: 0.9rem; }
.pill-row strong { color: #FFFFFF; }
.diversification-callout { margin: 0 0 24px; position: relative; overflow: hidden; border-color: rgba(255,255,255,0.18); }
.diversification-callout::before { content: ""; position: absolute; inset: -80px auto auto -80px; width: 220px; height: 220px; border-radius: 999px; background: var(--profile-color); opacity: 0.18; filter: blur(10px); }
.diversification-callout h2 { position: relative; margin: 0 0 8px; font-size: clamp(1.45rem, 2.6vw, 2rem); letter-spacing: -0.03em; }
.diversification-callout p { position: relative; max-width: 1000px; margin: 0; font-size: 1.08rem; line-height: 1.55; color: rgba(255,255,255,0.92); font-weight: 650; }
@media (max-width: 980px) { .portfolio-layout { grid-template-columns: 1fr; } }


/* =========================
   TELA 8 - SIMULAÇÃO
========================= */
.simulation {
    align-items: flex-start;
    justify-content: center;
    background:
        radial-gradient(circle at top left, rgba(91, 73, 255, 0.24), transparent 34%),
        radial-gradient(circle at bottom right, rgba(43, 142, 255, 0.18), transparent 32%),
        linear-gradient(180deg, #050816 0%, #090D1F 100%);
    overflow-y: auto;
    padding: 42px 0 60px;
}
.simulation-shell { width: min(1180px, 92vw); }
.simulation-header { background: rgba(15,19,40,0.86); border: 1px solid rgba(126,114,255,0.22); border-radius: 30px; padding: 34px; box-shadow: 0 18px 60px rgba(0,0,0,0.35); margin-bottom: 26px; }
.simulation-kicker { margin: 0 0 12px; color: rgba(234, 238, 255, 0.72); font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; }
.simulation-title { margin: 0; font-size: clamp(2.2rem, 4.5vw, 4.2rem); line-height: 1.02; letter-spacing: -0.045em; }
.simulation-title span { color: var(--profile-color); }
.simulation-desc { max-width: 900px; margin: 18px 0 0; font-size: 1.08rem; line-height: 1.68; color: rgba(236,239,255,0.86); }
.simulation-inputs, .chart-panel, .table-panel, .simulation-note, .educational-panel, .emotional-panel { background: rgba(255,255,255,0.065); border: 1px solid rgba(255,255,255,0.12); border-radius: 24px; padding: 24px; box-shadow: 0 16px 38px rgba(0,0,0,0.22); backdrop-filter: blur(8px); margin-bottom: 22px; }
.simulation-input-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 18px 0 22px; }
.input-group label { display: block; margin-bottom: 8px; font-weight: 800; color: #FFFFFF; }
.input-group input { width: 100%; height: 54px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.14); background: rgba(0,0,0,0.18); color: #FFFFFF; font-size: 1.05rem; padding: 0 14px; outline: none; }
.input-group input:focus { border-color: var(--profile-color); box-shadow: 0 0 0 3px rgba(255,255,255,0.06); }
.simulation-actions { display: flex; justify-content: center; }
.simulation-actions .cta { min-width: 320px; height: 64px; }
.results-summary { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 22px; }
.summary-card { background: rgba(255,255,255,0.055); border: 1px solid rgba(255,255,255,0.10); border-radius: 18px; padding: 18px; }
.summary-card span { display: block; color: rgba(236,239,255,0.68); font-size: 0.9rem; margin-bottom: 8px; }
.summary-card strong { display: block; font-size: clamp(1.35rem, 2.4vw, 2rem); color: var(--profile-color); }
.chart-wrap { width: 100%; height: 380px; }
.sim-table-wrap { overflow-x: auto; }
.sim-table { width: 100%; border-collapse: collapse; min-width: 850px; overflow: hidden; border-radius: 16px; }
.sim-table th { background: linear-gradient(90deg, #5B49FF, #8577FF); color: #FFFFFF; text-align: right; padding: 14px 12px; font-size: 0.88rem; }
.sim-table th:first-child, .sim-table td:first-child { text-align: left; }
.sim-table td { border-bottom: 1px solid rgba(255,255,255,0.10); color: rgba(236,239,255,0.84); padding: 13px 12px; text-align: right; font-size: 0.9rem; }
.sim-table tr:last-child td { background: rgba(43, 142, 255, 0.12); color: #FFFFFF; font-weight: 900; }
.simulation-note { color: rgba(236,239,255,0.74); line-height: 1.55; font-size: 0.94rem; }
.educational-panel { background: linear-gradient(135deg, rgba(91,73,255,0.12), rgba(43,142,255,0.08)); }
.educational-panel summary { cursor: pointer; list-style: none; font-size: clamp(1.25rem, 2vw, 1.65rem); font-weight: 800; color: #FFFFFF; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.educational-panel summary::-webkit-details-marker { display: none; }
.educational-panel summary::after { content: "▾"; font-size: 1.3rem; color: var(--profile-color); transition: transform 0.2s ease; }
.educational-panel[open] summary::after { transform: rotate(180deg); }
.educational-panel .edu-content { margin-top: 18px; color: rgba(236,239,255,0.82); line-height: 1.7; }
.educational-panel .formula-box { margin-top: 14px; padding: 16px; border-radius: 16px; background: rgba(255,255,255,0.065); border: 1px solid rgba(255,255,255,0.10); font-weight: 700; color: #FFFFFF; }
.emotional-panel { margin-top: 8px; background: linear-gradient(135deg, rgba(239,68,68,0.12), rgba(91,73,255,0.11)); }
.emotional-panel h2 { margin: 0 0 12px; font-size: clamp(1.6rem, 2.4vw, 2.2rem); }
.emotional-panel p { color: rgba(236,239,255,0.82); line-height: 1.7; font-size: 1.02rem; margin: 0 0 12px; }
.emotional-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 18px; }
.emotional-item { border-radius: 18px; padding: 16px; background: rgba(255,255,255,0.065); border: 1px solid rgba(255,255,255,0.10); }
.emotional-item strong { display: block; margin-bottom: 8px; color: #FFFFFF; }
.emotional-item span { color: rgba(236,239,255,0.72); line-height: 1.5; font-size: 0.94rem; }
@media (max-width: 940px) { .emotional-list { grid-template-columns: 1fr; } }
.simulation-bottom-actions { display: flex; justify-content: flex-start; margin-top: 18px; }
@media (max-width: 900px) { .simulation-input-grid, .results-summary { grid-template-columns: 1fr; } }

/* =========================
   TELA 9 - EDUCAÇÃO
========================= */
.education {
    align-items: flex-start;
    justify-content: center;
    background:
        radial-gradient(circle at top left, rgba(91, 73, 255, 0.22), transparent 34%),
        radial-gradient(circle at bottom right, rgba(43, 142, 255, 0.16), transparent 30%),
        linear-gradient(180deg, #050816 0%, #090D1F 100%);
    overflow-y: auto;
    padding: 42px 0 70px;
}
.education-shell { width: min(1180px, 92vw); }
.education-hero { background: rgba(15,19,40,0.86); border: 1px solid rgba(126,114,255,0.22); border-radius: 30px; padding: 36px; box-shadow: 0 18px 60px rgba(0,0,0,0.35); margin-bottom: 24px; }
.education-kicker { margin: 0 0 12px; color: rgba(234,238,255,0.72); font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.12em; }
.education-title { margin: 0; font-size: clamp(2.2rem, 4.7vw, 4.4rem); line-height: 1.02; letter-spacing: -0.045em; }
.education-title span { color: #8577FF; }
.education-subtitle { max-width: 940px; margin: 18px 0 0; color: rgba(236,239,255,0.84); font-size: 1.08rem; line-height: 1.7; }
.education-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 18px; }
.education-card { background: rgba(255,255,255,0.065); border: 1px solid rgba(255,255,255,0.12); border-radius: 24px; padding: 24px; box-shadow: 0 16px 38px rgba(0,0,0,0.22); backdrop-filter: blur(8px); }
.education-card.full { grid-column: 1 / -1; }
.education-card h2 { margin: 0 0 14px; font-size: clamp(1.35rem, 2.1vw, 1.8rem); }
.education-card p, .education-card li { color: rgba(236,239,255,0.78); line-height: 1.65; font-size: 1rem; }
.education-card ul { margin: 10px 0 0; padding-left: 22px; }
.book-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 16px; }
.book-card { padding: 16px; border-radius: 18px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.10); }
.book-card strong { display: block; color: #FFFFFF; margin-bottom: 8px; }
.book-card span { display: block; color: rgba(236,239,255,0.72); line-height: 1.5; font-size: 0.94rem; }
.final-callout { position: relative; overflow: hidden; background: linear-gradient(135deg, rgba(91,73,255,0.18), rgba(43,142,255,0.10)); }
.final-callout::before { content: ""; position: absolute; width: 220px; height: 220px; border-radius: 999px; background: #8577FF; opacity: 0.16; filter: blur(12px); top: -95px; right: -75px; }
.final-callout h2, .final-callout p { position: relative; }
.education-actions { display: flex; align-items: center; justify-content: center; gap: 14px; margin-top: 26px; flex-wrap: wrap; }
.btn-education { min-width: 300px; height: 64px; border-radius: 18px; border: none; background: linear-gradient(90deg, #5B49FF 0%, #8577FF 100%); color: white; font-size: 1.05rem; font-weight: 900; cursor: pointer; box-shadow: 0 12px 30px rgba(103,80,255,0.30); }
.btn-education:hover { transform: translateY(-2px); filter: brightness(1.06); }
@media (max-width: 860px) { .education-grid, .book-grid { grid-template-columns: 1fr; } .education-card.full { grid-column: auto; } }


@media (max-width: 1180px) { .result-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 720px) { .result-grid { grid-template-columns: 1fr; } .asset-card { min-height: auto; } }

@media (max-width: 940px) {
    .screen {
        min-height: 1040px;
        height: auto;
        padding: 24px 0 36px;
        overflow-y: auto;
    }

    .hero {
        min-height: 760px;
    }

    .quiz-wrap {
        width: 92vw;
    }

    .options {
        grid-template-columns: 1fr;
        gap: 14px;
    }

    .nav {
        flex-direction: column;
        width: 100%;
    }

    .btn {
        width: 100%;
        max-width: 340px;
    }
}
</style>
</head>

<body>

<section class="screen hero active" id="screenIntro">
    <div class="hero-content">
        <h1 class="hero-title">Sistema de Orientação Financeira</h1>
        <p class="hero-subtitle">
            Receba recomendações personalizadas, simule cenários e construa seu
            futuro financeiro com mais segurança.
        </p>
        <button class="cta" id="startBtn">
            <span>Iniciar estratégia</span>
            <span>→</span>
        </button>
    </div>
</section>

<section class="screen quiz" id="screenQuiz">
    <div class="quiz-wrap">
        <div class="progress-wrap">
            <div class="progress-track">
                <div class="progress-fill" id="progressFill"></div>
            </div>
        </div>

        <h1 class="quiz-title" id="quizTitle"></h1>
        <p class="quiz-subtitle" id="quizSubtitle"></p>
        <div class="question" id="quizQuestion"></div>

        <div class="options" id="options"></div>

        <div class="nav">
            <button class="btn btn-back" id="backBtn">Voltar</button>
            <button class="btn btn-next" id="nextBtn">Próximo</button>
        </div>

        <div class="helper" id="helperText">Selecione uma opção para continuar.</div>
    </div>
</section>

<section class="screen result" id="screenResult">
    <div class="result-shell" id="resultContent"></div>
</section>

<section class="screen portfolio" id="screenPortfolio">
    <div class="portfolio-shell" id="portfolioContent"></div>
</section>

<section class="screen simulation" id="screenSimulation">
    <div class="simulation-shell" id="simulationContent"></div>
</section>

<section class="screen education" id="screenEducation">
    <div class="education-shell">
        <section class="education-hero">
            <p class="education-kicker">Área educacional</p>
            <h1 class="education-title">Continue sua <span>jornada financeira</span></h1>
            <p class="education-subtitle">
                Investir bem não depende apenas de escolher ativos. Depende de entender conceitos básicos,
                manter consistência, controlar emoções e continuar aprendendo ao longo do tempo.
            </p>
        </section>

        <div class="education-grid">
            <section class="education-card">
                <h2>Primeiros passos</h2>
                <ul>
                    <li>Comece com valores que não comprometam sua vida financeira.</li>
                    <li>Priorize construir uma reserva antes de assumir riscos maiores.</li>
                    <li>Invista com regularidade: pequenos aportes mensais fazem diferença no longo prazo.</li>
                    <li>Evite tentar acertar o melhor momento do mercado.</li>
                </ul>
            </section>

            <section class="education-card">
                <h2>Conceitos essenciais</h2>
                <ul>
                    <li><strong>Diversificação:</strong> dividir o dinheiro entre ativos diferentes para reduzir riscos.</li>
                    <li><strong>Juros compostos:</strong> rendimentos que passam a gerar novos rendimentos.</li>
                    <li><strong>Liquidez:</strong> facilidade de transformar o investimento em dinheiro.</li>
                    <li><strong>Volatilidade:</strong> intensidade das oscilações de preço ao longo do tempo.</li>
                </ul>
            </section>

            <section class="education-card full">
                <h2>Livros recomendados</h2>
                <p>Essas leituras ajudam a formar base, mentalidade e disciplina para investir melhor.</p>
                <div class="book-grid">
                    <div class="book-card"><strong>Psicologia Financeira — Morgan Housel</strong><span>Excelente para entender comportamento, paciência, risco e tomada de decisão.</span></div>
                    <div class="book-card"><strong>O Investidor Inteligente — Benjamin Graham</strong><span>Clássico sobre análise, margem de segurança e visão racional de longo prazo.</span></div>
                    <div class="book-card"><strong>Pai Rico, Pai Pobre — Robert Kiyosaki</strong><span>Introdução simples à mentalidade de patrimônio, ativos e independência financeira.</span></div>
                    <div class="book-card"><strong>O Homem Mais Rico da Babilônia — George Clason</strong><span>Livro curto e acessível sobre poupar, investir e criar bons hábitos financeiros.</span></div>
                </div>
            </section>

            <section class="education-card">
                <h2>O que estudar depois</h2>
                <ul>
                    <li>Renda fixa: Tesouro Direto, CDB, LCI/LCA, marcação a mercado.</li>
                    <li>Fundos: taxas, lâmina do fundo, histórico e estratégia.</li>
                    <li>Renda variável: ações, ETFs, FIIs e risco de mercado.</li>
                    <li>Planejamento: objetivos, prazo, reserva e tolerância a risco.</li>
                </ul>
            </section>

            <section class="education-card final-callout">
                <h2>Mensagem final</h2>
                <p>
                    Você não precisa dominar tudo para começar, mas precisa começar com consciência.
                    O mais importante é investir de forma compatível com sua realidade, aprender continuamente
                    e evitar decisões impulsivas.
                </p>
                <p>
                    Com tempo, consistência e disciplina, a educação financeira deixa de ser teoria e passa a
                    virar construção real de patrimônio.
                </p>
            </section>
        </div>

        <div class="education-actions">
            <button class="btn-soft" id="backToSimulationBtn">Voltar para simulação</button>
            <button class="btn-education" id="restartJourneyBtn">Reiniciar jornada</button>
        </div>
    </div>
</section>


<script>
const questions = [
    {
        title: "Precisamos conhecer um pouco mais sobre o seu perfil",
        subtitle: "Existem diversos tipos de investimentos. Alguns são mais seguros e com um retorno um pouco menor. Outros podem ser mais arriscados, mas trazem a possibilidade de ganhos maiores.",
        question: "O que você prioriza ao investir?",
        key: "perfil",
        options: [
            ["conservador", "Busco primeiro segurança, não quero perder dinheiro"],
            ["moderado", "Tolero pequenas oscilações, mas nada que arrisque meu patrimônio"],
            ["arrojado", "Aceito algumas perdas, em busca de ganhos maiores no longo prazo"],
            ["agressivo", "Busco a maior rentabilidade no curto prazo, assumindo altos riscos"]
        ]
    },
    {
        title: "Agora vamos entender seu horizonte de investimento",
        subtitle: "O prazo influencia diretamente o tipo de investimento recomendado. Quanto maior o tempo disponível, maior pode ser a flexibilidade da estratégia.",
        question: "Por quanto tempo você pretende manter seus investimentos?",
        key: "prazo",
        options: [
            ["menos_1_ano", "Menos de 1 ano"],
            ["1_3_anos", "Entre 1 e 3 anos"],
            ["3_5_anos", "Entre 3 e 5 anos"],
            ["mais_5_anos", "Mais de 5 anos"]
        ]
    },
    {
        title: "Conte um pouco sobre sua experiência",
        subtitle: "Saber o quanto você já conhece sobre investimentos ajuda o sistema a adaptar as recomendações e as explicações ao seu momento atual.",
        question: "Qual seu nível de experiência com investimentos?",
        key: "experiencia",
        options: [
            ["nunca_investi", "Nunca investi"],
            ["investi_pouco", "Já investi pouco"],
            ["alguma_experiencia", "Tenho alguma experiência"],
            ["invisto_frequencia", "Invisto com frequência"]
        ]
    },
    {
        title: "Por fim, vamos avaliar sua reação ao risco",
        subtitle: "Oscilações fazem parte de muitos investimentos. Entender como você reagiria ajuda a evitar recomendações incompatíveis com seu perfil.",
        question: "Se seu investimento caísse 10% em um mês, o que você faria?",
        key: "queda",
        options: [
            ["resgataria", "Resgataria imediatamente para evitar mais perdas"],
            ["esperaria", "Esperaria um tempo para ver se recupera"],
            ["manteria", "Manteria o investimento pensando no longo prazo"],
            ["investiria_mais", "Investiria mais, aproveitando a queda"]
        ]
    }
];

const screens = {
    intro: document.getElementById("screenIntro"),
    quiz: document.getElementById("screenQuiz"),
    result: document.getElementById("screenResult"),
    portfolio: document.getElementById("screenPortfolio"),
    simulation: document.getElementById("screenSimulation"),
    education: document.getElementById("screenEducation")
};

const startBtn = document.getElementById("startBtn");
const backBtn = document.getElementById("backBtn");
const nextBtn = document.getElementById("nextBtn");

const progressFill = document.getElementById("progressFill");
const quizTitle = document.getElementById("quizTitle");
const quizSubtitle = document.getElementById("quizSubtitle");
const quizQuestion = document.getElementById("quizQuestion");
const optionsBox = document.getElementById("options");
const helperText = document.getElementById("helperText");
const resultContent = document.getElementById("resultContent");
const portfolioContent = document.getElementById("portfolioContent");
const simulationContent = document.getElementById("simulationContent");

let currentQuestion = 0;
let answers = {};

function showScreen(name) {
    Object.values(screens).forEach(screen => screen.classList.remove("active"));
    screens[name].classList.add("active");
}

function renderQuestion() {
    const data = questions[currentQuestion];

    quizTitle.textContent = data.title;
    quizSubtitle.textContent = data.subtitle;
    quizQuestion.textContent = data.question;
    progressFill.style.width = `${((currentQuestion + 1) / questions.length) * 100}%`;

    optionsBox.innerHTML = "";

    data.options.forEach(([value, label]) => {
        const btn = document.createElement("button");
        btn.className = "option";
        btn.type = "button";
        btn.dataset.value = value;
        btn.textContent = label;

        if (answers[data.key] === value) {
            btn.classList.add("selected");
        }

        btn.addEventListener("click", () => {
            answers[data.key] = value;

            document.querySelectorAll(".option").forEach(option => {
                option.classList.remove("selected");
            });

            btn.classList.add("selected");
            nextBtn.classList.add("enabled");
            helperText.textContent = "Resposta selecionada. Clique em Próximo para continuar.";
        });

        optionsBox.appendChild(btn);
    });

    if (answers[data.key]) {
        nextBtn.classList.add("enabled");
        helperText.textContent = "Resposta selecionada. Clique em Próximo para continuar.";
    } else {
        nextBtn.classList.remove("enabled");
        helperText.textContent = "Selecione uma opção para continuar.";
    }
}

const scoreMap = {
    perfil: { conservador: 1, moderado: 2, arrojado: 3, agressivo: 4 },
    prazo: { menos_1_ano: 1, "1_3_anos": 2, "3_5_anos": 3, mais_5_anos: 4 },
    experiencia: { nunca_investi: 1, investi_pouco: 2, alguma_experiencia: 3, invisto_frequencia: 4 },
    queda: { resgataria: 1, esperaria: 2, manteria: 3, investiria_mais: 4 }
};

const profileData = {
    conservador: {
        nome: "Conservador", cor: "#22c55e", foco: "Segurança + previsibilidade",
        descricao: "Seu resultado indica que você prioriza estabilidade, proteção do patrimônio e menor exposição a grandes oscilações. A carteira sugerida foca em renda fixa, liquidez e previsibilidade.",
        ativos: [
            ["Tesouro Selic", "Título público com baixo risco e alta liquidez.", "É adequado para quem quer segurança e acesso mais fácil ao dinheiro.", "Baixo", "Alta", "Imposto de Renda regressivo.", "Reserva de emergência e objetivos de curto prazo."],
            ["CDB", "Empréstimo ao banco com rendimento definido.", "Combina previsibilidade com possibilidade de proteção do FGC.", "Baixo a médio", "Depende do produto.", "Imposto de Renda regressivo.", "Objetivos de curto e médio prazo."],
            ["LCI / LCA", "Renda fixa isenta de Imposto de Renda para pessoa física.", "Pode aumentar o retorno líquido sem elevar tanto o risco.", "Baixo", "Geralmente menor que Tesouro Selic.", "Isenta de IR para pessoa física.", "Objetivos de médio prazo."],
            ["Tesouro IPCA+", "Título público que protege contra a inflação.", "Ajuda a preservar o poder de compra no longo prazo.", "Baixo, mas oscila antes do vencimento.", "Alta, mas vender antes pode gerar perdas.", "Imposto de Renda regressivo.", "Aposentadoria e metas de longo prazo."],
            ["Fundos de renda fixa", "Carteira diversificada de ativos conservadores.", "Facilita diversificação sem escolher cada título manualmente.", "Baixo a médio", "Depende do fundo.", "IR e possível come-cotas.", "Diversificação conservadora."]
        ],
        glossario: [
            ["Liquidez", "Facilidade de resgatar o dinheiro investido. No perfil conservador, isso é importante porque reduz o risco de ficar preso em um investimento quando precisar do dinheiro."],
            ["FGC", "Fundo Garantidor de Créditos. Pode proteger aplicações como CDB, LCI e LCA dentro dos limites estabelecidos, caso a instituição financeira tenha problemas."],
            ["Renda fixa", "Tipo de investimento em que as regras de remuneração são conhecidas desde o início, como um percentual do CDI, taxa fixa ou IPCA mais juros."],
            ["Tesouro Direto", "Programa que permite investir em títulos públicos federais, como Tesouro Selic e Tesouro IPCA+. É muito usado por iniciantes pela segurança e acessibilidade."],
            ["IPCA", "Índice oficial de inflação do Brasil. Investimentos atrelados ao IPCA ajudam a proteger o poder de compra ao longo do tempo."],
            ["IR regressivo", "Modelo em que a alíquota do Imposto de Renda diminui conforme o dinheiro fica investido por mais tempo."],
            ["Come-cotas", "Cobrança antecipada de imposto que pode ocorrer em alguns fundos. Ela reduz automaticamente parte das cotas do investidor."],
            ["Reserva de emergência", "Dinheiro separado para imprevistos. Normalmente deve ficar em investimentos seguros e líquidos, como Tesouro Selic ou CDB com liquidez diária."]
        ],
        alocacaoSugerida: [30, 25, 20, 15, 10],
        fraseDiversificacao: "O segredo para investir bem não é escolher apenas um investimento, mas diversificar. Distribuir seu dinheiro entre diferentes tipos de investimento ajuda a reduzir riscos."
    },
    moderado: {
        nome: "Moderado", cor: "#facc15", foco: "Equilíbrio entre risco e retorno",
        descricao: "Seu resultado indica que você aceita algum risco para buscar retornos melhores, mas ainda valoriza controle e equilíbrio. A carteira sugerida mistura renda fixa mais sofisticada e ativos com maior potencial.",
        ativos: [
            ["Fundos Imobiliários (FIIs)", "Investimentos ligados ao mercado imobiliário.", "Podem gerar renda passiva e diversificação.", "Médio", "Geralmente alta na bolsa.", "Rendimentos podem ser isentos; ganho de capital é tributado.", "Renda passiva e diversificação."],
            ["Fundos Multimercado", "Fundos que misturam vários tipos de investimento.", "Dão acesso a estratégias diferentes com gestão profissional.", "Médio a alto", "Depende do fundo.", "IR e possível come-cotas.", "Diversificação com maior potencial de retorno."],
            ["Debêntures incentivadas", "Títulos de empresas com potencial de maior retorno.", "Podem pagar mais que investimentos conservadores.", "Médio", "Pode ser baixa.", "Geralmente isentas de IR para pessoa física.", "Renda fixa de médio e longo prazo."],
            ["ETFs de renda fixa", "Fundos negociados em bolsa que seguem índices de renda fixa.", "Oferecem diversificação simples e baixo custo.", "Baixo a médio", "Geralmente boa.", "Ganho de capital tributado.", "Diversificação prática."],
            ["CRI / CRA", "Crédito imobiliário e agrícola.", "Podem oferecer retorno maior e isenção de IR.", "Médio", "Pode ser baixa.", "Geralmente isentos de IR para pessoa física.", "Renda fixa com maior retorno esperado."]
        ],
        glossario: [
            ["FII", "Fundo Imobiliário. Permite investir em ativos ligados ao mercado imobiliário, como shoppings, galpões, escritórios ou títulos imobiliários."],
            ["Renda passiva", "Entrada recorrente de dinheiro gerada por um ativo, como aluguéis distribuídos por FIIs ou rendimentos de alguns investimentos."],
            ["ETF", "Fundo negociado em bolsa que busca acompanhar um índice. Pode facilitar a diversificação com custo mais baixo."],
            ["Debênture", "Título de dívida emitido por empresas. Pode render mais que produtos conservadores, mas depende da saúde financeira da empresa emissora."],
            ["CRI/CRA", "Títulos ligados ao crédito imobiliário e agrícola. Podem ter isenção de IR para pessoa física, mas costumam exigir atenção ao risco de crédito e à liquidez."],
            ["Risco de crédito", "Possibilidade de quem emitiu o título não conseguir pagar corretamente os juros ou devolver o dinheiro investido."],
            ["Diversificação", "Estratégia de dividir o dinheiro em diferentes ativos para reduzir a dependência de um único investimento."],
            ["Liquidez", "Facilidade de vender ou resgatar o investimento. No perfil moderado, alguns ativos podem ter liquidez menor em troca de maior retorno esperado."]
        ],
        alocacaoSugerida: [25, 25, 20, 15, 15],
        fraseDiversificacao: "Diversificar é o equilíbrio entre segurança e crescimento. Combinar diferentes tipos de investimento ajuda a melhorar seus resultados sem assumir riscos excessivos."
    },
    agressivo: {
        nome: "Agressivo", cor: "#ef4444", foco: "Crescimento + maior risco",
        descricao: "Seu resultado indica maior tolerância a oscilações e foco em crescimento. A carteira sugerida inclui renda variável e ativos de maior risco, que exigem estudo, controle emocional e visão de longo prazo.",
        ativos: [
            ["Ações", "Pequenas partes de empresas listadas na bolsa.", "Podem gerar valorização expressiva no longo prazo.", "Alto", "Geralmente alta em ações mais negociadas.", "Varia conforme operação e ganho.", "Crescimento de longo prazo."],
            ["BDRs / ETFs internacionais", "Exposição ao mercado global.", "Ajuda a diversificar fora do Brasil.", "Alto", "Depende do ativo.", "Ganho de capital tributado.", "Diversificação internacional."],
            ["Criptoativos", "Ativos digitais com alta volatilidade.", "Podem ter alto potencial, mas com risco elevado.", "Muito alto", "Geralmente alta, dependendo do ativo.", "Pode haver tributação sobre ganho.", "Parcela pequena e especulativa."],
            ["Fundos de ações", "Gestão profissional em renda variável.", "Permitem exposição a ações com apoio de gestores.", "Alto", "Depende do fundo.", "IR sobre ganhos.", "Crescimento com gestão profissional."],
            ["Derivativos / Opções", "Estratégias avançadas de alto risco.", "Podem ser usados para proteção, especulação ou alavancagem, mas exigem conhecimento técnico.", "Muito alto", "Depende do contrato.", "Tributação específica conforme a operação.", "Estratégias avançadas, não simulação linear comum."]
        ],
        glossario: [
            ["Ações", "Pequenas partes de empresas negociadas na bolsa. O investidor pode ganhar com valorização e, em alguns casos, dividendos."],
            ["Bolsa de valores", "Ambiente organizado onde investidores compram e vendem ativos como ações, FIIs, ETFs, BDRs e opções."],
            ["Volatilidade", "Intensidade das oscilações de preço. Ativos agressivos costumam variar mais, podendo subir ou cair bastante em pouco tempo."],
            ["BDR", "Certificado negociado no Brasil que representa exposição a empresas estrangeiras, como companhias dos Estados Unidos."],
            ["ETF internacional", "Fundo negociado em bolsa que permite exposição a mercados globais, setores ou índices de outros países."],
            ["Criptoativo", "Ativo digital com alta volatilidade. Pode ter grande potencial de ganho, mas também perdas fortes e rápidas."],
            ["ETF internacional", "Forma prática de acessar mercados globais, moedas fortes e empresas fora do Brasil, ajudando a reduzir dependência do mercado nacional."],
            ["Gestão de risco", "Conjunto de regras para limitar perdas, controlar exposição e evitar decisões impulsivas em ativos de maior risco."],
            ["Derivativos", "Contratos financeiros como opções e futuros. Podem ampliar ganhos, mas também perdas, por isso não são tratados como investimento comum na simulação."]
        ],
        alocacaoSugerida: [30, 25, 15, 30, 0],
        fraseDiversificacao: "Mesmo investidores agressivos precisam diversificar. Distribuir seus investimentos ajuda a proteger seu patrimônio em cenários negativos."
    }
};

let currentProfileKey = null;
let portfolioAllocation = {};

function calculateScore() {
    return Object.keys(scoreMap).reduce((total, key) => total + (scoreMap[key][answers[key]] || 0), 0);
}

function getProfile(score) {
    if (score <= 6) return "conservador";
    if (score <= 10) return "moderado";
    return "agressivo";
}

function renderResult() {
    const score = calculateScore();
    currentProfileKey = getProfile(score);
    const profile = profileData[currentProfileKey];
    const cards = profile.ativos.map(asset => `
        <article class="asset-card">
            <h3>${asset[0]}</h3>
            <p>${asset[1]}</p>
            <div class="asset-tags">
                <span class="asset-tag">Risco: ${asset[3]}</span>
                <span class="asset-tag">Liquidez: ${asset[4]}</span>
            </div>
            <details class="asset-details">
                <summary>Ver detalhes</summary>
                <ul>
                    <li><strong>Por que faz sentido:</strong> ${asset[2]}</li>
                    <li><strong>Tributação:</strong> ${asset[5]}</li>
                    <li><strong>Quando costuma ser usado:</strong> ${asset[6]}</li>
                </ul>
            </details>
        </article>
    `).join("");

    const glossary = profile.glossario.map(term => `
        <span class="term" data-tip="${term[1]}">${term[0]} ⓘ</span>
    `).join("");

    resultContent.style.setProperty("--profile-color", profile.cor);
    resultContent.innerHTML = `
        <div class="result-header">
            <p class="result-kicker">Resultado do perfil</p>
            <h1 class="result-title">Seu perfil é: <span>${profile.nome}</span></h1>
            <p class="result-desc"><strong>Foco:</strong> ${profile.foco}. ${profile.descricao}</p>
        </div>

        <h2 class="recommend-title">Investimentos recomendados para o seu perfil</h2>
        <p class="recommend-subtitle">
            Essas opções combinam com o nível de risco identificado no questionário. Na próxima etapa, você poderá montar a carteira definindo quanto deseja colocar em cada ativo.
        </p>

        <div class="result-grid">${cards}</div>

        <div class="glossary">
            <h2>Glossário rápido do perfil ${profile.nome}</h2>
            <div class="glossary-row">${glossary}</div>
        </div>
        <div class="result-actions">
            <button class="btn-soft" id="restartBtn">Refazer questionário</button>
            <button class="cta" id="goPortfolioBtn">Montar minha carteira</button>
        </div>
    `;


    document.getElementById("restartBtn").addEventListener("click", () => {
        currentQuestion = 0;
        answers = {};
        portfolioAllocation = {};
        renderQuestion();
        showScreen("quiz");
    });

    document.getElementById("goPortfolioBtn").addEventListener("click", () => {
        renderPortfolio();
        showScreen("portfolio");
    });
}

function renderPortfolio() {
    if (!currentProfileKey) {
        currentProfileKey = getProfile(calculateScore());
    }

    const profile = profileData[currentProfileKey];
    const assets = profile.ativos;

    if (!portfolioAllocation[currentProfileKey]) {
        portfolioAllocation[currentProfileKey] = {};
        assets.forEach((asset, index) => {
            portfolioAllocation[currentProfileKey][asset[0]] = profile.alocacaoSugerida[index];
        });
    }

    const sliders = assets.map((asset) => {
        const nome = asset[0];
        const valor = portfolioAllocation[currentProfileKey][nome] || 0;
        return `
            <div class="slider-card">
                <div class="slider-top">
                    <span class="slider-name">${nome}</span>
                    <span class="slider-value" id="value-${slugify(nome)}">${valor}%</span>
                </div>
                <input type="range" min="0" max="100" step="5" value="${valor}" data-asset="${nome}" id="slider-${slugify(nome)}">
                <div class="slider-hint">${asset[1]}</div>
            </div>
        `;
    }).join("");

    const rows = assets.map((asset) => {
        const nome = asset[0];
        const valor = portfolioAllocation[currentProfileKey][nome] || 0;
        return `<div class="pill-row"><span>${nome}</span><strong id="row-${slugify(nome)}">${valor}%</strong></div>`;
    }).join("");

    portfolioContent.style.setProperty("--profile-color", profile.cor);
    portfolioContent.innerHTML = `
        <div class="portfolio-header">
            <p class="portfolio-kicker">Montagem da carteira</p>
            <h1 class="portfolio-title">Monte sua carteira <span>${profile.nome}</span></h1>
            <p class="portfolio-desc">
                Ajuste quanto deseja colocar em cada ativo recomendado. A soma precisa fechar em 100% para a carteira ficar completa.
            </p>
        </div>

        <section class="diversification-callout">
            <h2>Diversificação importa</h2>
            <p>${profile.fraseDiversificacao}</p>
        </section>

        <div class="portfolio-layout">
            <section class="allocation-panel">
                <h2>Distribuição por ativo</h2>
                <p class="allocation-subtitle">Use os controles abaixo para personalizar sua carteira. A sugestão inicial já vem preenchida de acordo com o perfil calculado.</p>
                ${sliders}
            </section>

            <aside class="summary-panel">
                <h2>Resumo da alocação</h2>
                <p class="summary-subtitle">Acompanhe se a carteira já está fechando corretamente.</p>
                <div class="total-number" id="portfolioTotal">0%</div>
                <div class="total-bar"><div class="total-fill" id="portfolioFill"></div></div>
                <div class="status-box" id="portfolioStatus"></div>
                <div class="pill-list">${rows}</div>
                <div class="portfolio-actions">
                    <button class="btn-continue-portfolio" id="goSimulationBtn">Continuar para simulação</button>
                </div>
            </aside>
        </div>

        <div class="portfolio-bottom-actions">
            <button class="btn-soft" id="backToResultBtn">Voltar</button>
        </div>
    `;

    document.querySelectorAll('#portfolioContent input[type="range"]').forEach(slider => {
        slider.addEventListener("input", (event) => {
            const assetName = event.target.dataset.asset;
            portfolioAllocation[currentProfileKey][assetName] = Number(event.target.value);
            updatePortfolioSummary();
        });
    });

    document.getElementById("backToResultBtn").addEventListener("click", () => showScreen("result"));
    document.getElementById("goSimulationBtn").addEventListener("click", () => {
        const total = getPortfolioTotal();
        if (total === 100) {
            renderSimulation();
            showScreen("simulation");
        }
    });

    updatePortfolioSummary();
}

function slugify(text) {
    return text
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/(^-|-$)/g, "");
}

function getPortfolioTotal() {
    if (!portfolioAllocation[currentProfileKey]) return 0;
    return Object.values(portfolioAllocation[currentProfileKey]).reduce((sum, value) => sum + Number(value || 0), 0);
}

function updatePortfolioSummary() {
    const profile = profileData[currentProfileKey];
    const total = getPortfolioTotal();
    const totalEl = document.getElementById("portfolioTotal");
    const fillEl = document.getElementById("portfolioFill");
    const statusEl = document.getElementById("portfolioStatus");
    const continueBtn = document.getElementById("goSimulationBtn");

    totalEl.textContent = `${total}%`;
    fillEl.style.width = `${Math.min(total, 100)}%`;

    profile.ativos.forEach(asset => {
        const nome = asset[0];
        const valor = portfolioAllocation[currentProfileKey][nome] || 0;
        const valueEl = document.getElementById(`value-${slugify(nome)}`);
        const rowEl = document.getElementById(`row-${slugify(nome)}`);
        if (valueEl) valueEl.textContent = `${valor}%`;
        if (rowEl) rowEl.textContent = `${valor}%`;
    });

    const maxAllocation = Math.max(...Object.values(portfolioAllocation[currentProfileKey]).map(Number));
    let concentrationWarning = "";
    if (maxAllocation >= 70) {
        concentrationWarning = `<div class="portfolio-warning">Atenção: sua carteira está muito concentrada em um único ativo. Isso pode aumentar o risco.</div>`;
    }

    if (total < 100) {
        statusEl.innerHTML = `Faltam <strong>${100 - total}%</strong> para completar sua carteira.${concentrationWarning}`;
        continueBtn.classList.remove("enabled");
    } else if (total > 100) {
        statusEl.innerHTML = `Você passou <strong>${total - 100}%</strong> do limite. Reduza algum ativo para fechar em 100%.${concentrationWarning}`;
        continueBtn.classList.remove("enabled");
    } else {
        statusEl.innerHTML = `Carteira completa: <strong>100%</strong>. Agora você pode seguir para a simulação.${concentrationWarning}`;
        continueBtn.classList.add("enabled");
    }
}

const expectedReturns = {
    // Perfil conservador: renda fixa, preservação de capital e retorno atrelado à Selic/IPCA.
    "Tesouro Selic": { pessimista: 0.080, base: 0.105, otimista: 0.120 },
    "CDB": { pessimista: 0.080, base: 0.105, otimista: 0.120 },
    "LCI / LCA": { pessimista: 0.075, base: 0.095, otimista: 0.110 },
    "Tesouro IPCA+": { pessimista: 0.090, base: 0.115, otimista: 0.140 },
    "Fundos de renda fixa": { pessimista: 0.070, base: 0.100, otimista: 0.115 },

    // Perfil moderado: equilíbrio entre renda fixa sofisticada e ativos com maior potencial.
    "Fundos Imobiliários (FIIs)": { pessimista: 0.040, base: 0.120, otimista: 0.160 },
    "Fundos Multimercado": { pessimista: 0.060, base: 0.110, otimista: 0.150 },
    "Debêntures incentivadas": { pessimista: 0.070, base: 0.125, otimista: 0.150 },
    "ETFs de renda fixa": { pessimista: 0.080, base: 0.105, otimista: 0.120 },
    "CRI / CRA": { pessimista: 0.075, base: 0.120, otimista: 0.145 },

    // Perfil agressivo: ações globais, renda variável e cripto, com maior volatilidade.
    "Ações": { pessimista: 0.030, base: 0.160, otimista: 0.260 },
    "BDRs / ETFs internacionais": { pessimista: 0.025, base: 0.140, otimista: 0.230 },
    "Criptoativos": { pessimista: 0.010, base: 0.300, otimista: 0.800 },
    "Fundos de ações": { pessimista: 0.025, base: 0.140, otimista: 0.240 },
    "Derivativos / Opções": { pessimista: 0.000, base: 0.000, otimista: 0.000, simulavel: false }
};

const profileTotalReturns = {
    conservador: { pessimista: 0.082, base: 0.106, otimista: 0.123 },
    moderado: { pessimista: 0.064, base: 0.116, otimista: 0.145 },
    agressivo: { pessimista: 0.024, base: 0.170, otimista: 0.345 }
};

function formatCurrency(value) {
    return value.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function formatPercent(value) {
    return `${value.toFixed(2).replace(".", ",")}%`;
}

function getEmotionalSection(profileKey) {
    const sections = {
        conservador: `
            <section class="emotional-panel">
                <h2>Controle emocional</h2>
                <p>Para o perfil conservador, controle emocional significa evitar decisões precipitadas quando surgem notícias negativas, quedas pontuais ou comparações com investimentos que prometem retornos maiores. O foco principal é proteger o patrimônio, manter previsibilidade e respeitar o prazo escolhido.</p>
                <p>Mesmo investimentos conservadores podem oscilar ou render menos em alguns momentos. A disciplina está em não abandonar a estratégia por ansiedade e em lembrar que segurança, liquidez e consistência também são partes importantes de uma boa carteira.</p>
                <div class="emotional-list">
                    <div class="emotional-item"><strong>Não persiga promessas fáceis</strong><span>Retornos muito altos geralmente vêm com riscos maiores. Para um conservador, trocar segurança por pressa pode comprometer o objetivo.</span></div>
                    <div class="emotional-item"><strong>Proteja sua reserva</strong><span>Evite colocar dinheiro de curto prazo em ativos de maior risco. Reserva e objetivos próximos precisam de liquidez e estabilidade.</span></div>
                    <div class="emotional-item"><strong>Mantenha constância</strong><span>Aportes regulares e paciência costumam ser mais importantes do que tentar encontrar o investimento perfeito.</span></div>
                </div>
            </section>`,
        moderado: `
            <section class="emotional-panel">
                <h2>Controle emocional</h2>
                <p>Para o perfil moderado, controle emocional é encontrar equilíbrio: aceitar alguma oscilação para buscar retornos melhores, mas sem transformar a carteira em uma aposta. Esse investidor precisa lidar com momentos de queda sem abandonar a estratégia e com momentos de alta sem exagerar no risco.</p>
                <p>A disciplina está em diversificar, rebalancear quando necessário e manter o plano de longo prazo. Uma carteira moderada pode ter partes mais arriscadas, mas elas devem funcionar em conjunto com ativos mais previsíveis.</p>
                <div class="emotional-list">
                    <div class="emotional-item"><strong>Evite excesso de confiança</strong><span>Ganhos em um período não significam que todo o dinheiro deve ir para ativos mais arriscados.</span></div>
                    <div class="emotional-item"><strong>Use a diversificação</strong><span>Combinar ativos de comportamentos diferentes ajuda a reduzir ansiedade e melhora a estabilidade da carteira.</span></div>
                    <div class="emotional-item"><strong>Revise sem impulsividade</strong><span>Ajustar a carteira é saudável, mas decisões motivadas por medo ou euforia tendem a prejudicar o resultado.</span></div>
                </div>
            </section>`,
        agressivo: `
            <section class="emotional-panel">
                <h2>Controle emocional</h2>
                <p>Investir não é apenas escolher ativos com bom potencial de retorno. No mercado, principalmente em renda variável, é normal enfrentar quedas, notícias negativas, oscilações fortes e períodos em que a carteira parece não evoluir. O controle emocional é a capacidade de não tomar decisões impulsivas nesses momentos.</p>
                <p>Para um perfil agressivo, disciplina é ainda mais importante. Buscar crescimento exige aceitar volatilidade, manter visão de longo prazo e evitar decisões baseadas em medo ou euforia. Uma carteira pode cair no curto prazo mesmo quando a estratégia faz sentido para o futuro.</p>
                <div class="emotional-list">
                    <div class="emotional-item"><strong>Evite agir no pânico</strong><span>Quedas fazem parte do mercado. Vender tudo no pior momento pode transformar uma oscilação temporária em prejuízo definitivo.</span></div>
                    <div class="emotional-item"><strong>Tenha uma estratégia</strong><span>Definir prazo, aportes e diversificação ajuda a reduzir decisões emocionais e mantém o foco no objetivo.</span></div>
                    <div class="emotional-item"><strong>Respeite seu risco</strong><span>Mesmo investidores agressivos precisam limitar exposição, diversificar e entender que retorno maior vem acompanhado de incerteza maior.</span></div>
                </div>
            </section>`
    };
    return sections[profileKey] || sections.moderado;
}

function renderSimulation() {
    const profile = profileData[currentProfileKey];
    simulationContent.style.setProperty("--profile-color", profile.cor);
    simulationContent.innerHTML = `
        <div class="simulation-header">
            <p class="simulation-kicker">Simulação financeira</p>
            <h1 class="simulation-title">Simule sua carteira <span>${profile.nome}</span></h1>
            <p class="simulation-desc">Informe o valor inicial, os aportes mensais e o prazo. Depois de simular, o sistema mostra a evolução total da carteira, a evolução de cada ativo e uma tabela comparativa.</p>
        </div>
        <section class="simulation-inputs">
            <h2>Dados da simulação</h2>
            <div class="simulation-input-grid">
                <div class="input-group"><label for="initialAmount">Valor inicial investido</label><input id="initialAmount" type="number" min="0" step="100" value="1000"></div>
                <div class="input-group"><label for="monthlyContribution">Aporte mensal</label><input id="monthlyContribution" type="number" min="0" step="50" value="100"></div>
                <div class="input-group"><label for="investmentYears">Período em anos, máximo 10</label><input id="investmentYears" type="number" min="1" max="10" step="1" value="5"></div>
                <div class="input-group"><label for="returnScenario">Cenário de retorno</label><select id="returnScenario"><option value="pessimista">Pessimista</option><option value="base" selected>Base</option><option value="otimista">Otimista</option></select></div>
            </div>
            <div class="simulation-actions"><button class="cta" id="runSimulationBtn">Simular investimento</button></div>
        </section>
        <div id="simulationResults" style="display:none;">
            <div class="results-summary">
                <div class="summary-card"><span>Valor total investido</span><strong id="totalInvestedCard">-</strong></div>
                <div class="summary-card"><span>Valor líquido estimado</span><strong id="finalValueCard">-</strong></div>
                <div class="summary-card"><span>Ganho líquido estimado</span><strong id="netGainCard">-</strong></div>
                <div class="summary-card"><span>Retorno anual do perfil</span><strong id="profileReturnCard">-</strong></div>
            </div>
            <section class="chart-panel">
                <h2>Evolução estimada da carteira</h2>
                <p class="allocation-subtitle">A linha principal mostra o crescimento da carteira total. As demais linhas mostram a evolução estimada de cada ativo.</p>
                <div class="chart-wrap"><canvas id="simulationChart"></canvas></div>
            </section>
            <section class="simulation-note">Esta simulação usa estimativas educacionais de retorno anual em três cenários: pessimista, base e otimista. Ela não é promessa de rentabilidade. Ativos de renda variável e criptoativos podem ter perdas, oscilações fortes e resultados diferentes do cenário apresentado.</section>
            <details class="educational-panel">
                <summary>Entenda a simulação</summary>
                <div class="edu-content">
                    <p><strong>Juros compostos</strong> são os juros que passam a render sobre os próprios rendimentos. No começo, o crescimento da carteira costuma depender mais do seu esforço de aporte do que dos juros. Com o passar do tempo, os rendimentos acumulados também começam a gerar novos rendimentos.</p>
                    <p><strong>No primeiro ano, seu patrimônio cresce mais pelo seu esforço do que pelos juros.</strong> Com o tempo, os juros assumem mais importância, porque cada rendimento se soma ao patrimônio e ajuda a formar uma base maior para os próximos meses.</p>
                    <div class="formula-box">Fórmula simplificada: Valor futuro = valor inicial × (1 + taxa mensal)<sup>meses</sup> + aportes mensais acumulados com juros compostos.</div>
                    <p>Por isso, prazo, constância nos aportes e disciplina costumam ser tão importantes quanto escolher bons ativos.</p>
                </div>
            </details>
            <section class="table-panel">
                <h2>Tabela da simulação</h2>
                <div class="sim-table-wrap"><table class="sim-table" id="simulationTable"></table></div>
                ${currentProfileKey === "agressivo" ? `<p class="allocation-subtitle" style="margin-top:16px;">Observação: derivativos/opções aparecem na montagem da carteira para fins educativos, mas não entram como crescimento linear na simulação, porque são instrumentos avançados usados para proteção, especulação ou alavancagem. Se você deixar percentual em derivativos, ele não será tratado como retorno previsível.</p>` : ""}
            </section>
            ${getEmotionalSection(currentProfileKey)}
            <div class="education-actions">
                <button class="btn-education" id="goToEducationBtn">Avançar para área educacional</button>
            </div>
        </div>
        <div class="simulation-bottom-actions"><button class="btn-soft" id="backToPortfolioBtn">Voltar para carteira</button></div>
    `;
    document.getElementById("runSimulationBtn").addEventListener("click", runSimulation);
    document.getElementById("backToPortfolioBtn").addEventListener("click", () => showScreen("portfolio"));
    document.getElementById("goToEducationBtn").addEventListener("click", () => showScreen("education"));
}

function runSimulation() {
    const initialAmount = Math.max(0, Number(document.getElementById("initialAmount").value || 0));
    const monthlyContribution = Math.max(0, Number(document.getElementById("monthlyContribution").value || 0));
    const yearsInput = Number(document.getElementById("investmentYears").value || 1);
    const years = Math.max(1, Math.min(10, yearsInput));
    document.getElementById("investmentYears").value = years;
    const months = years * 12;
    const scenario = document.getElementById("returnScenario").value;
    const allocation = portfolioAllocation[currentProfileKey] || {};
    const simulatedAllocationTotal = Object.entries(allocation)
        .filter(([assetName, percent]) => assetName !== "Derivativos / Opções" && Number(percent || 0) > 0)
        .reduce((sum, [assetName, percent]) => sum + Number(percent || 0), 0) / 100;
    const labels = Array.from({ length: months }, (_, index) => `${index + 1}m`);
    const assetResults = [];
    const totalSeries = Array(months).fill(0);
    let totalNet = 0;
    let totalInvested = (initialAmount + (monthlyContribution * months)) * simulatedAllocationTotal;

    Object.entries(allocation).forEach(([assetName, percent]) => {
        const weight = Number(percent || 0) / 100;
        if (weight <= 0) return;
        if (assetName === "Derivativos / Opções") return;
        const annualRate = expectedReturns[assetName]?.[scenario] ?? 0.10;
        const monthlyRate = Math.pow(1 + annualRate, 1 / 12) - 1;
        const investedInAsset = (initialAmount * weight) + (monthlyContribution * weight * months);
        let value = initialAmount * weight;
        const series = [];
        for (let month = 0; month < months; month++) {
            value = value * (1 + monthlyRate) + (monthlyContribution * weight);
            series.push(value);
            totalSeries[month] += value;
        }
        const grossValue = value;
        const grossGain = grossValue - investedInAsset;
        const taxRate = getTaxRate(assetName, months);
        const taxValue = Math.max(0, grossGain * taxRate);
        const netValue = grossValue - taxValue;
        const netGain = netValue - investedInAsset;
        const netReturn = investedInAsset > 0 ? (netGain / investedInAsset) * 100 : 0;
        const grossReturn = investedInAsset > 0 ? (grossGain / investedInAsset) * 100 : 0;
        totalNet += netValue;
        assetResults.push({ assetName, annualRate, investedInAsset, grossValue, grossReturn, taxValue, netValue, netGain, netReturn, series });
    });

    const totalNetGain = totalNet - totalInvested;
    document.getElementById("totalInvestedCard").textContent = formatCurrency(totalInvested);
    document.getElementById("finalValueCard").textContent = formatCurrency(totalNet);
    document.getElementById("netGainCard").textContent = formatCurrency(totalNetGain);
    const profileRate = profileTotalReturns[currentProfileKey]?.[scenario] ?? 0;
    document.getElementById("profileReturnCard").textContent = formatPercent(profileRate * 100) + " a.a.";
    renderSimulationChart(labels, totalSeries, assetResults);
    renderSimulationTable(assetResults);
    document.getElementById("simulationResults").style.display = "block";
}

function getTaxRate(assetName, months) {
    const taxFreeAssets = ["LCI / LCA", "Debêntures incentivadas", "CRI / CRA"];
    if (taxFreeAssets.includes(assetName)) return 0;
    if (assetName.includes("Cripto") || assetName.includes("Ações") || assetName.includes("BDRs") || assetName.includes("ETFs internacionais")) return 0.15;
    if (months <= 6) return 0.225;
    if (months <= 12) return 0.20;
    if (months <= 24) return 0.175;
    return 0.15;
}

function renderSimulationChart(labels, totalSeries, assetResults) {
    const canvas = document.getElementById("simulationChart");
    const ctx = canvas.getContext("2d");
    if (window.investmentChart) window.investmentChart.destroy();

    window.investmentChart = new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                { label: "Carteira total", data: totalSeries, borderWidth: 4, tension: 0.28, pointRadius: 0 },
                ...assetResults.map(result => ({ label: result.assetName, data: result.series, borderWidth: 2, tension: 0.28, pointRadius: 0 }))
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: "index", intersect: false },
            plugins: {
                legend: { labels: { color: "#FFFFFF", usePointStyle: true } },
                tooltip: { callbacks: { label: context => `${context.dataset.label}: ${formatCurrency(context.parsed.y)}` } }
            },
            scales: {
                x: { ticks: { color: "rgba(255,255,255,0.68)", maxTicksLimit: 12 }, grid: { color: "rgba(255,255,255,0.08)" } },
                y: { ticks: { color: "rgba(255,255,255,0.68)", callback: value => formatCurrency(value) }, grid: { color: "rgba(255,255,255,0.08)" } }
            }
        }
    });
}

function renderSimulationTable(assetResults) {
    const header = assetResults.map(result => `<th>${result.assetName}</th>`).join("");
    const row = (label, getter) => `<tr><td>${label}</td>${assetResults.map(result => `<td>${getter(result)}</td>`).join("")}</tr>`;
    document.getElementById("simulationTable").innerHTML = `
        <thead><tr><th>Indicador</th>${header}</tr></thead>
        <tbody>
            ${row("Valor investido", r => formatCurrency(r.investedInAsset))}
            ${row("Retorno anual usado", r => formatPercent(r.annualRate * 100))}
            ${row("Valor bruto acumulado", r => formatCurrency(r.grossValue))}
            ${row("Rentabilidade bruta", r => formatPercent(r.grossReturn))}
            ${row("Valor pago em IR estimado", r => formatCurrency(r.taxValue))}
            ${row("Valor líquido acumulado", r => formatCurrency(r.netValue))}
            ${row("Rentabilidade líquida", r => formatPercent(r.netReturn))}
            ${row("Ganho líquido", r => formatCurrency(r.netGain))}
        </tbody>
    `;
}



document.getElementById("backToSimulationBtn").addEventListener("click", () => showScreen("simulation"));
document.getElementById("restartJourneyBtn").addEventListener("click", () => {
    answers = {};
    currentQuestion = 0;
    if (window.investmentChart) window.investmentChart.destroy();
    showScreen("intro");
});

startBtn.addEventListener("click", () => {
    currentQuestion = 0;
    renderQuestion();
    showScreen("quiz");
});

backBtn.addEventListener("click", () => {
    if (currentQuestion === 0) {
        showScreen("intro");
        return;
    }

    currentQuestion -= 1;
    renderQuestion();
});

nextBtn.addEventListener("click", () => {
    const key = questions[currentQuestion].key;

    if (!answers[key]) {
        return;
    }

    if (currentQuestion < questions.length - 1) {
        currentQuestion += 1;
        renderQuestion();
    } else {
        renderResult();
        showScreen("result");
    }
});

</script>

</body>
</html>
"""

html = html.replace("__HERO_BG__", f"data:image/png;base64,{hero_bg}")
html = html.replace("__QUIZ_BG__", f"data:image/png;base64,{quiz_bg}")

components.html(html, height=1200, scrolling=True)
