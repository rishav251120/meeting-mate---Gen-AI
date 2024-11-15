from flask import Flask, request, render_template, jsonify, send_file, redirect, url_for
from PIL import Image
import io
import requests
import torch
from transformers import AutoProcessor, AutoModelForCausalLM
import pyttsx3

# Initialize Flask app
app = Flask(__name__)

# Load Florence-2 Model (Replace 'florence2_model_name' with the actual model name if available)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base-ft", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-base-ft", trust_remote_code=True)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def resize_image(image, target_size=(224, 224)):
    """Resize image to the target size for better model processing."""
    return image.resize(target_size)

def generate_caption(image, prompt="default caption"):
    """Generate a descriptive caption for the image using the prompt."""
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    caption_ids = model.generate(**inputs)
    caption = processor.decode(caption_ids[0], skip_special_tokens=True)
    return caption

import os

def text_to_speech(text):
    """Convert text to speech and save it as an audio file using gTTS."""
    from gtts import gTTS
    
    # Ensure the static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Convert text to audio and save
    tts = gTTS(text=text, lang='en')
    tts.save('static/caption_audio.mp3')

@app.route('/')
def index():
    """Render the HTML page."""
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    prompt = request.form.get("prompt", "default caption")  # Get the prompt from the form
    image = Image.open(request.files['image'].stream)

    resized_image = resize_image(image)
    
    # Generate caption based on prompt
    caption = generate_caption(resized_image, prompt)
    
    # Convert caption to speech and save as audio
    text_to_speech(caption)

    response = {
        "caption": caption,
        "audio_url": "/static/caption_audio.mp3"
    }
    return render_template("result.html", **response)

if __name__ == "__main__":
    app.run(debug=True)