import streamlit as st
from lang_helper import t

def stylize_header(text, icon="📁"):
    st.markdown(f"<h4>{icon} {text}</h4>", unsafe_allow_html=True)

def expander_section(title, description, content_func):
    with st.expander(f"{title} — {description}", expanded=False):
        content_func()

def show_projects(project_list):
    for project in project_list:
        st.write(f"📁 {project['name']} ({project['id']})")

def show_gallery(schemes):
    for s in schemes:
        st.image(s["thumbnail"], caption=s["name"], width=160)

def show_radio_group(options, default):
    return st.radio(t("choose_option"), options, index=options.index(default))

def show_checkbox_list(options):
    return st.multiselect(t("select_items"), options)

def apply_button_row(actions: dict):
    cols = st.columns(len(actions))
    for i, (label, func) in enumerate(actions.items()):
        if cols[i].button(label):
            func()

def show_user_badge(user):
    role = user.get("role", "viewer")
    st.sidebar.success(f"🧑 {user['username']} — {t('role_' + role)}")

def show_help_button():
    if st.button(t("open_help")):
        st.toast(t("help_launched"))

def show_plugin_selector(plugins):
    return st.selectbox(t("choose_plugin"), [p["name"] for p in plugins])

def render_plugin_output(plugin, data):
    st.subheader(plugin["description"])
    result = plugin["run"](data)
    st.write(result)

def render_sensor_panel(data):
    for sensor, value in data.items():
        st.metric(label=sensor.capitalize(), value=value)

def show_notification_config():
    st.write("📡 Konfiguracija obaveštenja")
    st.radio("Kanal", ["email", "telegram", "slack"])
    st.slider("Prag", 0, 100, value=70)