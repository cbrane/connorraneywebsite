# Import necessary libraries
import streamlit as st
from pathlib import Path
from PIL import Image

# Define constants
current_directory = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = str(current_directory / "assets" / "20210214--44I2260-modified.png")
page_title = "Connor Raney"
page_icon = "🤗"

# Define personal information
linkedin = "https://www.linkedin.com/in/connorraney"
resume_link = "https://drive.google.com/file/d/1fg-UZmT4t5EJl6ypbx4J-_uDcNRlAMUt/view?usp=sharing"
cover_letter = "https://drive.google.com/file/d/128T_BkhyCaFCBhmiXrU7jN8SN3KuLFUa/view?usp=sharing"
github = "https://github.com/cbrane"
email = "connor@connorraney.com"
mailto_link = f"mailto:{email}"

# Set page configuration
st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
)

# Hero Section
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title("Connor Raney")
    st.write("""Entrepreneur and Aspiring Data Scientist Studying Quantitative 
             Methods & Business Analytics at Babson College""")
    st.link_button("🔗 My LinkedIn", linkedin)
    st.link_button("👨‍💻 My Github", github)
    st.link_button("📑 My Resume", resume_link)
    st.link_button("📫 My Cover Letter", cover_letter)
    st.link_button("✉ Email Me!", mailto_link)

# About Me Section
st.header("👋 About Me!")

st.write("""From automating mobile game currency sales at age twelve to engineering 
         cutting-edge AI solutions today, my journey has been driven by a passion 
         for technology and innovation. My path has led me through diverse fields
         including software development, e-commerce, and Web3, culminating in 
         my current focus on artificial intelligence and its transformative potential.""")

st.write("""As an AI Engineer Intern at Barbaricum, I'm at the forefront of 
         applying AI to revolutionize defense technology solutions. I've developed 
         fully automated systems using Large Language Models and multi-agent 
         architectures, dramatically increasing our capacity to analyze complex 
         opportunities and make data-driven decisions.""")

st.write("""My entrepreneurial background, which includes founding several 
         ventures in my early career, now fuels my drive to push the boundaries 
         of what's possible with AI. I combine technical expertise in Python, 
         machine learning, and cloud technologies with an innovative mindset, 
         allowing me to envision creative applications of AI and transform them 
         into practical, scalable solutions.""")

st.write("""Currently pursuing a BS in Business Administration with a concentration 
         in Quantitative Methods and Business Analytics at Babson College, I'm 
         also collaborating with The Generator - Babson's Interdisciplinary AI 
         Lab. My goal is to continue my education with a master's in Data Science 
         or AI, further deepening my expertise in this rapidly evolving field.""")

st.write("""I'm passionate about leveraging AI to create positive change across 
         industries. Whether it's optimizing business processes, enhancing 
         decision-making, or tackling complex societal challenges, I believe in 
         the power of AI to transform our world for the better. Always eager to 
         connect with fellow AI enthusiasts, technologists, and innovators. 
         Let's explore how we can shape the future with AI!""")

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