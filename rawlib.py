import io
import os
import re

from PIL import Image
from gi import require_version
require_version('GExiv2', '0.10')
from gi.repository import GExiv2  # pylint: disable=wrong-import-position


def get_preview_bytes(exif):
    props = exif.get_preview_properties()
    height = 0
    ind = None
    for i, prop in enumerate(props):
        if prop.get_height() > height:
            height = prop.get_height()
            ind = i
    return exif.get_preview_image(props[ind]).get_data()


def get_metadata(path):
    try:
        exif = GExiv2.Metadata(path=path)
    except TypeError:
        exif = GExiv2.Metadata()
        exif.open_path(path)
    return exif


def miniature(nef, size, overwrite):
    jpg = '{nefpath}/jpg/{filename}.from_raw.jpg'.format(
        nefpath=(os.path.dirname(nef) or '.'),
        filename='.'.join(os.path.basename(nef).split('.')[:-1])
    )

    if os.path.exists(jpg):
        if not overwrite:
            print('file {} already exists. Skipping...'.format(jpg))
            return
        else:
            print('file {} exists; overwriting it as desired'.format(jpg))

    try:
        os.mkdir(os.path.dirname(jpg))
    except FileExistsError:
        pass

    print('{} => {}'.format(nef, jpg))

    exif = get_metadata(path=nef)
    orientation = exif.get_orientation()

    im_bytes = io.BytesIO(get_preview_bytes(exif))

    img = Image.open(im_bytes)
    img.thumbnail((size, size))
    img.save(jpg)
    exif2 = get_metadata(path=jpg)
    exif2.set_orientation(orientation)

    exif2.save_file(jpg)


def find_raws(folder, *, listdir=None):
    listdir = listdir or os.listdir
    rule = re.compile(r'\.nef$', re.IGNORECASE)
    return [os.path.join(folder, name)
            for name in listdir(folder)
            if rule.search(name)]


def process_folder(directory, size, overwrite,
                   *, find_raws_fn=None, miniature_fn=None):
    find_raws_fn = find_raws_fn or find_raws
    miniature_fn = miniature_fn or miniature
    for nef in find_raws_fn(directory):
        miniature_fn(nef, size, overwrite)
