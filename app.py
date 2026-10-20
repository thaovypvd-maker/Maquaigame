import random
import streamlit as st
# from questions import QUESTIONS
import questions
QUESTIONS = questions.QUESTIONS

st.set_page_config(
    page_title="Âm Binh Ký",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

BG_URL = "https://raw.githubusercontent.com/thaovypvd-maker/Maquaigame/80969180e42358d1ec24d4ae8fd4612de5b3a02c/Background%20.JPG"

TITLES = [
    (0, 3, "Pháp sư hệ vật lý", "🔮"),
    (4, 5, "Thầy pháp tập sự", "🧙"),
    (6, 8, "Full sách thánh", "📖"),
    (9, 10, "Trấn giữ tam giới", "🐉"),
]

def get_title(n):
    for lo, hi, name, icon in TITLES:
        if lo <= n <= hi:
            return name, icon
    return TITLES[0][2], TITLES[0][3]

defaults = {
    "started": False,
    "q_idx": 0,
    "lanterns": 0,
    "wrong_attempted": set(),
    "show_wrong": False,
    "show_explanation": False,
    "finished": False,
    "quiz": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def start_new_game():
    st.session_state.quiz = random.sample(QUESTIONS, 10)
    st.session_state.q_idx = 0
    st.session_state.lanterns = 0
    st.session_state.wrong_attempted = set()
    st.session_state.show_wrong = False
    st.session_state.show_explanation = False
    st.session_state.finished = False
    st.session_state.started = True

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;900&family=Playfair+Display:wght@700;900&display=swap');

#MainMenu, footer, header {{ visibility: hidden; }}

.stApp {{
    background-image: linear-gradient(rgba(2,8,20,0.62), rgba(2,8,20,0.82)), url('{BG_URL}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Be Vietnam Pro', sans-serif;
    color: #e0f0ff;
}}

h1, h2, h3 {{
    color: #7feaff !important;
    text-shadow: 0 0 10px #00c8ff, 0 0 24px #0088ff, 0 0 48px #0033aa;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    letter-spacing: 1px;
}}

.main-title {{
    text-align: center;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #9ff0ff;
    text-shadow: 0 0 12px #00d5ff, 0 0 28px #0088ff, 0 0 60px #0033aa;
    margin: 10px 0 6px 0;
    letter-spacing: 3px;
}}
.subtitle {{
    text-align: center;
    color: #7ab8d8;
    font-size: 0.9rem;
    margin-bottom: 22px;
    letter-spacing: 4px;
    text-transform: uppercase;
}}

@keyframes rainbowLED {{
    0%   {{ border-color: #ff2d55; box-shadow: 0 0 14px rgba(255,45,85,0.9), 0 0 32px rgba(255,45,85,0.45), inset 0 0 12px rgba(255,45,85,0.28); }}
    14%  {{ border-color: #ff9500; box-shadow: 0 0 14px rgba(255,149,0,0.9), 0 0 32px rgba(255,149,0,0.45), inset 0 0 12px rgba(255,149,0,0.28); }}
    28%  {{ border-color: #ffea00; box-shadow: 0 0 14px rgba(255,234,0,0.9), 0 0 32px rgba(255,234,0,0.45), inset 0 0 12px rgba(255,234,0,0.28); }}
    42%  {{ border-color: #2dff5c; box-shadow: 0 0 14px rgba(45,255,92,0.9), 0 0 32px rgba(45,255,92,0.45), inset 0 0 12px rgba(45,255,92,0.28); }}
    57%  {{ border-color: #00e5ff; box-shadow: 0 0 14px rgba(0,229,255,0.9), 0 0 32px rgba(0,229,255,0.45), inset 0 0 12px rgba(0,229,255,0.28); }}
    71%  {{ border-color: #2d6bff; box-shadow: 0 0 14px rgba(45,107,255,0.9), 0 0 32px rgba(45,107,255,0.45), inset 0 0 12px rgba(45,107,255,0.28); }}
    85%  {{ border-color: #bb33ff; box-shadow: 0 0 14px rgba(187,51,255,0.9), 0 0 32px rgba(187,51,255,0.45), inset 0 0 12px rgba(187,51,255,0.28); }}
    100% {{ border-color: #ff2d55; box-shadow: 0 0 14px rgba(255,45,85,0.9), 0 0 32px rgba(255,45,85,0.45), inset 0 0 12px rgba(255,45,85,0.28); }}
}}

.intro-box {{
    background: rgba(0, 22, 45, 0.68);
    border: 2px solid #00d5ff;
    border-radius: 14px;
    padding: 26px 28px;
    margin: 20px 0;
    backdrop-filter: blur(6px);
    animation: rainbowLED 5s linear infinite;
    color: #dff6ff;
    line-height: 1.8;
}}
.intro-label {{
    color: #7feaff;
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 900;
    margin-bottom: 16px;
    text-shadow: 0 0 10px rgba(0,213,255,0.7);
    letter-spacing: 3px;
    text-align: center;
}}
.intro-text {{
    font-size: 1.02rem;
    margin-bottom: 14px;
    text-align: justify;
}}
.intro-whisper {{
    color: #ffaa66;
    text-align: center;
    font-style: italic;
    margin-top: 22px;
    font-size: 1rem;
    text-shadow: 0 0 10px rgba(255,170,102,0.5);
    letter-spacing: 1px;
}}

.status-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(0, 20, 40, 0.55);
    border: 1px solid rgba(0, 213, 255, 0.5);
    border-radius: 12px;
    padding: 10px 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 12px rgba(0, 213, 255, 0.35);
    backdrop-filter: blur(4px);
    font-weight: 600;
    color: #bfe9ff;
}}
.status-bar .lanterns {{
    font-size: 1.1rem;
    letter-spacing: 2px;
    color: #ffd27f;
}}

.question-box {{
    background: rgba(0, 22, 45, 0.62);
    border: 3px solid #00d5ff;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 20px;
    backdrop-filter: blur(6px);
    animation: rainbowLED 4s linear infinite;
    font-size: 1.18rem;
    font-weight: 700;
    color: #dff6ff;
    text-shadow: 0 0 8px rgba(0, 213, 255, 0.6);
}}

[class*="st-key-opt_"] button {{
    background: rgba(0, 18, 38, 0.72) !important;
    color: #dff6ff !important;
    border: 2px solid #00c8ff !important;
    border-radius: 10px !important;
    padding: 14px 22px !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    width: 100% !important;
    text-align: left !important;
    transition: all 0.18s ease !important;
    animation: rainbowLED 2.5s linear infinite !important;
    margin-bottom: 6px;
}}
[class*="st-key-opt_"] button:hover {{
    background: rgba(0, 60, 110, 0.9) !important;
    color: #ffffff !important;
    transform: translateY(-1px) scale(1.01);
}}

.st-key-start_btn button {{
    background: rgba(70, 40, 0, 0.85) !important;
    border: 2px solid #ffcc55 !important;
    color: #fff4d0 !important;
    box-shadow: 0 0 16px #ffcc55, inset 0 0 12px rgba(255,204,85,0.3) !important;
    animation: goldBlink 1.8s infinite !important;
    text-align: center !important;
    font-size: 1.15rem !important;
    padding: 15px 22px !important;
    margin-top: 16px !important;
}}
.st-key-start_btn button:hover {{
    background: rgba(120, 70, 0, 0.95) !important;
    box-shadow: 0 0 30px #ffe9a0, 0 0 60px rgba(255,233,160,0.7) !important;
}}
@keyframes goldBlink {{
    0%, 100% {{ border-color: #ffcc55; box-shadow: 0 0 12px rgba(255,204,85,0.7), inset 0 0 10px rgba(255,204,85,0.25); }}
    50% {{ border-color: #ffe9a0; box-shadow: 0 0 28px rgba(255,233,160,1), inset 0 0 22px rgba(255,233,160,0.45); }}
}}

.st-key-continue_btn button {{
    background: rgba(0, 60, 30, 0.85) !important;
    border: 2px solid #22ff88 !important;
    color: #d4ffe4 !important;
    box-shadow: 0 0 14px #22ff88, inset 0 0 12px rgba(34,255,136,0.3) !important;
    animation: greenBlink 1.8s infinite !important;
    text-align: center !important;
    font-size: 1.12rem !important;
    padding: 14px 22px !important;
    margin-top: 14px !important;
}}
.st-key-continue_btn button:hover {{
    background: rgba(0, 100, 50, 0.95) !important;
    box-shadow: 0 0 26px #44ffaa, 0 0 52px rgba(68,255,170,0.7) !important;
}}
@keyframes greenBlink {{
    0%, 100% {{ border-color: #22ff88; box-shadow: 0 0 10px rgba(34,255,136,0.6), inset 0 0 10px rgba(34,255,136,0.2); }}
    50% {{ border-color: #88ffcc; box-shadow: 0 0 24px rgba(136,255,204,1), inset 0 0 20px rgba(136,255,204,0.4); }}
}}

.st-key-retry_btn {{
    position: fixed !important;
    bottom: 12% !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 100001 !important;
    width: min(400px, 85vw) !important;
}}
.st-key-retry_btn button {{
    background: rgba(80, 20, 0, 0.92) !important;
    border: 2px solid #ff8833 !important;
    color: #ffe0c8 !important;
    box-shadow: 0 0 16px #ff8833, inset 0 0 12px rgba(255,136,51,0.35) !important;
    animation: orangeBlink 1.2s infinite !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    padding: 14px 22px !important;
}}
.st-key-retry_btn button:hover {{
    background: rgba(140, 40, 0, 0.95) !important;
    box-shadow: 0 0 30px #ffaa55, 0 0 60px rgba(255,170,85,0.7) !important;
}}
@keyframes orangeBlink {{
    0%, 100% {{ border-color: #ff8833; box-shadow: 0 0 12px rgba(255,136,51,0.7), inset 0 0 10px rgba(255,136,51,0.25); }}
    50% {{ border-color: #ffbb66; box-shadow: 0 0 28px rgba(255,187,102,1), inset 0 0 22px rgba(255,187,102,0.45); }}
}}

.st-key-restart_btn button {{
    background: rgba(40, 0, 60, 0.85) !important;
    border: 2px solid #bb66ff !important;
    color: #f0dfff !important;
    box-shadow: 0 0 16px #bb66ff, inset 0 0 12px rgba(187,102,255,0.3) !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    padding: 14px 22px !important;
}}
.st-key-restart_btn button:hover {{
    background: rgba(70, 0, 110, 0.95) !important;
    box-shadow: 0 0 30px #cc88ff, 0 0 60px rgba(204,136,255,0.7) !important;
}}

.explain-box {{
    background: rgba(0, 30, 50, 0.78);
    border: 2px solid #00ffcc;
    border-radius: 14px;
    padding: 22px 26px;
    margin: 18px 0;
    backdrop-filter: blur(6px);
    box-shadow: 0 0 18px #00ffcc, 0 0 40px rgba(0,255,204,0.5), inset 0 0 22px rgba(0,255,204,0.15);
    color: #e0fff8;
    font-size: 1.05rem;
    line-height: 1.7;
}}
.explain-box .correct-ans {{
    color: #7dffcf;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0,255,180,0.7);
    margin-bottom: 14px;
    font-size: 1.1rem;
}}
.explain-box .label {{
    color: #7feaff;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-size: 0.85rem;
    margin-bottom: 6px;
    display: block;
}}
.explain-box .concept {{
    font-size: 1rem;
    color: #d0f0ff;
}}

.wrong-overlay {{
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at center, rgba(220,30,30,0.92), rgba(40,0,0,0.98));
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    animation: redFlash 0.5s ease-out;
    font-family: 'Be Vietnam Pro', sans-serif;
    pointer-events: none;
}}
@keyframes redFlash {{
    0% {{ opacity: 0; }}
    50% {{ opacity: 1; background: radial-gradient(circle at center, rgba(255,80,80,0.95), rgba(80,0,0,1)); }}
    100% {{ opacity: 1; }}
}}
.wrong-text {{
    color: #fff;
    font-size: 3.2rem;
    font-weight: 900;
    letter-spacing: 6px;
    text-shadow: 0 0 20px #ff0000, 0 0 40px #ff3333, 0 0 80px #aa0000;
    margin-bottom: 30px;
    animation: textShake 0.5s infinite;
}}
@keyframes textShake {{
    0%, 100% {{ transform: translateX(0); }}
    25% {{ transform: translateX(-4px); }}
    75% {{ transform: translateX(4px); }}
}}
.ghost-icons {{
    font-size: 7rem;
    display: inline-block;
    opacity: 0;
    animation: descend 2.8s ease-in-out forwards;
    filter: drop-shadow(0 0 24px #ff2222) drop-shadow(0 0 48px #aa0000);
}}
@keyframes descend {{
    0% {{ transform: translateY(-500px); opacity: 0; }}
    20% {{ opacity: 1; }}
    100% {{ transform: translateY(0); opacity: 1; }}
}}
.wrong-hint {{
    color: #ffd0d0;
    font-size: 0.95rem;
    margin-top: 36px;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0.9;
    text-align: center;
}}

.end-box {{
    background: rgba(0, 20, 40, 0.75);
    border: 3px solid #00d5ff;
    border-radius: 16px;
    padding: 30px 28px;
    text-align: center;
    backdrop-filter: blur(8px);
    animation: rainbowLED 5s linear infinite;
    margin: 20px 0;
}}
.end-label {{
    color: #7ab8d8;
    letter-spacing: 4px;
    font-size: 0.85rem;
    text-transform: uppercase;
    margin-bottom: 8px;
}}
.end-title {{
    color: #9ff0ff;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    font-size: 2.3rem;
    font-weight: 900;
    text-shadow: 0 0 14px #00d5ff, 0 0 30px #0088ff, 0 0 60px #0033aa;
    letter-spacing: 2px;
    margin-bottom: 8px;
}}
.end-icon {{
    font-size: 4rem;
    margin-bottom: 10px;
}}
.end-lanterns {{
    font-size: 1.5rem;
    color: #ffd27f;
    letter-spacing: 4px;
    margin: 14px 0;
    text-shadow: 0 0 10px rgba(255,180,80,0.7);
}}
.tier-list {{
    margin-top: 22px;
    padding-top: 18px;
    border-top: 1px dashed rgba(0,213,255,0.4);
    font-size: 0.92rem;
    color: #a8c8e0;
    text-align: left;
}}
.tier-list .tier {{
    padding: 6px 0;
    border-bottom: 1px dashed rgba(0,213,255,0.15);
}}
.tier-list .tier.current {{
    color: #9ff0ff;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0,213,255,0.7);
}}
.re-attempt-note {{
    text-align: center;
    color: #ffaa66;
    margin-top: 12px;
    font-style: italic;
    font-size: 0.92rem;
    text-shadow: 0 0 6px rgba(255,170,102,0.4);
}}

@media (max-width: 640px) {{
    .main-title {{ font-size: 1.5rem; }}
    .wrong-text {{ font-size: 2rem; }}
    .ghost-icons {{ font-size: 5rem; }}
    .end-title {{ font-size: 1.7rem; }}
    .question-box {{ font-size: 1.02rem; padding: 16px 18px; }}
    .status-bar {{ font-size: 0.85rem; }}
    .intro-box {{ padding: 18px 20px; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

def lanterns_display(n):
    return "🏮" * n if n > 0 else "—"

def render_status_bar(idx):
    st.markdown(f"""
    <div class="status-bar">
        <div>📜 Câu {idx+1} / 10</div>
        <div class="lanterns">{lanterns_display(st.session_state.lanterns)} ({st.session_state.lanterns})</div>
    </div>
    """, unsafe_allow_html=True)

def render_intro():
    st.markdown("""
    <div class="intro-box">
        <div class="intro-label">📜 · Lời Tựa ·</div>
        <div class="intro-text">
            Giữa cõi âm dương mờ ảo, con người từ ngàn đời vẫn truyền tai nhau những câu chuyện về ma quái —
            những linh hồn không siêu thoát, những yêu tinh ẩn mình trong cây cỏ, sông hồ, và cả trong
            những ngôi nhà tưởng chừng bình yên nhất.
        </div>
        <div class="intro-text">
            <b>Âm Binh Ký</b> là hành trình lật giở <b>10 trang ký sự</b> về các loài ma quỷ trong dân gian Việt Nam.
            Mỗi câu trả lời đúng, ngươi sẽ thắp lên một ngọn đèn 🏮 — soi đường thoát khỏi màn đêm âm khí.
            Nhưng coi chừng: chỉ cần một phen lầm lạc, ma quỷ sẽ hiện về, và cơ hội tích đèn sẽ vụt mất.
        </div>
        <div class="intro-whisper">Ngươi đã sẵn sàng bước vào cõi âm chưa…? 👻</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🕯️   Bắt đầu hành trình", key="start_btn", use_container_width=True):
        start_new_game()
        st.rerun()

def render_question():
    idx = st.session_state.q_idx
    if idx >= len(st.session_state.quiz):
        st.session_state.finished = True
        st.rerun()
    q = st.session_state.quiz[idx]
    render_status_bar(idx)

    st.markdown(f'<div class="question-box">❓ {q["q"]}</div>', unsafe_allow_html=True)

    was_wrong = idx in st.session_state.wrong_attempted

    for i, opt in enumerate(q["options"]):
        label = f"{chr(65+i)}. {opt}"
        if st.button(label, key=f"opt_{idx}_{i}", use_container_width=True):
            if i == q["correct"]:
                if not was_wrong:
                    st.session_state.lanterns += 1
                st.session_state.show_explanation = True
                st.rerun()
            else:
                st.session_state.wrong_attempted.add(idx)
                st.session_state.show_wrong = True
                st.rerun()

    if was_wrong:
        st.markdown('<div class="re-attempt-note">⚠ Bạn đã trả lời sai câu này — lần này không tính điểm 🏮</div>',
                    unsafe_allow_html=True)

def render_wrong():
    st.markdown("""
    <div class="wrong-overlay">
        <div class="wrong-text">SAI RỒI!</div>
        <div class="ghost-icons">👻😡</div>
        <div class="wrong-hint">Ma quỷ đang hiện về...</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("↺  Chọn lại câu trả lời", key="retry_btn", use_container_width=True):
        st.session_state.show_wrong = False
        st.rerun()
    st.stop()

def render_explanation():
    idx = st.session_state.q_idx
    q = st.session_state.quiz[idx]
    correct_letter = chr(65 + q["correct"])
    correct_text = q["options"][q["correct"]]

    render_status_bar(idx)
    st.markdown(f'<div class="question-box">❓ {q["q"]}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="explain-box">
        <span class="label">✅ Đáp án đúng</span>
        <div class="correct-ans">{correct_letter}. {correct_text}</div>
        <span class="label">📖 Khái niệm</span>
        <div class="concept">{q["explanation"]}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("➜  Tiếp tục", key="continue_btn", use_container_width=True):
        st.session_state.show_explanation = False
        st.session_state.q_idx += 1
        if st.session_state.q_idx >= len(st.session_state.quiz):
            st.session_state.finished = True
        st.rerun()

def render_end():
    n = st.session_state.lanterns
    title_name, title_icon = get_title(n)

    tiers_html = ""
    for lo, hi, name, icon in TITLES:
        is_current = (lo <= n <= hi)
        cls = "tier current" if is_current else "tier"
        range_text = f"{lo}–{hi}"
        marker = " ◀ BẠN" if is_current else ""
        tiers_html += f'<div class="{cls}">{icon} {range_text} 🏮 → {name}{marker}</div>'

    st.markdown(f"""
    <div class="end-box">
        <div class="end-icon">{title_icon}</div>
        <div class="end-label">Danh hiệu của bạn</div>
        <div class="end-title">{title_name}</div>
        <div class="end-lanterns">{lanterns_display(n)} {n}/10 🏮</div>
        <div class="tier-list">
            <div style="color:#7feaff;font-weight:700;margin-bottom:8px;">🏅 Các danh hiệu khác</div>
            {tiers_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄  Chơi lại từ đầu", key="restart_btn", use_container_width=True):
        st.session_state.started = False
        st.session_state.finished = False
        st.session_state.quiz = []
        st.rerun()

st.markdown('<div class="main-title">👻 ÂM BINH KÝ 👻</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ký sự trắc nghiệm ma quái dân gian</div>', unsafe_allow_html=True)

if st.session_state.finished:
    render_end()
elif not st.session_state.started:
    render_intro()
elif st.session_state.show_wrong:
    render_wrong()
elif st.session_state.show_explanation:
    render_explanation()
else:
    render_question()
