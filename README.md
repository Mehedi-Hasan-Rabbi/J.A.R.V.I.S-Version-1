# J.A.R.V.I.S-Version-1
Voice Enabled Personal Assistant using Python.

### NOTE:
Please update the following lines according to your system location:
- `Jarvis.py`: Line 140
- `GUI.py`: Lines 178, 182, 186, 190, 194, 198

Update Whatsapp numbers from `GUI.py` line 108

---

## Features
- Tell time and date
- Switch between male and female voice
- Voice command and text command modes
- Send WhatsApp messages using voice
- Wikipedia search
- Google and YouTube search
- Get weather information
- Open file explorer, Chrome, and other applications
- Read any selected text
- Tell a joke
- Take a screenshot
- Take notes
- Generate passwords
- Flip a coin or roll a die
- Provide system usage information and more

---

## Technologies Used
- **Python**
- **pyttsx3** – Python text-to-speech library
- **speech_recognition** – Google Speech Recognition API
- **Natural Language Toolkit (NLTK)** – Platform for building Python programs to work with human language data
- **PyAutoGUI** – Cross-platform GUI automation Python module
- **Weather API** – Simple, fast, and free weather API from OpenWeatherMap

---

## How to Run This Project

1. Open this folder using VSCode or another code editor.
2. All the dependencies are already downloaded in the virtual environment (venv). Or, check the `requirements.txt`.
3. Activate the virtual environment:
   - On Windows:  
     ```bash
     ./venv/Scripts/activate
     ```
   - On Linux/macOS:  
     ```bash
     source venv/bin/activate
     ```
4. Run the `GUI.py` file:
   ```bash
   python GUI.py
