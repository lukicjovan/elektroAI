import pytest
import streamlit as st
from ui_helpers import (
    stylize_header,
    expander_section,
    show_projects,
    show_checkbox_list,
    apply_button_row,
)

def test_stylize_header_runs():
    stylize_header("Test Header", icon="🧪")
    assert True

def test_expander_section_executes():
    def dummy():
        st.write("Inside dummy section")
    expander_section("Title", "Description", dummy)
    assert True

def test_show_projects_runs():
    dummy_projects = [{"name": "Test1", "id": 1}, {"name": "Test2", "id": 2}]
    show_projects(dummy_projects)
    assert True

def test_show_checkbox_list_empty():
    result = show_checkbox_list([])
    assert isinstance(result, list)

def test_apply_button_row():
    def dummy(): return None
    apply_button_row({"Run": dummy})
    assert True