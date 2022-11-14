import cv2
import numpy
import system.utils as u

def binarize_image_with_text(img_str,thresh_val=120,max_val=255):
    """
    > This function takes an image as input, converts it to HSV, splits the channels, and then applies a
    threshold to the V channel to binarize the image
    
    :param img_str: the path to the image you want to binarize
    :param thresh_val: The threshold value for the binarization, defaults to 120 (optional)
    :param max_val: The value to be given if pixel value is more than (sometimes less than) the
    threshold value, defaults to 255 (optional)
    """
    img = cv2.imread(img_str)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    thresh, bw = cv2.threshold(v,thresh_val, max_val, cv2.THRESH_BINARY)
    cv2.imwrite(f'{u.dt_string}/binarized_mask.png', bw)

def fill_by_content_aware_alternative(img_str,mask_str,inpaintRadius=32):
    """
    > The function takes an image and a mask as input, and returns an image with the masked area filled
    in
    
    :param img_str: the path to the image you want to fill
    :param mask_str: The path to the mask image
    :param inpaintRadius: Radius of a circular neighborhood of each point inpainted that is considered
    by the algorithm. Small values look less blurred, while larger values look more pixelated or
    blurred, defaults to 32 (optional)
    """
    img = cv2.imread(img_str)
    mask = cv2.imread(mask_str, 0)

    dest = cv2.inpaint(img, mask, inpaintRadius, cv2.INPAINT_NS)
    cv2.imwrite(f"{u.dt_string}/result_without_text.png",dest)

def inpainting_with_border(img_str,thresh_val=0,max_val=150,size=2,inpaintRadius=11):
    """
    > The function takes an image, converts it to HSV, extracts the saturation channel, thresholds it,
    dilates the thresholded image, and then uses the dilated image as a mask to inpaint the original
    image
    
    :param img_str: the path to the image you want to inpaint
    :param thresh_val: The threshold value for the saturation channel, defaults to 0 (optional)
    :param max_val: The maximum value to use with the THRESH_BINARY_INV thresholding type, defaults to
    150 (optional)
    :param size: the size of the kernel used in the morphological operation, defaults to 2 (optional)
    :param inpaintRadius: The radius of circular neighborhood of each point inpainted that is considered
    by the algorithm. Small values look less blurred, while larger values look more pixelated or
    blurred, defaults to 11 (optional)
    """
    img = cv2.imread(img_str)

    # congreen to hsv and extract saturation
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    sat = hsv[:,:,1]

    # thresold and ingreen
    thresh,dst = cv2.threshold(sat, thresh_val, max_val, cv2.THRESH_BINARY_INV)
    

    # apply morphology dilate
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size,size))
    thresh = cv2.morphologyEx(dst, cv2.MORPH_DILATE, kernel)

    # do inpainting
    result1 = cv2.inpaint(img, thresh, inpaintRadius, cv2.INPAINT_TELEA)
    result2 = cv2.inpaint(img, thresh, inpaintRadius, cv2.INPAINT_NS)

    # save results
    cv2.imwrite(f"{u.dt_string}/result_without_text_THRESHOLD.png", thresh)    
    cv2.imwrite(f"{u.dt_string}/result_without_text_TELEA.png", result1)
    cv2.imwrite(f"{u.dt_string}/result_without_text_NS.png", result2)