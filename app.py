import streamlit as st
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = str(current_dir / "assets" / "20210214--44I2260-modified.png")
email = "connor@connorraney.com"
linkedin = "https://www.linkedin.com/in/connorraney"
resume_file = "https://drive.google.com/file/d/1VXVvgAtZkZJQQ93bVfV7YeDC75fwjRcI/view?usp=sharing"

def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

# --- OPEN PDF & RESUME FILE ---
# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Connor Raney",
    page_icon="🤗",
)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title("Connor Raney")
    st.write("Entrepreneur & Analytics Major at Babson College")
    st.write("📑 [My Resume](%s)" % resume_file)
    st.write("🔗 [My LinkedIn](%s)" % linkedin)
    st.write("✉ Email Me!", email)

st.header("👋 About Me!")
st.write("From the age of twelve, when I automated the sale of mobile game currency, I've been infatuated with the world of business. My journey has taken me through diverse industries, from influencer marketing and software development to e-commerce and the booming sneaker market, and most recently, into the exciting realm of Web3 and NFTs.")
st.write("I'm a true business enthusiast, always eager to learn and grow. My love for entrepreneurship started at a young age and has only intensified, becoming the driving force in my life. I've had my fair share of successes and failures, all of which have contributed to over $1m in revenue across seven years of company-building experience.")
st.write("My passion for business extends to every role I've embraced, be it internships or my own ventures. I bring a bubbly, fun, and engaging personality to any workplace, and my expertise lies in networking, ideation, marketing strategies, and launching online businesses.")
st.write("As a hockey and analytics lover, I'm thrilled to combine these interests by concentrating in quantitative methods and business analytics at Babson College. I'm always keen to connect and expand my network, so don't hesitate to reach out!")

st.header("Hobbies!")
colm1, colm2, colm3 = st.columns(3, gap="small")
with colm1:
    st.subheader("Hockey 🥅")
    st.write("I am a huge hockey fan, and love crunching different hockey analytics. I'm also a huge New York Rangers fan, I went to over 20 games in the last 21-22 season, including every home playoff game!")
with colm2:
    st.subheader("Poker ♠")
    st.write("I've been playing poker in the MA & RI area and am super interested in the numbers aspect behind Poker. By running solvers, & studying ranges and equities, I've been learning a lot overall.")
with colm3:
    st.subheader("Analytics & Python 📊")
    st.write("I am a little bit of a numbers nerd when it comes to hockey. Lately I've picked up python for both data science and web development (this site!) and it's been very fun!")