import numpy as np
from PIL import Image

class Bitmap:
    def __init__(self, image):
        if isinstance(image, str):
            img = Image.open(image).convert('RGB')
        else:
            img = image.convert('RGB')
        self.width, self.height = img.size
        self.pixels = np.array(img, dtype=np.int16)
