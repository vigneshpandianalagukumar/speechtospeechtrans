# asr.py

import vosk
import json
from config import SAMPLE_RATE, VOSK_MODEL_PATH

class ASR:
    def __init__(self):
        self.model = vosk.Model(VOSK_MODEL_PATH)
        self.recognizer = vosk.KaldiRecognizer(self.model, SAMPLE_RATE)

    def process(self, audio_bytes):
        if self.recognizer.AcceptWaveform(audio_bytes):
            result = json.loads(self.recognizer.Result())
            return result.get("text", "").strip()
        return ""
