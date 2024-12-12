import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import numpy as np
import queue
import speech_recognition as sr
import pyttsx3  # For text-to-speech
import google.generativeai as genai  # For interacting with Gemini API

# Set up Gemini API key (replace with your actual API key)
genai.configure(api_key="replace with your API key")  # Replace with your Gemini API key

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Text-to-speech function
def speak_output(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to generate a response using Gemini API
def generate_response(prompt):
    try:
        st.write("Processing your input with Gemini...")
        model = genai.GenerativeModel("gemini-1.5-flash")  # Specify the Gemini model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "I'm sorry, I encountered an issue generating a response."

# Custom audio processor for WebRTC
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_frames = queue.Queue()

    def recv_audio(self, frame: np.ndarray, sample_rate: int):
        # Queue audio frames for processing
        self.audio_frames.put((frame, sample_rate))
        return None

    def get_audio_chunk(self):
        if not self.audio_frames.empty():
            frame, sample_rate = self.audio_frames.get()
            return frame, sample_rate
        return None, None

# Speech recognition function using `speech_recognition`
def recognize_speech(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    try:
        # Process audio using the `speech_recognition` library
        audio = sr.AudioData(audio_data, sample_rate, 2)
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the audio."
    except sr.RequestError as e:
        return f"Speech recognition service error: {e}"

# Streamlit App
st.title("Speech-to-Speech Chatbot")
st.write("Speak to the bot and get intelligent responses!")

# Input options
input_method = st.radio("Choose input method:", ["Type input", "Speak input"])

if input_method == "Type input":
    user_input = st.text_input("Enter your text:")
    if st.button("Submit"):
        if user_input:
            # Generate response
            bot_response = generate_response(user_input)
            st.success(f"Bot Response: {bot_response}")
            # Speak response
            speak_output(bot_response)
        else:
            st.warning("Please enter some text.")

elif input_method == "Speak input":
    st.write("Click 'Start' and speak into your microphone.")
    
    # WebRTC streamer for audio input
    webrtc_ctx = webrtc_streamer(
        key="speech-input",
        mode=WebRtcMode.SENDRECV,
        audio_processor_factory=AudioProcessor,
        media_stream_constraints={"audio": True, "video": False},
    )

    if webrtc_ctx.audio_processor:
        audio_frame, sample_rate = webrtc_ctx.audio_processor.get_audio_chunk()
        if audio_frame is not None:
            st.write("Processing speech input...")
            # Convert audio frame to a format compatible with `speech_recognition`
            recognized_text = recognize_speech(audio_frame.tobytes(), sample_rate)

            if recognized_text:
                st.success(f"You said: {recognized_text}")
                # Generate bot response
                bot_response = generate_response(recognized_text)
                st.success(f"Bot Response: {bot_response}")
                # Speak bot response
                speak_output(bot_response)
            else:
                st.error("No input detected. Please try again.")

st.write("Note: Ensure your microphone is enabled and accessible in your browser.")
