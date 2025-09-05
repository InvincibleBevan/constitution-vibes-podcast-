from gtts import gTTS
from pydub import AudioSegment
import os
from episodes_data import episodes

os.makedirs("episodes", exist_ok=True)

anthem = AudioSegment.from_mp3("assets/anthem_instrumental.mp3")
anthem = anthem - 20  # lower anthem volume

for title, text in episodes.items():
    tts = gTTS(text=text, lang="en")
    voice_file = f"episodes/{title}_voice.mp3"
    tts.save(voice_file)

    voice = AudioSegment.from_mp3(voice_file)
    anthem_loop = anthem * (len(voice) // len(anthem) + 1)

    mixed = anthem_loop.overlay(voice)
    final_file = f"episodes/{title}.mp3"
    mixed.export(final_file, format="mp3")

    print(f"✅ Episode saved: {final_file}")
