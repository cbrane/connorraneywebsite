import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import webbrowser

# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Connor_Raney_-_.pdf"
profile_pic = current_dir / "assets" / "20210214--44I2260-modified.png"
nhl_logo = current_dir / "assets" / "nhllogo.png"
nyr_logo = current_dir / "assets" / "nyrlogo.png"
poker_chips = current_dir / "assets" / "pokerchips.png"
poker_cards = current_dir / "assets" / "pokercards.png"
email = "connor@connorraney.com"
linkedin = "https://www.linkedin.com/in/connor-raney-90a787176"

def open_linkedin_link():
           link = linkedin
           webbrowser.open(link)

def open_resume_pdf():
        resumefile = resume_file
        webbrowser.open(resumefile)

# --- OPEN PDF & RESUME FILE ---
with open(resume_file, "rb") as pdf_file:
     PDFbyte = pdf_file.read()
     profile_pic = Image.open(profile_pic)
     nhl_logo = Image.open(nhl_logo)
     nyr_logo = Image.open(nyr_logo)
     poker_chips = Image.open(poker_chips)
     poker_cards = Image.open(poker_cards)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Connor Raney",
    page_icon="🤗",)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
        st.image(profile_pic, width=230)
with col2:
     st.title("Connor Raney")
     st.write("Entrepreneur & Analytics Major at Babson College")
     st.button("📑 My Resume", on_click=open_resume_pdf)
     st.button("🔗 My LinkedIn", on_click=open_linkedin_link)
     st.write("✉ Email Me!", email)

st.header("👋 About Me!")     
st.write("From the age of twelve, when I automated the sale of mobile game currency, I've been infatuated with the world of business. My journey has taken me through diverse industries, from influencer marketing and software development to e-commerce and the booming sneaker market, and most recently, into the exciting realm of Web3 and NFTs.")
st.write("I'm a true business enthusiast, always eager to learn and grow. My love for entrepreneurship started at a young age and has only intensified, becoming the driving force in my life. I've had my fair share of successes and failures, all of which have contributed to over $1m in revenue across seven years of company-building experience.")
st.write("My passion for business extends to every role I've embraced, be it internships or my own ventures. I bring a bubbly, fun, and engaging personality to any workplace, and my expertise lies in networking, ideation, marketing strategies, and launching online businesses.")
st.write("As a hockey and analytics lover, I'm thrilled to combine these interests by concentrating in quantitative methods and business analytics at Babson College. I'm always keen to connect and expand my network, so don't hesitate to reach out!")

colm1, colm2, colm3 = st.columns(3, gap="small")
with colm1:
     st.header("Hobbies!")
     st.subheader("Hockey 🥅")
     st.write("I am a huge hockey fan, and love crunching different hockey analytics. I'm also a huge New York Rangers fan, I went to over 20 games in the last 21-22 season, including every home playoff game!")
with colm2:
     st.header("ㅤ")
     st.subheader("Poker ♠")
     st.write("I've been playing poker in the MA & RI area and am super interested in the numbers aspect behind Poker. By running solvers, & studying ranges and equities, I've been learning a lot overall.")
with colm3:
     st.header("ㅤ")
     st.subheader("Analytics & Python 📊")
     st.write("I am a little bit of a numbers nerd when it comes to hockey. Lately I've picked up python for both data science and web development (this site!) and it's been very fun!")