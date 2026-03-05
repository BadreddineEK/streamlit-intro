import streamlit as st

st.set_page_config(page_title="Widgets", page_icon="🎛️", layout="wide")

# ── Language ─────────────────────────────────────────────────────────
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

if FR:
    st.title("🎛️ Les Widgets")
    st.caption("Les widgets sont les briques de base de toute interaction utilisateur dans Streamlit.")
    st.markdown("Chaque widget retourne une **valeur Python** utilisable directement. Pas de callbacks complexes — juste une variable.")
else:
    st.title("🎛️ Widgets")
    st.caption("Widgets are the building blocks of every user interaction in Streamlit.")
    st.markdown("Each widget returns a **Python value** you can use directly. No complex callbacks — just a variable.")

st.divider()

# ── st.button ────────────────────────────────────────────────────────
st.markdown("### 🔘 st.button")
col1, col2 = st.columns(2, gap="large")
with col1:
    label = "Clique ici" if FR else "Click here"
    msg   = "✅ Bouton cliqué !" if FR else "✅ Button clicked!"
    if st.button(label, type="primary"):
        st.success(msg)
    st.caption("`True` quand cliqué, `False` sinon." if FR else "`True` when clicked, `False` otherwise.")
with col2:
    st.code('if st.button("Click here", type="primary"):\n    st.success("Clicked!")')

st.divider()

# ── st.slider ────────────────────────────────────────────────────────
st.markdown("### 🎚️ st.slider")
col1, col2 = st.columns(2, gap="large")
with col1:
    lbl = "Choisis une valeur" if FR else "Pick a value"
    val = st.slider(lbl, min_value=0, max_value=100, value=42)
    txt = f"Valeur sélectionnée : **{val}**" if FR else f"Selected value: **{val}**"
    st.write(txt)
with col2:
    st.code('val = st.slider("Pick a value", min_value=0, max_value=100, value=42)\nst.write(f"Value: {val}")')

st.divider()

# ── st.selectbox ─────────────────────────────────────────────────────
st.markdown("### 📋 st.selectbox")
col1, col2 = st.columns(2, gap="large")
with col1:
    lbl   = "Ta librairie data préférée ?" if FR else "Your favourite data library?"
    choix = st.selectbox(lbl, ["Pandas", "Polars", "DuckDB", "Spark"])
    txt   = f"Tu as choisi : **{choix}**" if FR else f"You picked: **{choix}**"
    st.write(txt)
with col2:
    st.code('choix = st.selectbox("Your favourite?", ["Pandas", "Polars", "DuckDB", "Spark"])\nst.write(f"You picked: {choix}")')

st.divider()

# ── st.text_input ────────────────────────────────────────────────────
st.markdown("### ✏️ st.text_input")
col1, col2 = st.columns(2, gap="large")
with col1:
    lbl = "Ton prénom" if FR else "Your first name"
    nom = st.text_input(lbl, placeholder="ex: Badreddine")
    if nom:
        txt = f"Bienvenue, **{nom}** 👋" if FR else f"Welcome, **{nom}** 👋"
        st.write(txt)
with col2:
    st.code('nom = st.text_input("Your first name")\nif nom:\n    st.write(f"Welcome, {nom} 👋")')

st.divider()

# ── st.checkbox ──────────────────────────────────────────────────────
st.markdown("### ☑️ st.checkbox")
col1, col2 = st.columns(2, gap="large")
with col1:
    lbl  = "Afficher les détails" if FR else "Show details"
    show = st.checkbox(lbl)
    if show:
        msg = "> 📋 Voici les détails masqués par défaut." if FR else "> 📋 Here are the hidden details."
    else:
        msg = "> *(contenu masqué)*" if FR else "> *(content hidden)*"
    st.markdown(msg)
with col2:
    st.code('show = st.checkbox("Show details")\nif show:\n    st.write("Here are the details")')

st.divider()

# ── st.multiselect ───────────────────────────────────────────────────
st.markdown("### 🏷️ st.multiselect")
col1, col2 = st.columns(2, gap="large")
with col1:
    lbl   = "Ton stack data ?" if FR else "Your data stack?"
    stack = st.multiselect(lbl,
        ["Python", "SQL", "Streamlit", "Docker", "Snowflake", "dbt", "FastAPI"],
        default=["Python", "Streamlit"]
    )
    if stack:
        txt = ("Stack sélectionnée : " if FR else "Selected stack: ") + ", ".join(stack)
        st.write(txt)
with col2:
    st.code('stack = st.multiselect(\n    "Your data stack?",\n    ["Python", "SQL", "Streamlit", "Docker"],\n    default=["Python", "Streamlit"]\n)')

st.divider()
if FR:
    st.info("👈 Module suivant : **Données & Graphiques**")
else:
    st.info("👈 Next module: **Data & Charts**")
