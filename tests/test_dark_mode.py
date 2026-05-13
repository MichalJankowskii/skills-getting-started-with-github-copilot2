from fastapi.testclient import TestClient

from src.app import app


def test_index_has_dark_mode_toggle():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert 'id="theme-toggle"' in response.text
    assert "Switch to Dark Mode" in response.text


def test_dark_mode_styles_and_script_exist():
    client = TestClient(app)
    styles = client.get("/static/styles.css")
    script = client.get("/static/app.js")

    assert styles.status_code == 200
    assert script.status_code == 200
    assert "body.dark-mode" in styles.text
    assert "theme-toggle" in script.text
    assert "localStorage" in script.text
