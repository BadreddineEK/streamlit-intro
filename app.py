import streamlit as st

st.set_page_config(
    page_title="Streamlit — Guide Interactif",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Language toggle ──────────────────────────────────────────────────
with st.sidebar:
    lang = st.radio("🌐 Language", ["🇫🇷 Français", "🇬🇧 English"], horizontal=True, label_visibility="collapsed")
    st.divider()
    st.markdown("### 👤 Author" if "English" in lang else "### 👤 Auteur")
    st.markdown("""
**Badreddine EL KHAMLICHI**

[![GitHub](https://img.shields.io/badge/GitHub-BadreddineEK-black?logo=github)](https://github.com/BadreddineEK)
[![Portfolio](https://img.shields.io/badge/Portfolio-Voir-blue)](https://badreddineek.github.io/portfolioBadreddine)
    """)

FR = "English" not in lang

# ── Contenu ──────────────────────────────────────────────────────────
if FR:
    st.title("🐍 Apprendre Streamlit, avec Streamlit")
    st.subheader("Un guide interactif, pédagogique et concret.")
    st.markdown("""
Streamlit, c'est la réponse à une question que tout data scientist finit par se poser :

> *"J'ai un modèle/une analyse qui tourne bien en local… comment je la montre à des gens qui ne codent pas ?"

En quelques dizaines de lignes Python, Streamlit transforme un script en application web interactive,
déployable gratuitement en ligne — sans HTML, sans CSS, sans JavaScript.
    """)
else:
    st.title("🐍 Learn Streamlit, with Streamlit")
    st.subheader("An interactive, practical and beginner-friendly guide.")
    st.markdown("""
Streamlit answers the question every data scientist eventually asks:

> *"My model runs great locally… how do I show it to people who don't code?"

With just a few dozen lines of Python, Streamlit turns a script into an interactive web app,
deployable online for free — no HTML, no CSS, no JavaScript required.
    """)

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⚡ Setup", "< 5 min", help="pip install + 1 fichier .py" if FR else "pip install + 1 .py file")
with col2:
    st.metric("📦 Libraries", "100 %", "Pandas, Plotly, sklearn…")
with col3:
    st.metric("🚀 Deploy", "Free" if not FR else "Gratuit", "Streamlit Cloud")
with col4:
    st.metric("🐍 Language", "Python only", "no JS/HTML needed" if not FR else "pas de JS/HTML")

st.divider()

if FR:
    st.markdown("## 🗺️ Ce que tu vas apprendre")
    modules = [
        ("🎛️", "Les widgets",            "Boutons, sliders, selectbox, text_input… tous les composants interactifs."),
        ("📊", "Données & graphiques",   "Afficher des DataFrames, tracer des courbes avec Plotly, filtrer en temps réel."),
        ("🧱", "Layouts & mise en page", "Colonnes, tabs, expanders, sidebar — structurer une vraie app."),
        ("🚀", "Déployer son app",       "Passer de localhost:8501 à une URL publique en 5 minutes."),
    ]
else:
    st.markdown("## 🗺️ What you'll learn")
    modules = [
        ("🎛️", "Widgets",               "Buttons, sliders, selectbox, text_input… all interactive components."),
        ("📊", "Data & charts",          "Display DataFrames, plot with Plotly, filter in real time."),
        ("🧱", "Layouts",               "Columns, tabs, expanders, sidebar — build a structured app."),
        ("🚀", "Deployment",             "Go from localhost:8501 to a public URL in 5 minutes."),
    ]

for icon, titre, desc in modules:
    with st.container(border=True):
        st.markdown(f"### {icon} {titre}")
        st.write(desc)

st.divider()

if FR:
    st.markdown("## ⚡ Démarrer en 3 lignes")
else:
    st.markdown("## ⚡ Get started in 3 lines")

st.code("""
# 1. Install
pip install streamlit

# 2. Create hello.py
import streamlit as st
st.title("Hello, World!")
st.write("My Streamlit app is running 🚀")

# 3. Run
streamlit run hello.py
""", language="bash")

if FR:
    st.info("👈 Commence par le module **Les widgets** dans le menu de gauche.")
else:
    st.info("👈 Start with the **Widgets** module in the left menu.")
