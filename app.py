# Import necessary libraries
import streamlit as st
from pathlib import Path
from PIL import Image

# Define constants
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
PROFILE_PIC = str(CURRENT_DIR / "assets" / "20210214--44I2260-modified.png")
PAGE_TITLE = "Connor Raney"
PAGE_ICON = "🤗"

# Define personal information
email = "connor@connorraney.com"
linkedin = "https://www.linkedin.com/in/connorraney"
resume_link = "https://drive.google.com/file/d/1VXVvgAtZkZJQQ93bVfV7YeDC75fwjRcI/view?usp=sharing"
cover_letter = "https://drive.google.com/file/d/1JzuhEKzRqYb7TzbAyK5MVyrBuGS7e-SK/view?usp=sharing"
github = "https://github.com/cbrane"

# Define helper functions
def v_space(lines):
    """Create vertical space in the Streamlit app."""
    for _ in range(lines):
        st.write('&nbsp;')

# Set page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

# Hero Section
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(PROFILE_PIC, width=230)

with col2:
    st.title("Connor Raney")
    st.write("""Entrepreneur and Aspiring Data Scientist Studying Quantitative 
             Methods & Business Analytics at Babson College""")
    st.markdown(f"🔗 [My LinkedIn]({linkedin})")
    st.markdown(f"👨‍💻 [My Github]({github})")
    st.markdown(f"📑 [My Resume]({resume_link})")
    st.markdown(f"📫 [My Cover Letter]({cover_letter})")
    st.markdown(f"✉ [Email Me!]({email})")

# About Me Section
st.header("👋 About Me!")

st.write("""From the age of twelve, when I automated the sale of mobile game 
         currency, I've been infatuated with the world of business. My journey 
         has taken me through diverse industries, from influencer marketing and 
         software development to e-commerce and the booming sneaker market, and 
         most recently, into the exciting realm of Web3 and NFTs.""")

st.write("""I'm a true business enthusiast, always eager to learn and grow. 
         My love for entrepreneurship started at a young age and has only 
         intensified, becoming the driving force in my life. I've had my fair 
         share of successes and failures, all of which have contributed to over 
         $1m in revenue across seven years of company-building experience.""")

st.write("""My passion for business extends to every role I've embraced, be it 
         internships or my own ventures. I bring a bubbly, fun, and engaging 
         personality to any workplace, and my expertise lies in networking, 
         ideation, marketing strategies, and launching online businesses.""")

st.write("""As a hockey and analytics lover, I'm thrilled to combine these 
         interests by concentrating in quantitative methods and business 
         analytics at Babson College. I'm always keen to connect and expand my 
         network, so don't hesitate to reach out!""")

st.write("""After I graduate Babson College in May 2025, I am aiming to pursue
         my Masters in Data Science so that I can further my learning in a more 
         STEM-oriented environment. As of right now, some of my main interests 
         are Machine Learning, AI, Quantitative Analysis (especially when it 
         comes to hockey statistics!) and also programming.""")

# Hobbies Section
st.header("Hobbies!")
colm1, colm2, colm3 = st.columns(3, gap="small")

# Bottom Hockey Column (1/3)
with colm1:
    st.subheader("Hockey 🥅")
    st.write("""I am a huge hockey fan, and love crunching different hockey  
             analytics, check out my Github for my latest project! I'm a massive
              New York Rangers fan and over the last few seasons I've been to 
             over 30 games!""")

# Bottom Photography Column (2/3)
with colm2:
    st.subheader("Photography 📸")
    st.write("""My dad is a photographer specializing in sports and I am now  
             just picking up the hobby as well! You can check out some of my  
             photos on Instagram, @imagesbyconnor, if you are interested.""")

# Analytics/ Python Column (3/3)
with colm3:
    st.subheader("DS & Analytics 📊")
    st.write("""I'm a little bit of a numbers nerd when it comes to hockey. I've
              been working with both R and Python and you can check out my  
             latest NHL Defensive Ice Time Project using R on my Github!""")