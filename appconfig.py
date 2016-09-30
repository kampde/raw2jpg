"""
There are no settings/configuration values that you can modify in this
file, so please stay away.

Due to the fact that modules are only loaded once, this acts as a singleton.
"""

import os

from configargparse import ArgumentParser


def _str_to_bool(text):
    """
    convert a string to boolean. 'true', 'TRUE', 'TrUe', 'Yes', '1', 'y' and
    similar returns True, otherwise returns False
    :param text: text to convert to boolean
    :return: the boolean representation of the text
    """
    return text.lower() in ['true', 'yes', 'y', '1']


def _get_config():
    cfg_home = os.getenv('XDG_CONFIG_HOME', '~/.config')
    parser = ArgumentParser(default_config_files=[cfg_home + '/raw2jpg.conf'])
    parser.add_argument('directories', metavar='DIRECTORY', nargs='*',
                        help='Directory to process')
    parser.add_argument('-s', '--size', default=1920, type=int,
                        help='Size to generate the jpgs (max edge)')
    parser.add_argument('--overwrite', default=False, type=_str_to_bool,
                        help='Overwrite generated image if it already exists')
    parser.add_argument('--clean', default=False, action='store_true',
                        help='Remove RAW files for which the related JPG file '
                             'has already been removed')
    return parser.parse_args()


config = _get_config()
