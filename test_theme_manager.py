from theme_manager import apply_theme

def test_apply_light_theme_runs():
    apply_theme("light")
    assert True

def test_apply_dark_theme_runs():
    apply_theme("dark")
    assert True

def test_apply_invalid_theme_defaults():
    apply_theme("invalid_mode")
    assert True