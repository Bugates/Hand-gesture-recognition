import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip frame for easier hand gestures
    frame = cv2.flip(frame, 1)
    
    # Convert to HSV and create skin mask
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Morphological operations to clean the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour by area and ignore small areas
        contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(contour)
        if area > 5000:  # Filter out small areas to avoid noise
            # Convex hull and defects
            hull = cv2.convexHull(contour, returnPoints=False)
            defects = cv2.convexityDefects(contour, hull)

            # Draw the contour and hull
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)
            
            # Check if there are convexity defects
            if defects is not None:
                count_defects = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(contour[s][0])
                    end = tuple(contour[e][0])
                    far = tuple(contour[f][0])

                    # Calculate the angle and filter based on depth and angle
                    a = np.linalg.norm(np.array(end) - np.array(start))
                    b = np.linalg.norm(np.array(far) - np.array(start))
                    c = np.linalg.norm(np.array(far) - np.array(end))
                    angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c)) * 57  # angle in degrees

                    # Identify defects based on angle and distance threshold
                    if angle <= 90 and d > 10000:  # Adjusted threshold
                        count_defects += 1

                # Determine gesture based on number of defects
                if count_defects > 2:
                    cv2.putText(frame, "Open Hand", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)  # Adjusted y-coordinate
                else:
                    cv2.putText(frame, "Closed Hand", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)  # Adjusted y-coordinate

    cv2.imshow('Hand Gesture', frame)
    
    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
