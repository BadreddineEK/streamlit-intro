import streamlit as st

st.set_page_config(page_title="Widgets", page_icon="🎛️", layout="wide")

st.markdown('<style>[data-testid="stSidebarNav"] { display: none; }</style>', unsafe_allow_html=True)

with st.sidebar:
    lang = st.radio("🌐 Language", ["🇫🇷 Français", "🇬🇧 English"], horizontal=True, label_visibility="collapsed")
    FR = "English" not in lang
    st.divider()
    st.markdown("### 🗺️ Navigation")
    st.page_link("app.py",             label="🏠  " + ("Accueil" if FR else "Home"))
    st.page_link("pages/1_widgets.py", label="🎛️  " + ("Les Widgets" if FR else "Widgets"))
    st.page_link("pages/2_data.py",    label="📊  " + ("Données & Graphiques" if FR else "Data & Charts"))
    st.page_link("pages/3_layouts.py", label="🧱  " + ("Layouts" if FR else "Layouts"))
    st.page_link("pages/4_deploy.py",  label="🚀  " + ("Déploiement" if FR else "Deployment"))
    st.page_link("pages/5_ml_demo.py", label="🤖  " + ("Démo ML" if FR else "ML Demo"))
    st.divider()
    st.markdown("### 👤 " + ("Auteur" if FR else "Author"))
    st.markdown("""
**Badreddine EL KHAMLICHI**
[![GitHub](https://img.shields.io/badge/GitHub-BadreddineEK-black?logo=github)](https://github.com/BadreddineEK)
[![Portfolio](https://img.shields.io/badge/Portfolio-Voir-blue)](https://badreddineek.github.io/portfolioBadreddine)
    """)

FR = "English" not in lang

if FR:
    st.title("🎛️ Les Widgets")
    st.caption("Les widgets sont les briques de base de toute interaction utilisateur dans Streamlit.")
    st.markdown("Chaque widget retourne une **valeur Python** utilisable directement. Pas de callbacks — juste une variable.")
else:
    st.title("🎛️ Widgets")
    st.caption("Widgets are the building blocks of every user interaction in Streamlit.")
    st.markdown("Each widget returns a **Python value** you can use directly. No callbacks — just a variable.")

st.divider()

st.markdown("### 🔘 st.button")
col1, col2 = st.columns(2, gap="large")
with col1:
    if st.button("Clique ici" if FR else "Click here", type="primary"):
        st.success("✅ Bouton cliqué !" if FR else "✅ Button clicked!")
    st.caption("`True` quand cliqué, `False` sinon." if FR else "`True` when clicked, `False` otherwise.")
with col2:
    st.code('if st.button("Click here", type="primary"):\n    st.success("Clicked!")')

st.divider()
st.markdown("### 🎚️ st.slider")
col1, col2 = st.columns(2, gap="large")
with col1:
    val = st.slider("Choisis une valeur" if FR else "Pick a value", 0, 100, 42)
    st.write((f"Valeur : **{val}**") if FR else (f"Value: **{val}**"))
with col2:
    st.code('val = st.slider("Pick a value", 0, 100, 42)\nst.write(f"Value: {val}")')

st.divider()
st.markdown("### 📋 st.selectbox")
col1, col2 = st.columns(2, gap="large")
with col1:
    choix = st.selectbox("Ta librairie préférée ?" if FR else "Your favourite library?", ["Pandas", "Polars", "DuckDB", "Spark"])
    st.write((f"Tu as choisi : **{choix}**") if FR else (f"You picked: **{choix}**"))
with col2:
    st.code('choix = st.selectbox("Favourite?", ["Pandas", "Polars", "DuckDB"])\nst.write(f"You picked: {choix}")')

st.divider()
st.markdown("### ✏️ st.text_input")
col1, col2 = st.columns(2, gap="large")
with col1:
    nom = st.text_input("Ton prénom" if FR else "Your first name", placeholder="ex: Badreddine")
    if nom:
        st.write((f"Bienvenue, **{nom}** 👋") if FR else (f"Welcome, **{nom}** 👋"))
with col2:
    st.code('nom = st.text_input("Your name")\nif nom:\n    st.write(f"Welcome, {nom}!")')

st.divider()
st.markdown("### ☑️ st.checkbox")
col1, col2 = st.columns(2, gap="large")
with col1:
    show = st.checkbox("Afficher les détails" if FR else "Show details")
    st.markdown("> 📋 Détails visibles." if (show and FR) else ("> 📋 Details visible." if show else ("> *(masqué)*" if FR else "> *(hidden)*")))
with col2:
    st.code('show = st.checkbox("Show details")\nif show:\n    st.write("Details here")')

st.divider()
st.markdown("### 🏷️ st.multiselect")
col1, col2 = st.columns(2, gap="large")
with col1:
    stack = st.multiselect("Ton stack ?" if FR else "Your stack?",
        ["Python", "SQL", "Streamlit", "Docker", "Snowflake", "dbt", "FastAPI"],
        default=["Python", "Streamlit"])
    if stack:
        st.write(("Stack : " if FR else "Stack: ") + ", ".join(stack))
with col2:
    st.code('stack = st.multiselect("Your stack?",\n    ["Python", "SQL", "Streamlit"],\n    default=["Python"])')

st.divider()
st.info("👈 " + ("Module suivant : **Données & Graphiques**" if FR else "Next: **Data & Charts**"))
