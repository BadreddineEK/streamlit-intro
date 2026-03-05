import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="ML Demo", page_icon="🤖", layout="wide")
st.markdown('<style>[data-testid="stSidebarNav"]{display:none}</style>', unsafe_allow_html=True)

with st.sidebar:
    lang = st.radio("🌐", ["🇫🇷 FR", "🇬🇧 EN"], horizontal=True, key="lang_ml", label_visibility="collapsed")
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
    st.title("🤖 Démo ML Interactive")
    st.caption("Entraîne un vrai modèle, ajuste les hyperparamètres, visualise les résultats — en temps réel.")
    st.markdown("Contrôle le dataset, l’algorithme et les hyperparamètres. Le modèle se reentraîne à chaque modification.")
else:
    st.title("🤖 Interactive ML Demo")
    st.caption("Train a real model, tune hyperparameters, visualise results — live.")
    st.markdown("Control the dataset, algorithm and hyperparameters. The model retrains on every change.")

st.divider()

# ── Dataset loader (caché) ────────────────────────────────────────────────────────────
@st.cache_data
def get_dataset(name: str):
    if name == "Iris":
        d = load_iris()
    else:
        d = load_breast_cancer()
    X = pd.DataFrame(d.data, columns=d.feature_names)
    y = pd.Series(d.target, name="target")
    labels = list(d.target_names)
    return X, y, labels

# ── Config ────────────────────────────────────────────────────────────────────
col_cfg1, col_cfg2, col_cfg3 = st.columns(3)
with col_cfg1:
    dataset_choice = st.selectbox(
        "📊 Dataset",
        ["Iris", "Breast Cancer"],
        help=("Iris: 3 types de fleurs (150 éch.) | Breast Cancer: classification tumorale (569 éch.)" if FR
              else "Iris: 3 flower types (150 samples) | Breast Cancer: tumour classification (569 samples)")
    )
with col_cfg2:
    model_choice = st.selectbox(
        "🧠 " + ("Algorithme" if FR else "Algorithm"),
        ["Random Forest", "Gradient Boosting", "Logistic Regression", "SVM"]
    )
with col_cfg3:
    test_size = st.slider(
        "✂️ Test split", 0.1, 0.5, 0.2, 0.05,
        help=("Proportion des données réservées au test" if FR else "Proportion of data reserved for testing")
    )

# Hyperparamètres
st.markdown("#### ⚙️ " + ("Hyperparamètres" if FR else "Hyperparameters"))
hp1, hp2, hp3 = st.columns(3)

if model_choice == "Random Forest":
    with hp1: n_est   = st.slider("n_estimators", 10, 300, 100, 10)
    with hp2: max_d   = st.slider("max_depth", 1, 20, 5)
    with hp3: min_s   = st.slider("min_samples_split", 2, 20, 2)
    model_params = {"n_estimators": n_est, "max_depth": max_d, "min_samples_split": min_s, "random_state": 42}
elif model_choice == "Gradient Boosting":
    with hp1: n_est   = st.slider("n_estimators", 10, 300, 100, 10)
    with hp2: lr      = st.slider("learning_rate", 0.01, 0.5, 0.1, 0.01)
    with hp3: max_d   = st.slider("max_depth", 1, 10, 3)
    model_params = {"n_estimators": n_est, "learning_rate": lr, "max_depth": max_d, "random_state": 42}
elif model_choice == "Logistic Regression":
    with hp1: C_val   = st.slider("C", 0.01, 10.0, 1.0, 0.01)
    with hp2: max_it  = st.slider("max_iter", 100, 2000, 500, 50)
    with hp3: st.empty()
    model_params = {"C": C_val, "max_iter": max_it, "random_state": 42}
else:  # SVM
    with hp1: C_val   = st.slider("C", 0.01, 10.0, 1.0, 0.01)
    with hp2: kernel  = st.selectbox("kernel", ["rbf", "linear", "poly"])
    with hp3: st.empty()
    model_params = {"C": C_val, "kernel": kernel, "probability": True}

st.divider()

# ── Entraînement ───────────────────────────────────────────────────────────────
X, y, labels = get_dataset(dataset_choice)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42, stratify=y
)
scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_train)
X_te_s = scaler.transform(X_test)

MODELS = {
    "Random Forest":       RandomForestClassifier,
    "Gradient Boosting":   GradientBoostingClassifier,
    "Logistic Regression": LogisticRegression,
    "SVM":                 SVC,
}

with st.spinner("⏳ " + ("Entraînement en cours…" if FR else "Training…")):
    clf = MODELS[model_choice](**model_params)
    clf.fit(X_tr_s, y_train)
    y_pred = clf.predict(X_te_s)
    acc    = accuracy_score(y_test, y_pred)
    cm     = confusion_matrix(y_test, y_pred)

# Métriques
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric("✅ Accuracy", f"{acc:.1%}",
              delta=f"{acc - 0.5:.1%} vs random",
              delta_color="normal" if acc >= 0.75 else "inverse")
with col_m2: st.metric("📚 Train", f"{len(X_train)} " + ("exemples" if FR else "samples"))
with col_m3: st.metric("🧪 Test",  f"{len(X_test)} "  + ("exemples" if FR else "samples"))
with col_m4: st.metric("🏷️ Classes", len(labels))

st.divider()

# Visualisations
tab_cm, tab_pca, tab_feat, tab_code = st.tabs([
    "📊 Confusion Matrix",
    "🔭 PCA",
    "🏆 " + ("Importance des features" if FR else "Feature importance"),
    "📄 Code"
])

with tab_cm:
    st.markdown("**" + ("La diagonale = les bons classements. Hors diagonale = les erreurs du modèle." if FR
                        else "Diagonal = correct predictions. Off-diagonal = model mistakes.") + "**")
    fig_cm = px.imshow(
        cm, text_auto=True,
        x=labels, y=labels,
        color_continuous_scale="Blues",
        labels=dict(x="Prédit" if FR else "Predicted", y="Réel" if FR else "Actual")
    )
    fig_cm.update_layout(height=380)
    st.plotly_chart(fig_cm, use_container_width=True)

with tab_pca:
    st.markdown("**" + ("Projection des données en 2D avec la PCA. Chaque couleur = une classe." if FR
                        else "Data projected to 2D with PCA. Each colour = one class.") + "**")
    pca    = PCA(n_components=2, random_state=42)
    X_all_s = scaler.transform(X)
    X_2d    = pca.fit_transform(X_all_s)
    df_pca  = pd.DataFrame(X_2d, columns=["PC1", "PC2"])
    df_pca["class"] = [labels[i] for i in y]
    fig_pca = px.scatter(
        df_pca, x="PC1", y="PC2", color="class",
        title=f"PCA — {pca.explained_variance_ratio_.sum():.1%} " + ("variance expliquée" if FR else "variance explained"),
        template="plotly_dark"
    )
    st.plotly_chart(fig_pca, use_container_width=True)

with tab_feat:
    has_importance = model_choice in ("Random Forest", "Gradient Boosting")
    has_coef      = model_choice == "Logistic Regression"
    if has_importance:
        feat_df = pd.DataFrame({"feature": X.columns, "importance": clf.feature_importances_})\
                    .sort_values("importance", ascending=True).tail(15)  # top 15 pour Breast Cancer
        st.plotly_chart(
            px.bar(feat_df, x="importance", y="feature", orientation="h",
                   color="importance", color_continuous_scale="Viridis",
                   title="Top 15 Feature Importances"),
            use_container_width=True
        )
    elif has_coef:
        coefs = np.abs(clf.coef_).mean(axis=0)
        feat_df = pd.DataFrame({"feature": X.columns, "importance": coefs})\
                    .sort_values("importance", ascending=True).tail(15)
        st.plotly_chart(
            px.bar(feat_df, x="importance", y="feature", orientation="h",
                   color="importance", color_continuous_scale="Viridis",
                   title="Top 15 — Mean |Coefficient|"),
            use_container_width=True
        )
    else:
        st.info("ℹ️ " + ("Feature importance non disponible pour SVM." if FR else "Feature importance not available for SVM."))

with tab_code:
    st.markdown("**" + ("Le code exact qui fait tourner cette démo :" if FR else "The exact code running this demo:") + "**")
    st.code("""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
clf.fit(X_train, y_train)

acc = accuracy_score(y_test, clf.predict(X_test))
print(f"Accuracy: {acc:.1%}")
""")

st.divider()

# ── Prédiction manuelle ─────────────────────────────────────────────────────
st.markdown("## 🎯 " + ("Prédire sur de nouvelles données" if FR else "Predict on new data"))
st.markdown("**" + ("Ajuste les valeurs des features ci-dessous et vois la prédiction en temps réel." if FR
                    else "Adjust the feature values below and get a live prediction.") + "**")

# Pour Breast Cancer, trop de features (30) — on ne montre que les top 6 selon importance
if dataset_choice == "Breast Cancer" and model_choice in ("Random Forest", "Gradient Boosting"):
    top_features = pd.Series(clf.feature_importances_, index=X.columns).nlargest(6).index.tolist()
elif dataset_choice == "Breast Cancer":
    top_features = X.columns[:6].tolist()  # fallback: 6 premières
else:
    top_features = X.columns.tolist()  # Iris : 4 features, on les montre toutes

input_cols = st.columns(len(top_features))
input_vals_dict = {}
for col_ui, feat in zip(input_cols, top_features):
    with col_ui:
        v = st.number_input(
            feat[:18],  # tronque les noms longs
            min_value=float(X[feat].min()),
            max_value=float(X[feat].max()),
            value=float(X[feat].mean()),
            format="%.3f",
            key=f"input_{feat}"
        )
        input_vals_dict[feat] = v

# Reconstruire le vecteur complet (valeur moyenne pour les features non affichées)
full_input = X.mean().to_dict()
full_input.update(input_vals_dict)
full_array  = np.array([full_input[f] for f in X.columns]).reshape(1, -1)
full_scaled = scaler.transform(full_array)

pred_class = clf.predict(full_scaled)[0]
pred_proba = clf.predict_proba(full_scaled)[0]

col_res1, col_res2 = st.columns([1, 2])
with col_res1:
    st.success(f"🎯 " + ("Prédiction" if FR else "Prediction") + f" : **{labels[pred_class]}**")
with col_res2:
    fig_p = px.bar(
        pd.DataFrame({"class": labels, "probability": pred_proba}),
        x="class", y="probability",
        color="probability", color_continuous_scale="Blues",
        title="" + ("Probabilités par classe" if FR else "Probabilities per class"),
        range_y=[0, 1]
    )
    fig_p.update_layout(height=240, margin=dict(t=30, b=0))
    st.plotly_chart(fig_p, use_container_width=True)

st.divider()
st.success("🎉 " + ("Guide terminé ! Retrouve d’autres projets ici →" if FR else "Guide complete! Find more projects here →"))
c1, c2 = st.columns(2)
with c1: st.link_button("🐙 GitHub — BadreddineEK", "https://github.com/BadreddineEK", use_container_width=True)
with c2: st.link_button("🌐 Portfolio", "https://badreddineek.github.io/portfolioBadreddine", use_container_width=True)
