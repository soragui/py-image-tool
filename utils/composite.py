
from PIL import Image

def composite_images(images, 
                     output_image, 
                     margin=10, 
                     padding=10, 
                     direction='vertical'):
    """
        Create composite image with image list and two directions
        @author: soragui-gpt
        images: list of image to composite
        output_image: composite image result
        margin: number of pixels marin
        padding: number of pixels padding
        alignment: left , right , or center
        direction: direction to composite the images vertically or horizontally
    """
    # Open and load images
    img_list = [Image.open(img_path) for img_path in images]

    # Calculate the dimensions of the final composite image
    if 'vertical' == direction:
        width = max(img.width for img in img_list) + 2 * padding
        height = sum(img.height for img in img_list) + (len(img_list) - 1) * margin + 2 * padding
    elif 'horizontal' == direction:
        width = sum(img.width for img in img_list) + (len(img_list) - 1) * margin + 2 * padding
        height = max(img.height for img in img_list) + 2 * padding
    else:
        raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")
    
    # Create a new blank image with the calculated dimensions
    composite_img = Image.new('RGB', (width, height), (255, 255, 255))

    # Paste each image onto the composite image with margins and padding
    x_offset, y_offset = padding, padding
    for img in img_list:
        
        composite_img.paste(img, (x_offset, y_offset))

        if 'vertical' == direction:
            y_offset += img.height + margin
        elif 'horizontal' == direction:
            x_offset += img.width + margin

    # Save the final composite image
    composite_img.save(output_image)
