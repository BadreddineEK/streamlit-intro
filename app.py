import streamlit as st

st.set_page_config(
    page_title="Streamlit — Guide Interactif",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('<style>[data-testid="stSidebarNav"]{display:none}</style>', unsafe_allow_html=True)

def sidebar(key="home"):
    with st.sidebar:
        lang = st.radio("🌐", ["🇫🇷 FR", "🇬🇧 EN"], horizontal=True,
                        key=f"lang_{key}", label_visibility="collapsed")
        FR = "EN" not in lang
        st.divider()
        st.markdown("### 🗺️ Navigation")
        st.page_link("app.py",             label="🏠  " + ("Accueil"             if FR else "Home"))
        st.page_link("pages/1_widgets.py", label="🎛️  " + ("Les Widgets"          if FR else "Widgets"))
        st.page_link("pages/2_data.py",    label="📊  " + ("Données & Graphiques"  if FR else "Data & Charts"))
        st.page_link("pages/3_layouts.py", label="🧱  " + ("Layouts"              if FR else "Layouts"))
        st.page_link("pages/4_deploy.py",  label="🚀  " + ("Déploiement"           if FR else "Deployment"))
        st.page_link("pages/5_ml_demo.py", label="🤖  " + ("Démo ML"              if FR else "ML Demo"))
        st.divider()
        st.markdown("### 👤 " + ("Auteur" if FR else "Author"))
        st.markdown("""
**Badreddine EL KHAMLICHI**

[![GitHub](https://img.shields.io/badge/GitHub-BadreddineEK-black?logo=github)](https://github.com/BadreddineEK)
[![Portfolio](https://img.shields.io/badge/Portfolio-blue)](https://badreddineek.github.io/portfolioBadreddine)
        """)
        return FR

FR = sidebar("home")

if FR:
    st.title("🐍 Apprendre Streamlit, avec Streamlit")
    st.subheader("Un guide interactif, pédagogique et concret.")
    st.markdown("""
Streamlit répond à une question que tout data scientist finit par se poser :

> *« J'ai un modèle qui tourne bien en local… comment je le montre à des gens qui ne codent pas ? »*

En quelques dizaines de lignes Python, Streamlit transforme un script en application web interactive,
déployable gratuitement — sans HTML, sans CSS, sans JavaScript.
    """)
else:
    st.title("🐍 Learn Streamlit, with Streamlit")
    st.subheader("An interactive, practical, beginner-friendly guide.")
    st.markdown("""
Streamlit answers the question every data scientist eventually asks:

> *“My model runs great locally… how do I show it to people who don’t code?”*

With a few dozen lines of Python, Streamlit turns a script into an interactive web app,
deployable for free — no HTML, no CSS, no JavaScript.
    """)

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("⚡ Setup", "< 5 min")
with col2: st.metric("📦 Libraries", "100 %", "Pandas, Plotly, sklearn…")
with col3: st.metric("🚀 " + ("Déploiement" if FR else "Deploy"), "🌟 Free", "Streamlit Cloud")
with col4: st.metric("🐍 Code", "Python only", "pas de JS/HTML" if FR else "no JS/HTML")

st.divider()
st.markdown("## 🗺️ " + ("Ce que tu vas apprendre" if FR else "What you’ll learn"))

modules = [
    ("🎛️", "Les Widgets"          if FR else "Widgets",
              "Boutons, sliders, selectbox…" if FR else "Buttons, sliders, selectbox…"),
    ("📊", "Données & Graphiques"   if FR else "Data & Charts",
              "DataFrames filtrables + Plotly." if FR else "Filterable DataFrames + Plotly."),
    ("🧱", "Layouts"                if FR else "Layouts",
              "Colonnes, tabs, expanders." if FR else "Columns, tabs, expanders."),
    ("🚀", "Déploiement"            if FR else "Deployment",
              "localhost → URL publique en 5 min." if FR else "localhost → public URL in 5 min."),
    ("🤖", "Démo ML"                if FR else "ML Demo",
              "Modèle interactif, live." if FR else "Interactive model, live."),
]
cols = st.columns(5)
for col, (icon, titre, desc) in zip(cols, modules):
    with col:
        with st.container(border=True):
            st.markdown(f"#### {icon} {titre}")
            st.caption(desc)

st.divider()
st.markdown("## ⚡ " + ("Démarrer en 3 lignes" if FR else "Get started in 3 lines"))
st.code("""
pip install streamlit

# hello.py
import streamlit as st
st.title("Hello World 🚀")
st.write("My first Streamlit app!")

streamlit run hello.py
""", language="bash")
st.info("👈 " + ("Commence par **Les Widgets** dans la sidebar." if FR else "Start with **Widgets** in the sidebar."))
