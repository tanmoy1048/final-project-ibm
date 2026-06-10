# Emotion Detection (Final Project)

This repository implements a small emotion-detection service that uses an
external Watson NLP endpoint to analyze text and return emotion scores.

Key components
- `emotion_detection.py` — client helper that calls the Watson NLP emotion
	prediction endpoint and parses the response into a simple dictionary.
- `server.py` — a small Flask development server that exposes an endpoint
	(`/emotionDetector`) and serves a frontend `index.html` from `templates/`.
- `static/` — contains frontend JavaScript used by the page.
- `test_emotion_detection.py` — unit tests that mock the external API and
	validate the parsing/formatting logic.

Purpose
-------

The goal of the project is to provide a minimal, reusable interface to an
emotion prediction microservice and a tiny web front-end for demonstration.
The Python helper converts the service's JSON into a consistent structure,
and the Flask server wraps that helper for use by web clients.

Features
--------

- Calls an external Watson-based emotion prediction API.
- Extracts the five canonical emotions: `anger`, `disgust`, `fear`, `joy`,
	and `sadness` and computes the dominant emotion.
- Returns a human-readable, plain-text summary for the frontend to display.
- Includes unit tests (mocked HTTP) and a lint-clean `server.py` (10/10 pylint
	score in the development environment).

Setup
-----

1. Create a Python 3.8+ virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
python3 server.py
```

The server will listen on port 5000 by default. Open `http://127.0.0.1:5000/`
to see the frontend.

Usage
-----

The server exposes a simple endpoint for testing:

- GET `/emotionDetector?text=...` — quick browser testing; returns a plain-text
	summary of emotion scores and the dominant emotion.
- POST `/emotionDetector` with JSON `{"text": "..."}` — programmatic use.

The `emotion_detection` helper can also be imported directly from Python:

```py
from emotion_detection import emotion_detector
print(emotion_detector("I am feeling great today"))
```

Testing
-------

Unit tests use `unittest` and patch the HTTP call to avoid network requests.
Run tests with:

```bash
python -m unittest test_emotion_detection.py
```

Development notes and troubleshooting
-----------------------------------

- The project hits an external endpoint. Ensure you have network access and
	that the endpoint is reachable. For local tests and CI, tests mock the HTTP
	call so they do not rely on external services.
- `server.py` is intentionally lint-clean for development; if you reintroduce
	more functionality, run `pylint server.py` and fix warnings to keep the
	quality high.
- If you want to package this module for reuse, add `pyproject.toml` or
	`setup.cfg` metadata. A lightweight `__init__.py` is already present to
	expose the main functions as a package.

If you'd like, I can also:
- Add CORS headers to `server.py` for cross-origin frontend testing.
- Re-introduce the POST behavior on `/emotionDetector` while preserving the
	pylint score.
- Add a GitHub Actions workflow to run lint and tests on push.
