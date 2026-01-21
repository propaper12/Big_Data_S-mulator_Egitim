# pages/3_Reference_Architectures.py
import streamlit as st
import graphviz

st.set_page_config(page_title="Reference Architectures", page_icon="🏛️")

st.title("🏛️ Reference Architectures")

tab1, tab2 = st.tabs(["Lambda Architecture", "Modern Data Stack"])

with tab1:
    st.header("The Lambda Architecture")
    st.markdown(
        "Designed to handle massive quantities of data by taking advantage of both batch- and stream-processing methods.")

    g = graphviz.Digraph()
    g.attr(rankdir='LR')
    g.attr('node', shape='box', style='filled')

    g.node("Kafka", fillcolor="#90EE90")
    g.node("Hadoop/HDFS", label="Batch Layer (Master Dataset)", fillcolor="#FFD700")
    g.node("Spark Streaming", label="Speed Layer", fillcolor="#FF6347")
    g.node("Serving Batch", label="Serving Layer (Batch Views)", fillcolor="#DDA0DD")
    g.node("Serving Speed", label="Serving Layer (Real-time Views)", fillcolor="#DDA0DD")
    g.node("App", label="Query/Dashboard", fillcolor="#ADD8E6")

    g.edge("Kafka", "Hadoop/HDFS")
    g.edge("Kafka", "Spark Streaming")
    g.edge("Hadoop/HDFS", "Serving Batch", label="MapReduce/Spark")
    g.edge("Spark Streaming", "Serving Speed")
    g.edge("Serving Batch", "App")
    g.edge("Serving Speed", "App")

    st.graphviz_chart(g)

with tab2:
    st.header("Modern Data Stack (Lakehouse)")
    st.markdown("Simplified architecture unifying Data Lake and Warehouse concepts.")

    g2 = graphviz.Digraph()
    g2.attr(rankdir='LR')
    g2.attr('node', shape='box', style='filled')

    g2.node("Connectors", label="Fivetran/Airbyte", fillcolor="#90EE90")
    g2.node("Lake", label="S3/ADLS (Delta Lake)", fillcolor="#00CED1")
    g2.node("Spark", label="Spark/Databricks", fillcolor="#FF6347")
    g2.node("DW", label="Snowflake/BigQuery", fillcolor="#ADD8E6")
    g2.node("dbt", label="dbt (Transformation)", fillcolor="#D3D3D3")
    g2.node("BI", label="Looker/Superset", fillcolor="#DDA0DD")

    g2.edge("Connectors", "Lake", label="Raw")
    g2.edge("Lake", "Spark", label="ETL")
    g2.edge("Spark", "DW", label="Gold Tables")
    g2.edge("DW", "dbt", label="SQL Modeling")
    g2.edge("dbt", "DW", label="Views")
    g2.edge("DW", "BI")

    st.graphviz_chart(g2)