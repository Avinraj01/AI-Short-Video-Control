import time

current_reel = {
    "genre": None,
    "start_time": None,
    "emotions": []
}

all_reels = []


def start_reel(genre):
    """Start tracking a new reel."""
    current_reel["genre"] = genre or "unknown"
    current_reel["start_time"] = time.time()
    current_reel["emotions"] = []


def add_emotion(emotion):
    """Add an emotion observation for the current reel."""
    if current_reel["start_time"] is None:
        return

    valid_emotions = {"happy", "neutral", "sad"}

    if emotion in valid_emotions:
        current_reel["emotions"].append(emotion)


def end_reel():
    """Finish the current reel and store its analytics."""
    if current_reel["start_time"] is None:
        return

    duration = time.time() - current_reel["start_time"]
    emotions = current_reel["emotions"]

    if emotions:
        total = len(emotions)

        happy = emotions.count("happy") / total * 100
        neutral = emotions.count("neutral") / total * 100
        sad = emotions.count("sad") / total * 100
    else:
        happy = neutral = sad = 0

    all_reels.append({
        "genre": current_reel["genre"] or "unknown",
        "duration": round(max(duration, 0), 2),
        "happy": round(happy, 2),
        "neutral": round(neutral, 2),
        "sad": round(sad, 2)
    })

    # Reset current reel state
    current_reel["genre"] = None
    current_reel["start_time"] = None
    current_reel["emotions"] = []


def get_all_data():
    """Return all tracked reel analytics."""
    return all_reels.copy()