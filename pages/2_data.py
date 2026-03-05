import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Data & Charts", page_icon="📊", layout="wide")

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
    st.title("📊 Données & Graphiques")
    st.caption("Afficher, filtrer et visualiser des données — le cœur du métier de data scientist.")
    st.markdown("Streamlit s'intègre nativement avec **Pandas** et **Plotly**. En quelques lignes, tu passes d'un DataFrame brut à un dashboard interactif.")
else:
    st.title("📊 Data & Charts")
    st.caption("Display, filter and visualise data — the core of a data scientist's job.")
    st.markdown("Streamlit integrates natively with **Pandas** and **Plotly**. In just a few lines, you go from a raw DataFrame to an interactive dashboard.")

st.divider()

@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=120, freq="D")
    df = pd.DataFrame({
        "date":         dates,
        "sales":        np.cumsum(np.random.randn(120) * 10 + 5).clip(min=0),
        "region":       np.random.choice(["North", "South", "East", "West"], 120),
        "product":      np.random.choice(["Product A", "Product B", "Product C"], 120),
        "satisfaction": np.random.uniform(3, 5, 120).round(1),
    })
    return df

df = load_data()

# ── st.dataframe ─────────────────────────────────────────────────────
st.markdown("### 🗂️ st.dataframe")
with st.expander("📄 Code" if not FR else "📄 Voir le code", expanded=False):
    st.code("""
@st.cache_data          # ← caches the result, avoids reloading on every interaction
def load_data():
    df = pd.read_csv("my_file.csv")
    return df

df = load_data()
st.dataframe(df, use_container_width=True)
""")
st.dataframe(df.head(10), use_container_width=True)
if FR:
    st.caption("`@st.cache_data` est essentiel : il évite de recharger les données à chaque interaction.")
else:
    st.caption("`@st.cache_data` is key: it prevents reloading data on every user interaction.")

st.divider()

# ── Filtres ──────────────────────────────────────────────────────────
st.markdown("### 🔍 " + ("Filtres interactifs" if FR else "Interactive filters"))
if FR:
    st.markdown("Combine des widgets avec ton DataFrame pour filtrer en temps réel.")
else:
    st.markdown("Combine widgets with your DataFrame to filter data in real time.")

with st.expander("📄 Voir le code" if FR else "📄 Code", expanded=False):
    st.code("""
region  = st.multiselect("Region", df["region"].unique(), default=df["region"].unique())
product = st.selectbox("Product", ["All"] + list(df["product"].unique()))

df_f = df[df["region"].isin(region)]
if product != "All":
    df_f = df_f[df_f["product"] == product]

st.dataframe(df_f)
""")

col_f1, col_f2 = st.columns(2)
with col_f1:
    lbl_r   = "Région" if FR else "Region"
    regions = st.multiselect(lbl_r, df["region"].unique(), default=df["region"].unique())
with col_f2:
    lbl_p   = "Produit" if FR else "Product"
    all_lbl = "Tous" if FR else "All"
    product = st.selectbox(lbl_p, [all_lbl] + sorted(df["product"].unique()))

df_f = df[df["region"].isin(regions)]
if product not in ("Tous", "All"):
    df_f = df_f[df_f["product"] == product]

st.dataframe(df_f, use_container_width=True)
rows_txt = f"{len(df_f)} lignes affichées sur {len(df)}" if FR else f"{len(df_f)} rows shown out of {len(df)}"
st.caption(rows_txt)

st.divider()

# ── Graphiques ───────────────────────────────────────────────────────
st.markdown("### 📈 st.plotly_chart")

t1_lbl = "Courbe temporelle" if FR else "Time series"
t2_lbl = "Barres par région" if FR else "Bars by region"
t3_lbl = "Scatter"           if FR else "Scatter"

tab1, tab2, tab3 = st.tabs([t1_lbl, t2_lbl, t3_lbl])

with tab1:
    with st.expander("📄 Voir le code" if FR else "📄 Code"):
        st.code('fig = px.line(df, x="date", y="sales", color="product")\nst.plotly_chart(fig, use_container_width=True)')
    title = "Évolution des ventes" if FR else "Sales over time"
    fig1 = px.line(df_f, x="date", y="sales", color="product", title=title)
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    with st.expander("📄 Voir le code" if FR else "📄 Code"):
        st.code('fig = px.bar(df.groupby("region")["sales"].sum().reset_index(), x="region", y="sales", color="region")\nst.plotly_chart(fig, use_container_width=True)')
    sales_r = df_f.groupby("region")["sales"].sum().reset_index()
    title   = "Ventes par région" if FR else "Sales by region"
    fig2    = px.bar(sales_r, x="region", y="sales", color="region", title=title)
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    with st.expander("📄 Voir le code" if FR else "📄 Code"):
        st.code('fig = px.scatter(df, x="sales", y="satisfaction", color="product", size="satisfaction")\nst.plotly_chart(fig, use_container_width=True)')
    title = "Ventes vs Satisfaction" if FR else "Sales vs Satisfaction"
    fig3  = px.scatter(df_f, x="sales", y="satisfaction", color="product",
                       size="satisfaction", hover_data=["region", "date"], title=title)
    st.plotly_chart(fig3, use_container_width=True)

st.divider()
if FR:
    st.info("👈 Module suivant : **Layouts & Mise en page**")
else:
    st.info("👈 Next module: **Layouts**")
