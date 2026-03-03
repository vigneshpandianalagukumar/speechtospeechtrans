# main.py

import sounddevice as sd
import threading
from config import SAMPLE_RATE, BLOCK_SIZE
from asr import ASR
from translator import Translator
from tts import TTS

asr = ASR()
translator = Translator()
tts = TTS()

is_speaking = threading.Event()

def callback(indata, frames, time, status):
    if is_speaking.is_set():
        return

    audio_bytes = bytes(indata)
    text = asr.process(audio_bytes)

    if text and len(text.split()) >= 2:
        print("English:", text)
        hindi = translator.translate(text)
        print("Hindi:", hindi)

        def speak_thread():
            is_speaking.set()
            tts.speak(hindi)
            is_speaking.clear()

        threading.Thread(target=speak_thread, daemon=True).start()

with sd.RawInputStream(
    samplerate=SAMPLE_RATE,
    blocksize=BLOCK_SIZE,
    dtype="int16",
    channels=1,
    callback=callback
):
    threading.Event().wait()
