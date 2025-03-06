import openai
from pathlib import Path
from pydub import AudioSegment
from pydub.playback import play

# OpenAI API Key
openai.api_key = "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"

# 🎙 Function to Convert Text to Speech and Play It
def speak_tars(text):
    response = openai.Audio.create(
        model="text-davinci-002",
        input=text
    )

    audio_file = Path(__file__).parent / "tars_voice.mp3"
    with open(audio_file, "wb") as f:
        f.write(response["data"])

    # Load and play the audio
    sound = AudioSegment.from_file(audio_file, format="mp3")
    play(sound)

# 🚀 Test the Speech Function
if __name__ == "__main__":
    text = "Hello, I am TARS. Your best AI companion with a little bit of attitude."
    speak_tars(text)