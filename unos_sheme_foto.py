import streamlit as st
from lang_helper import t
from upload_zone import render_upload
from render_shema import preview_shema
from storage import save_shema
from ui_helpers import expander_section
from auth_manager import get_current_user
from database import insert_shema

def shema_ui():
    def content():
        user = get_current_user()
        if not user:
            st.warning(t("login_required"))
            return

        # Drag & Drop zona
        uploaded_file, suggested_name = render_upload()

        if uploaded_file:
            st.text_input(t("shema_name"), value=suggested_name, key="shema_name")
            preview_shema(uploaded_file)

            if st.button(t("save_shema")):
                name = st.session_state.get("shema_name", suggested_name)
                preview_path = save_shema(uploaded_file, name)
                insert_shema(project_id=1, file_path=uploaded_file.name, preview_path=preview_path)
                st.success(t("shema_saved"))

    expander_section(t("shema_section"), t("shema_section_description"), content)