import streamlit as st
from gallery import render_sidebar_gallery

def test_render_sidebar_gallery_with_empty_list():
    render_sidebar_gallery([])
    assert True

def test_render_sidebar_gallery_with_mock_data():
    sheme = [
        {"name": "Test šema 1", "thumbnail": "preview/test1.png"},
        {"name": "Test šema 2", "thumbnail": "preview/test2.png"},
    ]
    render_sidebar_gallery(sheme)
    assert True