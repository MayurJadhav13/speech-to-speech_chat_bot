# Speech-to-Speech Chatbot with Gemini API

This repository contains a Speech-to-Speech chatbot application that leverages the Gemini API for generating intelligent responses to user queries. The project is implemented in Python and includes a command-line interface and a web-based Streamlit application.

---

## Features
- **Speech-to-Text:** Captures user speech via a microphone and converts it into text using the Google Speech-to-Text API.
- **Text Generation:** Generates intelligent and context-aware responses using the Gemini API.
- **Text-to-Speech:** Converts generated responses back into speech using pyttsx3.
- **Web Interface:** Streamlit-based interface for both typing and speaking inputs.
- **Real-Time Interaction:** Supports real-time microphone input using WebRTC.

---

## Requirements
### Python Packages
- `speechrecognition`: For speech-to-text conversion.
- `pyttsx3`: For text-to-speech conversion.
- `google-generativeai`: For interacting with the Gemini API.
- `streamlit`: For building the web application.
- `streamlit-webrtc`: For real-time microphone input via WebRTC.
- `numpy`: For audio frame processing.

### External API Key
You need an API key for the Gemini API. Replace the placeholder with your actual API key in the script.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run the Command-Line Bot
To use the bot in a terminal:
```bash
python main.py
```

### 2. Run the Web Application
To launch the web app using Streamlit:
```bash
streamlit run app.py
```

### 3. Interact with the Bot
- **Command-Line Interface:** Speak into your microphone, and the bot will respond in speech.
- **Web Application:** Choose between typing your input or speaking via the microphone.

---

## File Structure
```
├── main.py         # CLI-based Speech-to-Speech bot
├── app.py          # Streamlit web application
├── requirements.txt# List of Python dependencies
├── README.md       # Project documentation (this file)
```

---

## Configuration
### API Key Setup
Replace the `#replace with your API key` placeholder in `main.py` and `app.py` with your actual Gemini API key.
```python
genai.configure(api_key="your-api-key")
```

---

## Notes
- Ensure that your microphone is connected and accessible.
- Allow browser permissions for the microphone when using the web app.
- The Gemini API requires an active internet connection.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributions
Feel free to submit issues and pull requests to improve this project.

---

## Acknowledgements
- Google Speech-to-Text API
- Gemini API
- Streamlit Community
