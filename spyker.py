from gtts import gTTS
import os
import sys

mytext = ""
if len(sys.argv) == 1:
    mytext = "No text input."

# get text from cmd line
# first argument is program name
for i in range(1, len(sys.argv)):
    mytext += " " + sys.argv[i]

# convert
speech = gTTS(text=mytext, lang="en", slow=False)

# play and clean
speech.save("tts.mp3")
os.system("mpg123 tts.mp3")
os.remove("tts.mp3")
