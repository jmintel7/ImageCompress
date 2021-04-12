
from PIL import ExifTags
from PIL import Image




def image_reduce(source,destination):
    ratio = 60

    image = Image.open(source)

    try:
        exif = dict((ExifTags.TAGS[k], v) for k, v in image._getexif().items() if k in ExifTags.TAGS)
        orientation = exif['Orientation']
        if orientation == 3:
            image = image.rotate(180, expand=True)
        elif orientation == 6:
            image = image.rotate(270, expand=True)
        elif orientation == 8:
            image = image.rotate(90, expand=True)
    except:
        pass

    image.save(destination, optimize=True, quality=ratio)



