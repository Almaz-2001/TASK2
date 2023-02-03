import os
from PIL import Image

def convert_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.gif'):
            try:
                with Image.open(os.path.join(directory, filename)) as im:
                    im = im.convert('RGB')
                    jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                    im.save(os.path.join(directory, jpg_filename), 'JPEG', quality=90)
                    os.remove(os.path.join(directory, filename))
            except OSError:
                print(f'Cannot convert {filename}')

# Example usage:
convert_to_jpg('/path/to/scraped/images/folder')
