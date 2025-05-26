import cv2
import numpy as np

# Open the first camera (usually the default webcam)
cap = cv2.VideoCapture(0)  # Use the correct camera index for your system

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Define the minimum size for a "safe" area (to make sure it's large enough for landing)
min_area_size = 50  # minimum width and height of safe area for landing

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()
    
    if not ret:
        print("Video Feed ended")
        break

    # Resize image for easier visualization
    image = cv2.resize(frame, (600, 500))

    # CONVERTING TO GRAYSCALE
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # BLUR 
    blur = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)   # Use odd numbers as kernel size

    # EDGE CASCADE using Canny
    canny = cv2.Canny(blur, 125, 175)  # Reduce the canny by using the blur image

    # Find contours
    contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the detected contours
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

    # Loop through the image and find areas where there are no contours (safe areas)
    for contour in contours:
        # Get the bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Draw the contour bounding box (green)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        print(f"Contour bounding box coordinates: x={x}, y={y}, w={w}, h={h}")   # coordinates of contour bounding box

    # Loop through the image and find areas where there are no contours (safe areas)
    for y in range(0, image.shape[0], 50):  # Check 50-pixel blocks
        for x in range(0, image.shape[1], 50):  # Check 50-pixel blocks
            # Define a region of interest (ROI)
            roi = mask[y:y+50, x:x+50]

            # If the sum of the mask in this area is 0, it means no contours in this area
            if np.sum(roi) == 0:
                # Check if the area is big enough for landing
                cv2.rectangle(image, (x, y), (x+50, y+50), (255, 0, 0), 2)  # Blue rectangle for safe area
                
                print(f"Safe bounding box coordinates: x={x}, y={y}, w=50, h=50")   # coordinates of safe area

    
    cv2.imshow("Live Feed with Contours and Safe Landing Areas", image)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
