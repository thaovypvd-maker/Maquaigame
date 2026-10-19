import streamlit as st

st.set_page_config(
    page_title="Ma Quái Dân Gian",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==== ẢNH NỀN (raw GitHub) ====
BG_URL = "https://raw.githubusercontent.com/thaovypvd-maker/Maquaigame/80969180e42358d1ec24d4ae8fd4612de5b3a02c/Background%20.JPG"

# ==== BỘ CÂU HỎI ====
QUESTIONS = [
    {
        "q": "Loại ma nào là người bị hổ cắn trong văn hóa dân gian?",
        "options": ["Ma trành", "Ma da", "Quỷ đói", "Hổ tinh"],
        "correct": 0,
        "explanation": "Ma trành là linh hồn của người bị hổ ăn thịt. Người này không thể siêu thoát mà trở thành \"nô lệ\" cho con hổ, đi dụ dỗ thêm người khác cho hổ bắt ăn.",
    },
    {
        "q": "Những linh hồn mất ở sông hồ được dân gian tin là sẽ thành ma gì?",
        "options": ["Ma lon", "Ma đuối", "Ma da", "Giao Long"],
        "correct": 2,
        "explanation": "Ma da là linh hồn của những người chết đuối, thường ẩn nấp ở sông, ao, hồ. Dân gian quan niệm ma da hay kéo chân người bơi lội để bắt thế mạng nhằm tìm cách siêu thoát.",
    },
    {
        "q": "Một loài quỷ có nguồn gốc từ Phật Giáo của Ấn Độ, đóng vai trò canh giữ, bảo vệ chùa chiền là?",
        "options": ["Quỷ đói", "Quỷ đầu cẩu", "Quỷ vương", "Quỷ dạ xoa - Yaksha"],
        "correct": 3,
        "explanation": "Quỷ Dạ Xoa là một chủng loại linh thể hoặc quỷ thần có nguồn gốc từ thần thoại Ấn Độ cổ đại, sau này được du nhập và tiếp biến trong văn hóa Phật giáo, Bà-la-môn giáo và dân gian Á Đông.",
    },
    {
        "q": "Một yêu quái là một cây chiên đàn cổ thụ, ngàn năm thành yêu quái đó là?",
        "options": ["Hồ ly tinh", "Mộc tinh - quỷ xương cuồng", "Tinh tinh", "Xà tinh"],
        "correct": 1,
        "explanation": "Mộc tinh hay còn gọi là quỷ xương cuồng là một yêu quái nổi tiếng trong truyền thuyết và thần thoại dân gian Việt Nam từ thời thượng cổ (thời đại Kinh Dương Vương đến thời Đinh Tiên Hoàng).",
    },
    {
        "q": "Chó trắng mũi đỏ trong dân gian thường được gắn với hình ảnh là?",
        "options": ["Chó đội nón mê", "Quỷ đầu cẩu", "Cẩu huyết", "Tất cả đáp án trên"],
        "correct": 0,
        "explanation": "Chó đội nón mê là một sinh vật hoặc điềm gở mang tính truyền thuyết và tín ngưỡng dân gian lâu đời tại Việt Nam (đặc biệt là vùng đồng quê Bắc Bộ).",
    },
    {
        "q": "Loại ma được thờ cúng trong nhà để bảo vệ, canh giữ điền trạch là?",
        "options": ["Ma trơi", "Ma lai", "Ma xó", "Ma men"],
        "correct": 2,
        "explanation": "Ma xó là một loại linh hồn hoặc vong linh được \"nuôi dưỡng\" và thờ cúng trong nhà để canh giữ, bảo vệ gia trạch hoặc phục vụ cho mục đích riêng của chủ nhân.",
    },
    {
        "q": "Loại ma có hình dạng là một đám lửa xanh?",
        "options": ["Ma giấu", "Ma đói - ngạ quỷ", "Thần trùng", "Ma trơi"],
        "correct": 3,
        "explanation": "Ma trơi là hiện tượng các đốm lửa nhỏ, lập lòe màu xanh nhạt, trắng, đỏ hoặc vàng thường xuất hiện vào ban đêm ở các khu vực như nghĩa trang, bãi tha ma hay đầm lầy.",
    },
    {
        "q": "Một dạng quỷ hút máu trong văn hóa tín ngưỡng Tây Bắc là?",
        "options": ["Ma cà rồng", "Ma cà chua", "Ma cà tím", "Phí phông"],
        "correct": 3,
        "explanation": "Trong thế giới quan của người Thái, Phí Phông được xem là một dạng quỷ hút máu hoặc kết hợp giữa xác người và hồn ma.",
    },
    {
        "q": "Loài thủy quái có hình dạng giống rồng trong dân gian là?",
        "options": ["Thuồng luồng", "Long vương", "Lông bông", "Ma da"],
        "correct": 0,
        "explanation": "Thuồng luồng là một loài thủy quái huyền thoại trong văn hóa dân gian Việt Nam và Á Đông. Được mô tả là hung dữ, có sức mạnh lớn, thường lật úp ghe thuyền hoặc bắt người hại dân vùng sông nước.",
    },
    {
        "q": "Một loại ma hay được dùng để chửi người khác?",
        "options": ["Ma lai", "Ma gà", "Âm binh", "Quỷ nhập tràng"],
        "correct": 2,
        "explanation": "Âm binh thường bao gồm các vong hồn chưa siêu thoát, oan hồn, linh hồn binh lính tử trận, hoặc các cô hồn vất vưởng được các thầy phù thủy, pháp sư, thầy cúng chiêu mộ và sai khiến.",
    },
]

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

# ==== KHỞI TẠO STATE ====
defaults = {
    "q_idx": 0,
    "lanterns": 0,
    "wrong_attempted": set(),
    "show_wrong": False,
    "show_explanation": False,
    "finished": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ==== CSS ====
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
    font-size: 2.2rem;
    font-weight: 900;
    color: #9ff0ff;
    text-shadow: 0 0 12px #00d5ff, 0 0 28px #0088ff, 0 0 60px #0033aa;
    margin: 10px 0 6px 0;
    letter-spacing: 2px;
}}
.subtitle {{
    text-align: center;
    color: #7ab8d8;
    font-size: 0.9rem;
    margin-bottom: 22px;
    letter-spacing: 3px;
    text-transform: uppercase;
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
    border: 2px solid #00d5ff;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 20px;
    backdrop-filter: blur(6px);
    animation: ledPulse 2.2s infinite;
    font-size: 1.18rem;
    font-weight: 700;
    color: #dff6ff;
    text-shadow: 0 0 8px rgba(0, 213, 255, 0.6);
}}
@keyframes ledPulse {{
    0%, 100% {{
        border-color: #00b8e8;
        box-shadow: 0 0 10px #00b8e8, 0 0 22px rgba(0,184,232,0.4), inset 0 0 14px rgba(0,184,232,0.15);
    }}
    50% {{
        border-color: #9ff0ff;
        box-shadow: 0 0 22px #00d5ff, 0 0 48px rgba(0,213,255,0.85), inset 0 0 28px rgba(0,213,255,0.35);
    }}
}}

.stButton > button {{
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
    box-shadow: 0 0 10px rgba(0,200,255,0.5), inset 0 0 8px rgba(0,200,255,0.15) !important;
    transition: all 0.18s ease !important;
    animation: ledBlink 1.6s infinite;
    margin-bottom: 6px;
}}
.stButton > button:hover {{
    background: rgba(0, 60, 110, 0.9) !important;
    color: #ffffff !important;
    transform: translateY(-1px) scale(1.01);
    box-shadow: 0 0 22px #00e5ff, 0 0 44px rgba(0,229,255,0.7), inset 0 0 16px rgba(0,229,255,0.35) !important;
    border-color: #00ffff !important;
}}
@keyframes ledBlink {{
    0%, 100% {{
        border-color: #00c8ff;
        box-shadow: 0 0 8px rgba(0,200,255,0.55), inset 0 0 8px rgba(0,200,255,0.15);
    }}
    50% {{
        border-color: #00ffff;
        box-shadow: 0 0 20px rgba(0,255,255,0.9), inset 0 0 16px rgba(0,255,255,0.35);
    }}
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
    0% {{
        transform: translateY(-500px);
        opacity: 0;
    }}
    20% {{
        opacity: 1;
    }}
    100% {{
        transform: translateY(0);
        opacity: 1;
    }}
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
    border: 2px solid #00d5ff;
    border-radius: 16px;
    padding: 30px 28px;
    text-align: center;
    backdrop-filter: blur(8px);
    box-shadow: 0 0 22px #00d5ff, 0 0 60px rgba(0,213,255,0.6), inset 0 0 28px rgba(0,213,255,0.15);
    margin: 20px 0;
    animation: ledPulse 3s infinite;
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
    font-size:()
 4rem;
    margin-bottom: 10px       ;
}}
.end-lantern sts {{
    font-size:.r 1.5rem;
    colorer: #ffd27fun;
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
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ==== HELPERS ====
def lanterns_display(n):
    return "🏮" * n if n > 0 else "—"

def render_status_bar(idx):
    st.markdown(f"""
    <div class="status-bar">
        <div>📜 Câu {idx+1} / 10</div>
        <div class="lanterns">{lanterns_display(st.session_state.lanterns)} ({st.session_state.lanterns})</div>
    </div>
    """, unsafe_allow_html=True)

# ==== SCREENS ====
def render_question():
    idx = st.session_state.q_idx
    q = QUESTIONS[idx]
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
    q = QUESTIONS[idx]
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
        if st.session_state.q_idx >= len(QUESTIONS):
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
        for k in ["q_idx", "lanterns", "show_wrong", "show_explanation", "finished"]:
            st.session_state[k] = 0 if k in ("q_idx", "lanterns") else False
        st.session_state.wrong_attempted = set()

# ==== HEADER ====
st.markdown('<div class="main-title">👻 MA QUÁI DÂN GIAN 👻</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Trắc nghiệm tâm linh · 10 câu hỏi</div>', unsafe_allow_html=True)

# ==== ROUTING ====
if st.session_state.finished:
    render_end()
elif st.session_state.show_wrong:
    render_wrong()
elif st.session_state.show_explanation:
    render_explanation()
else:
    render_question()
