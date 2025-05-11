🚘 Beam Light Detection and Intensity Analysis using Computer Vision
Welcome to my project on Beam Light Detection and Intensity Analysis using Computer Vision!
This project focuses on identifying vehicle headlights (beam lights) in both images and video streams, analyzing how bright they are, and deciding whether a beam dimming action is needed. The idea is simple — improve night-time driving safety by minimizing glare from oncoming vehicles.

📖 About the Project
When you drive at night, the glare from other vehicles’ high-beam headlights can be dangerously blinding. Although modern cars are starting to feature automatic headlight dimming systems, many of them either require expensive hardware or rely on complex deep learning models that aren't always ideal for real-time use.

So, for this project, I built a lightweight, efficient, and effective system using Python and OpenCV. It detects beam lights from images and video frames, measures their intensity, and gives a recommendation whether dimming is required — all without the need for heavy hardware or resource-hungry AI models.

📂 What’s Inside This Repository
This repository includes everything you need to test both image-based and video-based beam light detection:

Beam Light Detection in Image.py → Detects beam lights in static images.

Beam Light Detection in Video.py → Detects beam lights frame-by-frame in video.

Dataset.zip → Contains sample images for testing the image detection script.

video-2.mp4 → A sample video to test the video detection script.

README.md → The project overview you’re reading now.

📚 Libraries Used
OpenCV

imutils

scikit-image

numpy

matplotlib

shutil, os, zipfile, time, pathlib (for file and folder management)

🚀 How to Run the Project
Note: The original code is designed for Google Colab, but you can easily adapt it for local execution by adjusting the file paths.

📌 On Google Colab:
Upload Dataset.zip and Beam Light Detection in Image.py to your Google Drive.

Open the Colab notebook or script.

Update the drive_path variable in the code with the correct path to your Drive location.

Run the entire script.

The images from Dataset.zip will be extracted, processed one by one, and detection results will be displayed visually.

Summary intensity histograms and graphs will appear at the end.

📸 For Video Detection:
Upload video-2.mp4 and Beam Light Detection in Video.py to your Google Drive.

Open the Colab notebook or script.

Update the drive_path variable in the code with the correct path to your Drive location.

Run the entire script.

The script will process the video frame-by-frame, detect beam light regions in real-time, display detection overlays, and plot live grayscale histograms for intensity analysis.

✨ Features
Detects vehicle beam lights in both images and video.

Measures the average intensity and bright pixel count within detected light regions.

Provides real-time feedback on whether a beamlight dimming action is needed.

Works reliably in varied conditions — fog, rain, tunnels, curved roads, and dense city lights.

Lightweight and fast — no deep learning models or special hardware required.

Includes clear visual feedback by highlighting detected beam regions and displaying intensity values.

⚙️ How It Works
The system follows a straightforward but effective computer vision workflow:

Preprocess the image/video frame by resizing, converting it to grayscale, and applying Gaussian blur to remove noise.

Apply adaptive thresholding to isolate bright regions (potential headlights).

Use morphological operations like erosion and dilation to clean up the result.

Label and analyze connected bright regions using contour detection.

Measure the intensity and bright pixel count for each detected region.

Decide if dimming is required based on configurable intensity and pixel count thresholds.

Show visual output with highlighted detections, intensity values, and a grayscale intensity histogram.
