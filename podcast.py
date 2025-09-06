import os
from openai import OpenAI

# Create episodes folder if not exists
os.makedirs("episodes", exist_ok=True)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Episodes content with Kenyan vibe
episodes = {
    "Intro": """
Welcome to The Constitution Vibes – prepared with SiR J,
powered by VibesOfTheTribe.
This is where we break down the Kenyan Constitution for the common mwananchi.
Grab your kahawa or madafu – let's vibe and learn!
    """,

    "Episode_0_Preamble": """
We, the people of Kenya—proud, diverse, and determined—acknowledge the supremacy of God,
honour those who fought for freedom,
and commit ourselves to justice, prosperity, and unity.
Think of it as the opening chorus of our Kenyan anthem in legal form.
    """,

    "Episode_1": """
Chapter 1 – Sovereignty of the People and Supremacy of this Constitution.
Translation? The power belongs to you, the people.
Not politicians, not offices – YOU.
And this Constitution is the supreme law – no shortcuts.
    """,

    "Episode_2": """
Chapter 2 – The Republic.
Kenya is a unitary, sovereign state – not for sale, not for lease.
Borders intact, flag flying, hakuna mchezo.
    """,

    "Episode_3": """
Chapter 3 – Citizenship.
Being Kenyan is more than just a passport – it’s rights, duties,
and belonging to the tribe called Kenya.
    """,

    "Episode_4": """
Chapter 4 – The Bill of Rights.
This is the heart of the Constitution – your freedoms, protections,
and guarantees as a mwananchi.
Freedom of speech, movement, equality – ni kama user manual ya your rights.
    """,

    "Episode_5": """
Chapter 5 – Land and Environment.
Land is emotional in Kenya.
This chapter settles who owns what, how land is managed, and how to protect the environment.
Basically – shamba na mti zetu, tuzitunze.
    """,

    "Episode_6": """
Chapter 6 – Leadership and Integrity.
Leaders must be role models – si watu wa scandal kila wiki.
Integrity is not optional – it’s constitutional.
    """,

    "Episode_7": """
Chapter 7 – Representation of the People.
Elections, voting, IEBC – all covered here.
Your vote is your voice, protect it.
    """,

    "Episode_8": """
Chapter 8 – The Legislature.
This is Parliament – Senate and National Assembly.
Their job? Make laws, check the Executive, na kusimamia wananchi.
    """,

    "Episode_9": """
Chapter 9 – The Executive.
President, Deputy, Cabinet Secretaries.
This is the engine room of government – lakini power iko limited by the Constitution.
    """,

    "Episode_10": """
Chapter 10 – Judiciary.
Hakuna mchezo hapa.
Courts interpret the law, protect justice, and act as referee between Wanjiku and serikali.
    """,

    "Episode_11": """
Chapter 11 – Devolved Government.
Counties, governors, MCAs.
Power is brought closer to the people – devolution ndio decentralization.
    """,

    "Episode_12": """
Chapter 12 – Public Finance.
Money matters – taxes, budgets, and spending.
Transparency and accountability ndio key – si kulipa ushuru halafu mtu anakula.
    """,

    "Episode_13": """
Chapter 13 – Public Service.
Civil servants, government officers – the team that runs daily services.
They must serve wananchi, not frustrate them.
    """,

    "Episode_14": """
Chapter 14 – National Security.
Police, Defence Forces, intelligence.
Security belongs to the people, not to be abused against the people.
    """,

    "Episode_15": """
Chapter 15 – Commissions and Independent Offices.
These are watchdogs – like EACC, Auditor-General, etc.
They keep leaders accountable – lazima checks and balances.
    """,

    "Episode_16": """
Chapter 16 – Amendment of this Constitution.
Yes, it can be changed – but with proper process.
No backdoor tricks – wananchi must decide.
    """,

    "Episode_17": """
Chapter 17 – General Provisions.
This is like the fine print – definitions, applications, clarifications.
The backbone holding all chapters together.
    """,

    "Episode_18": """
Chapter 18 – Transitional and Consequential Provisions.
How Kenya moved from old order to new order in 2010.
Basically, how we shifted gears smoothly.
    """,

    "Outro": """
And that’s the journey through the Constitution of Kenya,
with SiR J – powered by VibesOfTheTribe.
Knowledge is power – now go out there, be informed, and own your voice as a mwananchi.
Stay woke, stay Kenyan.
Asante sana!
    """
}

# --- Generate episodes ---
for title, text in episodes.items():
    filename = f"episodes/{title}.mp3"

    # Skip if already generated
    if os.path.exists(filename):
        print(f"⏩ Skipping {filename}, already exists.")
        continue

    print(f"🎙️ Generating {filename} ...")
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",  # male voice, smooth and clear
        input=text
    )

    with open(filename, "wb") as f:
        f.write(response.read())

print("\n✅ All episodes generated successfully in 'episodes' folder!")
