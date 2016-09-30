import os


class DeleteBehavior:
    def __init__(self, os_mod=None):
        self.os = os_mod or os

    def apply(self, rawfile):
        self.os.remove(rawfile)


class RenameBehavior:
    def __init__(self, *, os_mod=None):
        self.os = os_mod or os

    def apply(self, rawfile):
        self.os.rename(rawfile, rawfile + '.discarded')
