import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Data & Charts", page_icon="📊", layout="wide")
st.markdown('<style>[data-testid="stSidebarNav"]{display:none}</style>', unsafe_allow_html=True)

with st.sidebar:
    lang = st.radio("🌐", ["🇫🇷 FR", "🇬🇧 EN"], horizontal=True, key="lang_d", label_visibility="collapsed")
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
    st.title("📊 Données & Graphiques")
    st.caption("DataFrames, filtres, Plotly — le quotidien du data scientist.")
else:
    st.title("📊 Data & Charts")
    st.caption("DataFrames, filters, Plotly — the data scientist’s daily toolkit.")

st.divider()

@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=120, freq="D")
    return pd.DataFrame({
        "date":         dates,
        "sales":        np.cumsum(np.random.randn(120) * 10 + 5).clip(min=0).round(2),
        "region":       np.random.choice(["North", "South", "East", "West"], 120),
        "product":      np.random.choice(["Product A", "Product B", "Product C"], 120),
        "satisfaction": np.random.uniform(3, 5, 120).round(1),
    })

df = load_data()

# --- st.dataframe
st.markdown("### 🗂️ `st.dataframe`")
with st.expander("📄 " + ("Voir le code" if FR else "Code")):
    st.code("""
@st.cache_data        # ← met en cache, évite de recharger à chaque interaction
def load_data():
    return pd.read_csv("file.csv")

df = load_data()
st.dataframe(df, use_container_width=True)
""")
st.dataframe(df.head(10), use_container_width=True)
st.caption("`@st.cache_data` : résultat mis en cache, pas de rechargement à chaque clic." if FR else "`@st.cache_data`: result is cached, no reload on every interaction.")

st.divider()

# --- Filtres
st.markdown("### 🔍 " + ("Filtres interactifs" if FR else "Interactive filters"))
with st.expander("📄 " + ("Voir le code" if FR else "Code")):
    st.code("""
regions = st.multiselect("Region", df["region"].unique(), default=df["region"].unique())
product = st.selectbox("Product", ["All"] + sorted(df["product"].unique()))

df_f = df[df["region"].isin(regions)]
if product != "All":
    df_f = df_f[df_f["product"] == product]
st.dataframe(df_f)
""")

col1, col2 = st.columns(2)
with col1:
    all_regions = sorted(df["region"].unique().tolist())
    regions = st.multiselect("Région" if FR else "Region", all_regions, default=all_regions)
with col2:
    all_label = "Tous" if FR else "All"
    product = st.selectbox("Produit" if FR else "Product", [all_label] + sorted(df["product"].unique().tolist()))

df_f = df[df["region"].isin(regions)] if regions else df.iloc[0:0]
if product not in ("Tous", "All"):
    df_f = df_f[df_f["product"] == product]

if df_f.empty:
    st.warning("⚠️ " + ("Aucune donnée pour cette sélection." if FR else "No data for this selection."))
else:
    st.dataframe(df_f, use_container_width=True)
    st.caption(f"{len(df_f)} / {len(df)} " + ("lignes" if FR else "rows"))

st.divider()

# --- Graphiques
st.markdown("### 📈 `st.plotly_chart`")
if df_f.empty:
    st.info("ℹ️ " + ("Sélectionne au moins une région pour afficher les graphiques." if FR else "Select at least one region to display charts."))
else:
    tab1, tab2, tab3 = st.tabs([
        "📈 " + ("Courbe" if FR else "Line"),
        "📊 " + ("Barres" if FR else "Bars"),
        "🔮 Scatter"
    ])
    with tab1:
        with st.expander("📄 Code"):
            st.code('fig = px.line(df, x="date", y="sales", color="product")\nst.plotly_chart(fig, use_container_width=True)')
        st.plotly_chart(
            px.line(df_f, x="date", y="sales", color="product",
                    title="Évolution des ventes" if FR else "Sales over time"),
            use_container_width=True
        )
    with tab2:
        with st.expander("📄 Code"):
            st.code('fig = px.bar(df.groupby("region")["sales"].sum().reset_index(), x="region", y="sales", color="region")\nst.plotly_chart(fig, use_container_width=True)')
        sales_r = df_f.groupby("region")["sales"].sum().reset_index()
        st.plotly_chart(
            px.bar(sales_r, x="region", y="sales", color="region",
                   title="Ventes par région" if FR else "Sales by region"),
            use_container_width=True
        )
    with tab3:
        with st.expander("📄 Code"):
            st.code('fig = px.scatter(df, x="sales", y="satisfaction", color="product", size="satisfaction")\nst.plotly_chart(fig, use_container_width=True)')
        st.plotly_chart(
            px.scatter(df_f, x="sales", y="satisfaction", color="product",
                       size="satisfaction", hover_data=["region", "date"],
                       title="Ventes vs Satisfaction"),
            use_container_width=True
        )

st.divider()
st.info("👈 " + ("Module suivant : **Layouts**" if FR else "Next: **Layouts**"))
