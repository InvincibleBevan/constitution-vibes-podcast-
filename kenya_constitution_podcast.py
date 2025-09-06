import os
from openai import OpenAI
from pydub import AudioSegment

# ✅ Initialize OpenAI
client = OpenAI(api_key="sk-proj-xxxx...")  # replace with your actual key

# ✅ Folders
episodes_dir = "episodes"
os.makedirs(episodes_dir, exist_ok=True)

# ✅ Anthem file (make sure anthem.mp3 exists in project root)
anthem_file = "anthem.mp3"
anthem = AudioSegment.from_mp3(anthem_file) if os.path.exists(anthem_file) else None

# ✅ Your podcast scripts
scripts = [
    "Welcome to Constitution Vibes! In this first episode, we break down the foundation of the Kenyan Constitution...",
    "In this second episode, let’s explore the Bill of Rights, a pillar of Kenyan democracy...",
    "Episode three is all about leadership and integrity under Chapter Six of the Constitution..."
]

# ✅ Generate episodes with anthem background
for i, text in enumerate(scripts, start=1):
    output_file = os.path.join(episodes_dir, f"episode_{i}.mp3")
    print(f"🎧 Generating {output_file}...")

    # 1. Generate narration with OpenAI TTS
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",  # Kenyan-male-like accent (closest available)
        input=text
    )

    narration_file = f"temp_{i}.mp3"
    with open(narration_file, "wb") as f:
        f.write(response.read())

    narration = AudioSegment.from_mp3(narration_file)

    # 2. Mix anthem with narration (lower volume of anthem)
    if anthem:
        background = anthem - 20  # soften anthem volume
        # Loop anthem to match narration length
        loops_needed = int(len(narration) / len(background)) + 1
        anthem_looped = background * loops_needed
        anthem_trimmed = anthem_looped[: len(narration)]
        final_mix = narration.overlay(anthem_trimmed)
    else:
        final_mix = narration

    # 3. Export final podcast
    final_mix.export(output_file, format="mp3")

    # cleanup
    os.remove(narration_file)

print("✅ All episodes generated with anthem background!")
