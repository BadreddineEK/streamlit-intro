import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import load_iris, load_wine
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="ML Demo", page_icon="🤖", layout="wide")
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
    st.title("🤖 Démo ML Interactive")
    st.caption("Entraîne un vrai modèle, ajuste les hyperparamètres, visualise les résultats — en temps réel.")
    st.markdown("""
    Ce module montre la puissance de Streamlit pour les projets ML :
    tu contrôles le dataset, l'algorithme et les hyperparamètres — le modèle se reentraîne à chaque changement.
    """)
else:
    st.title("🤖 Interactive ML Demo")
    st.caption("Train a real model, tune hyperparameters, visualise results — live.")
    st.markdown("""
    This module shows the power of Streamlit for ML projects:
    you control the dataset, algorithm and hyperparameters — the model retrains on every change.
    """)

st.divider()

# ── Configuration ────────────────────────────────────────────────────────
col_cfg1, col_cfg2, col_cfg3 = st.columns(3)

with col_cfg1:
    dataset_choice = st.selectbox(
        "📊 " + ("Dataset" if not FR else "Dataset"),
        ["Iris", "Wine"],
        help="Iris: 3 types de fleurs | Wine: 3 types de vin" if FR else "Iris: 3 flower types | Wine: 3 wine types"
    )

with col_cfg2:
    model_choice = st.selectbox(
        "🧠 " + ("Algorithme" if FR else "Algorithm"),
        ["Random Forest", "Gradient Boosting", "Logistic Regression", "SVM"]
    )

with col_cfg3:
    test_size = st.slider(
        "✂️ Test split", 0.1, 0.5, 0.2, 0.05,
        help="Proportion des données réservées au test" if FR else "Proportion of data reserved for testing"
    )

# Hyperparamètres selon le modèle
st.markdown("#### ⚙️ " + ("Hyperparamètres" if FR else "Hyperparameters"))
hp_col1, hp_col2, hp_col3 = st.columns(3)

if model_choice == "Random Forest":
    with hp_col1:
        n_estimators = st.slider("n_estimators", 10, 300, 100, 10)
    with hp_col2:
        max_depth = st.slider("max_depth", 1, 20, 5)
    with hp_col3:
        min_samples_split = st.slider("min_samples_split", 2, 20, 2)
    model_params = {"n_estimators": n_estimators, "max_depth": max_depth, "min_samples_split": min_samples_split, "random_state": 42}
elif model_choice == "Gradient Boosting":
    with hp_col1:
        n_estimators = st.slider("n_estimators", 10, 300, 100, 10)
    with hp_col2:
        learning_rate = st.slider("learning_rate", 0.01, 0.5, 0.1, 0.01)
    with hp_col3:
        max_depth = st.slider("max_depth", 1, 10, 3)
    model_params = {"n_estimators": n_estimators, "learning_rate": learning_rate, "max_depth": max_depth, "random_state": 42}
elif model_choice == "Logistic Regression":
    with hp_col1:
        C = st.slider("C (régularisation)" if FR else "C (regularisation)", 0.01, 10.0, 1.0, 0.01)
    with hp_col2:
        max_iter = st.slider("max_iter", 100, 1000, 200, 50)
    with hp_col3:
        st.empty()
    model_params = {"C": C, "max_iter": max_iter, "random_state": 42}
else:  # SVM
    with hp_col1:
        C = st.slider("C", 0.01, 10.0, 1.0, 0.01)
    with hp_col2:
        kernel = st.selectbox("kernel", ["rbf", "linear", "poly"])
    with hp_col3:
        st.empty()
    model_params = {"C": C, "kernel": kernel, "probability": True}

st.divider()

# ── Entraînement ────────────────────────────────────────────────────────────
@st.cache_data
def get_dataset(name):
    if name == "Iris":
        data = load_iris()
    else:
        data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")
    labels = list(data.target_names)
    return X, y, labels

X, y, labels = get_dataset(dataset_choice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

models_map = {
    "Random Forest":       RandomForestClassifier,
    "Gradient Boosting":   GradientBoostingClassifier,
    "Logistic Regression": LogisticRegression,
    "SVM":                 SVC,
}

with st.spinner("⏳ Entraînement en cours…" if FR else "⏳ Training…"):
    clf = models_map[model_choice](**model_params)
    clf.fit(X_train_s, y_train)
    y_pred = clf.predict(X_test_s)
    acc   = accuracy_score(y_test, y_pred)
    cm    = confusion_matrix(y_test, y_pred)

# ── Métriques ───────────────────────────────────────────────────────────────
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    delta_color = "normal" if acc >= 0.85 else "inverse"
    st.metric("✅ Accuracy", f"{acc:.1%}", delta=f"{acc-0.5:.1%} vs random", delta_color=delta_color)
with col_m2:
    st.metric("📚 " + ("Train" if not FR else "Train"), f"{len(X_train)} " + ("exemples" if FR else "samples"))
with col_m3:
    st.metric("🧪 Test", f"{len(X_test)} " + ("exemples" if FR else "samples"))
with col_m4:
    st.metric("🏷️ Classes", len(labels))

# ── Visualisations ─────────────────────────────────────────────────────────
st.divider()

tab_cm, tab_pca, tab_feat, tab_code = st.tabs([
    "📊 Confusion Matrix",
    "🔭 PCA",
    "🏆 " + ("Importance des features" if FR else "Feature importance"),
    "📄 Code"
])

with tab_cm:
    if FR:
        st.markdown("La **matrice de confusion** montre où le modèle se trompe. La diagonale = les bons classements.")
    else:
        st.markdown("The **confusion matrix** shows where the model makes mistakes. Diagonal = correct predictions.")
    fig_cm = px.imshow(
        cm, text_auto=True,
        x=labels, y=labels,
        color_continuous_scale="Blues",
        title="Confusion Matrix",
        labels=dict(x="Predicted" if not FR else "Prédit", y="Actual" if not FR else "Réel")
    )
    fig_cm.update_layout(height=400)
    st.plotly_chart(fig_cm, use_container_width=True)

with tab_pca:
    if FR:
        st.markdown("Visualisation des données réduites en **2 dimensions** avec la PCA. Les couleurs = les vraies classes.")
    else:
        st.markdown("Data projected onto **2 dimensions** with PCA. Colors = true classes.")
    pca = PCA(n_components=2)
    X_all_s = scaler.transform(X)
    X_pca   = pca.fit_transform(X_all_s)
    df_pca  = pd.DataFrame(X_pca, columns=["PC1","PC2"])
    df_pca["class"] = [labels[i] for i in y]
    fig_pca = px.scatter(
        df_pca, x="PC1", y="PC2", color="class",
        title=f"PCA — {pca.explained_variance_ratio_.sum():.1%} " + ("de variance expliquée" if FR else "variance explained"),
        template="plotly_dark"
    )
    st.plotly_chart(fig_pca, use_container_width=True)

with tab_feat:
    if model_choice in ("Random Forest", "Gradient Boosting"):
        importances = clf.feature_importances_
        feat_df = pd.DataFrame({"feature": X.columns, "importance": importances}).sort_values("importance", ascending=True)
        fig_feat = px.bar(
            feat_df, x="importance", y="feature", orientation="h",
            title="Feature Importances", color="importance",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_feat, use_container_width=True)
    elif model_choice == "Logistic Regression":
        coefs = np.abs(clf.coef_).mean(axis=0)
        feat_df = pd.DataFrame({"feature": X.columns, "importance": coefs}).sort_values("importance", ascending=True)
        fig_feat = px.bar(feat_df, x="importance", y="feature", orientation="h",
                          title="Logistic Regression — Mean |Coefficient|", color="importance",
                          color_continuous_scale="Viridis")
        st.plotly_chart(fig_feat, use_container_width=True)
    else:
        st.info("ℹ️ Feature importance non disponible pour SVM." if FR else "ℹ️ Feature importance not available for SVM.")

with tab_code:
    if FR:
        st.markdown("**Voici exactement le code qui fait tourner cette démo :**")
    else:
        st.markdown("**Here's the exact code running this demo:**")
    st.code("""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load data
data = load_iris()
X, y = data.data, data.target

# Split + scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# Train
clf = RandomForestClassifier(n_estimators=100, max_depth=5)
clf.fit(X_train, y_train)

# Evaluate
acc = accuracy_score(y_test, clf.predict(X_test))
print(f"Accuracy: {acc:.1%}")
""")

st.divider()

# ── Prédiction manuelle ─────────────────────────────────────────────────────
st.markdown("## 🎯 " + ("Prédire sur de nouvelles données" if FR else "Predict on new data"))
if FR:
    st.markdown("Ajuste les valeurs des features et obtiens une prédiction **en temps réel**.")
else:
    st.markdown("Adjust the feature values and get a **live** prediction.")

X_min, X_max = X.min(), X.max()
input_cols = st.columns(len(X.columns))
input_vals = []
for i, (col, feat) in enumerate(zip(input_cols, X.columns)):
    with col:
        v = st.number_input(
            feat[:20],
            min_value=float(X[feat].min()),
            max_value=float(X[feat].max()),
            value=float(X[feat].mean()),
            format="%.2f"
        )
        input_vals.append(v)

new_sample = np.array(input_vals).reshape(1, -1)
new_scaled  = scaler.transform(new_sample)
pred_class  = clf.predict(new_scaled)[0]
pred_proba  = clf.predict_proba(new_scaled)[0]

col_pred1, col_pred2 = st.columns([1, 2])
with col_pred1:
    st.success(f"🎯 " + ("Prédiction" if FR else "Prediction") + f" : **{labels[pred_class]}**")
with col_pred2:
    df_proba = pd.DataFrame({"class": labels, "probability": pred_proba})
    fig_proba = px.bar(
        df_proba, x="class", y="probability",
        color="probability", color_continuous_scale="Blues",
        title="" + ("Probabilités par classe" if FR else "Probabilities per class"),
        range_y=[0,1]
    )
    fig_proba.update_layout(height=250, margin=dict(t=30,b=0))
    st.plotly_chart(fig_proba, use_container_width=True)

st.divider()
st.success("🎉 " + ("Tu as exploré tout le guide ! N'oublie pas de voir les autres projets →" if FR else "You've completed the full guide! Check out the other projects →"))
col_a, col_b = st.columns(2)
with col_a:
    st.link_button("🐙 GitHub — BadreddineEK", "https://github.com/BadreddineEK", use_container_width=True)
with col_b:
    st.link_button("🌐 Portfolio", "https://badreddineek.github.io/portfolioBadreddine", use_container_width=True)
