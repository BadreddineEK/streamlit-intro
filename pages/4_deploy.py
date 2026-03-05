import streamlit as st

st.set_page_config(page_title="Déploiement", page_icon="🚀", layout="wide")

st.title("🚀 Déployer son app")
st.caption("De localhost:8501 à une URL publique — en 5 minutes, gratuitement.")

st.markdown("""
Une app qui tourne uniquement sur ton ordinateur ne sert qu'à toi.
Streamlit Cloud permet de déployer n'importe quel projet GitHub en quelques clics — et c'est **gratuit**.
""")

st.divider()

# ── Étapes ───────────────────────────────────────────────
st.markdown("## 📋 Les 5 étapes")

étapes = [
    ("1", "Crée ton fichier `requirements.txt`",
     "Liste toutes les librairies utilisées dans ton app.",
     "streamlit\npandas\nplotly\nnumpy"),
    ("2", "Push ton projet sur GitHub",
     "Ton repo doit contenir au minimum : `app.py` + `requirements.txt`.",
     "git add .\ngit commit -m 'feat: add streamlit app'\ngit push origin main"),
    ("3", "Va sur share.streamlit.io",
     "Connecte-toi avec ton compte GitHub.",
     None),
    ("4", "Clique sur 'New app'",
     "Sélectionne ton repo, ta branche, et le fichier principal (ex: `app.py`).",
     None),
    ("5", "Déploie 🎉",
     "Streamlit installe les dépendances, lance l'app, et te génère une URL publique.",
     None),
]

for num, titre, desc, code in étapes:
    with st.container(border=True):
        col1, col2 = st.columns([0.08, 0.92])
        with col1:
            st.markdown(f"## {num}")
        with col2:
            st.markdown(f"**{titre}**")
            st.write(desc)
            if code:
                st.code(code)

st.divider()

# ── requirements.txt ─────────────────────────────────────
st.markdown("## 📦 Le `requirements.txt` — point critique")
st.markdown("""
C'est le fichier le plus important du déploiement.
Si une librairie est absente, l'app plante au démarrage.
""")

with st.expander("Voir un exemple complet"):
    st.code("""
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.0.0
numpy>=1.26.0
scikit-learn>=1.4.0
# pinne les versions pour éviter les surprises
""", language="text")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### ✅ Bonne pratique")
        st.markdown("""
- Génère avec `pip freeze > requirements.txt`
- Ou mieux : liste manuellement uniquement ce que tu utilises
- Spécifie des versions minimales avec `>=`
        """)
with col2:
    with st.container(border=True):
        st.markdown("### ❌ Erreurs courantes")
        st.markdown("""
- Oublier une librairie → `ModuleNotFoundError` au déploiement
- Versionner trop strictement → conflits de dépendances
- Inclure des librairies locales inutiles (ex: `pywin32`)
        """)

st.divider()

# ── Alternatives ─────────────────────────────────────────
st.markdown("## 🔀 Alternatives à Streamlit Cloud")

alt = [
    ("🤗 Hugging Face Spaces", "Gratuit, idéal pour les apps ML/IA", "https://huggingface.co/spaces"),
    ("🐳 Docker + VPS",         "Plus flexible, nécessite un serveur", "https://docs.streamlit.io/deploy/tutorials/docker"),
    ("☁️ GCP / AWS / Azure",    "Pour des projets en production avec contraintes entreprise", "https://cloud.google.com"),
]

for icon_nom, desc, lien in alt:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{icon_nom}**")
            st.write(desc)
        with col2:
            st.link_button("Voir →", lien)

st.divider()

# ── Fin ───────────────────────────────────────────────────
st.success("🎉 Tu sais maintenant créer et déployer une app Streamlit de A à Z !")

st.markdown("## 👤 À propos de cette app")
with st.container(border=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
**Badreddine EL KHAMLICHI**  
Data Scientist @ Efor — Mission Boehringer Ingelheim, Lyon  
Diplôme ingénieur Polytech Lyon, double master Maths & MAE IAE Lyon  

J'utilise Streamlit au quotidien pour créer des outils data viz sur mesure.  
Cette app est mon retour d'expérience condensé.
        """)
    with col2:
        st.link_button("🐙 Mon GitHub", "https://github.com/BadreddineEK", use_container_width=True)
        st.link_button("🌐 Mon Portfolio", "https://badreddineek.github.io/portfolioBadreddine", use_container_width=True)
