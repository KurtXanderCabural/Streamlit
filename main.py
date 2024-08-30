add sidebar on this code:

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

    @keyframes slowTilt {{
        0%, 100% {{
            transform: rotate(0deg);
        }}
        50% {{
            transform: rotate(5deg);
        }}
    }}
    
    .box {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .box img {{
        animation: slowTilt 2s ease-in-out infinite;
        max-width: 40%;  /* Ensures image doesn't exceed container width */
        height: auto;     /* Maintains aspect ratio */
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
    <div class="box">
        <img src="{image_url}" alt="Kurt Xander Cabural">
    </div>
    """, unsafe_allow_html=True)

    # Set the title
    st.write(f"""
             <div class=
             "subtitle" style="text-align: center;">Front-end Developer and Web Designer</div>""",
              unsafe_allow_html=True)

    # Add Social Icons
    social_icons_data = {
    "Figma": ["https://www.figma.com/files/team/1239597512271544315/all-projects?fuid=1239597507354790543", "https://cdn-icons-png.flaticon.com/128/6423/6423305.png"],
    "LinkedIn": ["https://www.linkedin.com/in/kurt-xander-cabural-129132310/", "https://cdn-icons-png.flaticon.com/128/6422/6422202.png"],
    "GitHub": ["https://github.com/KurtXanderCabural", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    "Facebook": ["https://www.facebook.com/Cabural.Kurt.Xander.M", "https://cdn-icons-png.flaticon.com/128/6422/6422199.png"],
    "Discord": ["https://discord.com/channels/@me", "https://cdn-icons-png.flaticon.com/128/6422/6422197.png"]
    }

    social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons_data
]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
