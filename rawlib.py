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

