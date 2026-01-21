import streamlit as st
import graphviz
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import TECH_STACK, CATEGORY_COLORS, UI_TEXTS, get_category, auto_connect_nodes, validate_stack

st.set_page_config(page_title="Architect Studio", page_icon="🏗️", layout="wide")

if 'language' not in st.session_state:
    st.session_state.language = 'en'
lang = st.session_state.language
texts = UI_TEXTS[lang]

st.title("🏗️ Architecture Studio")

# --- 1. AKILLI ŞABLONLAR ---
PRESETS = {
    "🚀 Modern Real-Time Streaming": {
        "desc": "Kafka & Flink based low-latency pipeline on Kubernetes.",
        "tr_desc": "Kubernetes üzerinde Kafka ve Flink tabanlı düşük gecikmeli akış.",
        "stack": ["Kafka", "Zookeeper", "Flink", "S3", "ClickHouse", "Grafana", "Kubernetes", "Prometheus"]
    },
    "🏰 Cloud-Native Lakehouse": {
        "desc": "Modern storage layout with Delta Lake and Spark on Docker.",
        "tr_desc": "Docker üzerinde Delta Lake ve Spark ile modern veri gölü mimarisi.",
        "stack": ["Airbyte", "S3", "Delta Lake", "Spark", "Databricks", "MLflow", "Airflow", "Docker"]
    },
    "🐘 Legacy Hadoop Cluster": {
        "desc": "Traditional on-premise Big Data stack managed by YARN.",
        "tr_desc": "YARN tarafından yönetilen geleneksel sunucu tabanlı Büyük Veri yığını.",
        "stack": ["Flume", "HDFS", "Hadoop MR", "Hive", "Zookeeper", "YARN", "HBase"]
    },
    "⚡ High-Speed Analytics (No JVM)": {
        "desc": "Modern, fast tools without Java dependency.",
        "tr_desc": "Java bağımlılığı olmayan modern ve hızlı araçlar.",
        "stack": ["Redpanda", "Flink", "ClickHouse", "Superset", "Kubernetes", "Prometheus"]
    },
    "🕸️ Microservices & CDC": {
        "desc": "Event-driven architecture with CDC.",
        "tr_desc": "CDC (Veri Değişikliği Yakalama) ile olay güdümlü mimari.",
        "stack": ["Debezium", "Kafka", "Zookeeper", "PostgreSQL", "Redis", "Elasticsearch", "Kibana", "Docker"]
    }
}

if 'selected_stack' not in st.session_state: st.session_state.selected_stack = []
if 'generated_edges' not in st.session_state: st.session_state.generated_edges = []
if 'validation_errors' not in st.session_state: st.session_state.validation_errors = []

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚡ Quick Start")
    selected_preset_name = st.selectbox("📚 Select Blueprint", ["Custom Build"] + list(PRESETS.keys()), index=0)

    if selected_preset_name != "Custom Build":
        desc_key = "tr_desc" if lang == "tr" else "desc"
        st.info(f"ℹ️ {PRESETS[selected_preset_name][desc_key]}")
        if st.button("🚀 Load & Visualize", type="primary", use_container_width=True):
            stack = PRESETS[selected_preset_name]["stack"]
            st.session_state.selected_stack = stack
            layered_nodes, edges = auto_connect_nodes(stack)
            st.session_state.generated_edges = edges
            st.session_state.layered_nodes = layered_nodes
            st.session_state.validation_errors = []
            st.rerun()

    st.markdown("---")
    if st.button("🗑️ Reset All", use_container_width=True):
        st.session_state.selected_stack = []
        st.session_state.generated_edges = []
        st.session_state.validation_errors = []
        st.rerun()

# --- ANA EKRAN ---

if st.session_state.generated_edges:

    stack = st.session_state.selected_stack
    stack_len = len(stack)
    complexity = stack_len * 10 + len(st.session_state.generated_edges) * 5

    st.success(f"✅ Architecture Generated with {stack_len} components.")

    # ALTYAPI TESPİTİ (FRAME MANTIĞI)
    infra_frame = None
    if "Kubernetes" in stack:
        infra_frame = "Kubernetes Cluster"
    elif "Docker" in stack:
        infra_frame = "Docker Environment"
    elif "YARN" in stack:
        infra_frame = "Hadoop YARN Cluster"

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Components", stack_len)
    m2.metric("Connections", len(st.session_state.generated_edges))
    m3.metric("Complexity", f"{complexity}")
    m4.metric("Runtime Platform", infra_frame if infra_frame else "Bare Metal / Serverless")

    # --- GRAFİK ÇİZİMİ ---
    g = graphviz.Digraph()
    # Graphviz ayarları: Compound=True (Clusterlar arası çizgi için), Rankdir=LR (Soldan sağa)
    g.attr(compound='true', rankdir='LR', splines='ortho', nodesep='0.6', ranksep='0.8', bgcolor='transparent')
    g.attr('node', fontname="Sans-Serif", fontsize="11", style='filled')
    g.attr('edge', color='#555555', penwidth='1.2', arrowsize='0.7')

    layers = st.session_state.get('layered_nodes', {})
    edges = st.session_state.generated_edges

    # SaaS / External Servisler (Bunlar Infra Frame'in dışında kalmalı)
    # Listeyi genişletebilirsin
    SAAS_TOOLS = ["S3", "BigQuery", "Snowflake", "Redshift", "Athena", "Fivetran", "Databricks", "Tableau", "Looker",
                  "GCS", "ADLS Gen2"]

    # Infra Frame içinde olacak node'lar ve dışında olacaklar
    nodes_inside_frame = []
    nodes_outside_frame = []

    # Tüm node'ları tara ve ayır
    for layer_id, nodes in layers.items():
        for node in nodes:
            # Infra elemanlarının kendisi (K8s, Docker) çizilmeyecek, onlar Frame olacak.
            if node in ["Kubernetes", "Docker", "YARN"]:
                continue

            # Zookeeper gibi servisler Infra Frame içinde olur
            # SaaS araçları dışarıda olur
            if node in SAAS_TOOLS:
                nodes_outside_frame.append((layer_id, node))
            else:
                nodes_inside_frame.append((layer_id, node))

    # --- 1. ALTYAPI ÇERÇEVESİ (EĞER VARSA) ---
    if infra_frame:
        # "cluster_" öneki Graphviz'de görsel bir kutu çizer
        with g.subgraph(name="cluster_infrastructure") as infra:
            infra.attr(label=f"🏗️ {infra_frame} (Runtime)", style='rounded,filled', color='#eceff1', fontsize="12",
                       fontcolor="#455a64")

            # Çerçevenin içindeki node'ları çiz (Layer Layer gruplayarak)
            # Gruplama, içerdeki düzeni korumak için yine subgraph kullanır ama "cluster" öneki koymayız ki sınır çizmesin
            for layer_id in sorted(layers.keys()):
                layer_nodes = [n for l, n in nodes_inside_frame if l == layer_id]
                if layer_nodes:
                    with infra.subgraph(name=f"layer_grp_{layer_id}") as l_grp:
                        l_grp.attr(rank='same')  # Aynı katman aynı hizada olsun
                        for node in layer_nodes:
                            cat = get_category(node)
                            fill = "white"
                            shape = "box"
                            if layer_id in [2, 4]: shape = "cylinder"  # Storage/DB
                            if layer_id == 0: shape = "component"  # Zookeeper vb.

                            l_grp.node(node, label=node, fillcolor=fill, shape=shape)
    else:
        # Infra yoksa, içerdekileri normal çiz
        for layer_id, node in nodes_inside_frame:
            cat = get_category(node)
            shape = "cylinder" if layer_id in [2, 4] else "box"
            if layer_id == 0: shape = "component"
            g.node(node, label=node, fillcolor="white", shape=shape)

    # --- 2. DIŞ SERVİSLER (SAAS - ÇERÇEVE DIŞI) ---
    for layer_id, node in nodes_outside_frame:
        g.node(node, label=f"☁️ {node}\n(Managed)", fillcolor="#e3f2fd", shape="egg", style="filled,dashed")

    # --- 3. KENARLAR (EDGES) ---
    for source, target in edges:
        # Eğer Infra node'ları kaynak/hedef ise (örn eskiden kalma bir bağ), onları çizme
        if source in ["Kubernetes", "Docker", "YARN"] or target in ["Kubernetes", "Docker", "YARN"]:
            continue
        g.edge(source, target)

    # --- 4. ZOOKEEPER / PROMETHEUS BAĞLANTILARI ---
    # Bu servisler genelde infra içindedir, içerdeki diğer elemanlara bağlanırlar
    if layers.get(0):
        for node in layers[0]:
            if node == "Zookeeper" and "Zookeeper" not in ["Kubernetes", "Docker", "YARN"]:
                # Kafka vb. bul ve bağla
                for target in layers.get(1, []) + layers.get(3, []) + layers.get(4, []):
                    if target in ["Kafka", "Pulsar", "HBase", "Solr", "Flink", "ClickHouse"]:
                        g.edge(node, target, style="dashed", color="red", label="coord", fontsize="8")

            if node == "Prometheus":
                # Monitored targets
                targets = layers.get(1, []) + layers.get(3, [])
                if targets:
                    g.edge(node, targets[0], style="dotted", color="green", label="scrapes")

    st.graphviz_chart(g, use_container_width=True)

    # 3. KOD ÇIKTISI
    with st.expander("💾 Infrastructure as Code"):
        tab_tf, tab_docker = st.tabs(["Terraform", "Docker Compose"])
        with tab_tf:
            st.code(f"""# Terraform for {infra_frame if infra_frame else 'Stack'}
module "data_stack" {{
  source = "./modules/{infra_frame.lower().replace(' ', '_') if infra_frame else 'standard'}"
  components = {str(stack)}
}}""", language="hcl")
        with tab_docker:
            yaml_out = "version: '3.8'\nservices:\n"
            for comp in stack:
                if comp in ["Kubernetes", "Docker", "YARN"]: continue  # Bunlar servis değil platform
                name = comp.lower().replace(" ", "")
                yaml_out += f"  {name}:\n    image: bitnami/{name}:latest\n    networks: [data-net]\n"
            st.code(yaml_out, language="yaml")

# --- COMPONENT BUILDER ---
st.markdown("---")
st.subheader("🛠️ Customize Stack")

categories = {
    "📥 Ingestion": "Ingestion",
    "💾 Storage": "Storage",
    "⚙️ Processing": "Processing",
    "🗄️ Databases": "Databases",
    "🎼 Orchestration": "Orchestration",
    "🧠 AI/ML": "AI/ML",
    "📊 BI/Serving": "Serving/BI"
}

tabs = st.tabs(list(categories.keys()))
current_selection = st.session_state.selected_stack.copy()

for i, (tab_name, cat_key) in enumerate(categories.items()):
    with tabs[i]:
        if cat_key in TECH_STACK:
            techs = list(TECH_STACK[cat_key].keys())
            default_vals = [t for t in current_selection if t in techs]
            selected_in_cat = st.multiselect(f"Select {cat_key}", techs, default=default_vals, key=f"tab_{cat_key}",
                                             label_visibility="collapsed")
            for old in default_vals:
                if old not in selected_in_cat: current_selection.remove(old)
            for new in selected_in_cat:
                if new not in current_selection: current_selection.append(new)

if current_selection != st.session_state.selected_stack:
    if st.button("🔄 Update Architecture", type="primary"):
        st.session_state.selected_stack = current_selection
        errors = validate_stack(current_selection, lang=lang)
        if errors:
            st.session_state.validation_errors = errors
            st.session_state.generated_edges = []
        else:
            st.session_state.validation_errors = []
            layered_nodes, edges = auto_connect_nodes(current_selection)
            st.session_state.generated_edges = edges
            st.session_state.layered_nodes = layered_nodes
        st.rerun()

if st.session_state.validation_errors:
    st.error("⚠️ Configuration Error")
    for err in st.session_state.validation_errors:
        st.markdown(f"- {err}")