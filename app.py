import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ma Quái Dân Gian",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==== ẢNH NỀN ====
BG_URL = "https://raw.githubusercontent.com/thaovypvd-maker/Maquaigame/80969180e42358d1ec24d4ae8fd4612de5b3a02c/Background%20.JPG"

# ==== TEAM INFO (sửa theo nhóm bạn) ====
TEAM_NAME = "Nhóm Ma Quái"
TEAM_MEMBERS = "Thành viên: [Tên bạn 1] · [Tên bạn 2] · [Tên bạn 3]"
TEAM_CLASS = "Lớp: [Tên lớp] · Môn: Tin học"

# ==== BỘ CÂU HỎI ====
QUESTIONS = [
    {"q": "Loại ma nào là người bị hổ cắn trong văn hóa dân gian?",
     "options": ["Ma trành", "Ma da", "Quỷ đói", "Hổ tinh"], "correct": 0,
     "explanation": "Ma trành là linh hồn của người bị hổ ăn thịt. Người này không thể siêu thoát mà trở thành \"nô lệ\" cho con hổ, đi dụ dỗ thêm người khác cho hổ bắt ăn."},
    {"q": "Những linh hồn mất ở sông hồ được dân gian tin là sẽ thành ma gì?",
     "options": ["Ma lon", "Ma đuối", "Ma da", "Giao Long"], "correct": 2,
     "explanation": "Ma da là linh hồn của những người chết đuối, thường ẩn nấp ở sông, ao, hồ. Dân gian quan niệm ma da hay kéo chân người bơi lội để bắt thế mạng nhằm tìm cách siêu thoát."},
    {"q": "Một loài quỷ có nguồn gốc từ Phật Giáo của Ấn Độ, đóng vai trò canh giữ, bảo vệ chùa chiền là?",
     "options": ["Quỷ đói", "Quỷ đầu cẩu", "Quỷ vương", "Quỷ dạ xoa - Yaksha"], "correct": 3,
     "explanation": "Quỷ Dạ Xoa là một chủng loại linh thể hoặc quỷ thần có nguồn gốc từ thần thoại Ấn Độ cổ đại, sau này được du nhập và tiếp biến trong văn hóa Phật giáo, Bà-la-môn giáo và dân gian Á Đông."},
    {"q": "Một yêu quái là một cây chiên đàn cổ thụ, ngàn năm thành yêu quái đó là?",
     "options": ["Hồ ly tinh", "Mộc tinh - quỷ xương cuồng", "Tinh tinh", "Xà tinh"], "correct": 1,
     "explanation": "Mộc tinh hay còn gọi là quỷ xương cuồng là một yêu quái nổi tiếng trong truyền thuyết và thần thoại dân gian Việt Nam từ thời thượng cổ (thời đại Kinh Dương Vương đến thời Đinh Tiên Hoàng)."},
    {"q": "Chó trắng mũi đỏ trong dân gian thường được gắn với hình ảnh là?",
     "options": ["Chó đội nón mê", "Quỷ đầu cẩu", "Cẩu huyết", "Tất cả đáp án trên"], "correct": 0,
     "explanation": "Chó đội nón mê là một sinh vật hoặc điềm gở mang tính truyền thuyết và tín ngưỡng dân gian lâu đời tại Việt Nam (đặc biệt là vùng đồng quê Bắc Bộ)."},
    {"q": "Loại ma được thờ cúng trong nhà để bảo vệ, canh giữ điền trạch là?",
     "options": ["Ma trơi", "Ma lai", "Ma xó", "Ma men"], "correct": 2,
     "explanation": "Ma xó là một loại linh hồn hoặc vong linh được \"nuôi dưỡng\" và thờ cúng trong nhà để canh giữ, bảo vệ gia trạch hoặc phục vụ cho mục đích riêng của chủ nhân."},
    {"q": "Loại ma có hình dạng là một đám lửa xanh?",
     "options": ["Ma giấu", "Ma đói - ngạ quỷ", "Thần trùng", "Ma trơi"], "correct": 3,
     "explanation": "Ma trơi là hiện tượng các đốm lửa nhỏ, lập lòe màu xanh nhạt, trắng, đỏ hoặc vàng thường xuất hiện vào ban đêm ở các khu vực như nghĩa trang, bãi tha ma hay đầm lầy."},
    {"q": "Một dạng quỷ hút máu trong văn hóa tín ngưỡng Tây Bắc là?",
     "options": ["Ma cà rồng", "Ma cà chua", "Ma cà tím", "Phí phông"], "correct": 3,
     "explanation": "Trong thế giới quan của người Thái, Phí Phông được xem là một dạng quỷ hút máu hoặc kết hợp giữa xác người và hồn ma."},
    {"q": "Loài thủy quái có hình dạng giống rồng trong dân gian là?",
     "options": ["Thuồng luồng", "Long vương", "Lông bông", "Ma da"], "correct": 0,
     "explanation": "Thuồng luồng là một loài thủy quái huyền thoại trong văn hóa dân gian Việt Nam và Á Đông. Được mô tả là hung dữ, có sức mạnh lớn, thường lật úp ghe thuyền hoặc bắt người hại dân vùng sông nước."},
    {"q": "Một loại ma hay được dùng để chửi người khác?",
     "options": ["Ma lai", "Ma gà", "Âm binh", "Quỷ nhập tràng"], "correct": 2,
     "explanation": "Âm binh thường bao gồm các vong hồn chưa siêu thoát, oan hồn, linh hồn binh lính tử trận, hoặc các cô hồn vất vưởng được các thầy phù thủy, pháp sư, thầy cúng chiêu mộ và sai khiến."},
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

# ==== SESSION ====
defaults = {
    "stage": "intro",
    "q_idx": 0,
    "lanterns": 0,
    "wrong_attempted": set(),
    "show_wrong": False,
    "show_explanation": False,
    "just_earned": False,
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
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    letter-spacing: 1px;
}}

.main-title {{
    text-align: center;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #9ff0ff;
    text-shadow: 0 0 14px #00d5ff, 0 0 30px #0088ff, 0 0 60px #0033aa;
    margin: 8px 0 4px 0;
    letter-spacing: 3px;
    animation: titleFloat 4s ease-in-out infinite;
}}
@keyframes titleFloat {{
    0%, 100% {{ transform: translateY(0); text-shadow: 0 0 14px #00d5ff, 0 0 30px #0088ff, 0 0 60px #0033aa; }}
    50% {{ transform: translateY(-4px); text-shadow: 0 0 22px #00e5ff, 0 0 44px #00aaff, 0 0 90px #0055cc; }}
}}
.subtitle {{
    text-align: center;
    color: #7ab8d8;
    font-size: 0.9rem;
    margin-bottom: 22px;
    letter-spacing: 3px;
    text-transform: uppercase;
}}

/* ========== INTRO ========== */
.intro-box {{
    background: rgba(0, 20, 40, 0.72);
    border: 2px solid rgba(0, 213, 255, 0.55);
    border-radius: 18px;
    padding: 34px 28px;
    text-align: center;
    backdrop-filter: blur(8px);
    box-shadow: 0 0 24px rgba(0,213,255,0.5), 0 0 60px rgba(0,213,255,0.25), inset 0 0 30px rgba(0,213,255,0.1);
    margin: 18px 0;
    animation: introPulse 3.5s ease-in-out infinite;
}}
@keyframes introPulse {{
    0%, 100% {{ box-shadow: 0 0 24px rgba(0,213,255,0.5), 0 0 60px rgba(0,213,255,0.25), inset 0 0 30px rgba(0,213,255,0.1); }}
    50% {{ box-shadow: 0 0 36px rgba(0,229,255,0.8), 0 0 80px rgba(0,229,255,0.4), inset 0 0 40px rgba(0,229,255,0.15); }}
}}
.intro-emoji {{
    font-size: 5rem;
    display: block;
    margin-bottom: 10px;
    animation: ghostFloat 3s ease-in-out infinite;
}}
@keyframes ghostFloat {{
    0%, 100% {{ transform: translateY(0) rotate(-3deg); }}
    50% {{ transform: translateY(-10px) rotate(3deg); }}
}}
.intro-welcome {{
    font-size: 1.15rem;
    color: #dff6ff;
    line-height: 1.7;
    margin-bottom: 20px;
}}
.intro-team {{
    background: rgba(0, 30, 55, 0.6);
    border: 1px solid rgba(0, 200, 255, 0.4);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 18px 0;
    color: #a8d8f0;
    font-size: 0.95rem;
    line-height: 1.8;
    box-shadow: 0 0 12px rgba(0,200,255,0.25);
}}
.intro-team strong {{ color: #7feaff; }}
.intro-hint {{
    color: #ffcc88;
    font-size: 0.88rem;
    margin-top: 14px;
    font-style: italic;
    letter-spacing: 1px;
}}

/* ========== SCORE PANEL ========== */
.score-panel {{
    background: rgba(0, 20, 40, 0.7);
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 14px 20px 10px 20px;
    margin-bottom: 18px;
    backdrop-filter: blur(6px);
    animation: rainbowBorder 4s linear infinite;
}}
@keyframes rainbowBorder {{
    0%   {{ border-color: #ff0044; box-shadow: 0 0 14px #ff0044, 0 0 28px rgba(255,0,68,0.5), inset 0 0 12px rgba(255,0,68,0.15); }}
    16%  {{ border-color: #ff8800; box-shadow: 0 0 14px #ff8800, 0 0 28px rgba(255,136,0,0.5), inset 0 0 12px rgba(255,136,0,0.15); }}
    33%  {{ border-color: #ffff00; box-shadow: 0 0 14px #ffff00, 0 0 28px rgba(255,255,0,0.5), inset 0 0 12px rgba(255,255,0,0.15); }}
    50%  {{ border-color: #00ff88; box-shadow: 0 0 14px #00ff88, 0 0 28px rgba(0,255,136,0.5), inset 0 0 12px rgba(0,255,136,0.15); }}
    66%  {{ border-color: #00c8ff; box-shadow: 0 0 14px #00c8ff, 0 0 28px rgba(0,200,255,0.5), inset 0 0 12px rgba(0,200,255,0.15); }}
    83%  {{ border-color: #8800ff; box-shadow: 0 0 14px #8800ff, 0 0 28px rgba(136,0,255,0.5), inset 0 0 12px rgba(136,0,255,0.15); }}
    100% {{ border-color: #ff0044; box-shadow: 0 0 14px #ff0044, 0 0 28px rgba(255,0,68,0.5), inset 0 0 12px rgba(255,0,68,0.15); }}
}}
.score-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    gap: 10px;
}}
.score-col .label {{
    color: #7ab8d8;
    font-size: 0.72rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 2px;
}}
.score-col .value {{
    color: #9ff0ff;
    font-size: 1.6rem;
    font-weight: 900;
    text-shadow: 0 0 10px #00d5ff, 0 0 22px rgba(0,213,255,0.6);
    line-height: 1;
}}
.score-col .value span {{
    font-size: 0.9rem;
    color: #7ab8d8;
    margin-left: 2px;
    font-weight: 600;
}}
.score-col.center {{ text-align: center; flex: 1; }}
.score-col.right {{ text-align: right; }}
.score-col.right .value {{ color: #ffd27f; text-shadow: 0 0 10px #ffb84d, 0 0 22px rgba(255,184,77,0.6); }}

.lanterns-row {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 4px;
    min-height: 32px;
    align-items: center;
    margin-bottom: 6px;
}}
.lantern {{
    font-size: 1.35rem;
    display: inline-block;
    animation: lanternPop 0.55s cubic-bezier(0.34, 1.56, 0.64, 1) backwards;
    filter: drop-shadow(0 0 6px rgba(255,180,80,0.8));
}}
.lantern:nth-child(1)  {{ animation-delay: 0.00s; }}
.lantern:nth-child(2)  {{ animation-delay: 0.06s; }}
.lantern:nth-child(3)  {{ animation-delay: 0.12s; }}
.lantern:nth-child(4)  {{ animation-delay: 0.18s; }}
.lantern:nth-child(5)  {{ animation-delay: 0.24s; }}
.lantern:nth-child(6)  {{ animation-delay: 0.30s; }}
.lantern:nth-child(7)  {{ animation-delay: 0.36s; }}
.lantern:nth-child(8)  {{ animation-delay: 0.42s; }}
.lantern:nth-child(9)  {{ animation-delay: 0.48s; }}
.lantern:nth-child(10) {{ animation-delay: 0.54s; }}
@keyframes lanternPop {{
    0%   {{ transform: scale(0) rotate(-180deg); opacity: 0; }}
    60%  {{ transform: scale(1.35) rotate(15deg); opacity: 1; }}
    100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
}}
.no-lantern {{
    color: #4a6880;
    font-size: 0.85rem;
    letter-spacing: 2px;
    font-style: italic;
}}

.progress-track {{
    height: 6px;
    background: rgba(0, 30, 55, 0.9);
    border-radius: 4px;
    overflow: hidden;
    margin-top: 4px;
    box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
}}
.progress-fill {{
    height: 100%;
    background: linear-gradient(90deg, #00c8ff, #00ffcc, #7feaff);
    box-shadow: 0 0 12px #00e5ff, 0 0 20px rgba(0,229,255,0.7);
    border-radius: 4px;
    transition: width 0.6s ease;
}}
.plus-one {{
    display: inline-block;
    color: #ffd27f;
    font-weight: 900;
    font-size: 1.05rem;
    margin-left: 6px;
    text-shadow: 0 0 8px #ffb84d, 0 0 18px rgba(255,184,77,0.8);
    animation: plusFloat 1.6s ease-out forwards;
}}
@keyframes plusFloat {{
    0%   {{ transform: translateY(0); opacity: 0; }}
    15%  {{ opacity: 1; }}
    100% {{ transform: translateY(-22px); opacity: 0; }}
}}

/* ========== QUESTION BOX RAINBOW ========== */
.question-box {{
    background: rgba(0, 22, 45, 0.68);
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 20px;
    backdrop-filter: blur(6px);
    font-size: 1.18rem;
    font-weight: 700;
    color: #dff6ff;
    text-shadow: 0 0 8px rgba(0, 213, 255, 0.6);
    animation: rainbowBorder 3.5s linear infinite;
}}

/* ========== BUTTONS ========== */
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
    0%, 100% {{ border-color: #00c8ff; box-shadow: 0 0 8px rgba(0,200,255,0.55), inset 0 0 8px rgba(0,200,255,0.15); }}
    50% {{ border-color: #00ffff; box-shadow: 0 0 20px rgba(0,255,255,0.9), inset 0 0 16px rgba(0,255,255,0.35); }}
}}

/* Start button - rainbow */
.st-key-start_btn button {{
    background: rgba(20, 0, 40, 0.9) !important;
    color: #ffffff !important;
    font-size: 1.25rem !important;
    font-weight: 900 !important;
    padding: 18px 22px !important;
    letter-spacing: 3px !important;
    text-align: center !important;
    border: 2px solid transparent !important;
    animation: rainbowBorder 2.5s linear infinite, startPulse 2s ease-in-out infinite !important;
}}
@keyframes startPulse {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.03); }}
}}
.st-key-start_btn button:hover {{
    transform: scale(1.05) !important;
    color: #ffe0ff !important;
}}

/* Continue button */
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

/* Retry button */
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

/* Restart button */
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

/* ========== EXPLANATION ========== */
.explain-box {{
    background: rgba(0, 30, 50, 0.8);
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 22px 26px;
    margin: 18px 0;
    backdrop-filter: blur(6px);
    color: #e0fff8;
    font-size: 1.05rem;
    line-height: 1.7;
    animation: rainbowBorder 4s linear infinite;
}}
.explain-box .correct-ans {{
    color: #7dffcf;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0,255,180,0.7);
    margin-bottom: 14px;
    font-size: 1.15rem;
    animation: correctGlow 1.5s ease-in-out infinite;
}}
@keyframes correctGlow {{
    0%, 100% {{ text-shadow: 0 0 8px rgba(0,255,180,0.7); }}
    50% {{ text-shadow: 0 0 16px rgba(0,255,180,1), 0 0 32px rgba(0,255,180,0.6); }}
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
.explain-box .concept {{ font-size: 1rem; color: #d0f0ff; }}

/* ========== WRONG OVERLAY ========== */
.wrong-overlay {{
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at center, rgba(220,30,30,0.94), rgba(40,0,0,0.98));
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
    0%   {{ opacity: 0; }}
    50%  {{ opacity: 1; background: radial-gradient(circle at center, rgba(255,80,80,0.95), rgba(80,0,0,1)); }}
    100% {{ opacity: 1; }}
}}
.wrong-text {{
    color: #fff;
    font-size: 3.4rem;
    font-weight: 900;
    letter-spacing: 6px;
    text-shadow: 0 0 20px #ff0000, 0 0 40px #ff3333, 0 0 80px #aa0000;
    margin-bottom: 30px;
    animation: textShake 0.4s infinite;
}}
@keyframes textShake {{
    0%, 100% {{ transform: translateX(0); }}
    25% {{ transform: translateX(-5px); }}
    75% {{ transform: translateX(5px); }}
}}
.ghost-icons {{
    font-size: 7rem;
    display: inline-block;
    opacity: 0;
    animation: descend 2.8s cubic-bezier(0.6, 0.04, 0.98, 0.34) forwards;
    filter: drop-shadow(0 0 24px #ff2222) drop-shadow(0 0 48px #aa0000);
}}
@keyframes descend {{
    0%   {{ transform: translateY(-600px); opacity: 0; }}
    15%  {{ opacity: 1; }}
    85%  {{ transform: translateY(0); opacity: 1; }}
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

/* ========== END ========== */
.end-box {{
    background: rgba(0, 20, 40, 0.8);
    border: 2px solid transparent;
    border-radius: 16px;
    padding: 30px 28px;
    text-align: center;
    backdrop-filter: blur(8px);
    margin: 20px 0;
    animation: rainbowBorder 3s linear infinite;
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
    font-size: 2.4rem;
    font-weight: 900;
    text-shadow: 0 0 14px #00d5ff, 0 0 30px #0088ff, 0 0 60px #0033aa;
    letter-spacing: 2px;
    margin-bottom: 8px;
    animation: titleFloat 3s ease-in-out infinite;
}}
.end-icon {{
    font-size: 4.5rem;
    margin-bottom: 10px;
    animation: ghostFloat 2.5s ease-in-out infinite;
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

@media (max-width: 640px) {{
    .main-title {{ font-size: 1.6rem; }}
    .wrong-text {{ font-size: 2rem; }}
    .ghost-icons {{ font-size: 5rem; }}
    .end-title {{ font-size: 1.7rem; }}
    .question-box {{ font-size: 1.02rem; padding: 16px 18px; }}
    .score-col .value {{ font-size: 1.3rem; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ==== RENDER HELPERS ====
def render_score_bar(idx):
    pct = (idx / len(QUESTIONS)) * 100
    lanterns_html = "".join(f'<span class="lantern">🏮</span>' for _ in range(st.session_state.lanterns))
    if st.session_state.lanterns == 0:
        lanterns_html = '<span class="no-lantern">— chưa có đèn lồng nào —</span>'
    plus = '<span class="plus-one">+1 🏮</span>' if st.session_state.just_earned else ""
    st.markdown(f"""
    <div class="score-panel">
        <div class="score-top">
            <div class="score-col">
                <div class="label">Câu</div>
                <div class="value">{idx+1}<span>/{len(QUESTIONS)}</span></div>
            </div>
            <div class="score-col center">
                <div class="lanterns-row">{lanterns_html}</div>
            </div>
            <div class="score-col right">
                <div class="label">Điểm</div>
                <div class="value">{st.session_state.lanterns}<span>🏮</span>{plus}</div>
            </div>
        </div>
        <div class="progress-track"><div class="progress-fill" style="width:{pct}%"></div></div>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.just_earned:
        st.session_state.just_earned = False

def render_intro():
    st.markdown(f"""
    <div class="intro-box">
        <span class="intro-emoji">👻</span>
        <div class="intro-welcome">
            Chào mừng ngươi đến với <b>Ma Quái Dân Gian</b>!<br>
            Nơi đây có 10 câu hỏi về các loại ma quỷ trong tín ngưỡng dân gian Việt Nam.<br>
            Trả lời đúng để thắp sáng đèn lồng 🏮 và nhận danh hiệu pháp sư!
        </div>
        <div class="intro-team">
            <strong>{TEAM_NAME}</strong><br>
            {TEAM_MEMBERS}<br>
            {TEAM_CLASS}
        </div>
        <div class="intro-hint">🎵 Bật loa lên nhé — ma quỷ sẽ gào thét khi ngươi trả lời sai đó...</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)

    if st.button("▶  BẮT ĐẦU", key="start_btn", use_container_width=True):
        st.session_state.stage = "playing"
        st.session_state.q_idx = 0
        st.session_state.lanterns = 0
        st.session_state.wrong_attempted = set()
        st.session_state.show_wrong = False
        st.session_state.show_explanation = False
        st.session_state.just_earned = False
        st.rerun()

def render_question():
    idx = st.session_state.q_idx
    q = QUESTIONS[idx]
    render_score_bar(idx)

    st.markdown(f'<div class="question-box">❓ {q["q"]}</div>', unsafe_allow_html=True)

    was_wrong = idx in st.session_state.wrong_attempted

    for i, opt in enumerate(q["options"]):
        label = f"{chr(65+i)}. {opt}"
        if st.button(label, key=f"opt_{idx}_{i}", use_container_width=True):
            if i == q["correct"]:
                if not was_wrong:
                    st.session_state.lanterns += 1
                    st.session_state.just_earned = True
                st.session_state.show_explanation = True
                st.rerun()
            else:
                st.session_state.wrong_attempted.add(idx)
                st.session_state.show_wrong = True
                st.rerun()

    if was_wrong:
        st.markdown('<div class="re-attempt-note" style="text-align:center;color:#ffaa66;margin-top:12px;font-style:italic;">⚠ Bạn đã trả lời sai câu này — lần này không tính điểm 🏮</div>',
                    unsafe_allow_html=True)

def play_scream():
    scream_html = """
    <script>
    (function() {
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (ctx.state === 'suspended') ctx.resume();
            const now = ctx.currentTime;

            const master = ctx.createGain();
            master.gain.setValueAtTime(0.0001, now);
            master.gain.exponentialRampToValueAtTime(0.55, now + 0.08);
            master.gain.setValueAtTime(0.55, now + 1.0);
            master.gain.exponentialRampToValueAtTime(0.0001, now + 1.6);
            master.connect(ctx.destination);

            const k = 80, n = 8192;
            const curve = new Float32Array(n);
            for (let i = 0; i < n; ++i) {
                const x = (i * 2) / n - 1;
                curve[i] = ((3 + k) * x * 20 * (Math.PI / 180)) / (Math.PI + k * Math.abs(x));
            }
            const shaper = ctx.createWaveShaper();
            shaper.curve = curve;
            shaper.oversample = '4x';
            shaper.connect(master);

            const osc1 = ctx.createOscillator();
            osc1.type = 'sawtooth';
            osc1.frequency.setValueAtTime(1400, now);
            osc1.frequency.exponentialRampToValueAtTime(280, now + 1.3);

            const osc2 = ctx.createOscillator();
            osc2.type = 'square';
            osc2.frequency.setValueAtTime(220, now);
            osc2.frequency.exponentialRampToValueAtTime(80, now + 1.3);

            const lfo = ctx.createOscillator();
            lfo.frequency.value = 22;
            const lfoGain = ctx.createGain();
            lfoGain.gain.value = 120;
            lfo.connect(lfoGain);
            lfoGain.connect(osc1.frequency);

            const bp = ctx.createBiquadFilter();
            bp.type = 'bandpass';
            bp.frequency.setValueAtTime(2000, now);
            bp.frequency.exponentialRampToValueAtTime(700, now + 1.3);
            bp.Q.value = 4;
            bp.connect(shaper);

            osc1.connect(bp);
            osc2.connect(bp);

            const bufLen = ctx.sampleRate * 1.5;
            const noiseBuf = ctx.createBuffer(1, bufLen, ctx.sampleRate);
            const d = noiseBuf.getChannelData(0);
            for (let i = 0; i < bufLen; i++) {
                d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / bufLen, 1.8);
            }
            const noise = ctx.createBufferSource();
            noise.buffer = noiseBuf;
            const nf = ctx.createBiquadFilter();
            nf.type = 'highpass';
            nf.frequency.value = 1200;
            const ng = ctx.createGain();
            ng.gain.value = 0.4;
            noise.connect(nf);
            nf.connect(ng);
            ng.connect(shaper);

            osc1.start(now); osc1.stop(now + 1.4);
            osc2.start(now); osc2.stop(now + 1.4);
            lfo.start(now); lfo.stop(now + 1.4);
            noise.start(now);
        } catch (e) {
            console.log('Scream error:', e);
        }
    })();
    </script>
    """
    components.html(scream_html, height=0, width=0)

def render_wrong():
    play_scream()
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

    render_score_bar(idx)
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
            st.session_state.stage = "end"
        st.rerun()

def render_end():
    n = st.session_state.lanterns
    title_name, title_icon = get_title(n)

    tiers_html = ""
    for lo, hi, name, icon in TITLES:
        is_current = (lo <= n <= hi)
        cls = "tier current" if is_current else "tier"
        marker = " ◀ BẠN" if is_current else ""
        tiers_html += f'<div class="{cls}">{icon} {lo}–{hi} 🏮 → {name}{marker}</div>'

    lanterns_html = "".join("🏮" for _ in range(n)) if n > 0 else "—"

    st.markdown(f"""
    <div class="end-box">
        <div class="end-icon">{title_icon}</div>
        <div class="end-label">Danh hiệu của bạn</div>
        <div class="end-title">{title_name}</div>
        <div class="end-lanterns">{lanterns_html} &nbsp; {n}/10 🏮</div>
        <div class="tier-list">
            <div style="color:#7feaff;font-weight:700;margin-bottom:8px;">🏅 Các danh hiệu khác</div>
            {tiers_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄  Chơi lại từ đầu", key="restart_btn", use_container_width=True):
        st.session_state.stage = "intro"
        st.session_state.q_idx = 0
        st.session_state.lanterns = 0
        st.session_state.wrong_attempted = set()
        st.session_state.show_wrong = False
        st.session_state.show_explanation = False
        st.session_state.just_earned = False
        st.rerun()

# ==== HEADER ====
st.markdown('<div class="main-title">👻 MA QUÁI DÂN GIAN 👻</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Trắc nghiệm tâm linh · 10 câu hỏi</div>', unsafe_allow_html=True)

# ==== ROUTING ====
if st.session_state.stage == "intro":
    render_intro()
elif st.session_state.stage == "end":
    render_end()
elif st.session_state.show_wrong:
    render_wrong()
elif st.session_state.show_explanation:
    render_explanation()
else:
    render_question()
