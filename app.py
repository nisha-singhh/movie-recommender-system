import os
import streamlit as st
import pickle
import requests
import base64

# -----------------------------
# API Helpers
# -----------------------------
@st.cache_data 
def fetch_movie_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=c853b243"
    response = requests.get(url)
    return response.json()

@st.cache_data
def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=c853b243"
    try:
        response = requests.get(url)
        data = response.json()
        poster = data.get('Poster', None)
        if poster is None or poster == "N/A":
            poster = "https://via.placeholder.com/300x450?text=No+Image"
        return poster
    except:
        return "https://via.placeholder.com/300x450?text=No+Image"

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# -----------------------------
# Session State (Full Persistence)
# -----------------------------
if "page" not in st.session_state: st.session_state.page = "Home"
if "selected_movie" not in st.session_state: st.session_state.selected_movie = None
if "recommended_triggered" not in st.session_state: st.session_state.recommended_triggered = False
if "last_selected" not in st.session_state: st.session_state.last_selected = None
if "favourites" not in st.session_state: st.session_state.favourites = []

# -----------------------------
# Background & Full CSS (Restoring Visuals)
# -----------------------------
def set_bg_and_css(relative_path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, relative_path)
    
    encoded = ""
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

   # Aapka updated CSS (Maine spacing aur alignment thik kar di hai)
    css = f"""
    <style>
    /* 1. Full App Background */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}

    /* 2. Top Header (Logo + Nav + Search) */
    header[data-testid="stHeader"] {{
        background: rgba(10, 25, 47, 0.85);
        backdrop-filter: blur(15px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        height: 70px;
    }}

    /* Logo Styling */
    .logo-container {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding-left: 20px;
    }}

    /* 3. Navigation Bar Alignment */
    .nav-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin-top: -10px; /* Header ke saath align karne ke liye */
    }}

    .nav-btn {{
        background: linear-gradient(135deg, #0072ff 0%, #00c6ff 100%);
        color: white !important;
        padding: 8px 18px;
        border-radius: 50px; /* Pill shape */
        text-decoration: none;
        font-size: 14px;
        font-weight: 600;
        transition: 0.3s all ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}

    .nav-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,198,255,0.4);
    }}

    /* 4. Trending Ticker Sudhar */
    .ticker-container {{
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 8px 25px;
        margin: 20px auto;
        width: fit-content;
        font-size: 14px;
    }}

    /* 5. Main Hero Section */
    .main-title {{
        font-size: 56px;
        background: linear-gradient(to right, #00adb5, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
        margin-top: 40px;
    }}

    .subtext {{
        font-size: 20px;
        text-align: center;
        color: rgba(238, 238, 238, 0.8);
        margin-bottom: 30px;
    }}

    /* 6. Search/Select Box Fix */
    div[data-baseweb="select"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(0, 173, 181, 0.3) !important;
    }}

    /* 11. Movie Grid Buttons (Puraane wale fixes included) */
    [data-testid="stVerticalBlock"] > div > div > div > div.stButton {{
        height: 60px !important;
        display: flex !important;
        align-items: center !important;
    }}

    div.stButton > button[key^="btn_"] {{
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        height: 50px !important;
        background: rgba(0, 173, 181, 0.15) !important;
        border: 1px solid rgba(0, 173, 181, 0.4) !important;
        color: white !important;
        border-radius: 10px !important;
        font-size: 13px !important;
    }}

    /* Get Recommendation Button Style */
    .stButton>button {{
        background: linear-gradient(to right, #00c6ff, #0072ff) !important;
        padding: 12px 40px !important;
        border-radius: 30px !important;
        border: none !important;
        font-size: 18px !important;
    }}
    /* --- NEW MODERN FOOTER STYLING --- */
    .footer-container {{
        background: rgba(10, 25, 47, 0.95);
        color: #eeeeee;
        padding: 50px 0 20px 0;
        margin-top: 100px;
        border-top: 1px solid rgba(0, 173, 181, 0.3);
        width: 100%;
    }}

    .footer-content {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        padding: 0 20px;
    }}

    .footer-section {{
        flex: 1;
        min-width: 250px;
        margin-bottom: 30px;
    }}

    .footer-section h4 {{
        color: white;
        font-size: 18px;
        margin-bottom: 20px;
        font-weight: 600;
    }}

    .footer-section p, .footer-section a {{
        font-size: 14px;
        color: rgba(238, 238, 238, 0.7);
        text-decoration: none;
        display: block;
        margin-bottom: 10px;
        transition: 0.3s;
    }}

    .footer-section a:hover {{
        color: #00adb5;
        padding-left: 5px;
    }}

    .footer-bottom {{
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        padding-top: 20px;
        margin-top: 20px;
        font-size: 13px;
        color: rgba(238, 238, 238, 0.5);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
# Function jo title ko button ke andar dikhayega
def display_movie_grid(movie_data, grid_label):
    st.subheader(f"✨ {grid_label}")
    cols = st.columns(5)
    for idx, movie in enumerate(movie_data):
        with cols[idx % 5]:
            st.image(movie['poster'], use_container_width=True)
            # Ab Movie Title alag se nahi, seedha button ka label ban gaya hai
            if st.button(movie['title'], key=f"btn_{grid_label}_{idx}", use_container_width=True):
                st.session_state.selected_movie = movie['title']
                st.rerun()
# Calling the background function
set_bg_and_css("assets/golden-frame-blue-background.jpg")

# -----------------------------
# Navigation Logic
# -----------------------------
def go_home():
    st.session_state.page = "Home"
    st.session_state.selected_movie = None
    st.session_state.recommended_triggered = False
    st.rerun()

def go_favourites():
    st.session_state.page = "Favourites"
    st.session_state.selected_movie = None
    st.rerun()

# --- TOP NAVIGATION BAR ---
nav_cols = st.columns([2, 1, 1, 1, 1.5], gap="small") 

with nav_cols[0]:
    st.markdown("<h3 style='margin: 0; color: #00adb5;'>🎬 MRS</h3><p style='font-size:10px; margin:0; color:white;'>Movie Recommender System</p>", unsafe_allow_html=True) 

with nav_cols[1]:
    if st.button("🏠 Home", use_container_width=True):
        go_home()

with nav_cols[2]:
    st.button("🔍 Explore", use_container_width=True)

with nav_cols[3]:
    if st.button("💖 Favourites", use_container_width=True):
        go_favourites()

with nav_cols[4]:
    st.text_input("🔍 Quick Search", label_visibility="collapsed", placeholder="Search titles...")

# --- TRENDING TICKER ---
st.markdown("""
<div class="ticker-container">
    <span style="color: #f39c12; font-weight: bold;">🔥 Trending Now: </span> 
    <span style="color: #00adb5;">
        Dune Part Two | Oppenheimer | Deadpool & Wolverine | Inside Out 2 | Joker: Folie à Deux
    </span>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Data Loading (Core Logic)
# -----------------------------
try:
    movies = pickle.load(open('movie.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movie_list = movies['original_title'].values
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# -----------------------------
# Core Recommendation Function
# -----------------------------
def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[index]
    movie_list_ = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11] # Top 10 fetch
    recommended = []
    for i in movie_list_:
        title = movies.iloc[i[0]].original_title
        poster = fetch_poster(title)
        recommended.append((title, poster))
    return recommended

def display_movie_grid(movie_data, grid_label):
    st.subheader(f"✨ {grid_label}")
    cols = st.columns(5)
    for idx, movie in enumerate(movie_data):
        with cols[idx % 5]:
            # Poster image dikhayega
            st.image(movie['poster'], use_container_width=True)
            
            # Movie ka naam ab seedha button ke andar hoga
            # 'white-space: normal' use kiya hai taaki lamba naam button ke andar adjust ho jaye
            if st.button(movie['title'], key=f"btn_{grid_label}_{idx}", use_container_width=True):
                st.session_state.selected_movie = movie['title']
                st.rerun()

# -----------------------------
# MAIN APP FLOW (Full Functionality)
# -----------------------------

# 1. Page: Favourites
if st.session_state.page == "Favourites":
    st.title("⭐ My Saved Favourites")
    if not st.session_state.favourites:
        st.info("Aapki list abhi khali hai. Kuch movies add kijiye!")
    else:
        fav_data = [{"title": t, "poster": fetch_poster(t)} for t in st.session_state.favourites]
        display_movie_grid(fav_data, "My List")
    if st.button("Back to Home"): go_home()

# 2. Page: Movie Details (The full view you wanted)
elif st.session_state.selected_movie:
    data = fetch_movie_details(st.session_state.selected_movie)
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.image(data.get('Poster', ''), use_container_width=True)
    with col_b:
        st.header(st.session_state.selected_movie)
        st.markdown(f"**Rating:** ⭐ {data.get('imdbRating')}")
        st.markdown(f"**Genre:** {data.get('Genre')}")
        st.markdown(f"**Director:** {data.get('Director')}")
        st.markdown(f"**Actors:** {data.get('Actors')}")
        st.write(f"**Summary:** {data.get('Plot')}")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("💖 Save to Favourites"):
                if st.session_state.selected_movie not in st.session_state.favourites:
                    st.session_state.favourites.append(st.session_state.selected_movie)
                    st.success("Favourite mein add ho gaya!")
        with c2:
            if st.button("⬅️ Back to Browse"):
                st.session_state.selected_movie = None
                st.rerun()

# 3. Page: Home
else:
    st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Select a movie and we will find the best ones for you!</div>', unsafe_allow_html=True)

    # Search Section (Centered)
    search_col1, search_col2, search_col3 = st.columns([1, 2, 1])
    with search_col2:
        selected_movie_name = st.selectbox("Type or select a movie...", movie_list)
        if st.button("🔍 Get Recommendations"):
            st.session_state.recommended_triggered = True
            st.session_state.last_selected = selected_movie_name
            st.rerun()

    # Recommendations Result
    if st.session_state.recommended_triggered:
        recs = recommend(st.session_state.last_selected)
        rec_data = [{"title": r[0], "poster": r[1]} for r in recs]
        display_movie_grid(rec_data[:5], "🎯 Recommended For You")
        display_movie_grid(rec_data[5:], "🍿 More Like This")

    # Bottom Sections (Trending/Popular)
    st.write("---")
    popular_titles = movies['original_title'].iloc[20:30].tolist() # Example subset
    trending_data = [{"title": t, "poster": fetch_poster(t)} for t in popular_titles]
    display_movie_grid(trending_data, "🔥 Trending Worldwide")

#footer content 
st.markdown("""
<div class="footer-container">
    <div class="footer-content">
        <div class="footer-section">
            <h3 style="color: #00adb5;">🎬 MRS</h3>
            <p>Your personal gateway to cinema. We help you find the perfect movie based on your unique taste using advanced AI algorithms.</p>
        </div>
        <div class="footer-section">
            <h4>Quick Links</h4>
            <a href="#">Home</a>
            <a href="#">Explore</a>
            <a href="#">Favourites</a>
            <a href="#">Top Rated</a>
        </div>
        <div class="footer-section">
            <h4>Technology</h4>
            <p>🐍 Python & Streamlit</p>
            <p>🤖 Machine Learning</p>
            <p>📊 TMDB Dataset</p>
        </div>
        <div class="footer-section">
            <h4>Contact & Support</h4>
            <p>📍 MERI College, New Delhi</p>
            <p>✉️ support@mrs.app</p>
            <div class="social-icons">
                <span>🔗 GitHub</span> | <span>💼 LinkedIn</span>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2024 Movie Recommender System | MERI College Final Project</p>
        <p>Developed with ❤️ by Nisha | <span style="color: #00adb5;">● System Operational</span></p>
    </div>
</div>
""", unsafe_allow_html=True)