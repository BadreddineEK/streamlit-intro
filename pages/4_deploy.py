import streamlit as st

st.set_page_config(page_title="Deployment", page_icon="🚀", layout="wide")

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
    st.title("🚀 Déployer son app")
    st.caption("De localhost:8501 à une URL publique — en 5 minutes, gratuitement.")
    st.markdown("Une app qui tourne uniquement sur ton ordinateur ne sert qu'à toi. Streamlit Cloud permet de déployer n'importe quel projet GitHub en quelques clics — et c'est **gratuit**.")
else:
    st.title("🚀 Deploy your app")
    st.caption("From localhost:8501 to a public URL — in 5 minutes, for free.")
    st.markdown("An app that only runs on your machine is only useful to you. Streamlit Cloud lets you deploy any GitHub project in a few clicks — and it's **free**.")

st.divider()

# ── Étapes ───────────────────────────────────────────────────────────
st.markdown("## 📋 " + ("Les 5 étapes" if FR else "5 steps"))

if FR:
    étapes = [
        ("1", "Crée ton `requirements.txt`",
         "Liste toutes les librairies utilisées.",
         "streamlit\npandas\nplotly\nnumpy"),
        ("2", "Push sur GitHub",
         "Ton repo doit contenir : `app.py` + `requirements.txt`.",
         "git add .\ngit commit -m 'feat: streamlit app'\ngit push origin main"),
        ("3", "Va sur share.streamlit.io",
         "Connecte-toi avec ton compte GitHub.", None),
        ("4", "Clique sur 'New app'",
         "Sélectionne ton repo, ta branche, et le fichier principal (`app.py`).", None),
        ("5", "Déploie 🎉",
         "Streamlit installe les dépendances et génère une URL publique.", None),
    ]
else:
    étapes = [
        ("1", "Create your `requirements.txt`",
         "List all the libraries your app uses.",
         "streamlit\npandas\nplotly\nnumpy"),
        ("2", "Push to GitHub",
         "Your repo must contain: `app.py` + `requirements.txt`.",
         "git add .\ngit commit -m 'feat: streamlit app'\ngit push origin main"),
        ("3", "Go to share.streamlit.io",
         "Sign in with your GitHub account.", None),
        ("4", "Click 'New app'",
         "Select your repo, branch, and main file (`app.py`).", None),
        ("5", "Deploy 🎉",
         "Streamlit installs dependencies and gives you a public URL.", None),
    ]

for num, titre, desc, code in étapes:
    with st.container(border=True):
        col1, col2 = st.columns([0.07, 0.93])
        with col1:
            st.markdown(f"## {num}")
        with col2:
            st.markdown(f"**{titre}**")
            st.write(desc)
            if code:
                st.code(code)

st.divider()

# ── requirements.txt ─────────────────────────────────────────────────
st.markdown("## 📦 `requirements.txt` — " + ("point critique" if FR else "the critical file"))
if FR:
    st.markdown("Si une librairie est absente, l'app plante au démarrage. C'est le fichier le plus important du déploiement.")
else:
    st.markdown("If a library is missing, the app crashes on startup. It's the most important file for deployment.")

with st.expander("📄 Voir un exemple" if FR else "📄 See an example"):
    st.code("""
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.0.0
numpy>=1.26.0
scikit-learn>=1.4.0
""", language="text")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### ✅ " + ("Bonne pratique" if FR else "Best practice"))
        if FR:
            st.markdown("""
- Génère avec `pip freeze > requirements.txt`
- Ou liste manuellement uniquement ce que tu utilises
- Spécifie des versions minimales avec `>=`
            """)
        else:
            st.markdown("""
- Generate with `pip freeze > requirements.txt`
- Or manually list only what you actually use
- Specify minimum versions with `>=`
            """)
with col2:
    with st.container(border=True):
        st.markdown("### ❌ " + ("Erreurs courantes" if FR else "Common mistakes"))
        if FR:
            st.markdown("""
- Oublier une librairie → `ModuleNotFoundError`
- Versionner trop strictement → conflits
- Inclure des librairies locales inutiles (ex: `pywin32`)
            """)
        else:
            st.markdown("""
- Forgetting a library → `ModuleNotFoundError`
- Pinning versions too strictly → dependency conflicts
- Including local-only packages (e.g. `pywin32`)
            """)

st.divider()

# ── Alternatives ─────────────────────────────────────────────────────
st.markdown("## 🔀 " + ("Alternatives à Streamlit Cloud" if FR else "Alternatives to Streamlit Cloud"))

alt = [
    ("🤗 Hugging Face Spaces", "Gratuit, idéal pour les apps ML/IA" if FR else "Free, ideal for ML/AI apps",             "https://huggingface.co/spaces"),
    ("🐳 Docker + VPS",        "Plus flexible, nécessite un serveur" if FR else "More flexible, requires a server",       "https://docs.streamlit.io/deploy/tutorials/docker"),
    ("☁️ GCP / AWS / Azure",   "Pour la production avec contraintes entreprise" if FR else "For production with enterprise constraints", "https://cloud.google.com"),
]

for nom, desc, lien in alt:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{nom}**")
            st.write(desc)
        with col2:
            st.link_button("Voir →" if FR else "See →", lien)

st.divider()

# ── Fin ──────────────────────────────────────────────────────────────
if FR:
    st.success("🎉 Tu sais maintenant créer et déployer une app Streamlit de A à Z !")
else:
    st.success("🎉 You now know how to build and deploy a Streamlit app from scratch!")

st.markdown("## 👤 " + ("À propos de cette app" if FR else "About this app"))
with st.container(border=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        if FR:
            st.markdown("""
**Badreddine EL KHAMLICHI**  
Diplôme ingénieur Polytech Lyon · Double master Maths & MAE IAE Lyon  

J'utilise Streamlit au quotidien pour créer des outils data viz sur mesure.  
Cette app est mon retour d'expérience condensé.
            """)
        else:
            st.markdown("""
**Badreddine EL KHAMLICHI**  
Engineering degree Polytech Lyon · Double master Maths & MAE IAE Lyon  

I use Streamlit daily to build custom data visualisation tools.  
This app is my condensed hands-on experience.
            """)
    with col2:
        st.link_button("🐙 GitHub", "https://github.com/BadreddineEK", use_container_width=True)
        st.link_button("🌐 Portfolio", "https://badreddineek.github.io/portfolioBadreddine", use_container_width=True)
