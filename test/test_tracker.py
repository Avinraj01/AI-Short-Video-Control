import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tracker

def setup_function():
    tracker.all_reels.clear()

    tracker.current_reel["genre"] = None
    tracker.current_reel["start_time"] = None
    tracker.current_reel["emotions"] = []


def test_start_reel():
    tracker.start_reel("comedy")

    assert tracker.current_reel["genre"] == "comedy"
    assert tracker.current_reel["start_time"] is not None


def test_add_emotion():
    tracker.start_reel("music")

    tracker.add_emotion("happy")
    tracker.add_emotion("neutral")
    tracker.add_emotion("sad")

    assert tracker.current_reel["emotions"] == [
        "happy",
        "neutral",
        "sad"
    ]


def test_invalid_emotion_is_ignored():
    tracker.start_reel("gaming")

    tracker.add_emotion("happy")
    tracker.add_emotion("unknown")

    assert tracker.current_reel["emotions"] == ["happy"]


def test_end_reel():
    tracker.start_reel("education")

    tracker.add_emotion("happy")
    tracker.add_emotion("happy")
    tracker.add_emotion("sad")

    tracker.end_reel()

    data = tracker.get_all_data()

    assert len(data) == 1
    assert data[0]["genre"] == "education"
    assert data[0]["happy"] == 66.67
    assert data[0]["sad"] == 33.33
    assert data[0]["neutral"] == 0


def test_end_without_active_reel():
    tracker.end_reel()

    assert tracker.get_all_data() == []