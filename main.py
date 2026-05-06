
import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
from docx import Document
import os
import threading
import msvcrt


# Ask user for file
book = askopenfilename(title="Select a PDF or Word file", filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])


# Initialize pyttsx3
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')

# List available voices
print("Available voices:")
for idx, voice in enumerate(voices):
    lang_code = voice.languages[0]
    if isinstance(lang_code, bytes):
        lang_code = lang_code.decode('utf-8')
    print(f"[{idx}] {voice.name} | ID: {voice.id} | Lang: {lang_code}")

# Select voice
voice_idx = input(f"Enter the number of the voice you want to use (0-{len(voices)-1}): ").strip()
try:
    voice_idx = int(voice_idx)
    if 0 <= voice_idx < len(voices):
        speaker.setProperty('voice', voices[voice_idx].id)
        print(f"Using voice: {voices[voice_idx].name}")
    else:
        print("Invalid voice index. Using default voice.")
except Exception:
    print("Invalid input. Using default voice.")

# Set speech rate
rate = speaker.getProperty('rate')
print(f"Current speech rate: {rate}")
rate_input = input("Enter desired speech rate (e.g., 150 for slow, 200 for normal, 250 for fast): ").strip()
try:
    rate = int(rate_input)
    speaker.setProperty('rate', rate)
    print(f"Speech rate set to: {rate}")
except Exception:
    print("Invalid input. Using default rate.")

# Option to stop speech with a keypress
stop_flag = False
def check_for_stop():
    global stop_flag
    print("Press 's' to stop reading aloud at any time.")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key.lower() == b's':
                stop_flag = True
                speaker.stop()
                print("\nSpeech stopped by user.")
                break

stop_thread = threading.Thread(target=check_for_stop, daemon=True)
stop_thread.start()

ext = os.path.splitext(book)[1].lower()
if ext == '.pdf':
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    all_text = []
    for num in range(pages):
        if stop_flag:
            break
        page = pdfreader.pages[num]
        text = page.extract_text()
        print(f"Page {num+1} text:\n{text}\n{'-'*40}")
        if text:
            all_text.append(text)
        else:
            print(f"No text found on page {num+1}.")
    full_text = '\n'.join(all_text)
    if full_text.strip() and not stop_flag:
        print("\nReading aloud the entire document...\n")
        speaker.say(full_text)
        speaker.runAndWait()
    elif not stop_flag:
        print("No readable text found in the PDF.")
elif ext == '.docx':
    doc = Document(book)
    all_text = []
    for para in doc.paragraphs:
        if stop_flag:
            break
        print(f"Paragraph: {para.text}")
        if para.text.strip():
            all_text.append(para.text)
    full_text = '\n'.join(all_text)
    if full_text.strip() and not stop_flag:
        print("\nReading aloud the entire document...\n")
        speaker.say(full_text)
        speaker.runAndWait()
    elif not stop_flag:
        print("No text found in the Word document.")
else:
    print("Unsupported file type. Please select a PDF or DOCX file.")

print("\nNote: pyttsx3 uses system voices. For true multi-language support, you must have the desired language voice installed in your OS. pyttsx3 does not translate text; it only reads it aloud in the selected voice.\nYou can stop the speech at any time by pressing 's'.")