
from PIL import Image

from utils.composite import composite_images

IMAGE_PATH='./images/'

# Example usage
image_paths = [f'{IMAGE_PATH}image1.jpg',
              f'{IMAGE_PATH}image2.jpg', 
              f'{IMAGE_PATH}image3.jpg']

horizon_compose = f'{IMAGE_PATH}horizon_compose.jpg'

vertica_compose = f'{IMAGE_PATH}vertica_compose.jpg'

composite_images(image_paths, horizon_compose, margin=10, padding=10, direction='horizontal')
composite_images(image_paths, vertica_compose, margin=10, padding=10, direction='vertical')


