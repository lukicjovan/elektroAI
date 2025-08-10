import streamlit as st

def apply_theme(theme_mode="light"):
    if theme_mode == "dark":
        st.markdown("""
            <style>
            body {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
            }
            .stTextInput>div>div>input {
                background-color: #333;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body {
                background-color: #ffffff;
                color: #000000;
            }
            .stButton>button {
                background-color: #008CBA;
                color: white;
            }
            .stTextInput>div>div>input {
                background-color: #f0f0f0;
                color: black;
            }
            </style>
        """, unsafe_allow_html=True)