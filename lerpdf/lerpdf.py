from gtts import gTTS
import PyPDF2

with open("colinha.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

tts = gTTS(text, lang='pt-br')
tts.save("audio.mp3")
