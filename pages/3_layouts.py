import streamlit as st

st.set_page_config(page_title="Layouts", page_icon="🧱", layout="wide")

st.title("🧱 Layouts & Mise en page")
st.caption("Structurer une app lisible, c'est 50 % du travail.")

st.markdown("""
Streamlit propose plusieurs outils pour organiser le contenu :
`st.columns`, `st.tabs`, `st.expander`, `st.sidebar`.
Combine-les pour créer des interfaces claires et intuitives.
""")

st.divider()

# ── Columns ──────────────────────────────────────────────
st.markdown("### ↔️ st.columns")
st.markdown("Le moyen le plus simple de mettre du contenu côte à côte.")

with st.expander("Voir le code"):
    st.code("""
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Précision", "94.2 %", "+1.3 %")
with col2:
    st.metric("Recall", "91.8 %", "-0.5 %")
with col3:
    st.metric("F1-Score", "93.0 %", "+0.4 %")
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Précision", "94.2 %", "+1.3 %")
with col2:
    st.metric("Recall", "91.8 %", "-0.5 %")
with col3:
    st.metric("F1-Score", "93.0 %", "+0.4 %")

st.markdown("Tu peux aussi passer des ratios de largeur : `st.columns([2, 1])` pour une colonne 2x plus large.")
with st.expander("Voir le code"):
    st.code("col_large, col_small = st.columns([2, 1])")

st.divider()

# ── Tabs ─────────────────────────────────────────────────
st.markdown("### 📑 st.tabs")
st.markdown("Idéal pour organiser plusieurs vues d'un même sujet.")

with st.expander("Voir le code"):
    st.code("""
tab1, tab2 = st.tabs(["Vue données", "Vue graphique"])
with tab1:
    st.dataframe(df)
with tab2:
    st.plotly_chart(fig)
""")

tab1, tab2, tab3 = st.tabs(["📋 Résultat", "⚠️ Erreurs", "📝 Logs"])
with tab1:
    st.success("Pipeline exécuté avec succès — 1 247 lignes traitées.")
with tab2:
    st.warning("3 valeurs nulles détectées dans la colonne `prix`. Imputées par la médiane.")
with tab3:
    st.code("[INFO] 09:00:01 — Connexion BDD OK\n[INFO] 09:00:02 — Lecture fichier source : 1250 lignes\n[WARN] 09:00:03 — 3 nulls détectés, imputation médiane\n[INFO] 09:00:04 — Export terminé")

st.divider()

# ── Expander ─────────────────────────────────────────────
st.markdown("### 🗂️ st.expander")
st.markdown("Pour cacher du contenu secondaire et garder l'interface aérée.")

with st.expander("Voir le code"):
    st.code("""
with st.expander("Détails techniques", expanded=False):
    st.write("Contenu masqué par défaut, visible au clic.")
""")

with st.expander("📐 Détails du modèle ML", expanded=False):
    st.markdown("""
- **Algorithme** : Random Forest (500 arbres)
- **Features** : 23 variables d'entrée
- **Train/Test split** : 80/20
- **Validation** : Cross-validation 5 folds
- **Librairie** : scikit-learn 1.4
    """)

st.divider()

# ── Container avec bordure ───────────────────────────────
st.markdown("### 📦 st.container(border=True)")
st.markdown("Regroupe visuellement des éléments liés.")

with st.expander("Voir le code"):
    st.code("""
with st.container(border=True):
    st.markdown("### 🎯 Objectif")
    st.write("Prédire la demande hebdomadaire par SKU.")
""")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("### 🎯 Objectif")
        st.write("Prédire la demande hebdomadaire par SKU.")
with col2:
    with st.container(border=True):
        st.markdown("### 📦 Données")
        st.write("36 mois d'historique de ventes, 150 SKUs.")

st.divider()

# ── Messages ─────────────────────────────────────────────
st.markdown("### 💬 Messages : success / warning / error / info")

with st.expander("Voir le code"):
    st.code("""
st.success("Opération réussie !")
st.warning("Attention, données manquantes.")
st.error("Erreur critique — pipeline interrompu.")
st.info("Conseil : utilisez @st.cache_data pour les données lourdes.")
""")

st.success("Opération réussie !")
st.warning("Attention, données manquantes.")
st.error("Erreur critique — pipeline interrompu.")
st.info("Conseil : utilisez `@st.cache_data` pour les données lourdes.")

st.divider()
st.info("👈 Dernier module : **Déployer son app** — passer de localhost à une URL publique.")
