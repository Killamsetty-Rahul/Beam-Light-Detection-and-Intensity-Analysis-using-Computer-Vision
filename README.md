📸 Beam Light Detection and Intensity Analysis using Computer Vision
Welcome to my computer vision project where I’ve developed a system to detect and analyze beam light intensity from images. The main aim of this project is to identify bright light sources in images (like vehicle headlights) and recommend whether a beamlight dimming action is needed — a step towards improving night-time driving safety.

📌 Project Overview
This project uses image processing techniques and computer vision libraries like OpenCV, imutils, and scikit-image to detect intense beam lights from images. 

It performs:

Detection of bright regions (like beam lights) in images.

Analysis of their intensity levels and pixel concentration.

Suggests whether a beamlight dim action is needed.

Visual representation of detection results and grayscale histograms.

Plots of beam light intensity levels and detection accuracy for different test cases.

📂 Project Structure
python
Copy
Edit
Beam-Light-Detection-and-Intensity-Analysis-using-Computer-Vision/
│
├── beam_light_detection_in_image.py       # Main Python program
├── Dataset.zip                            # Compressed folder containing image dataset
└── README.md                              # Project description and instructions (this file)

📸 Sample Output
The code processes each image, detects bright spots, and shows:

The original image with detected bright regions circled.

A histogram of grayscale intensities.

Console logs with intensity and bright pixel count for each detected cluster.

Whether beamlight dimming is required for that case.

A summary plot of intensity levels and detection accuracy rates across test cases.

🔧 How It Works
Image Preprocessing:

Convert the image to grayscale.

Apply Gaussian blur to smoothen it.

Threshold to isolate bright regions.

Perform erosion and dilation to remove noise.

Detection:

Label connected components in the binary image.

Filter clusters based on pixel size constraints.

Detect contours for the remaining bright spots.

Analysis:

Calculate the mean intensity and bright pixel count for each cluster.

Determine whether beamlight dimming is needed based on set thresholds.

Visualization:

Display processed images with highlighted beam spots.

Show grayscale intensity histograms.

Generate a dual-axis plot comparing beam intensity and detection accuracy.

📊 Libraries Used
OpenCV

imutils

scikit-image

numpy

matplotlib

shutil, os, zipfile, time, pathlib (for file and folder management)

🚀 How to Run the Project
Note: The original code is designed for Google Colab, but you can easily adapt it for local execution by modifying paths.

📌 On Google Colab:
Upload Dataset.zip and beam_light_detection_in_image.py to your Google Drive.

Open the Colab notebook or script.

Update the drive_path in the code with your correct Drive location if needed.

Run the entire script.

The images from Dataset.zip will be extracted and processed.

Results will be displayed one by one.

Summary plots will appear at the end.

🎯 Sample Dataset
The dataset consists of images containing beam lights of varying intensities captured in night-time driving conditions. You can replace these images with your own test images — just ensure they're placed inside the Dataset folder (after extraction).

📈 Performance & Results
Bright light clusters are successfully detected and analyzed in all test images.

Recommendations for beamlight dimming based on intensity thresholds.

Visual outputs provide intuitive insights for each test case.

Summary graph displays test-wise beamlight intensity and detection accuracy.

📬 Contact
If you have any queries or suggestions, feel free to connect with me!

Killamsetty Rahul
📧 killamsettyrahul05@gmail.com
