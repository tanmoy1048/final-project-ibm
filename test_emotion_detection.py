import unittest
import json
from unittest.mock import patch

import emotion_detection


def make_response_text(emotion_map):
    return json.dumps({
        "emotionPredictions": [
            {"emotion": emotion_map}
        ]
    })


class TestEmotionDetector(unittest.TestCase):
    def helper(self, statement: str, dominant_emotion: str):
        # build an emotion map with the dominant emotion high
        emotion_map = {k: 0.0 for k in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        emotion_map[dominant_emotion] = 0.99

        with patch('emotion_detection.requests.post') as mock_post:
            mock_post.return_value.text = make_response_text(emotion_map)
            result = emotion_detection.emotion_detector(statement)

        # check dominant emotion
        self.assertEqual(result['dominant_emotion'], dominant_emotion)
        # check the score is present and approximately correct
        self.assertAlmostEqual(result[dominant_emotion], 0.99, places=5)

    def test_joy(self):
        self.helper('I am glad this happened', 'joy')

    def test_anger(self):
        self.helper('I am really mad about this', 'anger')

    def test_disgust(self):
        self.helper('I feel disgusted just hearing about this', 'disgust')

    def test_sadness(self):
        self.helper('I am so sad about this', 'sadness')

    def test_fear(self):
        self.helper('I am really afraid that this will happen', 'fear')


if __name__ == '__main__':
    unittest.main()
