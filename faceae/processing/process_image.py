import cv2
import numpy as np
from numpy.typing import NDArray
from typing import Union

def preprocess_image(image: Union[NDArray, str]):
    # 1. Detect the face and square it without resizing
    # 2. Resize it to a given dimension
    # 3. Pass it through the face alignment and check for R, t values
    # 4. Save these R, t information.
    # 4. Align the images -R, -t to bring them to center
    # 5. Note the position of lips in the aligned coordinate system
    # 6. Save the image and the list of landmarks along with the image as a separate file.
    raise NotImplementedError()

def preprocess_folder(root: str):
    # folder has a video
    # make a capture element and run a loop on all frames and call process_image
    raise NotImplementedError()

