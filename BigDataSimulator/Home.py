# Home.py
import streamlit as st

st.set_page_config(page_title="Big Data Simulator", page_icon="🏗️", layout="wide")

# Dil Seçimi Başlatma (Varsayılan: İngilizce)
if 'language' not in st.session_state:
    st.session_state.language = 'en'

st.sidebar.title("Settings / Ayarlar")
lang_choice = st.sidebar.radio("Language / Dil", ["English", "Türkçe"])

if lang_choice == "English":
    st.session_state.language = "en"
else:
    st.session_state.language = "tr"

lang = st.session_state.language

# İçerik
if lang == "en":
    st.title("🏗️ Big Data Architecture Simulator")
    st.markdown("### Welcome, Architect.")
    st.markdown("""
    This tool helps you learn Big Data Architecture by building it.

    1. **Inventory:** Learn about the tools.
    2. **Simulator:** Connect components. If you make a mistake (e.g., connecting Zookeeper to Spark), the system will teach you why it's wrong.
    """)
else:
    st.title("🏗️ Büyük Veri Mimarisi Simülatörü")
    st.markdown("### Hoşgeldiniz, Mimar.")
    st.markdown("""
    Bu araç, inşa ederek Büyük Veri Mimarisi öğrenmenize yardımcı olur.

    1. **Envanter:** Araçlar hakkında bilgi edinin.
    2. **Simülatör:** Bileşenleri birbirine bağlayın. Eğer bir hata yaparsanız (örn: Zookeeper'ı Spark'a bağlamak gibi), sistem neden yanlış olduğunu size öğretecektir.
    """)

st.info("Start via the Sidebar / Menüden başlayın." if lang == "en" else "Sol menüden sayfaları seçerek başlayın.")