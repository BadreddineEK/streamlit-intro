import streamlit as st

st.set_page_config(
    page_title="Streamlit — Guide Interactif",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🐍 Streamlit Guide")
    st.caption("Une app pour apprendre Streamlit… avec Streamlit.")
    st.divider()
    st.markdown("### 📚 Modules")
    st.page_link("app.py",            label="🏠 Accueil",              icon=None)
    st.page_link("pages/1_widgets.py",   label="🎛️ Les widgets",          icon=None)
    st.page_link("pages/2_data.py",      label="📊 Données & graphiques", icon=None)
    st.page_link("pages/3_layouts.py",   label="🧱 Layouts & mise en page",icon=None)
    st.page_link("pages/4_deploy.py",    label="🚀 Déployer son app",     icon=None)
    st.divider()
    st.markdown("### 👤 Auteur")
    st.markdown("""
**Badreddine EL KHAMLICHI**  
Data Scientist @ Efor  
Mission : Boehringer Ingelheim Lyon  

[![GitHub](https://img.shields.io/badge/GitHub-BadreddineEK-black?logo=github)](https://github.com/BadreddineEK)
[![Portfolio](https://img.shields.io/badge/Portfolio-Voir-blue)](https://badreddineek.github.io/portfolioBadreddine)
    """)

# ── Main ─────────────────────────────────────────────────
st.title("🐍 Apprendre Streamlit, avec Streamlit")
st.subheader("Un guide interactif, pédagogique et concret.")

st.markdown("""
Streamlit, c'est la réponse à une question que tout data scientist finit par se poser :

> *"J'ai un modèle/une analyse qui tourne bien en local… comment je la montre à des gens qui ne codent pas ?"*

En quelques dizaines de lignes Python, Streamlit transforme un script en application web interactive, déployable gratuitement en ligne — sans HTML, sans CSS, sans JavaScript.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⚡ Setup", "< 5 min", help="pip install + 1 fichier .py")
with col2:
    st.metric("📦 Librairies", "100 %", "compatibles (Pandas, Plotly, sklearn…)")
with col3:
    st.metric("🚀 Déploiement", "Gratuit", "via Streamlit Cloud")
with col4:
    st.metric("🐍 Langage", "Python only", "pas de JS/HTML requis")

st.divider()

st.markdown("## 🗺️ Ce que tu vas apprendre")

modules = [
    ("🎛️", "Les widgets",           "Boutons, sliders, selectbox, text_input… tous les composants interactifs."),
    ("📊", "Données & graphiques",  "Afficher des DataFrames, tracer des courbes avec Plotly, filtrer en temps réel."),
    ("🧱", "Layouts & mise en page","Colonnes, tabs, expanders, sidebar — structurer une vraie app."),
    ("🚀", "Déployer son app",      "Passer de localhost:8501 à une URL publique en 5 minutes."),
]

for icon, titre, desc in modules:
    with st.container(border=True):
        st.markdown(f"### {icon} {titre}")
        st.write(desc)

st.divider()
st.markdown("## ⚡ Commencer en 3 lignes")

st.code("""
# 1. Installer
pip install streamlit

# 2. Créer hello.py
import streamlit as st
st.title("Hello, World !")
st.write("Mon app Streamlit tourne 🚀")

# 3. Lancer
streamlit run hello.py
""", language="bash")

st.info("👈 Commence par le module **Les widgets** dans la sidebar pour aller plus loin.")
