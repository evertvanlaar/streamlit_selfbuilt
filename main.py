import streamlit as st

st.title('My first website!')
st.write('Welcome to my interactive website built using Python!!!!!!!')
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
