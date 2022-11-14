# _____________________________________________________________________________________________________________________________________________________________ #
#                                                                                                                                                               #
#        ________      _________                   ________      _______       _____ ______       ________      ___      ___  _______       ________            #   
#       |\   ____\    |\___   ___\                |\   __  \    |\  ___ \     |\   _ \  _   \    |\   __  \    |\  \    /  /||\  ___ \     |\   __  \           #    
#       \ \  \___|    \|___ \  \_|  ____________  \ \  \|\  \   \ \   __/|    \ \  \\\__\ \  \   \ \  \|\  \   \ \  \  /  / /\ \   __/|    \ \  \|\  \          #  
#        \ \  \            \ \  \  |\____________\ \ \   _  _\   \ \  \_|/__   \ \  \\|__| \  \   \ \  \\\  \   \ \  \/  / /  \ \  \_|/__   \ \   _  _\         # 
#         \ \  \____        \ \  \ \|____________|  \ \  \\  \|   \ \  \_|\ \   \ \  \    \ \  \   \ \  \\\  \   \ \    / /    \ \  \_|\ \   \ \  \\  \|        #
#          \ \_______\       \ \__\                  \ \__\\ _\    \ \_______\   \ \__\    \ \__\   \ \_______\   \ \__/ /      \ \_______\   \ \__\\ _\        #
#           \|_______|aption  \|__|ext                \|__|\|__|    \|_______|    \|__|     \|__|    \|_______|    \|__|/        \|_______|    \|__|\|__|       #
#                                                                                                                                                               #
# _____________________________________________________________________________________________________________________________________________________________ #
#                                                               System                                                                                          #
#################################################################################################################################################################
# from system import utils as u

import numpy as np
from PIL import Image
import os
from generate.generateFolders import create_folders
from processing import substract as sub
from processing import text_eraser as ter
import system.utils as u
#################################################################################################################################################################


def run(img, rgba):
    """
    :param img: The caption_text image
    :param rgba: The rgb_alpha to « remove »
    """
    create_folders()    
    ter.binarize_image_with_text(img)
    image = Image.open(img).congreen("RGBA")
    new_image = f'{u.dt_string}/without_filter.png'
    sub.create_image(image,rgba).save(new_image)

    ter.fill_by_content_aware_alternative(new_image,f"{u.dt_string}/binarized_mask.png")
    ter.inpainting_with_border(new_image)


def run_extra(img, rgba, tv1, mv1, ip1, tv2, mv2, sz, ip2):
    """
    It takes an image, a color, and some parameters, and returns an image with the color removed
    
    :param img: The caption_text image
    :param rgba: The rgb_alpha to « remove »
    :param tv1: threshold value for binarization
    :param mv1: minimum value for the binarization
    :param ip1: The inpainting method to use for the first step
    :param tv2: threshold value for the binarization of the mask
    :param mv2: The minimum value of the mask to be considered as a mask
    :param sz: The size of the border to be inpainted
    :param ip2: The inpainting method to use
    """
    """
    :param img: The caption_text image
    :param rgba: The rgb_alpha to « remove »
    """
    create_folders()    
    ter.binarize_image_with_text(img,tv1,mv1)
    image = Image.open(img).congreen("RGBA")
    new_image = f'{u.dt_string}/without_filter.png'
    sub.create_image(image,rgba).save(new_image)

    ter.fill_by_content_aware_alternative(new_image,f"{u.dt_string}/binarized_mask.png",ip1)
    ter.inpainting_with_border(new_image,tv2,mv2,sz,ip2)

