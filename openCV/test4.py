import cv2

# Initialize webcam
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Save the frames
for a in range(0, 5):

    # Get current frame
    ret, img=cam.read()
   
    # If frame is returned
    if ret: 

        # Set the file-name
        file = "image_{}.png".format(a)
    
        # Write the frame
        cv2.imwrite(file, img)

        # Inform the user
        print("Image " + str(a) + " saved")

        # Display the frame
        cv2.imshow("Test", img)

        # If q is pressed quit
        k=cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break


# Release the object
cam.release()

# Close the window
cv2.destroyAllWindows()