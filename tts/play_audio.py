#https://www.kdnuggets.com/use-hugging-face-transformers-text-to-speech-applications#:~:text=To%20use%20Hugging%20Face%20Transformers%20for%20Text%2Dto%2DSpeech%2C,can%20save%20or%20play%20directly.&text=Hugging%20Face%20provides%20powerful%20models,written%20text%20into%20spoken%20words.

pip install pydub
from pydub import AudioSegment
from pydub.playback import play

# Load and play the audio
audio = AudioSegment.from_wav("output.wav")
play(audio)
