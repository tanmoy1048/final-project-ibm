import requests
import json
from typing import Any, Dict


def parse_emotion_response_text(response_text: Any) -> Dict[str, Any]:
    """Convert the API response to a dict with the five emotions and dominant_emotion."""
    # Parse JSON if a string was provided
    data = json.loads(response_text) if isinstance(response_text, str) else response_text

    # Extract emotion scores from the API response structure
    emotion_data = data['emotionPredictions'][0]['emotion']

    # Build the output dict
    emotions = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness']
    }

    # Determine dominant emotion (highest score)
    dominant = max(emotions.items(), key=lambda kv: kv[1])[0]
    emotions['dominant_emotion'] = dominant

    return emotions


def emotion_detector(text_to_analyze: str) -> Dict[str, Any]:
    """Send text to the Emotion Predict service and return parsed emotion scores.

    Returns the standardized dict produced by `parse_emotion_response_text`.
    """
    # Define the URL for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required by the Watson NLP API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Create the payload dictionary matching the required input JSON format
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request to the service
    response = requests.post(url, json=myobj, headers=headers)

    # Parse response.text into the required output format
    return parse_emotion_response_text(response.text)
