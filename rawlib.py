import io
import os

from PIL import Image
from gi import require_version
require_version('GExiv2', '0.10')
from gi.repository import GExiv2


def get_preview_bytes(exif):
    props = exif.get_preview_properties()
    h = 0
    ind = None
    for i, prop in enumerate(props):
        if prop.get_height() > h:
            h = prop.get_height()
            ind = i
    return exif.get_preview_image(props[ind]).get_data()


def get_metadata(path):
    try:
        exif = GExiv2.Metadata(path=path)
    except TypeError:
        exif = GExiv2.Metadata()
        exif.open_path(path)
    return exif


def miniature(nef):
    jpg = '{nefpath}/jpg/{filename}.from_raw.jpg'.format(
        nefpath=(os.path.dirname(nef) or '.'),
        filename='.'.join(os.path.basename(nef).split('.')[:-1])
    )
    try:
        os.mkdir(os.path.dirname(jpg))
    except FileExistsError:
        pass

    print('{} => {}'.format(nef, jpg))

    exif = get_metadata(path=nef)
    orientation = exif.get_orientation()

    im_bytes = io.BytesIO(get_preview_bytes(exif))

    im = Image.open(im_bytes)
    width, height = im.size
    im.thumbnail((1920, 1920))
    im.save(jpg)
    exif2 = get_metadata(path=jpg)
    exif2.set_orientation(orientation)

    exif2.save_file(jpg)
