import streamlit as st
import os

def play_tutorial(video_path="tutorials/uputstvo.mp4"):
    st.subheader("🎓 Video Tutorijal")

    if not os.path.exists(video_path):
        st.warning(f"📁 Video fajl nije pronađen: {video_path}")
        return

    st.video(video_path)
    st.info("📌 Ako video ne radi, proveri da li fajl postoji u folderu 'tutorials/'")