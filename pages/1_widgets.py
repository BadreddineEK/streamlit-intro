import streamlit as st

st.set_page_config(page_title="Les Widgets", page_icon="🎛️", layout="wide")

st.title("🎛️ Les Widgets")
st.caption("Les widgets sont les briques de base de toute interaction utilisateur dans Streamlit.")

st.markdown("""
Chaque widget retourne une **valeur Python** que tu utilises directement dans ton code.
Pas d'event listeners, pas de callbacks complexes — juste une variable.
""")

st.divider()

# ── Bouton ───────────────────────────────────────────────
st.markdown("### 🔘 st.button")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    if st.button("Clique ici", type="primary"):
        st.success("✅ Le bouton a été cliqué !")
    st.caption("Retourne `True` quand cliqué, `False` sinon.")
with col2:
    st.code('if st.button("Clique ici", type="primary"):\n    st.success("Cliqué !")') 

st.divider()

# ── Slider ───────────────────────────────────────────────
st.markdown("### 🎚️ st.slider")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    val = st.slider("Choisis une valeur", min_value=0, max_value=100, value=42)
    st.write(f"Valeur sélectionnée : **{val}**")
with col2:
    st.code('val = st.slider("Choisis une valeur", min_value=0, max_value=100, value=42)\nst.write(f"Valeur : {val}")')

st.divider()

# ── Selectbox ────────────────────────────────────────────
st.markdown("### 📋 st.selectbox")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    options = ["Pandas", "Polars", "DuckDB", "Spark"]
    choix = st.selectbox("Ta librairie data préférée ?", options)
    st.write(f"Tu as choisi : **{choix}**")
with col2:
    st.code('options = ["Pandas", "Polars", "DuckDB", "Spark"]\nchoix = st.selectbox("Ta librairie préférée ?", options)\nst.write(f"Tu as choisi : {choix}")')

st.divider()

# ── Text input ───────────────────────────────────────────
st.markdown("### ✏️ st.text_input")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    nom = st.text_input("Ton prénom", placeholder="ex: Badreddine")
    if nom:
        st.write(f"Bienvenue, **{nom}** 👋")
with col2:
    st.code('nom = st.text_input("Ton prénom", placeholder="ex: Badreddine")\nif nom:\n    st.write(f"Bienvenue, {nom} 👋")')

st.divider()

# ── Checkbox ─────────────────────────────────────────────
st.markdown("### ☑️ st.checkbox")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    dark = st.checkbox("Activer le mode sombre (simulé)")
    if dark:
        st.markdown("> 🌑 Imagine que l'interface vient de passer en sombre.")
    else:
        st.markdown("> ☀️ Mode clair activé.")
with col2:
    st.code('dark = st.checkbox("Mode sombre")\nif dark:\n    st.write("Mode sombre activé")')

st.divider()

# ── Multiselect ──────────────────────────────────────────
st.markdown("### 🏷️ st.multiselect")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    stack = st.multiselect(
        "Ton stack data ?",
        ["Python", "SQL", "Streamlit", "Docker", "Snowflake", "dbt", "FastAPI"],
        default=["Python", "Streamlit"]
    )
    if stack:
        st.write("Stack sélectionnée :", ", ".join(stack))
with col2:
    st.code('stack = st.multiselect(\n    "Ton stack data ?",\n    ["Python", "SQL", "Streamlit", "Docker"],\n    default=["Python", "Streamlit"]\n)')

st.divider()
st.info("👈 Passe au module **Données & graphiques** pour voir comment afficher et explorer des données.")
