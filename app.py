"""ODISHA AI ONE — Build AI for the World
Main application entry point.

Tagline: "Local Intelligence. Global Impact."
Tech Stack: Python, Streamlit, Pandas, Plotly, SQLite.
Architecture: Decoupled frontend calling backend services and database layer.
"""

import streamlit as st

# Configure page layout and meta (must be the first Streamlit command)
st.set_page_config(
    page_title="ODISHA AI ONE — Build AI for the World",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.footer import render_footer
from components.sidebar import render_sidebar
from components.ui_utils import load_custom_css
from database.schema import init_db
from database.seed_data import seed_resources_if_empty
from views.about_view import render_about_page
from views.assistant_view import render_assistant_page
from views.dashboard_view import render_dashboard_page
from views.global_impact_view import render_global_impact_page
from views.home_view import render_home_page
from views.innovation_lab_view import render_innovation_lab_page
from views.project_hub_view import render_project_hub_page
from views.resource_hub_view import render_resource_hub_page
from views.settings_view import render_settings_page


def init_app_state():
    """Ensure database schema is initialized and persistent session states are registered."""
    # Initialize SQLite database and verified resource index
    init_db()
    seed_resources_if_empty()

    # Session defaults
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = "Odisha Innovator"
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = "Student / Researcher"
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = "user_demo"
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = "session_odisha_001"
    if "language_preference" not in st.session_state:
        st.session_state["language_preference"] = "English"


def main():
    """Main routing and execution loop."""
    init_app_state()
    load_custom_css()

    # Persistent Sidebar Navigation
    current_page = render_sidebar()

    # Page Router
    if current_page == "Home":
        render_home_page()
    elif current_page == "AI Dashboard":
        render_dashboard_page()
    elif current_page == "Odia AI Assistant":
        render_assistant_page()
    elif current_page == "AI Project Hub":
        render_project_hub_page()
    elif current_page == "AI Innovation Lab":
        render_innovation_lab_page()
    elif current_page == "AI Resource Hub":
        render_resource_hub_page()
    elif current_page == "Global Impact":
        render_global_impact_page()
    elif current_page == "About the Initiative":
        render_about_page()
    elif current_page == "Settings":
        render_settings_page()
    else:
        render_home_page()

    # Consistent Platform Footer
    render_footer()


if __name__ == "__main__":
    main()
