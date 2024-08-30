import streamlit as st

def web_portfolio():
    # Page configs
    st.set_page_config(page_title="Kurt Xander Cabural", page_icon="⭐")
    
    # Set the page title with waving hand emoji animation
    st.write(f"""
    <style>
    .waving-hand {{
        display: inline-block;
        animation: wave 1s linear infinite;
    }}
    
    @keyframes wave {{
        0% {{
            transform: rotate(0deg);
        }}
        25% {{
            transform: rotate(15deg);
        }}
        50% {{
            transform: rotate(0deg);
        }}
        75% {{
            transform: rotate(-15deg);
        }}
        100% {{
            transform: rotate(0deg);
        }}
    }}

    @keyframes rotate {{
        0% {{
            transform: rotate(0deg);
        }}
        100% {{
            transform: rotate(360deg);
        }}
    }}
    
    .animated-img {{
        width: 200px;
        height: auto;
        border-radius: 50%;
        animation: rotate 5s linear infinite;
    }}
    </style>
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Kurt Xander Cabural</span>
    <span class="waving-hand">👋</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Use the raw GitHub URL for the profile image
    image_url = "https://raw.githubusercontent.com/KurtXanderCabural/Streamlit/main/kx.png"

    # Display the image with center alignment and animation
    st.write(f"""
    <div style="text-align: center;">
        <img src="{image_url}" alt="Kurt Xander Cabural" class="animated-img">
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
