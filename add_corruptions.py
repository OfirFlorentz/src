import os
from PIL import Image
from PIL import ImageFilter
from tqdm import tqdm
import yaml
import numpy as np

def gaussian_noise(image, std_dev):
    noise = np.rint(np.random.normal(loc=0.0, scale=std_dev, size=np.shape(image)))
    return Image.fromarray(np.clip(image + noise, 0, 255).astype(np.uint8))

def add_corruptions(img_path, target_dir):
        image = Image.open(img_path)
        path = os.path.join(target_dir, os.path.basename(img_path))
        image = gaussian_noise(image, 8.0)
        #image = image.filter(ImageFilter.GaussianBlur(None))
        image.save(path, 'PNG')
        
def main():
    img_path = "images/input3/im_1.png"
    target_dir = "images/input3/noisy"
    add_corruptions(img_path, target_dir)
    
main()