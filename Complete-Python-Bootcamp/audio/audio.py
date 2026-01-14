from docx import Document
import pyttsx3
import re

doc = Document("Java Architect Q&A.docx")

engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 1.0)

section_buffer = []
section_number = 1

def save_section(text, num):
    filename = f"SET_{num}.mp3"
    engine.save_to_file("\n".join(text), filename)
    print(f"Generated {filename}")

# Regex patterns that indicate a NEW MAJOR SECTION
SECTION_PATTERNS = [
    r"^🔥\s*SET\s*\d+",
    r"^🧠\s*AWS",
    r"^✅\s*Set\s*\d+",
    r"^\d+️⃣",              # emoji numbers
    r"^\d+\."               # numeric headings
]

def is_new_section(line):
    return any(re.match(p, line) for p in SECTION_PATTERNS)

for para in doc.paragraphs:
    line = para.text.strip()
    if not line:
        continue

    if is_new_section(line) and section_buffer:
        save_section(section_buffer, section_number)
        section_number += 1
        section_buffer = []

    section_buffer.append(line)

# Save last section
if section_buffer:
    save_section(section_buffer, section_number)

engine.runAndWait()

print("✅ ALL sections converted to audio")
