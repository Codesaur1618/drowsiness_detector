# README - Drowsiness Detection using OpenCV and dlib

This Python script detects drowsiness by monitoring a person's eyes using a webcam. It utilizes OpenCV for image processing and dlib for facial landmark detection to analyze the person's eyes and determine their state.

Prerequisites:

- Python (>= 3.x)
- OpenCV (cv2)
- numpy (>= 1.18)
- dlib (>= 19.22.1)
- imutils (>= 0.5.3)
- winsound (for Windows users)

Installation:

1. Make sure you have Python installed. You can download it from the official Python website (https://www.python.org/downloads/).
2. Install the required libraries using pip:pip install opencv-python numpy dlib imutils
3. For Windows users, you might also need to install the winsound library, which comes pre-installed with Python.

Usage:

1. Run the Python script in your terminal or IDE.
2. The script will start your webcam to capture frames.
3. It detects faces using dlib's frontal face detector and draws rectangles around them on the screen.
4. For each detected face, it identifies facial landmarks, particularly the eye regions.
5. By calculating the eye aspect ratio (EAR), it determines whether the eyes are open, closed, or blinking.
6. If the person's eyes are closed for a certain duration, an alarm sound will be played to indicate drowsiness.

Note:

- Make sure to have a webcam connected and working for the script to access.
- The script uses the EAR to classify eye states. The thresholds for determining "sleeping" or "drowsy" might need to be adjusted based on individual setups and environments.
- The alarm sound files bigalarm.wav and smallalarm.wav need to be present in the same directory as the script for the alarm functionality to work properly. You can customize the alarm sounds as needed.

Contributing:

If you want to contribute to this project, feel free to fork the repository, make improvements, and create a pull request.

License:

This project is licensed under the MIT License. Feel free to use and distribute it according to the terms of the license.

Warning:

Drowsy driving can be dangerous and cause accidents. This script is intended for educational and experimental purposes only. Always prioritize road safety and avoid using it in real-life driving situations.
