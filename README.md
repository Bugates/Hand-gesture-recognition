# Hand Gesture Recognition using OpenCV

This repository contains a Python script that detects hand gestures using a webcam and OpenCV. The program uses computer vision techniques to capture hand gestures in real-time and categorize them as "Open Hand" or "Closed Hand."

## Features
- **Real-time Hand Gesture Detection**: Using your webcam, the script identifies hand gestures in front of the camera.
- **Skin Detection**: The program uses HSV color space to detect skin tones and isolate the hand from the background.
- **Gesture Classification**: The hand gestures are classified based on the number of convexity defects detected in the hand contour.
    - "Open Hand": If there are more than 2 convexity defects.
    - "Closed Hand": If there are fewer than 2 convexity defects.
- **Contours and Convex Hull**: It draws contours and convex hulls around the hand to identify gestures more accurately.
- **Noise Reduction**: The program uses morphological operations (erosion, dilation, and Gaussian blur) to reduce noise in the mask.

## Requirements
To run this project, you'll need:
- Python 3.x
- OpenCV
- NumPy

Install the required dependencies:
```bash
pip install opencv-python numpy
```

## How to Run
1. Clone this repository to your local machine:
    ```bash
    https://github.com/Bugates/Hand-gesture-recognition 
    ```

2. Run the Python script:
    ```bash
    python hand_gesture_recognition.py
    ```
    The program will start using your webcam to detect and classify hand gestures in real-time.

    Press 'q' to exit the webcam feed.

## How It Works
- **Capture Frames**: The script continuously captures frames from the webcam.
- **HSV Skin Detection**: Converts the frame to the HSV color space and creates a mask to isolate skin regions.
- **Contours and Convex Hull**: Finds the contours in the mask, calculates the convex hull, and detects convexity defects.
- **Gesture Recognition**: Based on the number of defects, the program classifies the hand as "Open Hand" or "Closed Hand" and displays the result on the frame.

## Contributing
Feel free to contribute to this project by forking the repository and submitting pull requests. You can help improve the accuracy of the gesture recognition, optimize the code, or add new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

This basic hand gesture recognition system can be a foundation for creating more complex applications, such as controlling devices or interacting with user interfaces using hand gestures.
