# -*- coding: utf-8 -*-
"""Beam_Light_Detection_in_Image

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DfUJQEGjO-_KJIayf8ifVk0JsqLELZQf
"""

from google.colab import drive
drive.mount('/content/drive')

import shutil
import os
from zipfile import ZipFile

# Define paths
drive_path = "/content/drive/My Drive/Dataset.zip"  # Update this path if needed
colab_path = "/content/Dataset"

# Create dataset folder if not exists
os.makedirs(colab_path, exist_ok=True)

# Copy dataset from Drive to Colab
shutil.copy(drive_path, "/content/Dataset.zip")

# Extract dataset.zip
with ZipFile("/content/Dataset.zip", 'r') as zip_ref:
    zip_ref.extractall(colab_path)

print("Dataset extracted successfully!")

from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import os
import time
from matplotlib.animation import FuncAnimation

def analyze_image(image_path):
    # Input validation
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Read and process image
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Failed to load image: {image_path}")

    # Image processing parameters
    INTENSITY_THRESHOLD = 220
    BRIGHT_PIXEL_THRESHOLD = 500
    MAX_CLUSTER_SIZE = 10000
    MIN_CLUSTER_SIZE = 300

    # Resize image while maintaining aspect ratio
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # Convert to grayscale and apply preprocessing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)

    # Label connected components
    labels = measure.label(thresh, connectivity=2, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")

    # Initialize results storage
    cluster_results = []
    beamlight_decrement_needed = False

    # Process each labeled region
    for label in np.unique(labels):
        if label == 0:
            continue
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)

        if MIN_CLUSTER_SIZE <= numPixels <= MAX_CLUSTER_SIZE:
            mask = cv2.add(mask, labelMask)

    # Find and process contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if not cnts:
        print('No bright spots detected.')
        return image, gray, [], False

    cnts = contours.sort_contours(cnts)[0]

    # Analyze each contour
    for (i, c) in enumerate(cnts):
        # Draw circle and label
        ((cX, cY), radius) = cv2.minEnclosingCircle(c)
        cv2.circle(image, (int(cX), int(cY)), int(radius), (0, 0, 255), 3)
        cv2.putText(image, f"#{i + 1}", (int(cX) - 10, int(cY) - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # Calculate intensity metrics
        mask = np.zeros(gray.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mean_val = cv2.mean(gray, mask=mask)[0]
        bright_pixels = cv2.countNonZero(mask)

        cluster_results.append({
            'cluster_id': i + 1,
            'intensity': mean_val,
            'bright_pixels': bright_pixels,
            'center': (cX, cY),
            'radius': radius
        })

        if mean_val > INTENSITY_THRESHOLD and bright_pixels > BRIGHT_PIXEL_THRESHOLD:
            beamlight_decrement_needed = True

    return image, gray, cluster_results, beamlight_decrement_needed

def display_results(image, gray, cluster_results, beamlight_decrement_needed, image_name):
    print(f"\nProcessing: {image_name}")

    # Print cluster information
    for cluster in cluster_results:
        print(f"Cluster #{cluster['cluster_id']}: "
              f"Intensity = {cluster['intensity']:.2f}, "
              f"Bright Pixels = {cluster['bright_pixels']}")

    # Print recommendation
    if beamlight_decrement_needed:
        print("Beamlight decrement is required.")
    else:
        print("No dim and dip required, continue your journey. Drive safe.")

    # Create figure with subplots
    fig = plt.figure(figsize=(12, 5))

    # Plot 1: Original image with detected regions
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Detected Bright Regions - {image_name}")
    plt.axis('off')

    # Plot 2: Intensity histogram
    plt.subplot(122)
    plt.hist(gray.ravel(), bins=256, range=(0, 256), color='black')
    plt.title("Grayscale Intensity Histogram")
    plt.xlabel("Grayscale Intensity Value")
    plt.ylabel("Pixel Count")
    plt.xlim([0, 256])

    plt.tight_layout()

    # Set up timer for auto-closing
    timer = fig.canvas.new_timer(interval=3000)  # 3000 milliseconds = 3 seconds
    timer.add_callback(plt.close, fig)
    timer.start()

    plt.show(block=True)

def process_dataset():
    # Get the current directory
    current_dir = Path.cwd()
    dataset_dir = Path("/content/Dataset/Dataset")

    # Check if Dataset folder exists
    if not dataset_dir.exists():
        print(f"Error: 'Dataset' folder not found in {current_dir}")
        print("Please create a 'Dataset' folder and add your images to it.")
        return 1

    # Get list of image files
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')
    image_files = [f for f in dataset_dir.iterdir() if f.suffix.lower() in image_extensions]

    if not image_files:
        print(f"No image files found in {dataset_dir}")
        print(f"Supported formats: {', '.join(image_extensions)}")
        return 1

    print(f"Found {len(image_files)} images in Dataset folder")
    print("Each image will be displayed for 3 seconds before proceeding to the next one.")
    print("Press Ctrl+C to stop the process at any time.")

    # Process each image
    for image_path in image_files:
        try:
            # Analyze image
            image, gray, cluster_results, beamlight_decrement_needed = analyze_image(image_path)

            # Display results
            display_results(image, gray, cluster_results, beamlight_decrement_needed, image_path.name)

        except Exception as e:
            print(f"Error processing {image_path.name}: {str(e)}")
            continue

        # Small delay to ensure clean transition between images
        time.sleep(0.1)

    return 0

def main():
    try:
        return process_dataset()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main())

import numpy as np
import matplotlib.pyplot as plt

# Sample Data (Modify as per your actual results)
test_cases = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
intensity_levels = [80, 90, 75, 85, 95]  # Detected beam intensity levels (0-100 scale)
accuracy_rates = [92, 95, 90, 94, 97]  # Accuracy percentage of beam detection

# Creating a figure with two subplots
fig, ax1 = plt.subplots()

# Plot Beam Light Intensity
ax1.set_xlabel('Test Cases')
ax1.set_ylabel('Intensity Level', color='tab:blue')
ax1.plot(test_cases, intensity_levels, marker='o', linestyle='-', color='tab:blue', label="Beam Intensity")
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis to plot accuracy
ax2 = ax1.twinx()
ax2.set_ylabel('Accuracy Rate (%)', color='tab:red')
ax2.plot(test_cases, accuracy_rates, marker='s', linestyle='--', color='tab:red', label="Accuracy Rate")
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and Grid
plt.title('Beam Light Detection: Intensity & Accuracy Analysis')
fig.tight_layout()
plt.grid(True)
plt.show()

