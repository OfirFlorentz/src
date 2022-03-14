import math
import numpy as np
from PIL import Image
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim

def psnr_fn(image, reconstructed_image):
    rmse = math.sqrt(np.mean((image - reconstructed_image) ** 2))
    max_value = image.max()
    return 20 * math.log10(max_value / rmse)

#def ssim_fn(image, reconstructed_image):
#    image = image.transpose(1,2,0)
#    reconstructed_image = reconstructed_image.transpose(1,2,0)
#    return ssim(image, reconstructed_image, multichannel=True)

def main():
    orig_path = "data/DIV2KRK/gt/img_1_gt.png"
    orig_img = Image.open(orig_path)
    reconstructed_path = "images/output3/im_1/ZSSR_im_1.png"
    reconstructed_img = Image.open(reconstructed_path)
    print(f'PSNR = {psnr_fn(np.array(orig_img), np.array(reconstructed_img))}')
    #print(f'SSIM = {ssim_fn(np.array(orig_img), np.array(reconstructed_img))}')
    reconstructed_new_path = "images/output3-new/im_1/ZSSR_im_1.png"
    reconstructed_new_img = Image.open(reconstructed_new_path)
    print(f'new PSNR = {psnr_fn(np.array(orig_img), np.array(reconstructed_new_img))}')
main()