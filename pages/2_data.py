import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Données & Graphiques", page_icon="📊", layout="wide")

st.title("📊 Données & Graphiques")
st.caption("Afficher, filtrer et visualiser des données — le cœur du métier de data scientist.")

st.markdown("""
Streamlit s'intègre nativement avec **Pandas** et **Plotly**.
En quelques lignes, tu passes d'un DataFrame brut à un dashboard interactif.
""")

st.divider()

# ── Dataset de démo ──────────────────────────────────────
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=120, freq="D")
    df = pd.DataFrame({
        "date": dates,
        "ventes": np.cumsum(np.random.randn(120) * 10 + 5).clip(min=0),
        "région": np.random.choice(["Nord", "Sud", "Est", "Ouest"], 120),
        "produit": np.random.choice(["Produit A", "Produit B", "Produit C"], 120),
        "satisfaction": np.random.uniform(3, 5, 120).round(1),
    })
    return df

df = load_data()

# ── st.dataframe ─────────────────────────────────────────
st.markdown("### 🗂️ st.dataframe — Afficher un tableau")
with st.expander("Voir le code", expanded=False):
    st.code("""
@st.cache_data          # ← met en cache le résultat, évite de recharger à chaque run
def load_data():
    df = pd.read_csv("mon_fichier.csv")
    return df

df = load_data()
st.dataframe(df, use_container_width=True)
""")
st.dataframe(df.head(10), use_container_width=True)
st.caption("`@st.cache_data` est essentiel : il évite de recharger les données à chaque interaction utilisateur.")

st.divider()

# ── Filtres interactifs ───────────────────────────────────
st.markdown("### 🔍 Filtres interactifs")
st.markdown("Combine des widgets avec ton DataFrame pour filtrer en temps réel.")

with st.expander("Voir le code", expanded=False):
    st.code("""
région = st.multiselect("Région", df["région"].unique(), default=df["région"].unique())
produit = st.selectbox("Produit", ["Tous"] + list(df["produit"].unique()))

df_filtré = df[df["région"].isin(région)]
if produit != "Tous":
    df_filtré = df_filtré[df_filtré["produit"] == produit]

st.dataframe(df_filtré)
""")

col_f1, col_f2 = st.columns(2)
with col_f1:
    régions = st.multiselect("Région", df["région"].unique(), default=df["région"].unique())
with col_f2:
    produit = st.selectbox("Produit", ["Tous"] + sorted(df["produit"].unique()))

df_filtré = df[df["région"].isin(régions)]
if produit != "Tous":
    df_filtré = df_filtré[df_filtré["produit"] == produit]

st.dataframe(df_filtré, use_container_width=True)
st.caption(f"{len(df_filtré)} lignes affichées sur {len(df)} au total.")

st.divider()

# ── Graphiques Plotly ────────────────────────────────────
st.markdown("### 📈 st.plotly_chart — Graphiques interactifs")

tab1, tab2, tab3 = st.tabs(["Courbe temporelle", "Barres par région", "Scatter"])

with tab1:
    with st.expander("Voir le code"):
        st.code("""
fig = px.line(df, x="date", y="ventes", color="produit", title="Évolution des ventes")
st.plotly_chart(fig, use_container_width=True)
""")
    fig1 = px.line(df_filtré, x="date", y="ventes", color="produit",
                   title="Évolution des ventes dans le temps")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    with st.expander("Voir le code"):
        st.code("""
fig = px.bar(df.groupby("région")["ventes"].sum().reset_index(),
             x="région", y="ventes", color="région", title="Ventes par région")
st.plotly_chart(fig, use_container_width=True)
""")
    ventes_region = df_filtré.groupby("région")["ventes"].sum().reset_index()
    fig2 = px.bar(ventes_region, x="région", y="ventes", color="région",
                  title="Total ventes par région")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    with st.expander("Voir le code"):
        st.code("""
fig = px.scatter(df, x="ventes", y="satisfaction", color="produit",
                 size="satisfaction", hover_data=["région", "date"])
st.plotly_chart(fig, use_container_width=True)
""")
    fig3 = px.scatter(df_filtré, x="ventes", y="satisfaction", color="produit",
                      size="satisfaction", hover_data=["région", "date"],
                      title="Ventes vs Satisfaction client")
    st.plotly_chart(fig3, use_container_width=True)

st.divider()
st.info("👈 Module suivant : **Layouts & mise en page** pour structurer tout ça proprement.")
