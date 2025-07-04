from gtts import gTTS
import os

# Create the voices folder if it doesn't exist
voices_dir = "ksenia_voices"
if not os.path.exists(voices_dir):
    os.makedirs(voices_dir)

# Name to replace <name> placeholder
name ="Ksenia"  # Replace with desired name

# Message dictionaries
welcome_messages = {
    "message1": f"Bonjour {name}",
    "message2": f"Bienvenue {name}",
    "message3": f"Salut {name}",
    "message4": f"Bonsoir {name}",
    "message5": f"Wesh wesh {name} bien ou bien?",
    "message6": f"Coucou {name}",
    "message7": f"Yo {name} tu va bien?",
    "message8": f"Salut {name} tu nous a grave manquer",
    "message9": f"Hello {name}"
}

goodbye_messages = {
    "message1": f"Au revoir {name}",
    "message2": f"A bientot {name}",
    "message3": f"Adieu {name}",
    "message4": f"A la revoyure {name}",
    "message5": f"Reviens vite {name}",
    "message6": f"Bonsoir {name}",
    "message7": f"Tu va nous manquer {name}",
    "message8": f"Bon courrage {name}",
    "message9": f"Tchao {name}"
}

# Function to generate audio
def generate_audio(text, lang, filename):
    # Generate TTS with gTTS
    tts = gTTS(text=text, lang=lang)
    
    # Save to file
    file_path = os.path.join(voices_dir, filename)
    tts.save(file_path)
    
    # Check file size
    size_bytes = os.path.getsize(file_path)
    if size_bytes > 1_000_000:
        print(f"Warning: {filename} exceeds 1 MB ({size_bytes / 1_000_000:.2f} MB)")
    
    print(f"Generated: {filename}")

# Generate welcome messages
for key, text in welcome_messages.items():
    lang = "en" if key == "message9" else "fr"  # English for message9, French for others
    filename = f"welcome_{key}.mp3"
    generate_audio(text, lang, filename)

# Generate goodbye messages
for key, text in goodbye_messages.items():
    lang = "fr"  # All goodbye messages are in French
    filename = f"goodbye_{key}.mp3"
    generate_audio(text, lang, filename)

print(f"All audio files generated in {voices_dir}/")
