import streamlit as st
import os

st.header('STREAMLIT :red[colors] Tutorial')

st.subheader('Hey People You doing fine ??')

st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
st.title('A title with _BOLD_ :red[colors] and emojis :desert:')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

ASDF = ''' print ("Hello LAB")'''

st.code(ASDF, language="python")