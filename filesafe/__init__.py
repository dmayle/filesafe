#
from os import path

class Chroot(object):
    def __init__(self, chrootpath):
        # For safety reasons, the chroot path must start with a seperator to remove directory confusion
        self.chroot = path.abspath(chrootpath) + path.sep
        if not path.isdir(self.chroot):
            raise 'Some Error'
    def __call__(self, filepath):
        filechroot = path.abspath(filepath)
        # Needs to worry about similar names
        if not filechroot.startswith(self.chroot):
            raise IOError
        if filechroot == self.chroot:
            raise IOError
        return filepath
