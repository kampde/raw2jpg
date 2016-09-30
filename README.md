RAW2JPG
=============

Extract preview image from RAW photographs and create a thumbnail from it, for
faster review workflow. Thumbnails are created in the `jpg` subfolder.

Usage
-----

    ./raw2jpg [OPTIONS] directory_full_of_raw_files

Options
-------

Options may be specified in the command line or in a config file in
`$XDG_CONFIG_HOME/raw2jpg.conf`.

Current options are:

    -s, --size=SIZE    Use SIZExSIZE as the size of the generated JPG (will
                       keep aspect ratio).


Installation
============

`raw2jpg` relies on [gexiv2](https://wiki.gnome.org/Projects/gexiv2) for
extracting the jpg thumbnail from the raw file and reading and setting exif
metadata.  Probably you'll find the needed package in your distro's repository
(`libgexiv2-python3` in Fedora 24 or `libexiv2-dev` in Ubuntu)

Also, install pip dependencies:

    # pip3 install -r requirements.txt


Stability
=========

**Important**: This is merely an alpha version. Everything is subject to
change, including name of the program, command-line arguments, size/filename of
generated images, ...

This code is licensed under the Modified BSD License (see LICENSE).
