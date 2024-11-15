MeetingMate: Visual Description Assistant for Presentations
Project Goal
To provide descriptive insights into images of virtual meeting content, enabling visually impaired users to understand shared screens and presentation visuals by uploading snapshots of slides or meeting screenshots.
Objectives
Allow users to upload images of slides or screenshots.
Generate clear, descriptive captions for uploaded images to enhance meeting accessibility.
Technical Implementation Guide
Setup:
Create a Flask application with endpoints for image upload and processing.
Install Florence-2 dependencies (torch, transformers), along with Flask.
Image Processing:
Users upload meeting screenshots or images of slides. Resize images using Pillow to optimize Florence-2 processing.
Caption Generation:
Florence-2 generates descriptive captions for each uploaded image.
Implement Florence-2 prompts that focus on layout elements (e.g., text, charts, or images) to create detailed and relevant captions.
Accessibility Options:
Display captions in a text format on the interface.
Provide an audio output option using pyttsx3 to make captions accessible as spoken content.
Expected Outcomes
Enhanced accessibility to virtual meeting content for visually impaired users.
A user-friendly tool for understanding slide content without relying on sight.
