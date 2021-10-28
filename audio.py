import pyttsx3
import PyPDF2
book = open("Scienceofscience.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
countPages = pdfReader.numPages
speaker = pyttsx3.init()
speaker.setProperty(
    'voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

speaker.setProperty("rate", 145)

for i in range(1, countPages):
    eachPage = pdfReader.getPage(i)
    text = eachPage.extractText()
    speaker.say(text)
    speaker.runAndWait()
