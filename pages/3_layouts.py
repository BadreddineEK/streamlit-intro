import streamlit as st

st.set_page_config(page_title="Layouts", page_icon="🧱", layout="wide")

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
    st.title("🧱 Layouts & Mise en page")
    st.caption("Structurer une app lisible, c'est 50 % du travail.")
    st.markdown("Streamlit propose plusieurs outils pour organiser le contenu : `st.columns`, `st.tabs`, `st.expander`, `st.container`.")
else:
    st.title("🧱 Layouts")
    st.caption("A readable structure is half the work.")
    st.markdown("Streamlit offers several tools to organise content: `st.columns`, `st.tabs`, `st.expander`, `st.container`.")

st.divider()

# ── Columns ──────────────────────────────────────────────────────────
st.markdown("### ↔️ st.columns")
if FR:
    st.markdown("Le moyen le plus simple de mettre du contenu côte à côte.")
else:
    st.markdown("The simplest way to place content side by side.")

with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("""
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Accuracy", "94.2 %", "+1.3 %")
with col2:
    st.metric("Recall", "91.8 %", "-0.5 %")
with col3:
    st.metric("F1-Score", "93.0 %", "+0.4 %")
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Accuracy",  "94.2 %", "+1.3 %")
with col2:
    st.metric("Recall",    "91.8 %", "-0.5 %")
with col3:
    st.metric("F1-Score",  "93.0 %", "+0.4 %")

if FR:
    st.markdown("Tu peux aussi passer des ratios : `st.columns([2, 1])` pour une colonne 2× plus large.")
else:
    st.markdown("You can also pass ratios: `st.columns([2, 1])` for a column twice as wide.")

st.divider()

# ── Tabs ─────────────────────────────────────────────────────────────
st.markdown("### 📑 st.tabs")
if FR:
    st.markdown("Idéal pour organiser plusieurs vues d'un même sujet.")
else:
    st.markdown("Ideal for organising multiple views of the same topic.")

with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("""
tab1, tab2 = st.tabs(["Results", "Errors"])
with tab1:
    st.success("Pipeline completed.")
with tab2:
    st.warning("3 null values detected.")
""")

t1 = "✅ Résultat" if FR else "✅ Result"
t2 = "⚠️ Erreurs"  if FR else "⚠️ Errors"
t3 = "📝 Logs"
tab1, tab2, tab3 = st.tabs([t1, t2, t3])
with tab1:
    st.success("Pipeline exécuté avec succès — 1 247 lignes traitées." if FR else "Pipeline completed — 1,247 rows processed.")
with tab2:
    st.warning("3 valeurs nulles détectées dans `prix`. Imputées par la médiane." if FR else "3 null values detected in `price`. Imputed with median.")
with tab3:
    st.code("[INFO] 09:00:01 — DB connection OK\n[INFO] 09:00:02 — Source file read: 1250 rows\n[WARN] 09:00:03 — 3 nulls detected, median imputation\n[INFO] 09:00:04 — Export complete")

st.divider()

# ── Expander ─────────────────────────────────────────────────────────
st.markdown("### 🗂️ st.expander")
if FR:
    st.markdown("Pour cacher du contenu secondaire et garder l'interface aérée.")
else:
    st.markdown("To hide secondary content and keep the UI clean.")

with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("""
with st.expander("Technical details", expanded=False):
    st.write("Hidden by default, visible on click.")
""")

lbl_exp = "🔍 Détails du modèle ML" if FR else "🔍 ML Model details"
with st.expander(lbl_exp, expanded=False):
    st.markdown("""
- **Algorithm**: Random Forest (500 trees)
- **Features**: 23 input variables
- **Train/Test split**: 80/20
- **Validation**: 5-fold cross-validation
- **Library**: scikit-learn 1.4
    """)

st.divider()

# ── Container ────────────────────────────────────────────────────────
st.markdown("### 📦 st.container(border=True)")
if FR:
    st.markdown("Regroupe visuellement des éléments liés.")
else:
    st.markdown("Visually groups related elements together.")

with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("""
with st.container(border=True):
    st.markdown("### 🎯 Goal")
    st.write("Predict weekly demand per SKU.")
""")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### 🎯 " + ("Objectif" if FR else "Goal"))
        st.write("Prédire la demande hebdomadaire par SKU." if FR else "Predict weekly demand per SKU.")
with col2:
    with st.container(border=True):
        st.markdown("### 📦 " + ("Données" if FR else "Data"))
        st.write("36 mois d'historique, 150 SKUs." if FR else "36 months of history, 150 SKUs.")

st.divider()

# ── Messages ─────────────────────────────────────────────────────────
st.markdown("### 💬 " + ("Messages" if not FR else "Messages : success / warning / error / info"))

with st.expander("📄 Voir le code" if FR else "📄 Code"):
    st.code("""
st.success("Operation complete!")
st.warning("Missing data detected.")
st.error("Critical error — pipeline stopped.")
st.info("Tip: use @st.cache_data for large datasets.")
""")

st.success("Opération réussie !" if FR else "Operation complete!")
st.warning("Données manquantes détectées." if FR else "Missing data detected.")
st.error("Erreur critique — pipeline interrompu." if FR else "Critical error — pipeline stopped.")
st.info("`@st.cache_data` pour les données lourdes." if FR else "Tip: use `@st.cache_data` for large datasets.")

st.divider()
if FR:
    st.info("👈 Dernier module : **Déployer son app**")
else:
    st.info("👈 Last module: **Deployment**")
