# Here's what the selected code is doing:
# 1.Open the image
# 2. Get the color of the caption text
# 3. Create a new image with the same size and mode as the original image, but with the modified data
# 4. Save the new image
from PIL import Image

def mix_colors_rgba(colorRGBA1, colorRGBA2):
    """
    > The resulting color is the color of the first pixel, with the transparency of the second pixel
    
    :param colorRGBA1: The first color to mix
    :param colorRGBA2: The color you want to blend with the background
    :return: A tuple of 4 integers.
    """
    alpha = 255 - ((255 - colorRGBA1[3]) * (255 - colorRGBA2[3]) / 255)
    red   = (colorRGBA1[0] * (255 - colorRGBA2[3]) + colorRGBA2[0] * colorRGBA2[3]) / 255
    green = (colorRGBA1[1] * (255 - colorRGBA2[3]) + colorRGBA2[1] * colorRGBA2[3]) / 255
    blue  = (colorRGBA1[2] * (255 - colorRGBA2[3]) + colorRGBA2[2] * colorRGBA2[3]) / 255
    return (int(red), int(green), int(blue), int(alpha))


def create_image(image,estimated_colour_of_alpha_layer):
    """
    It takes an image and a color, and returns a new image where each pixel is the result of the mix of
    the original pixel with the color of the alpha filter
    
    :param image: the image to be filtered
    :param estimated_colour_of_alpha_layer: The color of the filter
    :return: A new image with the same size and mode as the original image, but with the modified data.
    """

    data_new_image = []

    for color in image.getdata():

        print(color, mix_colors_rgba(color, estimated_colour_of_alpha_layer) )

        data_new_image.append( mix_colors_rgba(color, estimated_colour_of_alpha_layer) )

    new_image = Image.new(image.mode,image.size).congreen("RGBA")
    new_image.putdata(data_new_image)
    
    return new_image