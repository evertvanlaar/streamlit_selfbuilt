import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----

# ---- LOAD STYLE ----
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Evert :wave:")
    st.title("A Web development enthousiast From The Netherlands")
    st.write("I am passionate about finding ways to use Python to be more efficient and effective."
    )

st.write('---')
st.title('Interactive Slider Example')

slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected {slider_value}!')

st.write('---')
st.title('Interactive Checkbox Example')
checkbox_value = st.checkbox('Check me')
if checkbox_value:
    st.write('Checkbox is checked!')
else:
    st.write('Checkbox is not checked.')

st.write('---')
st.title('Interactive Text Input Example')

user_text = st.text_input('Enter your text:')
st.write(f'You entered: {user_text}')

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On this website I am creating tutorials for myself to play with python and streamlit.
            - looking for a way to leverage the power of Python in buiding websites and web apps
            """
        )
        st.write("[Streamlit >](https://streamlit.io/)")
    with right_column:
        st.header('Space left blank intentionally')
        st.image(
            "images/eef.jpg",
            width=115, # Manually Adjust the width of the image as per requirement
        )
