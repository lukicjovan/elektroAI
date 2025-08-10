import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from usage_tracker import track_event
from ui_helpers import expander_section
from lang_helper import t

def prikazi_heatmapu_kvarova(podatak_matrix):
    def content():
        track_event("heatmap_kvarova", {"dimenzije": (len(podatak_matrix), len(podatak_matrix[0]))})

        df = pd.DataFrame(podatak_matrix)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df, annot=True, fmt="d", cmap="Reds", ax=ax)
        st.pyplot(fig)

        st.caption(t("heatmap_description"))

    expander_section(t("heatmap_section"), t("heatmap_details"), content)