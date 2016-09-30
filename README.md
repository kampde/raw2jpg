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


Stability
=========

**Important**: This is merely an alpha version. Everything is subject to
change, including name of the program, command-line arguments, size/filename of
generated images, ...

This code is licensed under the Modified BSD License (see LICENSE).
