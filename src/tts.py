# tts.py

import torch
import sounddevice as sd
from aksharamukha import transliterate
from config import TTS_SAMPLE_RATE, SPEAKER

class TTS:
    def __init__(self):
        self.model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_tts",
            language="indic",
            speaker="v3_indic"
        )

    def speak(self, text):
        roman = transliterate.process("Devanagari", "ISO", text)
        audio = self.model.apply_tts(
            text=roman,
            speaker=SPEAKER,
            sample_rate=TTS_SAMPLE_RATE
        )
        sd.play(audio, TTS_SAMPLE_RATE)
        sd.wait()
