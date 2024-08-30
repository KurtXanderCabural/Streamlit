import streamlit as st
from base64 import b64encode

def web_portfolio():
    # page configs 
    st.set_page_config(page_title = "Kurt Xander Cabural",page_icon="⭐")
    # Set the page title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Abhisheak Saraswat</span>👋
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

   

if __name__ == "__main__":
    web_portfolio()
