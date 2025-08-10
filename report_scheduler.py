import threading
import time
import datetime
import streamlit as st

def schedule_report(interval_minutes=60, callback=None):
    def worker():
        while True:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.toast(f"🕒 Zakazan izveštaj u {now}", icon="📄")
            if callback:
                callback()
            time.sleep(interval_minutes * 60)

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()