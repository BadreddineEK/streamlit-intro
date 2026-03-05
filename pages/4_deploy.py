import streamlit as st

st.set_page_config(page_title="Deployment", page_icon="🚀", layout="wide")
st.markdown('<style>[data-testid="stSidebarNav"]{display:none}</style>', unsafe_allow_html=True)

with st.sidebar:
    lang = st.radio("🌐", ["🇫🇷 FR", "🇬🇧 EN"], horizontal=True, key="lang_dp", label_visibility="collapsed")
    FR = "EN" not in lang
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
[![Portfolio](https://img.shields.io/badge/Portfolio-blue)](https://badreddineek.github.io/portfolioBadreddine)
    """)

if FR:
    st.title("🚀 Déployer son app")
    st.caption("De localhost:8501 à une URL publique — en 5 min, gratuitement.")
    st.markdown("Une app qui tourne uniquement sur ton ordinateur ne sert qu’à toi. Streamlit Cloud déploie n’importe quel repo GitHub en quelques clics — **gratuitement**.")
else:
    st.title("🚀 Deploy your app")
    st.caption("From localhost:8501 to a public URL — in 5 min, for free.")
    st.markdown("An app that only runs on your machine is only useful to you. Streamlit Cloud deploys any GitHub repo in a few clicks — **for free**.")

st.divider()
st.markdown("## 📋 " + ("Les 5 étapes" if FR else "5 steps"))

steps_fr = [
    ("1", "Crée ton `requirements.txt`",     "Liste toutes les librairies de ton app.",                  "streamlit\npandas\nplotly\nnumpy"),
    ("2", "Push sur GitHub",                  "`app.py` + `requirements.txt` dans le repo.",              "git add .\ngit commit -m 'feat: app'\ngit push origin main"),
    ("3", "Va sur share.streamlit.io",         "Connecte ton compte GitHub.",                             None),
    ("4", "Clique ‘New app’",               "Sélectionne repo, branche et `app.py`.",                   None),
    ("5", "Déploie 🎉",                       "Streamlit installe les déps et génère une URL publique.", None),
]
steps_en = [
    ("1", "Create `requirements.txt`",        "List all your app’s libraries.",                          "streamlit\npandas\nplotly\nnumpy"),
    ("2", "Push to GitHub",                   "Repo must contain `app.py` + `requirements.txt`.",         "git add .\ngit commit -m 'feat: app'\ngit push origin main"),
    ("3", "Go to share.streamlit.io",          "Sign in with your GitHub account.",                       None),
    ("4", "Click ‘New app’",                "Select repo, branch and `app.py`.",                        None),
    ("5", "Deploy 🎉",                        "Streamlit builds deps and gives you a public URL.",        None),
]
for num, titre, desc, code in (steps_fr if FR else steps_en):
    with st.container(border=True):
        c1, c2 = st.columns([0.07, 0.93])
        with c1: st.markdown(f"## {num}")
        with c2:
            st.markdown(f"**{titre}**")
            st.write(desc)
            if code: st.code(code)

st.divider()
st.markdown("## 📦 `requirements.txt`")
with st.expander("📄 " + ("Voir un exemple" if FR else "See an example")):
    st.code("streamlit>=1.32.0\npandas>=2.0.0\nplotly>=5.0.0\nnumpy>=1.26.0\nscikit-learn>=1.4.0", language="text")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### ✅ " + ("Bonnes pratiques" if FR else "Best practices"))
        st.markdown("- `pip freeze > requirements.txt`\n- Versions min avec `>=`\n- Lister uniquement ce qu’on utilise" if FR
                    else "- `pip freeze > requirements.txt`\n- Minimum versions with `>=`\n- Only list what you actually use")
with col2:
    with st.container(border=True):
        st.markdown("### ❌ " + ("Erreurs fréquentes" if FR else "Common mistakes"))
        st.markdown("- Librairie oubliée → `ModuleNotFoundError`\n- Versions trop strictes → conflits\n- Packages locaux (ex: `pywin32`)" if FR
                    else "- Missing lib → `ModuleNotFoundError`\n- Versions too strict → conflicts\n- Local-only packages (e.g. `pywin32`)")

st.divider()
st.markdown("## 🔀 " + ("Alternatives" if FR else "Alternatives"))
for nom, desc, url in [
    ("🤗 Hugging Face Spaces", "Gratuit, parfait pour ML/IA" if FR else "Free, great for ML/AI",         "https://huggingface.co/spaces"),
    ("🐳 Docker + VPS",        "Flexible, serveur requis" if FR else "Flexible, needs a server",        "https://docs.streamlit.io/deploy/tutorials/docker"),
    ("☁️ Cloud (GCP/AWS/Azure)", "Production enterprise" if FR else "Enterprise production",           "https://cloud.google.com"),
]:
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1: st.markdown(f"**{nom}**"); st.write(desc)
        with c2: st.link_button("Voir →" if FR else "See →", url)

st.divider()
st.success("🎉 " + ("Tu sais déployer une app Streamlit !" if FR else "You know how to deploy a Streamlit app!"))
st.info("🤖 " + ("Dernière étape : la **Démo ML** !" if FR else "Last step: the **ML Demo**!"))
