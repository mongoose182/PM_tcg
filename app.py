from PIL import Image
import streamlit as st 
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "PM", page_icon = ":flag_united_states:", layout = "wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css("style/style.css")

# Assets
lottie_eagle = load_lottie("https://lottie.host/f89e6578-a69c-4f18-b3fd-1d0c4445e63d/G20TYpauW3.json")
img_chris = Image.open("images/chris_christie_1.png")
img_andy = Image.open("images/jackson_1.png")

# HEADER

st.subheader("Welcome to the Political Machine TCG!")
st.title("Pick a Candidate!")
st.write("Here is our list of candidates: ")
st.write("Instructions: ")


# Candidates section

with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("List of Candidates")
        st.write("##")
        st.write("TEST TEXT")
    with right_column:
        st_lottie(lottie_eagle, height = 300, key = "eagle")

# --CANDIDATES--
with st.container():
    st.write("---")
    st.header("CANDIDATES")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_chris)
    with text_column:
        st.subheader("Chris Christie")
        st.write("This former govenor of NJ is ready to shut his oppponents down as hard as the GWB")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_andy)
    with text_column:
        st.subheader("Andrew Jackson")
        st.write("It's time to duel")

# CONTACT FORM
with st.container():
    st.write("---")
    st.header("Get in touch with us")
    st.write("##")

    contact_form = """""
    <form action="https://formsubmit.co/micwes@gmail.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "false">
    <input type="text" name="name" placeholder = "Your Name" required>
    <input type="email" name="email" placeholder = "Your email" required>
    <textarea name = "message" placeholder = "Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html = True)
with right_column:
    st.empty()