import cv2
import numpy as np

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture each frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for the blue color in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Define the range for the red color in HSV
    lower_red1 = np.array([0, 150, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 50])
    upper_red2 = np.array([180, 255, 255])

    # Define the range for the yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create masks for blue, red, and yellow colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours for blue, red, and yellow areas
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around detected blue areas
    for contour in contours_blue:
        if cv2.contourArea(contour) > 500:  # Filter small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Blue Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Draw bounding boxes around detected red areas
    for contour in contours_red:
        if cv2.contourArea(contour) > 500:  # Filter small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Red Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Draw bounding boxes around detected yellow areas
    for contour in contours_yellow:
        if cv2.contourArea(contour) > 500:  # Filter small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Yellow Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    # Display the original frame with bounding boxes
    cv2.imshow('Color Detection', frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
