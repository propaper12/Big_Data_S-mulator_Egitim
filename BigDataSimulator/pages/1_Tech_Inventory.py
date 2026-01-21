# pages/1_Tech_Inventory.py
import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import TECH_STACK, CATEGORY_COLORS, UI_TEXTS

st.set_page_config(page_title="Tech Encyclopedia", page_icon="📚", layout="wide")

if 'language' not in st.session_state:
    st.session_state.language = 'en'
lang = st.session_state.language
texts = UI_TEXTS[lang]

title = "📚 Big Data Technology Encyclopedia" if lang == "en" else "📚 Büyük Veri Teknolojileri Ansiklopedisi"
st.title(title)
st.markdown("---")

tabs = st.tabs(list(TECH_STACK.keys()))

for i, (category, techs) in enumerate(TECH_STACK.items()):
    with tabs[i]:
        color = CATEGORY_COLORS[category]
        st.markdown(f"<h3 style='color:{color}'>{category}</h3>", unsafe_allow_html=True)

        for tech_name, info in techs.items():
            desc_short = info["desc"][lang]
            desc_long = info["detail"][lang]  # Bu artık çok uzun
            link = info["link"]
            is_modern = info["modern"]
            dependency = info.get("dep")  # get ile al, yoksa hata vermesin

            status_icon = "🚀 Modern" if is_modern else "⏳ Legacy"
            status_color = "green" if is_modern else "red"

            with st.expander(f"**{tech_name}** -  _{desc_short}_"):
                c1, c2 = st.columns([3, 1])

                with c1:
                    st.markdown(f"### 📖 {('Description' if lang == 'en' else 'Detaylı Açıklama')}")
                    # Markdown kullanarak uzun metni render et
                    st.markdown(desc_long)
                    st.markdown(f"🔗 [**{texts['doc_link']}**]({link})")

                with c2:
                    st.info(f"**{texts['modernity']}:** :{status_color}[{status_icon}]")
                    if dependency:
                        st.warning(f"**{texts['dependency']}:**\n\n{dependency}")
                    else:
                        st.success("✅ Standalone")