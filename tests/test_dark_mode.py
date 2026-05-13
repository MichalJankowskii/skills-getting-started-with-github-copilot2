from pathlib import Path

from fastapi.testclient import TestClient

from src.app import app


def test_index_has_dark_mode_toggle():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert 'id="theme-toggle"' in response.text
    assert "Switch to Dark Mode" in response.text


def test_dark_mode_styles_and_script_exist():
    project_root = Path(__file__).resolve().parents[1]
    styles = (project_root / "src" / "static" / "styles.css").read_text()
    script = (project_root / "src" / "static" / "app.js").read_text()

    assert "body.dark-mode" in styles
    assert "theme-toggle" in script
    assert "localStorage" in script
