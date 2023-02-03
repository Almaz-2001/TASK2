import numpy as np
import cv2

def preprocess(cloth, cloth_mask):
    # Convert cloth image to numpy array
    cloth_img = cv2.imread(cloth)
    # Convert cloth mask to numpy array
    cloth_mask_img = cv2.imread(cloth_mask, 0)
    # Invert the cloth mask
    cloth_mask_img = cv2.bitwise_not(cloth_mask_img)
    # Set the background color to blue
    blue = [255, 0, 0]
    # Create a blue background image with the same size as the cloth image
    blue_background = np.zeros((cloth_img.shape[0], cloth_img.shape[1], 3), np.uint8)
    blue_background[:] = blue
    # Apply the cloth mask to the blue background
    blue_background_cloth = cv2.bitwise_and(blue_background, blue_background, mask=cloth_mask_img)
    # Combine the cloth image and the blue background using the cloth mask
    blue_background_cloth = cv2.addWeighted(cloth_img, 1, blue_background_cloth, 1, 0)
    # Return the blue background cloth
    return blue_background_cloth
