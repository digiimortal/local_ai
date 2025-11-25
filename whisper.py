# Import whisper python library
# https://pypi.org/project/openai-whisper/
import whisper

# Model choice for whisper 
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])

