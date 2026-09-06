import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analytics import generate_dashboard

def test_empty_data(capsys):
    generate_dashboard([])

    captured = capsys.readouterr()

    assert "No reel data available" in captured.out


def test_dashboard_generation(tmp_path, monkeypatch):
    data = [
        {
            "genre": "comedy",
            "duration": 10,
            "happy": 70,
            "neutral": 20,
            "sad": 10
        }
    ]

    monkeypatch.chdir(tmp_path)

    generate_dashboard(data)

    assert (tmp_path / "graph.png").exists()
    assert (tmp_path / "dashboard.html").exists()