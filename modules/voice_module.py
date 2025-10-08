import pyttsx3
import whisper

# Initialize TTS engine
engine = pyttsx3.init()

def speak_text(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# Initialize Whisper STT model
model = whisper.load_model("base")

def speech_to_text(audio_path):
    """Convert audio file to text"""
    result = model.transcribe(audio_path)
    return result['text']

# Example usage
if __name__ == "__main__":
    speak_text("Hello! I am your AI Study Buddy.")
    print(speech_to_text("data/audio/sample.wav"))
