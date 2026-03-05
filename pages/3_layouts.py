import streamlit as st

st.set_page_config(page_title="Layouts", page_icon="🧱", layout="wide")
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
    st.title("🧱 Layouts & Mise en page")
    st.caption("Structurer une app lisible, c'est 50 % du travail.")
else:
    st.title("🧱 Layouts")
    st.caption("A clean structure is half the work.")

st.divider()

st.markdown("### ↔️ st.columns")
with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("col1, col2, col3 = st.columns(3)\nwith col1: st.metric(\"Accuracy\", \"94.2%\", \"+1.3%\")\n# ratios: st.columns([2, 1])")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Accuracy", "94.2%", "+1.3%")
with col2: st.metric("Recall",   "91.8%", "-0.5%")
with col3: st.metric("F1-Score", "93.0%", "+0.4%")

st.divider()
st.markdown("### 📑 st.tabs")
with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code('tab1, tab2 = st.tabs(["Results", "Errors"])\nwith tab1: st.success("Done.")\nwith tab2: st.warning("3 nulls.")')
t1, t2, t3 = st.tabs(["✅ " + ("Résultat" if FR else "Result"), "⚠️ " + ("Erreurs" if FR else "Errors"), "📝 Logs"])
with t1: st.success("Pipeline OK — 1 247 lignes." if FR else "Pipeline OK — 1,247 rows.")
with t2: st.warning("3 valeurs nulles détectées." if FR else "3 null values detected.")
with t3: st.code("[INFO] 09:00:01 — DB OK\n[INFO] 09:00:02 — 1250 rows read\n[WARN] 09:00:03 — 3 nulls, median imputation\n[INFO] 09:00:04 — Export complete")

st.divider()
st.markdown("### 🗂️ st.expander")
with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code('with st.expander("ML details"):\n    st.write("Hidden by default.")')
with st.expander("🔍 " + ("Détails du modèle" if FR else "Model details")):
    st.markdown("- **Algo**: Random Forest (500 trees)\n- **Features**: 23\n- **Split**: 80/20\n- **CV**: 5-fold")

st.divider()
st.markdown("### 📦 st.container(border=True)")
with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code('with st.container(border=True):\n    st.markdown("### Goal")\n    st.write("Predict weekly demand.")')
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### 🎯 " + ("Objectif" if FR else "Goal"))
        st.write("Prédire la demande hebdomadaire par SKU." if FR else "Predict weekly demand per SKU.")
with col2:
    with st.container(border=True):
        st.markdown("### 📦 " + ("Données" if FR else "Data"))
        st.write("36 mois d'historique, 150 SKUs." if FR else "36 months history, 150 SKUs.")

st.divider()
st.markdown("### 💬 Messages")
with st.expander("📄 Code"):
    st.code('st.success("Done!")\nst.warning("Watch out.")\nst.error("Failed.")\nst.info("Tip here.")')
st.success("Opération réussie !" if FR else "Operation complete!")
st.warning("Données manquantes." if FR else "Missing data detected.")
st.error("Erreur critique." if FR else "Critical error.")
st.info("`@st.cache_data` pour les données lourdes." if FR else "Use `@st.cache_data` for large datasets.")

st.divider()
st.info("👈 " + ("Module suivant : **Déploiement**" if FR else "Next: **Deployment**"))
