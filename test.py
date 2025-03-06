import openai
import pyaudio
import wave

# OpenAI API Key
openai.api_key = "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"

# 🎤 Function to Record Audio
def record_audio(filename="speech.wav", duration=5):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    
    print("🎤 Speak now...")
    frames = []
    for _ in range(0, int(16000 / 1024 * duration)):
        frames.append(stream.read(1024))
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))

    print("✅ Audio Recorded!")

# 📝 Function to Transcribe Audio
def transcribe_audio(file_path="speech.wav"):
    with open(file_path, 'rb') as audio_file:
        response = openai.Audio.transcribe(model="whisper-1", file=audio_file)
    return response['text']

# 🚀 Test the Speech Recognition
record_audio()
text = transcribe_audio()
print("🗣 You said:", text)
