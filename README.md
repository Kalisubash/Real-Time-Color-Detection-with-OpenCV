This Python script captures video from a webcam and performs real-time color detection. It identifies and highlights blue, red, and yellow colors in the video feed using color thresholding in the HSV color space.

Features
Real-Time Detection: Detects and highlights blue, red, and yellow colors in real-time from the webcam feed.
Bounding Boxes: Draws bounding boxes around detected color areas and labels them accordingly.
Customizable Colors: You can adjust the color ranges for detection by modifying the HSV threshold values.

Requirements
Python 3.x
OpenCV library
Install the required library using pip:pip install opencv-python

Usage
Run the Script

Webcam Access: Ensure your webcam is properly connected and accessible.

Detection:

The script will open a window displaying the live webcam feed.
It will automatically detect and highlight blue, red, and yellow areas in the video.
Exit:

Press the 'q' key to stop the script and close the video feed window.
Code Overview
Video Capture: Captures video frames from the default webcam.
Color Space Conversion: Converts frames from BGR to HSV color space for better color detection.
Color Masking: Defines HSV ranges for blue, red, and yellow colors and creates masks for each color.
Contour Detection: Finds contours in the masked images and draws bounding boxes around detected color areas.
Display: Shows the video feed with bounding boxes and labels for detected colors.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

This README file provides an overview of the script's functionality, installation, usage, and contribution guidelines, making it easy for users to understand and use your project.
